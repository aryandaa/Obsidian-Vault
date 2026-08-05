#programming 
Kalau diminta menjelaskan routing dalam satu kalimat, aku akan bilang:
> **Routing adalah peta yang memberitahu Laravel request ini harus dikirim ke mana.**

Misalnya seseorang membuka:
```
http://localhost:8000/products
```
Laravel tidak akan menebak-nebak harus membuka file mana.

Yang pertama kali dilakukan adalah membuka:
```
routes/web.php
```

Misalnya isi file tersebut:
```php
Route::get('/products', function () {
    return 'Daftar Produk';
});
```
Saat URL `/products` dibuka, Laravel membaca route tersebut dan menjalankan function di dalamnya.

Alurnya sederhana:
```
Browser
    │
GET /products
    │
    ▼
routes/web.php
    │
    ▼
Route cocok?
    │
    ▼
Jalankan Closure / Controller
    │
    ▼
Kirim Response
```

Kalau tidak ada route yang cocok?
```
404 Not Found
```

Tidak ada sihir. Laravel hanya mencocokkan URL dengan daftar route yang kamu buat.

---
# Route::get()

Method yang paling sering kamu lihat adalah:
```php
Route::get('/products', function () {
    return 'Daftar Produk';
});
```

Artinya:
- `Route` → kelas untuk mendefinisikan route.
- `get()` → hanya menerima HTTP GET.
- `/products` → URL yang dicocokkan.
- `function () {}` → kode yang dijalankan jika URL cocok.

Kalau browser membuka:
```
/products
```

hasilnya:
```
Daftar Produk
```

---

# HTTP Method

Di web, request tidak hanya GET, Ada beberapa method yang paling sering digunakan.

## GET
Digunakan untuk **mengambil data**.

```php
Route::get('/products', function () {
    return 'Semua Produk';
});
```

Contoh:
```
GET /products
```

dan cuman mengambil/menampilkan, tidak akan mengubah data tersebut.

---
## POST
Digunakan untuk **mengirim atau menyimpan data**.

```php
Route::post('/products', function () {
    return 'Produk berhasil ditambah';
});
```

Misalnya form:
```
<form method="POST">
```

akan mengirim request POST.

---
## PUT
Digunakan untuk **mengubah seluruh data**.

```php
Route::put('/products/{id}', function ($id) {
    return "Update $id";
});
```

---
## PATCH

Digunakan untuk **mengubah sebagian data**.
Secara praktik di Laravel, PUT dan PATCH sering diperlakukan hampir sama. Perbedaannya berasal dari standar HTTP:

- **PUT** berarti mengganti keseluruhan resource.
- **PATCH** berarti hanya memperbarui sebagian field.

Contoh:
```php
Route::patch('/products/{id}', function ($id) {
    return "Update sebagian data $id";
});
```

---

## DELETE
Digunakan untuk menghapus data.

```php
Route::delete('/products/{id}', function ($id) {
    return "Hapus Product $id";
});
```

---

# Ringkasan CRUD
Kalau nanti membuat CRUD Product, biasanya seperti ini:

|Method|URL|Fungsi|
|---|---|---|
|GET|`/products`|Menampilkan semua produk|
|GET|`/products/create`|Menampilkan form tambah|
|POST|`/products`|Menyimpan produk|
|GET|`/products/{id}`|Menampilkan satu produk|
|GET|`/products/{id}/edit`|Menampilkan form edit|
|PUT/PATCH|`/products/{id}`|Mengubah produk|
|DELETE|`/products/{id}`|Menghapus produk|

Kalau tabel ini terasa familiar nanti, itu karena `Route::resource()` akan membuat semuanya secara otomatis.

---
# Mengembalikan Response

Route tidak harus mengembalikan string.
Misalnya:

```php
Route::get('/', function () {
    return view('welcome');
});
```
Laravel akan mengirim sebuah View.

Bisa juga mengembalikan array:
```php
Route::get('/user', function () {
    return [
        'name' => 'Yanda',
        'role' => 'Developer',
    ];
});
```
Laravel otomatis mengubahnya menjadi JSON.

Hasilnya:
```json
{
    "name": "Yanda",
    "role": "Developer"
}
```

Ini salah satu fitur yang membuat Laravel enak dipakai untuk membuat REST API.

---

# Urutan Route Itu Penting

Laravel membaca route **dari atas ke bawah**.

Misalnya:
```php
Route::get('/products/{id}', function ($id) {
    return $id;
});

Route::get('/products/create', function () {
    return 'Form Create';
});
```

Kalau membuka:
```
/products/create
```

Yang terjadi justru:
```
create
```
Karena Laravel menganggap `"create"` adalah nilai dari `{id}`.

Solusinya:
```php
Route::get('/products/create', function () {
    return 'Form Create';
});

Route::get('/products/{id}', function ($id) {
    return $id;
});
```
Route yang lebih spesifik sebaiknya ditulis lebih dulu daripada route yang menggunakan parameter.

---
# Route ke Controller

Dalam proyek sungguhan, route jarang berisi logika.

Biasanya seperti ini:
```php
use App\Http\Controllers\ProductController;

Route::get('/products', [ProductController::class, 'index']);
```

Artinya:
- buka URL `/products`
- buat objek `ProductController`
- jalankan method `index()`

Controller:
```php
class ProductController extends Controller
{
    public function index()
    {
        return "Daftar Produk";
    }
}
```
Inilah pola yang akan hampir selalu kamu lihat di proyek Laravel profesional.

---

# Cara Melihat Semua Route
Laravel menyediakan perintah yang sangat berguna:

```shell
php artisan route:list
```

Misalnya hasilnya:
```
GET      /                 Closure
GET      /products         ProductController@index
POST     /products         ProductController@store
GET      /login            LoginController@index
```

Kalau suatu hari route terasa "tidak jalan", `route:list` adalah salah satu tempat pertama yang perlu dicek. Ia menunjukkan route yang benar-benar dikenali Laravel, bukan yang kita kira sudah dibuat.

---

# Kesalahan yang Sering Dilakukan Pemula

1. Lupa mengimpor controller.
```php
use App\Http\Controllers\ProductController;
```

2. Salah HTTP method.
Misalnya route menggunakan:
```
Route::post(...)
```
tetapi browser mengaksesnya dengan GET.

Hasilnya:
```
405 Method Not Allowed
```

3. Salah urutan route sehingga parameter menangkap URL yang seharusnya spesifik.
4. Menaruh terlalu banyak logika di dalam route.

Route sebaiknya hanya bertugas mengarahkan request, sedangkan logika bisnis berada di Controller atau Service.

---

# Latihan
Kerjakan sendiri tanpa melihat jawaban: [Latihan Dasar Routing](Latihan%20Dasar%20Routing.md)
