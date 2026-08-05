#programming 
Bayangkan kamu memiliki website toko, kalau hanya ada halaman daftar produk, URL berikut sudah cukup.
```
/products
```

Tetapi bagaimana jika user ingin melihat **produk tertentu**?
Misalnya:
```
/products/1
/products/2
/products/15
/products/999
```

Tidak mungkin kita membuat route seperti ini:
```
Route::get('/products/1', ...);
Route::get('/products/2', ...);
Route::get('/products/3', ...);
Route::get('/products/4', ...);
```
Kalau produknya ada 100.000, apakah kita akan membuat 100.000 route? Tentu tidak. Komputer memang cepat, tapi tidak perlu diajak melakukan pekerjaan yang tidak masuk akal.

Laravel menyediakan **Route Parameter** untuk mengatasi masalah ini.

# Apa itu Route Parameter?

Route Parameter adalah bagian URL yang nilainya **berubah-ubah**.

Sintaksnya menggunakan `{}`.
```
Route::get('/products/{id}', function ($id) {
    return "Product ID : " . $id;
});
```

Perhatikan bagian:
```
{id}
```
Artinya:
> "Laravel, apa pun yang berada setelah `/products/`, simpan ke variabel `$id`."

---

# Cara Kerjanya

Misalnya user membuka:
```
/products/10
```

Laravel membaca route:
```
/products/{id}
```

Kemudian menganggap seolah-olah melakukan ini:
```
$id = 10;
```

Lalu menjalankan:
```
return "Product ID : " . $id;
```

Hasilnya:
```
Product ID : 10
```

Kalau URL:
```
/products/999
```

Maka:
```
$id = 999;
```

Output:
```
Product ID : 999
```

Tidak ada batasan jumlah angka. Selama URL cocok, Laravel akan mengambil nilainya.

---

# Nama Parameter Bebas

Banyak pemula mengira harus memakai `{id}`, Padahal bebas, Misalnya:
```php
Route::get('/products/{angka}', function ($angka) {
    return $angka;
});
```

atau
```php
Route::get('/products/{productId}', function ($productId) {
    return $productId;
});
```
Semuanya benar.

Yang penting:
```php
{productId}
```

harus sama dengan
```
$productId
```

---

# Kalau Namanya Berbeda?

Misalnya:
```php
Route::get('/products/{id}', function ($productId) {

});
```
Ini salah.

Karena Laravel akan mencari parameter bernama:
```
productId
```

Padahal yang ada di URL adalah:
```
id
```

Nama parameter route dan nama argumen function **harus sama**.

---

# Lebih dari Satu Parameter

Misalnya URL:
```
/users/yanda/posts/25
```

Route:
```php
Route::get('/users/{username}/posts/{post}', function ($username, $post) {

    return "User : $username <br> Post : $post";

});
```

Kalau dibuka:
```
/users/yanda/posts/25
```

Output:
```
User : yanda
Post : 25
```

Laravel mengambil parameter sesuai urutannya.

---

# Parameter Opsional

Kadang kita ingin parameter boleh ada, boleh tidak, Misalnya:
```
/profile
```

atau
```
/profile/yanda
```

Bisa menggunakan tanda `?`.
```php
Route::get('/profile/{name?}', function ($name = "Guest") {

    return "Halo " . $name;

});
```

Kalau membuka:

```
/profile
```

Output:
```
Halo Guest
```

Kalau membuka:
```
/profile/Yanda
```

Output:
```
Halo Yanda
```

Perhatikan bahwa parameter opsional **harus memiliki nilai default** pada function.
```
function ($name = "Guest")
```

Kalau tidak diberi default, PHP akan mengeluh karena `$name` bisa saja tidak dikirim.

---

# Constraint Parameter

Secara default Laravel menerima apa saja, Misalnya:

```
/products/abc
/products/123
/products/laravel
/products/!!!!
```
Semuanya dianggap valid.

Kalau hanya ingin menerima angka:
```php
Route::get('/products/{id}', function ($id) {
    return $id;
})->whereNumber('id');
```

Sekarang:
```
/products/10
```
✅ Berhasil

Sedangkan:
```
/products/abc
```
akan menghasilkan:
```
404 Not Found
```
Karena `abc` bukan angka.

---

# Constraint Lain

Laravel menyediakan beberapa helper.

Huruf saja:
```
->whereAlpha('name')
```

Huruf dan angka:
```
->whereAlphaNumeric('username')
```

UUID:
```
->whereUuid('id')
```

Regex sendiri:
```
->where('id', '[0-9]+')
```

Yang terakhir lebih fleksibel, tetapi biasanya helper bawaan sudah cukup.

---

# Route Parameter di Controller

Dalam proyek nyata, route parameter hampir selalu dikirim ke Controller.
```php
Route::get('/products/{id}', [ProductController::class, 'show']);
```

Controller:
```php
class ProductController extends Controller
{
    public function show($id)
    {
        return "Product ID : " . $id;
    }
}
```

Kalau membuka:
```
/products/25
```

Laravel akan memanggil:
```
show(25);
```

---

# Hubungan dengan Database

Misalnya tabel `products`:

|id|name|
|---|---|
|1|Laptop|
|2|Mouse|
|3|Keyboard|

Saat user membuka:
```
/products/2
```

Controller menerima:
```
$id = 2;
```

Lalu bisa mengambil data:
```php
$product = Product::find($id);
```

Di balik layar, Eloquent menjalankan query yang setara dengan:
```sql
SELECT * FROM products
WHERE id = 2;
```

Inilah alasan Route Parameter menjadi dasar sebelum belajar Eloquent dan CRUD.

---

# Best Practice

Untuk parameter, gunakan nama yang menggambarkan isinya.

Lebih baik:
```
/products/{product}
```

daripada:
```
/products/{x}
```

Karena saat route semakin banyak, nama yang jelas akan jauh lebih mudah dipahami.

---
# Latihan Route Parameter
[Latihan Route Parameter](Latihan%20Route%20Parameter.md)
