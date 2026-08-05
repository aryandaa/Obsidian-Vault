#programming 
Misalnya sekarang kita punya route seperti ini:
```php
Route::get('/products', [ProductController::class, 'index']);
```

Lalu di Blade kita membuat tombol.
```html
<a href="/products">Lihat Produk</a>
```

Kelihatannya tidak ada masalah, Tetapi bagaimana kalau suatu hari bos atau client berkata:
> "URL `/products` diganti menjadi `/barang` ya."

Maka kamu harus mencari semua kode yang berisi:
```
/products
```

Mungkin ada di:
- Blade
- Controller
- Redirect
- Middleware
- JavaScript
- Email
- API
Kalau project sudah berisi 500 file, pekerjaan ini menyebalkan. Satu URL berubah bisa membuat puluhan file ikut diubah.

Laravel punya solusi.
# Apa itu Named Route?

Named Route adalah **memberi nama pada route**, sehingga aplikasi tidak bergantung langsung pada URL.

Misalnya route:
```php
Route::get('/products', [ProductController::class, 'index'])
    ->name('products.index');
```

Perhatikan bagian:
```php
->name('products.index')
```

Sekarang route ini memiliki nama.
```
products.index
```

Nama inilah yang nanti dipakai di seluruh aplikasi

# Kenapa lebih baik?

Misalnya Blade tanpa Named Route
```html
<a href="/products">Produk</a>
```

Dengan Named Route
```html
<a href="{{ route('products.index') }}">Produk</a>
```

Apa bedanya?

Misalnya besok URL berubah menjadi
```php
Route::get('/barang', ...)
```

cukup ubah route menjadi
```php
Route::get('/barang', [ProductController::class, 'index'])
    ->name('products.index');
```

Blade **tidak perlu diubah sama sekali**, Karena Blade hanya mengenal
```php
route('products.index')
```

Laravel yang akan mencari URL sebenarnya.

# Cara Kerjanya

Misalnya route:
```php
Route::get('/products', [ProductController::class, 'index'])
    ->name('products.index');
```

Saat Blade memanggil
```php
route('products.index')
```

Laravel melakukan pencarian seperti ini (konsepnya):

```
Nama Route

products.index
↓
Cari URL
↓
/products
↓
Kembalikan URL
```

Jadi hasil akhirnya menjadi
```
/products
```

Kalau URL berubah menjadi

```
/produk
```

Laravel otomatis menghasilkan
```
/produk
```

tanpa mengubah Blade.

---

# Named Route dengan Parameter

Misalnya route:
```php
Route::get('/products/{id}', [ProductController::class, 'show'])
    ->name('products.show');
```

Sekarang ada parameter.

Kalau menggunakan URL biasa:
```html
<a href="/products/5">Detail</a>
```

Dengan Named Route:
```php
<a href="{{ route('products.show', 5) }}">
    Detail
</a>
```

atau lebih jelas:
```html
<a href="{{ route('products.show', ['id' => 5]) }}">
    Detail
</a>
```

Laravel menghasilkan:
```
/products/5
```

Kalau:
```
'id' => 20
```

hasilnya
```
/products/20
```

---

# Redirect Menggunakan Named Route

Misalnya setelah menyimpan produk.

Daripada
```php
return redirect('/products');
```

lebih baik
```php
return redirect()->route('products.index');
```

Kenapa? Karena kalau URL berubah redirect tetap berjalan.

---

# Cara Melihat Semua Nama Route

Laravel menyediakan:
```shell
php artisan route:list
```

Misalnya hasilnya:
```
GET  /products        products.index
GET  /products/{id}   products.show
POST /products        products.store
```

Kolom paling kanan menunjukkan nama route.

Kalau suatu hari muncul error:
```
Route [products.index] not defined.
```

Perintah `route:list` hampir selalu menjadi tempat pertama untuk mengecek apakah nama route benar-benar sudah terdaftar.

---

# Konvensi Penamaan

Laravel memiliki kebiasaan penamaan seperti ini:

|Fungsi|Nama Route|
|---|---|
|Daftar Produk|`products.index`|
|Detail Produk|`products.show`|
|Form Tambah|`products.create`|
|Simpan Produk|`products.store`|
|Form Edit|`products.edit`|
|Update Produk|`products.update`|
|Hapus Produk|`products.destroy`|

Kenapa memakai titik (`.`)? Karena titik membantu mengelompokkan route berdasarkan resource.

Semua route produk diawali dengan:
```
products.
```

Semua kategori nanti:
```
categories.
```

Ini membuat project besar jauh lebih rapi.

### Latihan Named Route
[Latihan Named Route](Latihan%20Named%20Route.md)
