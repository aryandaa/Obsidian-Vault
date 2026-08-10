#jaringan 
Pada komputer pribadi, kapasitas penyimpanan lokal seperti HDD atau SSD umumnya sudah cukup untuk memenuhi kebutuhan sehari-hari. Namun, pada lingkungan perusahaan, kebutuhan penyimpanan jauh lebih kompleks.

Sebuah organisasi biasanya membutuhkan kapasitas penyimpanan yang besar, kecepatan akses yang tinggi, kemampuan diakses oleh banyak server secara bersamaan, perlindungan data, serta kemudahan dalam pengelolaan dan pencadangan (_backup_).

Oleh karena itu, banyak perusahaan menggunakan **Storage Area Network (SAN)** dan **Network-Attached Storage (NAS)** sebagai bagian dari infrastruktur penyimpanan mereka.

---

### Apa itu Storage Area Network (SAN)?

**Storage Area Network (SAN)** adalah jaringan berkecepatan tinggi yang dirancang khusus untuk menghubungkan server dengan perangkat penyimpanan.

Karena berfungsi sebagai jaringan khusus untuk penyimpanan data, SAN sering disebut sebagai **jaringan penyimpanan di belakang server (network behind the servers)**.

Berbeda dengan jaringan komputer biasa yang digunakan untuk komunikasi umum, SAN hanya berfokus pada proses transfer data antara server dan media penyimpanan.

SAN terdiri dari infrastruktur komunikasi yang memungkinkan banyak server dan berbagai perangkat penyimpanan saling terhubung melalui perangkat jaringan seperti switch dan director.

Dengan menggunakan SAN, beberapa server dapat mengakses sistem penyimpanan yang sama secara bersamaan.

---

### Cara Kerja SAN

SAN dapat dianggap sebagai pengembangan dari konsep **storage bus**, yaitu jalur komunikasi yang menghubungkan server dengan perangkat penyimpanan.

Jika pada komputer biasa sebuah HDD atau SSD terhubung langsung ke server, pada SAN perangkat penyimpanan berada dalam jaringan khusus sehingga dapat digunakan bersama oleh banyak server.

Selain menyediakan jalur komunikasi, SAN juga memiliki **management layer**, yaitu lapisan yang bertugas mengelola:

- Koneksi antarperangkat.
    
- Perangkat penyimpanan.
    
- Hak akses server.
    
- Keamanan transfer data.
    
- Pengelolaan keseluruhan sistem penyimpanan.
    

Lapisan ini memastikan proses penyimpanan data berlangsung dengan aman, stabil, dan efisien.

---

### Keunggulan SAN

Pada sistem tradisional, satu server biasanya hanya terhubung ke sejumlah kecil perangkat penyimpanan yang dimilikinya sendiri.

SAN mengubah pendekatan tersebut dengan menyediakan penyimpanan yang dapat digunakan bersama oleh banyak server.

Keuntungan SAN antara lain:

- Kapasitas penyimpanan dapat digunakan bersama oleh beberapa server.
    
- Pengelolaan penyimpanan menjadi lebih terpusat.
    
- Skalabilitas lebih baik ketika kapasitas penyimpanan perlu ditambah.
    
- Memudahkan proses backup dan disaster recovery.
    
- Mendukung performa tinggi untuk aplikasi perusahaan.
    

Perangkat penyimpanan yang digunakan dalam SAN tidak harus berada di ruangan yang sama dengan server. Selama masih terhubung melalui jaringan SAN, server tetap dapat mengakses data tersebut.

---

## Komponen-Komponen SAN

Agar SAN dapat bekerja dengan baik, diperlukan beberapa komponen utama.

### 1. Fibre Channel

**Fibre Channel (FC)** adalah teknologi jaringan berkecepatan tinggi yang dirancang khusus untuk komunikasi antara server dan perangkat penyimpanan.

Fibre Channel menawarkan latensi rendah dan bandwidth tinggi sehingga sangat cocok digunakan pada lingkungan perusahaan yang membutuhkan performa tinggi.

Walaupun saat ini SAN juga dapat menggunakan teknologi seperti **iSCSI** melalui jaringan Ethernet, Fibre Channel masih banyak digunakan pada pusat data berskala besar.

---

### 2. Server Infrastructure

**Server infrastructure** adalah kumpulan server yang menggunakan sistem penyimpanan SAN.

Server-server tersebut dapat berasal dari berbagai platform dan menjalankan berbagai aplikasi, seperti:

- Database.
    
- Virtual Machine.
    
- Website.
    
- Sistem Enterprise Resource Planning (ERP).
    
- E-commerce.
    

Semakin banyak server yang digunakan dalam sebuah organisasi, semakin besar kebutuhan terhadap sistem penyimpanan bersama seperti SAN.

---

### 3. Storage System

**Storage system** merupakan kumpulan perangkat yang digunakan untuk menyimpan data.

Perangkat tersebut dapat berupa:

- Hard Disk Drive (HDD).
    
- Solid-State Drive (SSD).
    
- Flash Storage.
    
- Tape Drive.
    
- Tape Library.
    

Pemilihan media penyimpanan bergantung pada kebutuhan kapasitas, kecepatan, biaya, dan tujuan penggunaan.

---

### 4. Network System

Agar server dan perangkat penyimpanan dapat saling berkomunikasi, SAN menggunakan berbagai perangkat jaringan khusus.

Perangkat tersebut antara lain:

- Hub.
    
- Switch.
    
- Director.
    
- Router.
    

Perangkat-perangkat ini mengatur jalur komunikasi sehingga proses transfer data dapat berlangsung dengan cepat, aman, dan andal.

---

### Kesimpulan

Storage Area Network (SAN) merupakan solusi penyimpanan yang dirancang untuk lingkungan perusahaan yang membutuhkan kapasitas besar, performa tinggi, serta kemampuan berbagi penyimpanan di antara banyak server.

Dengan menggunakan SAN, organisasi dapat mengelola penyimpanan secara terpusat, meningkatkan ketersediaan data, mempermudah proses backup, dan menyediakan infrastruktur penyimpanan yang lebih fleksibel dibandingkan penyimpanan lokal tradisional.