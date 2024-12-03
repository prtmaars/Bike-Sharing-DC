# Washington DC Bike Sharing Rent Analysis 
Dicoding Data Analysis Project ✨

## Project Overview
Project ini adalah project analisis data dari Dicoding yang bertujuan untuk memahami pola sewa sepeda pada sistem bike sharing di Washington D.C., USA. Bike sharing adalah sistem penyewaan sepeda otomatis di mana pengguna dapat menyewa sepeda di satu lokasi dan mengembalikannya di lokasi yang berbeda. Sistem ini semakin populer karena berperan penting dalam mengatasi masalah kemacetan, lingkungan, dan kesehatan. Data yang digunakan dalam proyek ini mencakup informasi tentang jumlah sepeda yang disewa berdasarkan cuaca, musim, temperatur, dan waktu sewa, yang memungkinkan kita untuk menganalisis faktor-faktor yang mempengaruhi permintaan sepeda.

## Problem Understanding
Sistem bike sharing tidak hanya menyediakan solusi praktis untuk transportasi kota, tetapi juga menghasilkan data yang sangat berguna untuk analisis lebih lanjut. Dengan memantau pola sewa sepeda, kita dapat memperoleh wawasan yang lebih dalam tentang bagaimana cuaca, waktu, dan faktor lainnya mempengaruhi permintaan. Proyek ini bertujuan untuk menjawab dua pertanyaan utama terkait dengan penggunaan sepeda, yang akan membantu dalam merencanakan dan mengoptimalkan sistem bike sharing di masa depan.
Terdapat dua masalah utama yang ingin diselesaikan dalam proyek ini:
1. Analisis Cuaca: Bagaimana pengaruh kondisi cuaca dan temperatur terhadap jumlah total sepeda yang disewa?
   Analisis ini bertujuan untuk mengidentifikasi bagaimana perubahan cuaca, seperti cerah, hujan, atau temperatur ekstrem, dapat mempengaruhi jumlah sepeda yang disewa. Sebagai contoh, apakah hujan atau temperatur yang terlalu tinggi dapat mengurangi permintaan sepeda? Atau sebaliknya, apakah cuaca cerah meningkatkan penggunaan sepeda?
2. Analisis Layanan: Jam berapa dan hari apa permintaan sepeda paling tinggi?
   Analisis ini fokus pada pola waktu dan hari dalam seminggu yang paling sibuk untuk sistem bike sharing. Dengan mengetahui jam sibuk dan hari-hari tertentu yang menunjukkan permintaan tinggi, pengelola dapat merencanakan distribusi sepeda yang lebih efisien dan memastikan ketersediaan sepeda di waktu-waktu tertentu.


## Data Understanding
Dataset yang digunakan merupakan dataset rental sepeda di Washington D.C., USA. Data terdiri dari data harian dan data dalam interval 1 jam. Data yang digunakan merupakan data dari 1 Januari 2011 sampai dengan 31 Desember 2012. Dataset terdiri dari 16 kolom data dengan rincian sebagai berikut:
1. instant: Index data.
2. dteday : Tanggal diambilnya data.
3. season : Musim diambilnya data (1:spring, 2:summer, 3:fall, 4:winter).
4. yr : Tahun diambilnya data (0: 2011, 1:2012).
5. mnth : Bulan diambilnya data.
6. hr : Jam diambilnya data.
7. holiday : Boolean musim liburan (0: False, 1:True)
8. weekday : Hari dalam minggu (0-6).
9. workingday : Boolean hari kerja/libur (0: Kerja, 1:Libur).
10. weathersit : Kategori cuaca dengan rincian
    - 1: Cerah, Sedikit berawan, Sebagian berawan, Sebagian berawan
    - 2: Kabut + Berawan, Kabut + Awan terputus, Kabut + Sedikit berawan, Kabut
    - 3: Hujan salju ringan, Hujan ringan + Petir + Awan tersebar, Hujan ringan + Awan tersebar
    - 4: Hujan lebat + Butiran es + Petir + Kabut, Salju + Kabut
11. temp : Temperatur dalam derajat Celcius (°C). Nilai telah dinormalisasi dengan dibagi 41 (max).
12. atemp: Temperatur yang terasa dalam derajat Celcius (°C). Nilai telah dinormalisasi dengan dibagi 50 (max).
13. hum: Kelembapan. Nilai telah dinormalisasi dengan dibagi 100 (max).
14. windspeed: Kecepatan angin. Nilai telah dinormalisasi dengan dibagi 67 (max).
15. casual: Jumlah pengguna tidak terdaftar.
16. registered: Jumlah pengguna terdaftar.
17. cnt: Total jumlah sepeda sewaan, termasuk pengguna terdaftar dan tidak terdaftar.

## Analysis & Visualization

## Conclusion

___
