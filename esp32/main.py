import dht
import network
import time
import ujson
import urequests as requests
from machine import ADC, Pin
from umqtt.simple import MQTTClient



class UNI012:

  # Pins
  DHT_PIN = 23
  LDR_PIN = 35

  #Ubidots
  TOKEN = "BBUS-DQgX8dXeqm1hcpn9Bok6CZMXi3xIig"
  DEVICE_LABEL = "MACHINE"

  # Update rate
  UPDATE_RATE = 10 # second(s)

  def __init__(self) -> None:
    self._initialize_pins()
    self._connect_wifi()

  def start(self) -> None:
    while True:
      self._timer_callback()
      time.sleep(self.UPDATE_RATE)
  
  def _initialize_pins(self) -> None:
    self.dht = dht.DHT11(Pin(self.DHT_PIN))
    self.ldr = ADC(Pin(self.LDR_PIN))

  def _connect_wifi(self) -> None:
    print('Connecting to WiFi', end='')
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Rey', '123456789')
    while not sta_if.isconnected():
      print('.', end='')
      time.sleep(0.1)
    print(' Connected!')

  def _timer_callback(self) -> None:
    self.dht.measure()
    timestamp = time.localtime()
    current_timestamp = int(time.time() * 1000)
    data = ujson.dumps({
      'lux': self.ldr.read_u16(),
      'temperature': self.dht.temperature(),
      'humidity': self.dht.humidity(),
      'timestamp': current_timestamp,
    })
    print(data)
    UBIDOTS_URL = f"https://industrial.api.ubidots.com/api/v1.6/devices/{self.DEVICE_LABEL}"
    RAILWAY_URL = "https://sic6-stage2-basten-supremacy-production.up.railway.app/post_data"
    HEADERS = {"X-Auth-Token": self.TOKEN, "Content-Type": "application/json"}
    RAILWAY_HEADERS = {"Content-Type": "application/json"}
    while True:  
        print("\nMengirim data...")

        try:
            req1 = requests.post(UBIDOTS_URL, headers=HEADERS, data=data, timeout=5)
            req2 = requests.post(RAILWAY_URL, headers=RAILWAY_HEADERS, data=data, timeout=5)

            print(f"Ubidots Response: {req1.status_code}, {req1.text}")
            print(f"Railway Response: {req2.status_code}, {req2.text}")

            if req1.status_code == 200 and req2.status_code == 200:
                print("Success!")
                break

        except Exception as e:
            print(f"Error: {e}")

        print("Mengulang request...")
        time.sleep(1)

uni012 = UNI012()
uni012.start()
