#jaringan 
Perkembangan teknologi penyimpanan data tidak lagi hanya berfokus pada perangkat keras (hardware). Saat ini, banyak sistem penyimpanan modern menggunakan pendekatan berbasis perangkat lunak atau **Software-Defined Storage (SDS)** untuk meningkatkan fleksibilitas, efisiensi, dan kemudahan pengelolaan data.

Melalui pendekatan ini, administrator tidak lagi harus mengelola setiap perangkat penyimpanan secara terpisah. Sebaliknya, berbagai perangkat penyimpanan dapat dikelola sebagai satu sistem yang terintegrasi.

---

### 1. Software-Defined Storage (SDS)

**Software-Defined Storage (SDS)** adalah teknologi penyimpanan yang memisahkan (**decouple**) pengelolaan penyimpanan dari perangkat keras fisiknya.

Pada sistem penyimpanan tradisional, fitur dan pengelolaan storage sangat bergantung pada perangkat yang digunakan.

Sedangkan pada SDS, terdapat lapisan perangkat lunak (**software layer**) yang mengelola seluruh perangkat penyimpanan sehingga administrator tidak perlu berinteraksi langsung dengan masing-masing perangkat.

SDS memanfaatkan teknologi **virtualisasi** untuk menggabungkan berbagai media penyimpanan menjadi satu **storage pool**.

Storage pool tersebut kemudian dapat dialokasikan secara dinamis sesuai kebutuhan aplikasi atau server.

Pengelolaan SDS dapat dilakukan melalui:

- Dashboard administrasi.
    
- API.
    
- Sistem otomatis (automation).
    

Dibandingkan NAS atau SAN tradisional, SDS memberikan fleksibilitas yang lebih tinggi karena kapasitas penyimpanan dapat ditambah, dikurangi, atau dipindahkan dengan lebih mudah.

Selain itu, SDS dapat mengotomatiskan berbagai pekerjaan seperti:

- Penyediaan storage (_provisioning_).
    
- Monitoring.
    
- Optimasi kapasitas.
    
- Troubleshooting.
    

---

### 2. Storage Virtualization

**Storage virtualization** adalah teknologi yang menggabungkan beberapa perangkat penyimpanan fisik menjadi satu ruang penyimpanan virtual.

Sebagai contoh, sebuah organisasi memiliki:

- 4 SSD.
    
- 6 HDD.
    
- 2 Storage Array.
    

Dengan storage virtualization, seluruh perangkat tersebut dapat terlihat sebagai satu sistem penyimpanan yang besar.

Administrator tidak perlu mengetahui lokasi fisik setiap data karena sistem virtualisasi akan mengelolanya secara otomatis.

Pengelolaan storage virtualization biasanya dilakukan melalui satu konsol administrasi sehingga lebih mudah mengatur:

- Kapasitas penyimpanan.
    
- Keamanan.
    
- Performa.
    
- Ketersediaan data.
    

Teknologi ini banyak digunakan pada lingkungan virtualisasi server dan pusat data.

---

### 3. Hyperconverged Storage

**Hyperconverged Storage** adalah sistem penyimpanan yang menjadi bagian dari **Hyperconverged Infrastructure (HCI)**.

Pada infrastruktur tradisional, komponen berikut biasanya dipisahkan:

- Server.
    
- Storage.
    
- Network.
    

Sedangkan pada HCI, ketiga komponen tersebut digabungkan menjadi satu platform yang dikelola secara terpusat.

Di dalam HCI, penyimpanan menggunakan konsep SDS sehingga seluruh kapasitas storage dari beberapa server dapat digabungkan menjadi satu storage pool.

Melalui virtualisasi, penyimpanan tidak lagi bergantung pada satu perangkat tertentu.

Jika kapasitas penyimpanan atau komputasi perlu ditingkatkan, administrator cukup menambahkan node baru ke dalam cluster.

Sistem kemudian akan menggabungkan sumber daya tersebut secara otomatis.

Pendekatan ini membuat hyperconverged storage memiliki beberapa keunggulan, antara lain:

- Mudah diperluas (_scalable_).
    
- Pengelolaan lebih sederhana.
    
- Ketersediaan data lebih tinggi.
    
- Cocok untuk virtualisasi dan cloud computing.
    

---

### Hubungan Antar Teknologi

Perbedaan ketiga teknologi tersebut dapat diringkas sebagai berikut:

**Software-Defined Storage (SDS)**

→ Mengelola storage menggunakan lapisan perangkat lunak.

**Storage Virtualization**

→ Menggabungkan banyak storage fisik menjadi satu storage virtual.

**Hyperconverged Storage**

→ Mengintegrasikan storage, komputasi, dan jaringan dalam satu infrastruktur menggunakan SDS dan virtualisasi.