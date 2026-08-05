#latihan 
## Latihan 1 - Detail Produk
Sekarang toko kita memiliki halaman daftar produk.

Tambahkan route baru:
```
/products/{id}
```

Ketika membuka
```
/products/10
```

hasilnya
```
=== Detail Produk ===
ID Produk : 10
```

Gunakan **Controller**, jangan Closure.

Method yang dibuat:
```
show($id)
```

---
## Latihan 2 - Detail Kategori

Sebuah toko memiliki kategori.

Tambahkan route
```
/categories/{id}
```

Controller:
```
CategoryController
```

Method:
```
show($id)
```

Output:
```
=== Detail Category ===
ID Category : 5
```

Jika membuka
```
/categories/5
```

Kalau controller belum ada, buat menggunakan Artisan.

---

## Latihan 3 - Produk dalam Kategori

Sekarang kita ingin melihat semua produk berdasarkan kategori.

URL:
```
/categories/{category}/products
```

Contoh:
```
/categories/laptop/products
```

Output:
```
Kategori : laptop
```

Gunakan Controller.

Method:
```
indexByCategory($category)
```

---

## Latihan 4 - Profile User

Tambahkan route:
```
/profile/{username?}
```

Jika
```
/profile
```

Output:
```
Selamat Datang Guest
```

Jika
```
/profile/yanda
```

Output:
```
Selamat Datang yanda
```

Boleh menggunakan Closure untuk latihan ini karena masih sangat sederhana.

---

## Latihan 5 - Validasi Parameter

Tambahkan route:
```
/orders/{id}
```
Tetapi hanya menerima angka.

Misalnya
```
/orders/15
```

Output:
```
Order #15
```

Sedangkan
```
/orders/abc
```

Harus menjadi
```
404 Not Found
```

Gunakan:
```
->whereNumber('id')
```

# jawaban:

## Latihan 1
```php
Route::get('/products/{id}', [ProductController::class, 'show'])->whereNumber('id');
```

```php
public function show($id){
	return "Product ID : " . $id;
}
```

## Latihan 2
```php
Route::get('/categories/{id}', [CategoryController::class, 'show'])->whereNumber('id');
```

```php
public function show($id){
	return "ID Category : " . $id;
}
```

## Latihan 3
```php
Route::get('/categories/{category}/products', [ProductController::class, 'indexByCategory']);
```

```php
public function indexByCategory($category){
	return "Kategori : " . $category;
}
```

## Latihan 4
```php
Route::get('/profile/{username?}', [ProfileController::class, 'Showname'])->whereAlpha('username');
```

```php
public function Showname($username = "Guest"){
	return "Selamat Datang " . $username;
}
```

## Latihan 5
> Sdh aku gabung semua di latihan sebelumnya