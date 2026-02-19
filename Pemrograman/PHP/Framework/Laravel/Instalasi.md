#programming 
## **Langkah-Langkah Instalasi**

### **1. Instal XAMPP**

1. **Unduh XAMPP:** Unduh XAMPP dari apachefriends.org.
2. **Instal XAMPP:** Ikuti petunjuk instalasi untuk menginstal XAMPP di sistem Anda.
3. **Jalankan XAMPP:** Buka XAMPP Control Panel dan jalankan Apache dan MySQL.
    
### **2. Instal Composer**

1. **Unduh Composer:** Unduh dan instal Composer dari getcomposer.org.
2. **Verifikasi Instalasi:** Buka terminal atau _command prompt_ dan jalankan perintah berikut untuk memastikan Composer terinstal dengan benar:

Bash

```
composer --version
```
### **3. Instal Visual Studio Code**

1. **Unduh Visual Studio Code:** Unduh dan instal Visual Studio Code dari code.visualstudio.com.
2. **Instal Ekstensi PHP:** Buka Visual Studio Code, pergi ke Extensions (ikon kotak di sidebar), dan cari serta instal ekstensi PHP untuk dukungan pengembangan PHP.
    
### **4. Instal Laravel**

1. **Buka Terminal atau Command Prompt:** Arahkan ke folder `htdocs` di direktori instalasi XAMPP. Misalnya:
    Bash:
	`cd C:\xampp\htdocs`  `
2. **Instal Laravel:** Jalankan perintah berikut untuk menginstal Laravel:
    Bash
    `composer create-project --prefer-dist laravel/laravel nama_proyek`
    _Gantilah `nama_proyek` dengan nama proyek Anda._
### **5. Konfigurasi Environment**

1. **Ubah Nama File:** Ubah nama file `.env.example` menjadi `.env`:
    Bash:
    `mv .env.example .env`
2. **Sesuaikan Pengaturan Database:** Buka file `.env` dan sesuaikan pengaturan database:
    Plaintext:
```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=nama_database
DB_USERNAME=root
DB_PASSWORD=
```
    
### **6. Generate Application Key**
Laravel membutuhkan _application key_ untuk mengenkripsi data. Anda dapat menghasilkan _key_ ini dengan perintah berikut:
Bash
```
php artisan key:generate
```

### **7. Menjalankan Server Lokal**
Untuk menjalankan server lokal dan melihat aplikasi Laravel Anda, gunakan perintah berikut:
Bash:
```
php artisan serve
```
Server akan berjalan di http://localhost:8000.