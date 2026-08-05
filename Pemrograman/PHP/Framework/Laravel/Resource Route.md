#programming 
Menurutku ini adalah salah satu fitur Laravel yang paling "ajaib" saat pertama kali dipelajari. Setelah beberapa hari kita capek-capek menulis route satu per satu, sekarang Laravel berkata:
> "Sebenarnya... semua itu bisa ditulis dalam satu baris."

Untungnya kita **belajar manual dulu**. Jadi nanti kamu benar-benar mengerti apa yang dibuat oleh Laravel. Banyak orang langsung memakai `Route::resource()`, tetapi tidak tahu kenapa ada method `index`, `store`, `update`, dan `destroy`. Akibatnya saat ada error, mereka bingung harus mencari ke mana.

# Bab 8 - Resource Route

Sekarang project kita punya route seperti ini.

```php
Route::prefix('products')
    ->controller(ProductController::class)
    ->name('products.')
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

Padahal ini baru **5 route**, Kalau nanti ditambah:
- create
- edit
menjadi **7 route**.

Kalau ada Category? Tambah lagi 7 route.
Kalau Order? Tambah lagi 7 route.

Lama-lama `web.php` akan penuh.

# Apa itu Resource Route?

Laravel menyediakan:
```php
Route::resource('products', ProductController::class);
```
Selesai. Satu baris, Perintah di atas otomatis membuat:

|Method|URL|Controller|Name|
|---|---|---|---|
|GET|`/products`|index|products.index|
|GET|`/products/create`|create|products.create|
|POST|`/products`|store|products.store|
|GET|`/products/{product}`|show|products.show|
|GET|`/products/{product}/edit`|edit|products.edit|
|PUT/PATCH|`/products/{product}`|update|products.update|
|DELETE|`/products/{product}`|destroy|products.destroy|

Kalau diperhatikan, Ini persis seperti yang selama ini kita tulis manual.

Kenapa ada create dan edit? Karena CRUD lengkap terdiri dari:
```
Create
Read
Update
Delete
```

Laravel memisahkan:
```
create()
```
untuk menampilkan form.

Sedangkan
```
store()
```
untuk menyimpan data.

Begitu juga
```
edit()
```
menampilkan form edit.

Sedangkan
```
update()
```
menyimpan hasil edit.

Jadi:

```
GET  /products/create
```
↓
Menampilkan form.

```
POST /products
```
↓
Menyimpan data.

# Controller yang Sesuai

Karena Resource Route memiliki 7 route, Controller juga mempunyai 7 method.

```php
class ProductController extends Controller
{
    public function index()
    {

    }

    public function create()
    {

    }

    public function store()
    {

    }

    public function show($id)
    {

    }

    public function edit($id)
    {

    }

    public function update($id)
    {

    }

    public function destroy($id)
    {

    }
}
```

Makanya Laravel punya istilah **Resource Controller**.

---

# Membuat Resource Controller

Daripada membuat method satu-satu, Laravel menyediakan Artisan.
```shell
php artisan make:controller ProductController --resource
```

Laravel otomatis membuat:
```php
index()

create()

store()

show()

edit()

update()

destroy()
```
Kosong semua, Tinggal diisi.

---

# Cara Melihat Resource Route

Coba jalankan.
```shell
php artisan route:list
```

Kalau menggunakan
```php
Route::resource('products', ProductController::class);
```

hasilnya akan mirip:
```
GET      products
GET      products/create
POST     products
GET      products/{product}
GET      products/{product}/edit
PUT      products/{product}
DELETE   products/{product}
```

Beserta nama route-nya.

---

# Resource Route Tidak Wajib Dipakai

Ini penting, Banyak pemula mengira:
> Laravel harus memakai Resource Route.

Tidak, Kalau project hanya punya:
```
index
show
```
Boleh tetap manual.

Misalnya API pencarian.
```php
Route::get('/search', ...);
```
Tidak perlu dipaksa menjadi Resource.

Gunakan Resource hanya ketika memang membuat CRUD.

---

# only()

Misalnya project kita belum punya edit, Kita bisa membatasi.
```php
Route::resource('products', ProductController::class)
    ->only([
        'index',
        'show',
    ]);
```

Laravel hanya membuat:
```
products.index

products.show
```

---

# except()

Kebalikannya,Misalnya tidak ingin:
```
destroy
```

```php
Route::resource('products', ProductController::class)
    ->except([
        'destroy',
    ]);
```
Semua route dibuat, Kecuali destroy.

