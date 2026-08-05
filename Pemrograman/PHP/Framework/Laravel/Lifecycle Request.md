#programming 

> **Apa yang sebenarnya terjadi ketika kita membuka sebuah URL Laravel?**

Misalnya mengetik:
```
http://localhost:8000/products
```
Lalu menekan Enter.

Yang terjadi bukan langsung menjalankan `ProductController`, tetapi masih ada banyak tahapan yang dilewati, Kalau kita sederhanakan, alurnya seperti ini:
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
Service Container
    │
    ▼
Service Provider
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
View / JSON
    │
    ▼
Browser
```
Mari kita bedah satu per satu.

---
# 1. Browser Mengirim Request

Misalnya kamu membuka
```
/products
```
Browser akan mengirim HTTP Request Isinya bisa berupa:
```
GET /products HTTP/1.1
Host: localhost:8000
Accept: text/html
Cookie: ...
```
Laravel menerima request tersebut.

---
# 2. public/index.php

Semua request Laravel **selalu** masuk ke file ini.

```
public/
    index.php
```
Inilah pintu utama aplikasi.

Mau membuka:
```
/
/products
/login
/admin
```

Semuanya tetap masuk ke:
```
public/index.php
```
Makanya file ini sering disebut **Front Controller**, Artinya hanya ada **satu pintu masuk**.

# Kenapa hanya satu pintu?

Bayangkan sebuah mall kalau semua orang boleh masuk lewat jendela, pintu belakang, atap, bahkan ventilasi, satpam bakal menyerah dan pulang, Makanya mall punya satu pintu utama.

Laravel juga begitu, Semua request harus melewati pintu yang sama.

---
# 3. Bootstrap Laravel

Setelah masuk ke `index.php`, Laravel mulai "bangun", Ibarat kamu baru menyalakan komputer.
Yang dilakukan Laravel misalnya:
- membaca konfigurasi
- membaca `.env`
- mempersiapkan autoload Composer
- menyiapkan aplikasi
Saat tahap ini belum ada route yang dijalankan. 
Laravel baru bersiap bekerja.

---
# 4. Service Container

Nah... Ini bagian yang sering membuat pemula bingung, Untuk sekarang anggap saja begini:
Service Container adalah **gudang objek**.

Misalnya nanti controller membutuhkan:
```
ProductService
```

Tanpa menulis:
```php
$productService = new ProductService();
```
Laravel otomatis membuatkannya. Kenapa bisa? Karena Service Container yang mengurus.

Nanti kita pelajari khusus satu bab penuh.

---
# 5. Service Provider

Kalau Service Container adalah gudang, Service Provider adalah **orang yang mengisi gudang**.

Misalnya Laravel perlu:
- Database
- Cache
- Session
- Mail
- Queue
Semuanya didaftarkan di Service Provider. 

Tanpa Service Provider laravel tidak tahu harus membuat service apa.

---
# 6. Routing

Sekarang Laravel mulai melihat URL, Misalnya ada request
```
/products
```

Laravel membuka
```
routes/web.php
```

Kemudian mencari
```
Route::get('/products', ...);
```

Kalau ketemu Laravel tahu request harus dikirim ke mana.

Kalau tidak ada, langsung
```
404 Not Found
```

---
# 7. Middleware

Sebelum masuk Controller, Laravel bertanya dulu
> "Boleh nggak user ini masuk?"

Misalnya ada middleware:
```
->middleware('auth')
```

Kalau belum login Laravel menghentikan request.

Controller bahkan **tidak dijalankan**. Misalnya.
```
Request
↓
Middleware
↓
Belum Login
↓
Redirect Login
```
Controller tidak pernah dipanggil.

---
# 8. Controller

Barulah sekarang controller dijalankan.

Misalnya
```php
Route::get('/products', [ProductController::class, 'index']);
```

Laravel memanggil
```php
public function index()
{

}
```

Controller adalah tempat logika aplikasi. Misalnya
```php
$products = Product::all();
```

---

# 9. Model

Controller sering memanggil Model.
Misalnya
```php
Product::all();
```
Model bertugas berbicara dengan database karena Controller **tidak menulis SQL secara langsung** dan yang melakukannya adalah Eloquent.

---
# 10. Database

Barulah query dijalankan.
Misalnya

```sql
SELECT *
FROM products;
```
Database mengirim data kembali.

---

# 11. Response

Controller menerima data.

Misalnya
```php
return view('products.index', compact('products'));
```

atau
```php
return response()->json($products);
```
Laravel mengubahnya menjadi HTTP Response.

Misalnya
```
HTTP/1.1 200 OK
Content-Type: text/html
```
Lalu browser menampilkan hasilnya.

---

# Contoh Nyata

Misalnya kamu membuka:
```
/products
```

Di `web.php` ada:
```php
Route::get('/products', [ProductController::class, 'index']);
```

Controller:
```php
public function index()
{
    $products = Product::all();

    return view('products.index', compact('products'));
}
```

Maka yang terjadi:
```
Browser
    │
    ▼
GET /products
    │
    ▼
public/index.php
    │
    ▼
Bootstrap Laravel
    │
    ▼
Service Container
    │
    ▼
Service Provider
    │
    ▼
Routing
    │
    ▼
Middleware
    │
    ▼
ProductController@index
    │
    ▼
Product::all()
    │
    ▼
MySQL
    │
    ▼
Data Product
    │
    ▼
View products/index.blade.php
    │
    ▼
HTML
    │
    ▼
Browser
```

---

# Kenapa Lifecycle Penting?

Sekarang mungkin kamu merasa, "Yang penting kan aplikasinya jalan."
Memang. Tapi hampir semua fitur besar Laravel bekerja dengan **menyisip di titik-titik lifecycle**:
- **Middleware** bekerja sebelum Controller.
- **Dependency Injection** memanfaatkan Service Container sebelum Controller dibuat.
- **Authentication** mengecek pengguna di Middleware.
- **Validation** biasanya dilakukan saat request masuk ke Controller.
- **Eloquent** baru aktif ketika Controller meminta data.
- **Blade** baru dirender setelah Controller selesai bekerja.
- **Filament** yang sudah kamu pelajari pun berdiri di atas alur yang sama. Ia tidak membuat jalur baru, hanya memanfaatkan mekanisme Laravel yang sudah ada.

Begitu kamu memahami alur ini, materi seperti Service Container, Service Provider, Middleware, Event, Queue, bahkan Package Development akan terasa saling terhubung, bukan sekadar kumpulan fitur acak.