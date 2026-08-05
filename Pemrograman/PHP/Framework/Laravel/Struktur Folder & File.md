#programming 
Kalau diibaratkan tubuh manusia, folder Laravel adalah organ-organ yang punya pekerjaan masing-masing. Semuanya bekerja sama setiap kali ada request masuk.

Misalnya ada orang membuka
```
http://localhost:8000/products
```

Laravel tidak asal mencari file `products.php` tetapi Ia akan melewati banyak bagian ini:

```
Browser
      │
      ▼
public/index.php
      │
      ▼
Bootstrap Laravel
      │
      ▼
Route
      │
      ▼
Middleware
      │
      ▼
Controller
      │
      ▼
Model
      │
      ▼
Database
      │
      ▼
Controller
      │
      ▼
Blade
      │
      ▼
Browser
```
Seluruh folder Laravel dibuat agar alur ini berjalan.

## Structure Folder
## app/
Ini adalah folder yang paling sering kamu buka dan Di sinilah seluruh logika aplikasi berada, Misalnya:
```
app/
│
├── Models/
├── Http/
├── Providers/
├── Console/
├── Jobs/
├── Events/
└── Policies/
```

Kalau membuat
```
php artisan make:model Product
```
hasilnya ada di
```
app/Models/Product.php
```

Kalau membuat controller
```
php artisan make:controller ProductController
```
hasilnya berada di
```
app/Http/Controllers
```

Jadi bisa dibilang, **folder `app` adalah rumah utama kode yang kamu tulis sendiri**.

--- 
## routes/
Semua jalan masuk aplikasi ada di sini.
```
routes/
```

Berisi
```
web.php
api.php
console.php
channels.php
```

Yang paling sering digunakan adalah
```
web.php
```

Contoh umum (Routes Controller):
```php
Route::get('/products', [
	ProductController::class, 'index']);
```

Contoh lain (Closure):
```php
Route::get('/', function () {
	return view('welcome');
});
```

dan nanti aku akan membahas penggunaan routes controller lebih lanjut di pembahasan [Routes Controller](Routes%20Controller.md)

---
## resources/
Kalau `app` adalah otak, maka `resources` adalah wajah aplikasi, Di dalamnya terdapat:
```
resources/views
```
Misalnya:
```
welcome.blade.php
```

atau
```
products/index.blade.php
```
Semua HTML biasanya berada di sini.

---

## database/
Folder ini berisi seluruh kebutuhan database.
```
database/

migrations/
seeders/
factories/
```

Migration
```
Create users table
Create products table
```

Seeder
```
Isi data awal
```

Factory
```
Generate data palsu
```

Misalnya
```
ProductFactory
```
dapat menghasilkan
```
Laptop ASUS
Mouse Logitech
Keyboard Mechanical
```

ribuan data hanya dalam hitungan detik. Karena tidak ada yang waras mengisi 10.000 produk satu per satu hanya demi menguji pagination.

---
## public/

Ini satu-satunya folder yang boleh diakses browser karena di dalamnya terdapat:
```
index.php
```
Semua request Laravel selalu dimulai dari file ini.

Kalau kamu upload gambar
```
storage:link
```
hasil akhirnya juga akan bisa diakses melalui folder `public`.

---
## config/
Menyimpan semua konfigurasi Laravel, Misalnya:
```
config/app.php
config/database.php
config/cache.php
```
Kalau ingin mengubah database default, timezone, locale, cache, mail, hampir semuanya ada di folder ini.

---
## storage/
Laravel menyimpan banyak hal di sini, Misalnya:

```
logs
```

Kalau aplikasi error
```
storage/logs/laravel.log
```
adalah tempat pertama yang wajib kamu buka.

Selain itu ada
```
storage/app
storage/framework
```
untuk cache, session, upload, dan file lainnya.

---
## vendor/
Folder ini berisi seluruh library dari Composer, Misalnya

```
Laravel Framework
Monolog
Symfony
Carbon
Guzzle
```
Semua berada di sini.

Karena dibuat otomatis oleh Composer, **jangan pernah mengedit isi folder `vendor`**. Kalau kamu mengubahnya, pembaruan Composer berikutnya akan menimpa semua perubahanmu. Ibarat mengecat mobil orang lain yang sedang dipinjam.

# Gambaran besar
Sekarang coba lihat alurnya sekali lagi.

```
Browser
↓
public/
↓
routes/
↓
Controller
↓
Model
↓
Database
↓
Controller
↓
Blade
↓
Browser
```

Kalau kamu memahami alur ini, nanti saat belajar Middleware, Dependency Injection, Service Container, hingga Filament, semuanya terasa jauh lebih masuk akal karena mereka hanya "menyisip" di beberapa titik dalam alur tersebut.