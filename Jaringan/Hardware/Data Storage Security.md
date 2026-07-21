#jaringan 
**Data storage security** atau **keamanan penyimpanan data** adalah serangkaian teknologi, kebijakan, dan mekanisme yang digunakan untuk melindungi data yang tersimpan, baik pada media penyimpanan lokal (**on-premises**) maupun layanan berbasis cloud.

Tujuan utama data storage security adalah menjaga **kerahasiaan (confidentiality)**, **integritas (integrity)**, dan **ketersediaan (availability)** data dari berbagai ancaman, seperti:

- Kebocoran data (_data breach_).
    
- Serangan siber (_cyberattack_).
    
- Akses tanpa izin.
    
- Malware dan ransomware.
    
- Kerusakan atau kehilangan data.
    

Bagi organisasi, kebocoran data dapat menimbulkan kerugian finansial, gangguan operasional, serta menurunkan kepercayaan pelanggan.

Oleh karena itu, banyak organisasi menerapkan berbagai mekanisme keamanan untuk melindungi sistem penyimpanan data mereka.

---

### Mekanisme Keamanan Penyimpanan Data

Beberapa mekanisme yang umum digunakan antara lain:

#### 1. Access Control

Sistem memberikan hak akses yang berbeda kepada setiap pengguna berdasarkan peran atau kewenangannya.

Dengan cara ini, hanya pengguna yang memiliki izin yang dapat membaca, mengubah, atau menghapus data tertentu.

---

#### 2. Encryption

**Encryption (enkripsi)** adalah proses mengubah data menjadi bentuk yang tidak dapat dibaca tanpa menggunakan kunci (_key_) yang sesuai.

Apabila media penyimpanan dicuri atau diakses oleh pihak yang tidak berwenang, data yang terenkripsi tetap tidak dapat dibaca tanpa proses dekripsi.

---

#### 3. Data Masking

**Data masking** adalah teknik menyembunyikan sebagian isi data sensitif tanpa mengubah data aslinya.

Sebagai contoh:

**Nomor KTP**

```
6301********1234
```

atau

**Nomor kartu kredit**

```
4111 **** **** 1234
```

Teknik ini memungkinkan data tetap dapat digunakan tanpa menampilkan informasi sensitif secara lengkap.

---

#### 4. Data Redaction

**Data redaction** adalah proses menghapus atau menyembunyikan informasi sensitif secara permanen dari sebuah dokumen atau data sebelum dibagikan kepada pihak lain.

Teknik ini sering digunakan pada dokumen hukum, rekam medis, maupun dokumen pemerintahan.

---

#### 5. Audit dan Monitoring

Sistem penyimpanan modern biasanya mampu mencatat berbagai aktivitas yang terjadi pada data, seperti:

- Siapa yang mengakses data.
    
- Kapan data diakses.
    
- Perubahan yang dilakukan.
    
- Aktivitas yang mencurigakan.
    

Informasi tersebut membantu proses audit keamanan serta memastikan organisasi mematuhi berbagai regulasi yang berlaku.

---

### Cyber Resilience

Selain melindungi data, organisasi juga perlu memiliki kemampuan untuk tetap beroperasi ketika terjadi insiden keamanan.

Kemampuan tersebut dikenal sebagai **cyber resilience**.

Cyber resilience adalah kemampuan organisasi untuk:

- Mencegah serangan siber.
    
- Bertahan ketika serangan terjadi.
    
- Memulihkan sistem dan data setelah insiden.
    
- Melanjutkan operasional secepat mungkin.
    

Cyber resilience menggabungkan berbagai aspek, seperti:

- Business Continuity.
    
- Disaster Recovery.
    
- Information Security.
    
- Manajemen Risiko.
    

Dengan pendekatan ini, organisasi tidak hanya berusaha mencegah serangan, tetapi juga memastikan sistem tetap dapat dipulihkan apabila terjadi gangguan.

---

### Immutable Storage

Salah satu teknologi yang semakin banyak digunakan adalah **immutable storage**.

Immutable storage adalah media penyimpanan yang membuat data **tidak dapat diubah atau dihapus** selama periode waktu tertentu atau bahkan secara permanen sesuai kebijakan yang diterapkan.

Data masih dapat dibaca berkali-kali, tetapi tidak dapat dimodifikasi setelah disimpan.

Teknologi ini sangat berguna untuk:

- Backup.
    
- Arsip digital.
    
- Rekam medis.
    
- Data pemerintahan.
    
- Bukti digital.
    
- Log keamanan.
    

Karena data tidak dapat diubah, immutable storage membantu melindungi informasi dari:

- Manipulasi data.
    
- Penghapusan yang disengaja.
    
- Serangan ransomware.
    
- Perubahan yang tidak sah.
    

Oleh karena itu, immutable storage menjadi salah satu solusi penting dalam menjaga integritas data pada organisasi yang memiliki kebutuhan keamanan dan kepatuhan regulasi yang tinggi.