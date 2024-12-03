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
![Visualisasi 1](https://raw.githubusercontent.com/prtmaars/Bike-Sharing-DC/master/images/collage1.png)
Berdasarkan hasil analisis yang dilakukan, ditemukan bahwa sebagian besar penyewa cenderung menggunakan sepeda pada saat kondisi cuaca cerah, dengan persentase sebesar 70,94%. Sementara itu, pada kondisi cuaca berawan, persentase penyewa mencapai 24,15%. Penggunaan sepeda pada kondisi hujan ringan tercatat sebesar 4,90%, dan hanya 0,01% penyewa yang menggunakan sepeda saat hujan deras. Secara keseluruhan, jumlah penyewa sepeda pada kondisi cuaca cerah mencapai 2.338.432, pada cuaca berawan 796.026 penyewa, pada hujan ringan 161.600 penyewa, dan pada hujan deras hanya 223 penyewa. Selain itu, dari grafik korelasi antara suhu, kelembaban, dan jumlah sepeda yang disewa, terlihat bahwa suhu memiliki pengaruh positif terhadap jumlah sepeda yang disewa dengan nilai korelasi sebesar 0,4. Sebaliknya, kelembaban udara menunjukkan pengaruh yang sangat lemah terhadap jumlah sepeda yang disewa, dengan nilai korelasi -0,07. Hal ini menunjukkan bahwa suhu cenderung meningkatkan minat penyewa untuk menggunakan sepeda, sedangkan kelembaban relatif tidak memengaruhi keputusan penyewa secara signifikan.

![Visualisasi 2](https://raw.githubusercontent.com/prtmaars/Bike-Sharing-DC/master/images/collage2.png)
Visualisasi antara cuaca dengan penyewa sepeda dengan rincian keterangan yaitu ketika kondisi cuaca adalah 1 maka cuacanya cerah, sedikit berawan, sebagian berawan. Ketika kondisi cuaca adalah 2 maka cuacanya kabut + berawan, kabut + awan terputus, kabut + sedikit berawan, kabut. Ketika kondisi cuaca 3 maka cuacanya hujan salju ringan, hujan ringan + petir + awan tersebar, hujan ringan + awan tersebar. Ketika kondisi cuaca adalah 4 maka cuacanya hujan lebat + butiran es + petir + kabut, salju + kabut. Terlihat bahwa penyewa didominasi ketika kondisi cuaca cerah.

![Visualisasi 3](https://raw.githubusercontent.com/prtmaars/Bike-Sharing-DC/master/images/collage3.png)
Berdasarkan data yang diperoleh, jumlah penyewa sepeda berdasarkan hari menunjukkan bahwa Sabtu memiliki jumlah penyewa terbanyak dengan 487.825 penyewa, diikuti oleh Jumat dengan 485.821 penyewa dan Minggu dengan 477.886 penyewa. Hari-hari lainnya mencatatkan jumlah penyewa yang lebih rendah, dengan Senin menjadi hari dengan jumlah penyewa terendah, yaitu 444.182. Secara keseluruhan, data ini menunjukkan tren bahwa akhir pekan, khususnya Sabtu dan Jumat, menarik lebih banyak penyewa sepeda dibandingkan hari kerja lainnya.

Pada analisis berdasarkan jam, terlihat bahwa jam 17.00 menjadi waktu puncak dengan jumlah penyewa tertinggi, diikuti oleh jam 18.00. Selain itu, kategori waktu yang paling tinggi permintaannya terjadi pada rentang jam 7-9 pagi dan 17-19 sore. Grafik permintaan sepeda menunjukkan tren penurunan jumlah penyewa dari jam 17.00 hingga 23.00, kemudian mengalami penurunan lebih lanjut hingga mencapai titik terendah pada jam 4.00 pagi. Setelah itu, permintaan sepeda meningkat lagi antara jam 4.00 hingga 8.00 pagi, sementara rentang jam 8.00 hingga 17.00 menunjukkan fluktuasi permintaan yang naik turun, tergantung waktu tertentu.

Heatmap yang menggambarkan permintaan sepeda berdasarkan hari dan jam menunjukkan pola yang jelas. Pada hari Senin hingga Jumat, terdapat permintaan yang tinggi pada jam 7-9 pagi dan 17-19 sore, yang mencerminkan jam sibuk bagi penyewa sepeda, baik untuk perjalanan menuju tempat kerja atau pulang. Sementara itu, pada hari Sabtu dan Minggu, meskipun pola permintaan serupa dengan hari kerja, terdapat kehangatan yang lebih tinggi pada rentang jam 8-17 sore, yang menunjukkan bahwa penyewa sepeda lebih aktif di siang hari pada akhir pekan. Pola ini menunjukkan adanya perbedaan kebiasaan penggunaan sepeda antara hari kerja dan akhir pekan.

![Visualisasi 4](https://raw.githubusercontent.com/prtmaars/Bike-Sharing-DC/master/images/collage4.png)
Berdasarkan analisis yang dilakukan, telah dibuat kategori waktu sibuk berdasarkan permintaan sepeda, yaitu pada jam 7-9 pagi dan 17-19 sore, yang dianggap sebagai jam sibuk. Pada jam-jam ini, terlihat jelas adanya lonjakan permintaan sepeda. Namun, ketika analisis dilakukan berdasarkan musim liburan dan bukan liburan, terungkap bahwa pola lonjakan permintaan ini hanya terjadi pada musim bukan liburan. Pada musim liburan, meskipun jam 7-9 pagi tetap menjadi waktu dengan permintaan yang lebih rendah dibandingkan dengan hari biasa, lonjakan permintaan justru terjadi pada rentang jam 9-17 sore, yang menunjukkan bahwa penyewa cenderung menggunakan sepeda di siang hari, setelah jam pagi yang lebih sepi. Setelah jam 17, permintaan kembali menurun secara signifikan.

Selain itu, berdasarkan data yang diperoleh, proporsi penyewa sepeda pada musim liburan tercatat sebesar 45,2%, sementara pada musim bukan liburan mencapai 54,8%. Angka ini menunjukkan bahwa meskipun musim liburan memiliki pengaruh terhadap pola penggunaan sepeda, penyewa lebih banyak menggunakan sepeda pada musim bukan liburan, yang mencerminkan perbedaan aktivitas penyewa pada kedua periode tersebut.

## Conclusion
Konklusi Masalah 1: Analisis Cuaca
Berdasarkan hasil analisis, dapat disimpulkan bahwa kondisi cuaca memiliki pengaruh signifikan terhadap permintaan sepeda. Cuaca cerah menjadi faktor utama yang mendorong tingginya permintaan sepeda, dengan 70,94% penyewa memilih sepeda pada kondisi ini. Sebaliknya, cuaca hujan, baik ringan maupun deras, menunjukkan penurunan permintaan yang drastis, dengan hanya 4,90% penyewa pada kondisi hujan ringan dan 0,01% pada hujan deras. Analisis korelasi juga mengungkapkan bahwa suhu memiliki pengaruh positif terhadap jumlah sepeda yang disewa (korelasi 0,4), sementara kelembaban udara hampir tidak berpengaruh (korelasi -0,07). Hal ini menunjukkan bahwa cuaca cerah dan suhu yang lebih hangat cenderung meningkatkan permintaan sepeda, sedangkan hujan dan kelembaban tidak memiliki dampak signifikan.

Konklusi Masalah 2: Analisis Layanan
Dalam analisis berdasarkan waktu dan hari, ditemukan bahwa permintaan sepeda paling tinggi terjadi pada jam sibuk, yaitu antara pukul 7-9 pagi dan 17-19 sore. Pada hari Sabtu, terdapat jumlah penyewa terbanyak, diikuti oleh Jumat dan Minggu. Hal ini menunjukkan bahwa akhir pekan menarik lebih banyak penyewa dibandingkan hari kerja. Analisis berdasarkan musim liburan menunjukkan perbedaan pola permintaan, di mana pada musim liburan, permintaan sepeda cenderung lebih tinggi pada jam 9-17 sore, sementara jam 7-9 pagi cenderung lebih sepi. Proporsi penyewa pada musim liburan adalah 45,2%, sedangkan pada musim bukan liburan adalah 54,8%, menunjukkan bahwa meskipun musim liburan mempengaruhi pola penggunaan sepeda, lebih banyak penyewa yang menggunakan sepeda pada musim bukan liburan.

## Recommendation
Rekomendasi Berdasarkan Masalah 1:
1. Optimalkan Ketersediaan Sepeda pada Hari dengan Cuaca Cerah: Mengingat bahwa sebagian besar penyewa lebih memilih menggunakan sepeda saat cuaca cerah, disarankan agar sistem bike sharing meningkatkan ketersediaan sepeda pada hari-hari dengan prediksi cuaca cerah. Hal ini dapat dilakukan dengan memastikan sepeda tersedia lebih banyak di stasiun-stasiun yang terletak di lokasi strategis yang sering digunakan oleh penyewa pada cuaca cerah.
2. Tingkatkan Kampanye Promosi pada Hari Hujan dan Kondisi Cuaca Buruk: Untuk meningkatkan penggunaan sepeda pada kondisi cuaca yang kurang mendukung, seperti hujan ringan atau hujan deras, sistem dapat menawarkan promosi atau diskon khusus, seperti harga sewa lebih rendah atau sistem penyewaan yang lebih fleksibel. Ini dapat memotivasi pengguna untuk tetap menyewa sepeda meski cuaca tidak mendukung.
3. Pertimbangkan Penggunaan Sepeda Khusus pada Cuaca Dingin atau Ekstrem: Cuaca ekstrem, seperti suhu sangat tinggi atau hujan lebat, dapat membuat pengguna merasa kurang nyaman. Oleh karena itu, pertimbangkan untuk menyediakan sepeda yang lebih cocok untuk kondisi ekstrem, seperti sepeda dengan pelindung hujan atau lebih ringan untuk suhu panas, serta meningkatkan fasilitas perlindungan bagi penyewa (seperti pelindung hujan atau jaket untuk mengatasi cuaca dingin).

Rekomendasi Berdasarkan Masalah 2:
1. Penyesuaian Distribusi Sepeda pada Jam Sibuk: Berdasarkan analisis, jam sibuk terjadi pada rentang pukul 7-9 pagi dan 17-19 sore. Disarankan agar sistem bike sharing memprioritaskan distribusi sepeda di stasiun-stasiun yang sering digunakan pada jam-jam tersebut. Penyedia layanan juga bisa mempertimbangkan untuk menyediakan lebih banyak sepeda di daerah perkantoran atau lokasi yang memiliki konsentrasi tinggi pada jam sibuk.
2. Tingkatkan Ketersediaan Sepeda di Akhir Pekan: Permintaan sepeda meningkat pada akhir pekan, khususnya pada hari Sabtu dan Minggu. Oleh karena itu, penting untuk memastikan ketersediaan sepeda lebih banyak pada hari-hari tersebut, dengan memfokuskan pada lokasi populer seperti taman, pusat perbelanjaan, atau tempat wisata yang ramai dikunjungi.
3. Penyesuaian Pengaturan Sepeda pada Musim Liburan: Pada musim liburan, meskipun jam puncak sedikit berbeda, permintaan sepeda cenderung lebih tinggi pada jam 9-17 sore. Sistem dapat menyesuaikan distribusi sepeda dengan memperbanyak sepeda di stasiun yang sering digunakan selama siang hari di musim liburan. Selain itu, menawarkan promosi atau paket langganan yang menarik selama musim liburan bisa membantu menarik lebih banyak penyewa.
4. Pemantauan Perilaku Penyewa Berdasarkan Hari dan Waktu: Untuk lebih memahami pola penggunaan sepeda yang lebih spesifik, pemantauan lebih lanjut perlu dilakukan untuk mencatat variasi dalam kebiasaan penyewa dari hari ke hari. Dengan menggunakan data waktu dan hari yang lebih terperinci, sistem dapat mengatur rotasi sepeda dan memastikan ketersediaan sesuai dengan kebutuhan pengguna.
___
