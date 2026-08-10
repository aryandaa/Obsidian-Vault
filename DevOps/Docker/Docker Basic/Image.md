#devops 
Saat aplikasi kita dibungkus (package) menggunakan Docker, hasil akhirnya disebut **Docker Image**.

Image adalah paket yang berisi semua kebutuhan aplikasi agar dapat dijalankan di mana saja tanpa perlu menginstal dependensi satu per satu.

Dengan kata lain, **Docker Image adalah hasil distribusi (distribution package) dari sebuah aplikasi beserta seluruh dependensinya.**

Image inilah yang nantinya akan di-upload ke sebuah **Container Registry** (misalnya Docker Hub atau GitHub Container Registry), sehingga komputer lain cukup mengunduh image tersebut tanpa perlu melakukan proses instalasi ulang.

Setelah image berhasil diunduh, Docker dapat membuat sebuah **Container** dari image tersebut dan langsung menjalankan aplikasinya.


## Docker Image sebagai Template

Image dalam bahasa sederhananya adalah **template (cetakan) yang bersifat read-only**.

Artinya, isi image **tidak berubah** ketika dijalankan.

Ketika Docker menjalankan sebuah image, Docker akan membuat sebuah **container** yang memiliki lapisan (layer) tambahan yang bisa ditulis (writable layer).

```
Docker Image (Read Only)
        │
        ▼
Docker Container
(Read Only Layer + Writable Layer)
```

Karena image bersifat read-only, kita bisa membuat banyak container dari satu image yang sama tanpa saling memengaruhi.

Misalnya:

```
Laravel Image
      │
 ┌────┼────┐
 │    │    │
 ▼    ▼    ▼
Container A
Container B
Container C
```

Ketiganya berasal dari image yang sama, tetapi masing-masing memiliki data dan proses yang terpisah.

---
## Apa isi sebuah Docker Image?

Sebuah image biasanya berisi:

- Operating System minimal (Alpine, Ubuntu, Debian, BusyBox, dll.)
- Runtime aplikasi (PHP, Python, Node.js, Java, Go, dll.)
- Library
- Dependency
- Environment
- Konfigurasi
- Source Code (opsional, tergantung jenis aplikasinya)

Contoh image Laravel:

```
Ubuntu
PHP 8.4
Composer
Laravel
PHP Extensions
php.ini
Environment
```

Semua kebutuhan aplikasi sudah dibungkus menjadi satu paket.

--- 
## Image bukan Virtual Machine

Perlu dipahami bahwa image **bukanlah sistem operasi lengkap**.

Misalnya image Ubuntu.

Banyak orang mengira image Ubuntu berisi seluruh Ubuntu seperti yang diinstall di laptop.

Padahal kenyataannya tidak.

Image Ubuntu hanya berisi filesystem yang diperlukan untuk menjalankan aplikasi di dalam container.

Kernel Linux tetap menggunakan kernel dari komputer host.

```
Laptop
│
├── Linux Kernel
│
└── Docker Engine
      │
      └── Ubuntu Image
```

Karena itulah image Docker jauh lebih kecil dibanding Virtual Machine.

---
## Docker Hub menyediakan ribuan Image
![](img/Pasted%20image%2020260722210604.png)
Docker memiliki registry resmi bernama **Docker Hub**.

Di sana tersedia ribuan image open-source yang siap digunakan, misalnya:
- Ubuntu
- Debian
- Alpine
- Nginx
- Apache
- MySQL
- PostgreSQL
- Redis
- MongoDB
- Node.js
- Python
- PHP
- Golang

Karena image-image tersebut sudah dibuat oleh komunitas atau vendor resminya, kita tidak perlu membuat semuanya dari nol.

Misalnya untuk menjalankan Python:

```
docker pull python
```
atau
```
docker run python
```

Docker akan mengunduh image Python terlebih dahulu jika belum ada di komputer kita.

---
## Image Version (Tag)
![](img/Pasted%20image%2020260722214601.png)
Docker mendukung banyak versi image menggunakan **Tag**.

Tag berfungsi seperti nomor versi.

Contohnya:

```
python:3.10
python:3.11
python:3.12
python:3.13
```

Atau:

```
node:18
node:20
node:22
```

Sehingga kita dapat memilih versi yang sesuai dengan kebutuhan aplikasi.

Misalnya:

```
docker pull python:3.12
```

atau

```
docker run node:22
```

Jika tag tidak disebutkan, Docker biasanya akan menggunakan tag **latest**.

```
python
=
python:latest
```

Walaupun demikian, di lingkungan produksi **tidak disarankan menggunakan `latest`**, karena versi tersebut dapat berubah sewaktu-waktu dan menyebabkan aplikasi berjalan dengan versi yang berbeda dari sebelumnya.

---
## Image tersusun dari Layer

Salah satu keunggulan Docker adalah **Layer**.

Misalnya kita membuat image Laravel.

```
Layer 1 : Ubuntu
Layer 2 : PHP
Layer 3 : Composer
Layer 4 : Laravel
Layer 5 : Source Code
```

Jika nanti kita hanya mengubah source code Laravel, Docker **tidak perlu membangun ulang seluruh image**.

Docker hanya akan membuat ulang layer terakhir yang berubah.

Karena itulah proses build Docker bisa menjadi sangat cepat.

---

## Analogi sederhana

Bayangkan sebuah **cetakan kue**.

```
Image
=
Cetakan
```

Sedangkan

```
Container
=
Kue yang dibuat dari cetakan
```

Satu cetakan bisa menghasilkan banyak kue.

Begitu juga satu image dapat menghasilkan banyak container yang identik.

---

## Hubungan Image dan Container

```
Dockerfile
      │
      ▼
Build
      │
      ▼
Docker Image
      │
      ▼
docker run
      │
      ▼
Docker Container
```

Alur ini adalah inti cara kerja Docker. Kita menulis **Dockerfile**, Docker membangunnya menjadi **Image**, lalu setiap kali menjalankan `docker run`, Docker membuat **Container** baru dari image tersebut.

> **Kalimat yang paling mudah diingat:**
> 
> - **Dockerfile** = resep memasak.
> - **Docker Image** = makanan yang sudah dikemas dan siap didistribusikan.
> - **Docker Container** = makanan yang sudah dibuka dan sedang dinikmati (berjalan).