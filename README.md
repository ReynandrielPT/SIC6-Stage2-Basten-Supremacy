# 🌿 SIC6-Stage2-Basten-Supremacy
## Assignment 2 Stage 2

## 🌞 Perangkat Pengumpul Data Suhu, Kelembapan, dan Intesitas Cahaya 🌍

### 📌 Gambaran Proyek
Proyek ini  dikembangkan dalam **Samsung Innovation Campus**, merupakan perangkat **IoT** yang dirancang untuk megumpulkan data dan menampilkan data tersebut dalam platform **Ubidots** secara real-time.

## 🛠️ Teknologi yang Digunakan
- **Perangkat Keras:** ESP32, Kabel Jumper, BreadBoard, Resistor 10kOhm, Micro USB Cable, Sensor DHT11 (Suhu & Kelembaban), Sensor LDR (Cahaya)

---

## 🚀 Cara Kerja
Sensor mulanya mengumpulkan data lingkungan secara real-time. Untuk mengumpulkan data secara real-time dan secara bersamaan menyimpannya, kami menggunakan sebuah program yang dijalankan oleh ESP32 (bernamakan main.py). Berikut adalah hal-hal yang dilakukan oleh program tersebut:
   - Menginisialisasi perangkat keras, seperti sensor DHT11 dan LDR
   - Membuat sebuah koneksi dengan WiFi yang telah ditentukan
   - Membaca data yang dikoleksi oleh DHT11 dan LDR
   - Mengirimkan data yang telah diolah ke Ubidots
   - Menyimpan data yang telah diolah di sebuah _collection_ MongoDB
  
   Pengiriman data untuk ditampilkan oleh Ubidots dapat dilakukan langsung oleh ESP32 dengan programnya (main.py), namun penyimpanan data ke dalam _collection_ MongoDB perlu dilakukan melalui sebuah API eksternal. Untuk itu, kami membuat sebuah aplikasi kecil yang diberikan nama app.py. Aplikasi ini menggunakan Python Flask untuk menerima data pada route "/post_data".  Lalu, aplikasi akan menyimpannya ke dalam sebuah _collection_ MongoDB yang sudah ditentukan. Supaya API dapat diakses secara global, maka kami mendeployment app.py pada platform Railway yang disertakan dengan requirements.txt dan file Procfile untuk kebutuhan deployment. Dengan ini, ESP32 dapat mengirimkan data pada Ubidots serta secara tidak langsung menyimpannya di MongoDB. Kami juga menambahkan dht.py sebagai driver bagi sensor DHT11.
   
---

## Rancangan Sebenarnya
Proyek kami sebetulnya merupakan perangkat **IoT** yang dilengkapi dengan **AI** untuk mengumpulkan data lingkungan secara *real-time*. Kemudian data dianalisis oleh **AI** dan dihasilkanlah rekomendasi-rekomendasi tanaman yang sebaiknya ditanam untuk membantu tindakan **penghijauan**. Akan tetapi, karena keterbatasan alat, bahan, dan waktu, kami tidak sempat merealisasikan proyek ide kami ini.

## 📷 Demo Proyek & Screenshot
![image](https://github.com/user-attachments/assets/521afd4f-6c28-4c9a-9e09-9b7338b7e754)
Gambar Data Masuk ke Ubidots

![image](https://github.com/user-attachments/assets/75d8c52a-265e-42c8-8f07-5a8707647871)
Gambar Data Masuk ke MongoDB Atlas

![image](https://github.com/user-attachments/assets/f76b7be0-f1c0-405d-b392-e15527d14d81)
Gambar script main.py

![image](https://github.com/user-attachments/assets/f4f888ba-0549-4964-aa18-cd0ce927a82f)
Gambar script dht.py



---
