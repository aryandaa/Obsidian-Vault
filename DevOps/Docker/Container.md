#devops 
## Bayangkan kamu punya aplikasi Laravel

Aplikasi Laravel milikmu membutuhkan:
- PHP 8.4
- Composer
- Nginx
- MySQL
- Extension PHP tertentu (fileinfo, pdo_mysql, dll.)
- Konfigurasi khusus

Di laptopmu semuanya sudah terpasang dan Aplikasi berjalan lancar. Lalu kamu kirim project itu ke teman dan Temanmu menjalankan:

```
php artisan serve
```

Lalu muncul:

```
PHP Fatal Error...
```

Ternyata masalahnya adalah:

- PHP dia masih 8.2
- Composer versinya beda
- Extension belum diinstall
- MySQL versinya beda
- Path konfigurasi berbeda
# Apa itu Container?
Container adalah lingkungan (environment) yang terisolasi, ringan, dan berisi semua kebutuhan agar sebuah aplikasi bisa berjalan dengan cara yang sama di mana pun.

Di dalam container bisa ada:
```
Laravel Project
│
├── PHP
├── Composer
├── Nginx
├── Extension PHP
├── Environment Variable
└── Dependency lainnya
```

Ketika container dipindahkan ke komputer lain, isinya tetap sama.

# Analogi sederhana
Bayangkan sebuah **kotak makan (lunch box)**.
Di dalamnya ada:
Sandwich
Minuman
Buah
Snack

Semua sudah dikemas, Kamu tinggal membawa kotaknya. Tidak peduli apakah kamu makan di rumah,  di kampus,  di kantor,  atau di gunung Isi kotaknya tetap sama.

Container seperti itu.

```
Laptop A
┌─────────────┐
│ Container   │
│ Laravel     │
│ PHP         │
│ MySQL       │
└─────────────┘
```

Dipindahkan ke

```
Laptop B
┌─────────────┐
│ Container   │
│ Laravel     │
│ PHP         │
│ MySQL       │
└─────────────┘
```

Tetap identik.

# Apa yang membuat Container spesial?

Container **tidak mengemas sistem operasi penuh**., Ia hanya membawa hal-hal yang diperlukan aplikasi.

Misalnya:

```
Ubuntu Host
│
├── Docker Engine
│
├── Container Laravel
│     ├── PHP
│     ├── Composer
│     └── Laravel
│
├── Container MySQL
│     └── MySQL
│
└── Container Redis
      └── Redis
```

Semua container berbagi kernel dari sistem operasi host, sehingga jauh lebih ringan dibanding virtual machine.

# Container itu bukan Virtual Machine
Sering disamakan, padahal berbeda, Virtual Machine:

```
Hardware
↓
Host OS
↓
VirtualBox
↓
Ubuntu
↓
PHP
↓
Laravel
```

Container:

```
Hardware
↓
Host OS
↓
Docker Engine
↓
Container
↓
PHP
↓
Laravel
```

VM harus menjalankan sistem operasi lengkap. Container hanya menjalankan aplikasi beserta dependensinya.

# Kenapa container ringan?
Misalnya Ubuntu membutuhkan sekitar:
```
Ubuntu OS
≈ 2 GB
```
Sedangkan container nginx bisa hanya:
```
≈ 30 MB
```
Karena container tidak membawa seluruh sistem operasi.


# Container itu sebenarnya proses

Ini bagian yang sering mengejutkan pemula, Banyak orang mengira container adalah "komputer mini". Padahal, di Linux, container pada dasarnya adalah **proses biasa** yang diisolasi menggunakan fitur kernel seperti **namespaces** dan **cgroups**.

Misalnya kamu menjalankan:

```
docker run nginx
```

Docker membuat proses `nginx` yang:

- memiliki filesystem sendiri,
- jaringan sendiri,
- daftar proses sendiri,
- batas penggunaan CPU dan RAM sendiri.

Dari luar terlihat seperti komputer terpisah, padahal masih berjalan di kernel yang sama.

# Kenapa disebut "terisolasi"?

Misalnya ada dua container.

```
Container A

PHP 8.4
```

```
Container B

PHP 7.4
```

Keduanya bisa berjalan bersamaan tanpa saling mengganggu.

Begitu juga:

```
Container A
MySQL 8
```

```
Container B
MariaDB 11
```

Versinya bisa berbeda dan tetap aman karena masing-masing memiliki lingkungan sendiri.

# Kehidupan sebuah Container

Container memiliki siklus hidup sederhana:

```
Image
   │
   ▼
Create Container
   │
   ▼
Running
   │
   ▼
Stopped
   │
   ▼
Removed
```

Nanti kita akan belajar bahwa **container dibuat dari image**, seperti kue dibuat dari cetakan. Satu image bisa menghasilkan banyak container yang identik.

---

## Inti yang perlu diingat

Container **bukan** virtual machine kecil dan **bukan** sistem operasi lengkap. Ia adalah lingkungan terisolasi yang menjalankan satu atau beberapa proses aplikasi beserta semua dependensinya, sambil berbagi kernel dengan sistem operasi host. Karena itu container bisa ringan, cepat dibuat, mudah dipindahkan, dan menghasilkan perilaku aplikasi yang konsisten di mana pun dijalankan.

Kalau konsep ini sudah terasa masuk akal, langkah berikutnya yang paling logis adalah membahas **Docker Image**, karena hubungan **Image → Container** adalah fondasi seluruh cara kerja Docker.