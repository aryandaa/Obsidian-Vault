#programming 
Sebelum belajar sintaks, mari lihat masalahnya dulu.

Misalnya kita punya route seperti ini.
```php
Route::get('/products', [ProductController::class, 'index'])
    ->name('products.index');

Route::get('/products/{id}', [ProductController::class, 'show'])
    ->whereNumber('id')
    ->name('products.show');

Route::post('/products', [ProductController::class, 'store'])
    ->name('products.store');

Route::put('/products/{id}', [ProductController::class, 'update'])
    ->whereNumber('id')
    ->name('products.update');

Route::delete('/products/{id}', [ProductController::class, 'destroy'])
    ->whereNumber('id')
    ->name('products.destroy');
```

Lihat sesuatu? Semuanya diawali dengan
```
/products
```

Kalau nanti ada 20 route produk? Semuanya tetap menulis
```
/products
```
berulang-ulang.

Inilah alasan Route Group dibuat.

# Apa itu Route Group?

Route Group adalah cara mengelompokkan route yang memiliki kesamaan.

Kesamaan itu bisa berupa:
- Prefix URL
- Middleware
- Nama Route
- Controller
- Domain

Kita akan pelajari satu per satu.

---

# 1. Prefix

Yang paling sering digunakan.

Tadi kita punya lima route.

Sekarang kita kelompokkan.

```php
Route::prefix('products')->group(function () {

    Route::get('/', [ProductController::class, 'index'])
        ->name('products.index');

    Route::get('/{id}', [ProductController::class, 'show'])
        ->whereNumber('id')
        ->name('products.show');

    Route::post('/', [ProductController::class, 'store'])
        ->name('products.store');

});
```

Perhatikan.

Di dalam group tidak lagi menulis

```
/products
```

cukup
```
/
```

atau
```
/{id}
```
Karena Laravel otomatis menambahkan prefix.

Misalnya:
```php
Route::prefix('products')
```

berarti semua route menjadi:
```
/products
/products/{id}
/products
```

---

# Cara Laravel Membacanya

Laravel menganggapnya seperti ini.
```
Prefix

/products
↓
Route /
↓
Hasil
/products
```

dan
```
Prefix

/products
↓
Route /{id}
↓
Hasil
/products/{id}
```

---

# 2. Name Prefix

Selain URL, kita juga bisa mengelompokkan nama route.

Misalnya Tanpa group.
```php
->name('products.index')

->name('products.show')

->name('products.store')
```
Berulang lagi.

Laravel menyediakan:
```php
Route::prefix('products')
    ->name('products.')
    ->group(function () {

        Route::get('/', [ProductController::class, 'index'])
            ->name('index');

        Route::get('/{id}', [ProductController::class, 'show'])
            ->name('show');

        Route::post('/', [ProductController::class, 'store'])
            ->name('store');

});
```

Perhatikan, Di dalam group cukup:
```php
->name('index')
```

Laravel otomatis menggabungkan.
```
products.
```

```
index
```

=

```
products.index
```

Begitu juga

```
products.show
products.store
```

---

# 3. Controller Group

Sekarang lihat ini.
```
[ProductController::class, ...]
```
Ditulis berkali-kali.

Laravel bisa menghilangkannya.
```php
Route::controller(ProductController::class)
    ->group(function () {
        Route::get('/products', 'index');
        Route::post('/products', 'store');
        Route::get('/products/{id}', 'show');

});
```
Sekarang cukup menulis nama method.

Lebih ringkas.

---

# Menggabungkan Semuanya

Inilah yang sering dipakai di project Laravel.
```php
Route::prefix('products')
    ->name('products.')
    ->controller(ProductController::class)
    ->group(function () {

        Route::get('/', 'index')
            ->name('index');

        Route::get('/{id}', 'show')
            ->whereNumber('id')
            ->name('show');

        Route::post('/', 'store')
            ->name('store');

        Route::put('/{id}', 'update')
            ->whereNumber('id')
            ->name('update');

        Route::delete('/{id}', 'destroy')
            ->whereNumber('id')
            ->name('destroy');

});
```

Sekarang jauh lebih rapi.

---

# 4. Middleware Group

Nanti setelah belajar Authentication, Misalnya semua halaman admin harus login.

Daripada
```php
Route::get(...)
    ->middleware('auth');

Route::post(...)
    ->middleware('auth');

Route::delete(...)
    ->middleware('auth');
```

cukup
```php
Route::middleware('auth')
    ->group(function () {

        // semua route

});
```

Semua route di dalamnya otomatis memakai middleware tersebut.

---

# Kenapa Route Group Penting?

Bayangkan project kita nanti.
```
Products

7 route
```

```
Categories

7 route
```

```
Orders

8 route
```

```
Users

8 route
```

```
Dashboard

5 route
```

Total bisa lebih dari 35 route, Kalau semuanya ditulis tanpa group, file `web.php` akan cepat menjadi sulit dibaca.

Dengan Route Group, setiap resource punya "blok" sendiri sehingga lebih mudah dinavigasi.

## Latihan Route Group
[Latihan Route Group](Latihan%20Route%20Group.md)

