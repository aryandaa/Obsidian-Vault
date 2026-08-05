#programming 
Contoh Syntax Rountes Controller
```php
Route::get('/products', [
	ProductController::class, 'index']);
```
Artinya:
> Kalau ada request ke `/products`, jalankan method `index()`.

Misalnya kamu punya controller seperti ini:
```php
class ProductController extends Controller
{
    public function index()
    {
        return view('products.index');
    }
}
```
Jadi alurnya menjadi:
```
Browser
    │
    ▼
Route
    │
    ▼
ProductController@index
    │
    ▼
View
```


Dan contoh dari routes Closure:
```php
Route::get('/', function () {
	return view('welcome');
});
```
Di sini **tidak ada controller** tetapi Route langsung menjalankan sebuah **anonymous function (Closure)**  yang artinya kamu Seolah-olah kamu sedang menulis ini:
```php
function () {
    return view('welcome');
}
```
dan alurnya akan menjadi seperti
```
Browser
    │
    ▼
Route
    │
    ▼
Closure
    │
    ▼
View
```

### Closure
Bayangkan sebuah restoran Menggunakan Closure
```
Pelanggan
     │
     ▼
Kasir
     │
langsung membuat makanan
```
Kasir menerima pesanan sekaligus memasak, apakah Bisa? Bisa, Kalau restorannya cuma menjual mie instan, mungkin tidak masalah.

---
### Controller
```
Pelanggan
      │
      ▼
Kasir
      │
      ▼
Dapur
      │
      ▼
Chef
      │
      ▼
Makanan
```
Kasir hanya menerima pesanan, Yang memasak adalah chef.

dan jadi Lebih rapi karena setiap orang punya tugas masing-masing, diLaravel juga harus begitu.

---
## Kenapa project Laravel besar hampir selalu memakai Controller?

Misalnya nanti halaman `/products` harus:
- mengambil data database,
- menghitung diskon,
- mengecek login,
- melakukan pagination,
- mengirim event,
- mencatat log.

Kalau semuanya ditulis di route:
```php
Route::get('/products', function () {
    $products = Product::where('active', true)
        ->orderBy('created_at', 'desc')
        ->paginate(10);

    // validasi
    // logging
    // event
    // diskon
    // dll...

    return view('products.index', compact('products'));
});
```

Lama-lama `web.php` bisa berisi ratusan bahkan ribuan baris. Setiap membuka file itu rasanya seperti membuka gulungan kitab kuno yang tidak ada ujungnya.

tapi kalau memakai controller:
```php
Route::get('/products', [
	ProductController::class, 'index'
	]);
```
Maka semua logika dipindahkan ke:
```
ProductController
```
Sehingga `web.php` tetap bersih.

---

## Kapan memakai Closure?
Closure cocok untuk hal-hal sederhana, misalnya:

```php
Route::get('/', function () {
    return view('welcome');
});
```
atau
```php
Route::get('/about', function () {
    return "Tentang Kami";
});
```
atau ketika sedang mencoba fitur dengan cepat saat development.

---
## Kapan memakai Controller?
Begitu route mulai memiliki logika, apalagi berhubungan dengan database, hampir selalu gunakan Controller.

Contohnya:
```php
Route::get('/products', [ProductController::class, 'index']);
Route::post('/products', [ProductController::class, 'store']);
Route::put('/products/{product}', [ProductController::class, 'update']);
Route::delete('/products/{product}', [ProductController::class, 'destroy']);
```
Ini adalah cara yang digunakan di hampir semua proyek Laravel profesional.

### Jadi kesimpulannya

|Closure|Controller|
|---|---|
|Langsung menjalankan fungsi di route|Memanggil method pada class Controller|
|Cocok untuk route sederhana|Cocok untuk logika aplikasi|
|Cepat dibuat|Lebih rapi dan mudah dipelihara|
|Tidak dianjurkan untuk aplikasi besar|Standar pada proyek Laravel nyata|
