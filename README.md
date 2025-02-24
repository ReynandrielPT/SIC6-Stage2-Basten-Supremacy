# 🌿 SIC6-Stage2-Basten-Supremacy

## 🌞 Perangkat Tenaga Surya dengan AI & IoT untuk Reboisasi 🌍

### 📌 Gambaran Proyek
Proyek ini, dikembangkan dalam **Samsung Innovation Campus**, adalah perangkat **bertenaga surya dengan AI & IoT** yang dirancang untuk membantu **usaha reboisasi** dengan memberikan **rekomendasi tanaman** berdasarkan data lingkungan secara real-time.

## 🛠️ Teknologi yang Digunakan
- **Perangkat Keras:** ESP32, Kabel Jumper, BreadBoard, OLED, Resistor, Micro USB Cable, ABS Box, Baterai Isi Ulang, Sensor GPS, Sensor Kelembaban Tanah, Sensor DHT11 (Suhu & Kelembaban), Sensor Cahaya

---

## 🚀 Cara Kerja
1. **Pengumpulan Data** – Sensor mengumpulkan data lingkungan secara real-time.
   Untuk mengumpulkan data secara real-time dan secara bersamaan menyimpannya, kami menggunakan sebuah program yang dijalankan oleh ESP32 (bernamakan main.py). Berikut adalah hal-hal yang dilakukan oleh program tersebut:
   - Membaca data yang dikoleksi oleh DHT11 dan mengolahnya
   - Membuat sebuah koneksi dengan WiFi yang telah ditentukan
   - Mengirimkan data yang telah diolah ke Ubidots
   - Menyimpan data yang telah diolah di sebuah _collection_ MongoDB
  
   Pengiriman data untuk ditampilkan oleh Ubidots dapat dilakukan langsung oleh ESP32 dengan programnya (main.py), namun penyimpanan data ke dalam _collection_ MongoDB perlu dilakukan melalui sebuah API eksternal. Untuk itu, kami       membuat sebuah aplikasi kecil yang diberikan nama app.py. Aplikasi ini menggunakan Python Flask untuk menerima data pada route "/post_data". Lalu, aplikasi akan menyimpannya ke dalam sebuah _collection_ MongoDB yang sudah            ditentukan. Dengan ini, ESP32 dapat mengirimkan data pada Ubidots serta secara tidak langsung menyimpannya di MongoDB.
     
3. **Pemrosesan AI** – Model AI menganalisis kondisi dan merekomendasikan spesies tanaman yang sesuai.
4. **Dasbor Pengguna** – Pengguna dapat memantau data dan menerima saran dari aplikasi web atau mobile.

---

## 📷 Demo Proyek & Screenshot
![image](https://github.com/user-attachments/assets/521afd4f-6c28-4c9a-9e09-9b7338b7e754)
![image](https://github.com/user-attachments/assets/75d8c52a-265e-42c8-8f07-5a8707647871)
![image](https://github.com/user-attachments/assets/f76b7be0-f1c0-405d-b392-e15527d14d81)
![image](https://github.com/user-attachments/assets/f4f888ba-0549-4964-aa18-cd0ce927a82f)

---
