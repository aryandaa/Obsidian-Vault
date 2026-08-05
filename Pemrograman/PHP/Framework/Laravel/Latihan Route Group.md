#latihan 
Jangan buat project baru. Rapikan route yang sudah ada.
### Latihan 1

Kelompokkan seluruh route produk menggunakan:
```php
Route::prefix('products')
```

Pastikan URL yang dihasilkan tetap sama.

---

### Latihan 2

Tambahkan:
```php
->name('products.')
```

Sehingga route menjadi:
```
products.index
products.show
products.store
```
tanpa menulis `products.` berulang-ulang.

---

### Latihan 3

Gunakan:
```php
Route::controller(ProductController::class)
```

Sehingga di dalam group cukup menulis:
```
'index'
```

bukan lagi:
```
[ProductController::class, 'index']
```

---

### Latihan 4

Buat Route Group untuk Category.

Gunakan:

- Prefix `categories`
- Name prefix `categories.`
- Controller `CategoryController`

Lalu pindahkan route kategori yang sudah kita buat ke dalam group tersebut.

---

### Latihan 5

Jalankan lagi:

```
php artisan route:list
```

Pastikan:

- URL tetap sama.
- Nama route tetap sama.
- Semua route tetap bisa diakses.

Kalau hasil `route:list` tidak berubah selain urutan atau format, berarti refactor berhasil. Itulah tujuan Route Group: **merapikan kode tanpa mengubah perilaku aplikasi**.

### Jawaban:
```php
// Product Routes
Route::prefix('products')
    ->controller(ProductController::class)
    ->name('products.')
    ->group(function () {

        Route::get('/', 'index')->name('index');
        Route::get('/{id}', 'show')
            ->whereNumber('id')
            ->name('show');

    });

// Category Routes
Route::prefix('categories')
    ->controller(CategoryController::class)
    ->name('categories.')
    ->group(function () {

        Route::get('/', 'index')->name('index');
        Route::get('/{id}', 'show')
            ->whereNumber('id')
            ->name('show');

    });

// Product by Category
Route::controller(ProductController::class)
    ->group(function () {

        Route::get('/categories/{category}/products', 'indexByCategory')
            ->name('categories.products.index');

    });
```
