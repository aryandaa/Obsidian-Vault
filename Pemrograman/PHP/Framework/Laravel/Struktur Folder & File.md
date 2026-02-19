#programming 
## **Struktur Folder:**

Setelah instalasi, penting untuk memahami struktur folder Laravel:

- **app/**: Berisi kode aplikasi seperti model, controller, dan middleware.
    
- **bootstrap/**: Berisi file untuk bootstrap aplikasi.
    
- **config/**: Berisi file konfigurasi untuk berbagai komponen Laravel.
    
- **database/**: Berisi migrasi, seeder, dan file database lainnya.
    
- **public/**: Berisi file yang dapat diakses publik seperti index.php, CSS, dan JavaScript.
    
- **resources/**: Berisi view, file bahasa, dan aset lainnya.
    
- **routes/**: Berisi file routing aplikasi.
    
- **storage/**: Berisi file yang dihasilkan aplikasi seperti log dan cache.
    
- **tests/**: Berisi file untuk pengujian aplikasi.
    
- **vendor/**: Berisi dependensi yang diinstal oleh Composer.

## **Rincian Folder Utama**

### **1. app/**
Folder ini berisi kode aplikasi utama, termasuk model, controller, dan middleware.
- **Console/:** Berisi perintah Artisan yang dapat Anda buat.
    
- **Exceptions/:** Berisi handler untuk pengecualian.
    
- **Http/:** Berisi controller, middleware, dan request.
    
    - **Controllers/:** Tempat Anda menyimpan semua controller aplikasi.
        
    - **Middleware/:** Berisi middleware yang digunakan untuk memfilter permintaan HTTP.
        
- **Models/:** Berisi model Eloquent yang mewakili tabel database.
### **2. bootstrap/**
Folder ini berisi file yang digunakan untuk bootstrap aplikasi.
- **app.php:** File ini mem-bootstrapping framework dan memuat semua komponen aplikasi.
### **3. config/**
Folder ini berisi file konfigurasi untuk berbagai komponen Laravel.
- **app.php:** Konfigurasi utama aplikasi.
    
- **database.php:** Konfigurasi koneksi database.
    
- **mail.php:** Konfigurasi pengaturan email.
    
### **4. database/**
Folder ini berisi migrasi, seeder, dan file database lainnya.
- **migrations/:** Berisi file migrasi untuk membuat dan mengubah tabel database.
    
- **seeds/:** Berisi file seeder untuk mengisi database dengan data awal.
### **5. public/**
- **index.php**: _Entry point_ untuk semua permintaan ke aplikasi Anda.
    
### **6. resources/**
- **views/**: Berisi file Blade template yang digunakan untuk tampilan.
    
- **lang/**: Berisi file terjemahan untuk aplikasi multibahasa.
    
- **assets/**: Berisi file CSS dan JavaScript yang dapat dikompilasi.
    
### **7. routes/**
- **web.php**: Berisi rute untuk antarmuka web.
    
- **api.php**: Berisi rute untuk API.
    
### **8. storage/**
- **app/**: Berisi file yang dihasilkan oleh aplikasi.
    
- **logs/**: Berisi file log aplikasi.
    
- **framework/**: Berisi cache, sesi, dan file framework lainnya.
    
### **9. tests/**
- **Feature/**: Berisi pengujian fitur aplikasi.
    
- **Unit/**: Berisi pengujian unit aplikasi.
    
### **File Utama di Laravel**
- **.env**: File konfigurasi environment yang berisi pengaturan aplikasi seperti database, mail, dll.
    
- **composer.json**: File yang berisi informasi tentang proyek dan dependensi yang digunakan.
    
- **artisan**: CLI (_Command Line Interface_) Laravel untuk menjalankan berbagai perintah Artisan.



