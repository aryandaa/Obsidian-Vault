#programming 
Jangan hapus kode sebelumnya, cukup tambahkan atau ubah.
### Latihan 1

Tambahkan nama route pada halaman daftar produk:
```
/products
```

Nama route:
```
products.index
```

---

### Latihan 2

Tambahkan nama route pada halaman detail produk:
```
/products/{id}
```

Nama route:
```
products.show
```

---

### Latihan 3

Tambahkan nama route pada halaman detail kategori:
```
/categories/{id}
```

Nama route:
```
categories.show
```

---

### Latihan 4

Pada `ProductController`, buat method baru:
```
public function store()
{
    return redirect()->route('products.index');
}
```

Walaupun route `store` belum kita buat, latihan ini bertujuan membiasakan penggunaan `redirect()->route()` daripada `redirect('/products')`.

---

### Latihan 5

Jalankan:
```
php artisan route:list
```

Lalu amati hasilnya. Perhatikan bahwa sekarang akan muncul kolom **Name** yang berisi `products.index`, `products.show`, dan seterusnya. Biasakan mengecek `route:list` setiap selesai menambah route baru. Ini adalah alat debugging yang sangat sering dipakai developer Laravel.

## Jawaban:

## Latihan 1
```php
Route::get('/products', [
	ProductController::class, 'index'
]) -> name('products.index');
```

## Latihan 2
```php
Route::get('/products/{id}', [ProductController::class, 'show'])
	->whereNumber('id')
	->name('products.show');
```

## Latihan 3
```php
Route::get('/categories/{id}', [CategoryController::class, 'show'])
	->whereNumber('id')
	->name('categories.show');
```

## Latihan 4
```php
public function store(){
	return redirect()->route('products.index');
}
```

## Latihan 5
```
┌─[r3x@parrot]─[~/Documents/Belajar/BelajarLaravel]
└──╼ $php artisan route:list

  GET|HEAD  / ............................................................................................. routes/web.php:10
  GET|HEAD  about ......................................................................................... routes/web.php:14
  GET|HEAD  categories/{category}/products ................................................ ProductController@indexByCategory
  GET|HEAD  categories/{id} ..................................................... categories.show › CategoriesController@show
  GET|HEAD  contact ....................................................................................... routes/web.php:18
  GET|HEAD  products ............................................................... products.index › ProductController@index
  GET|HEAD  products/{id} ............................................................ products.show › ProductController@show
  GET|HEAD  profile/{username?} .................................................................. ProfileController@Showname
  GET|HEAD  storage/{path} storage.local › vendor/laravel/framework/src/Illuminate/Filesystem/FilesystemServiceProvider.php:…
  PUT       storage/{path} storage.local.upload › vendor/laravel/framework/src/Illuminate/Filesystem/FilesystemServiceProvid…
  GET|HEAD  up .................. vendor/laravel/framework/src/Illuminate/Foundation/Configuration/ApplicationBuilder.php:224

                                                                                                          Showing [11] routes

```
disini sangat jelas terlihat penamaan dari route yang dibuat tadi.