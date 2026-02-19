### 1. Pengenalan Routing
Routing adalah cara untuk menentukan bagaimana aplikasi merespons permintaan URL tertentu. Di Laravel, routing didefinisikan di file `routes/web.php` untuk rute web dan `routes/api.php` untuk rute API.

### 2. Mendefinisikan Rute
Rute dasar di Laravel dapat didefinisikan menggunakan metode HTTP seperti GET, POST, PUT, DELETE, dll. Berikut adalah contoh rute dasar:

```php
Route::get('/', function () {
    return view('welcome');
});
```
- **Route::get**: Mendefinisikan rute untuk permintaan GET.
    
- **view('welcome')**: Mengembalikan view bernama `welcome`.
    
### 3. Rute dengan Parameter
Anda dapat mendefinisikan rute dengan parameter dinamis. Parameter ini dapat diakses dalam fungsi penanganan rute:
```php
Route::get('/user/{id}', function ($id) {
    return 'User '.$id;
});
```
- **{id}**: Parameter dinamis yang dapat diakses dalam fungsi sebagai `$id`.

### 4. Rute dengan Nama
Anda dapat memberi nama rute untuk memudahkan referensi di seluruh aplikasi:
```php
Route::get('/profile', function () {
    // ...
})->name('profile');
```
- **name('profile')**: Memberi nama rute sebagai `profile`.
    
### 5. Rute ke Controller
Anda dapat mengarahkan rute ke metode controller untuk memisahkan logika dari definisi rute:

```php
Route::get('/user/{id}', [UserController::class, 'show']);
```
- `[UserController::class, 'show']`: Mengarahkan rute ke metode `show` di `UserController`.
    
### 6. Middleware pada Rute
Anda dapat menambahkan middleware pada rute untuk memfilter permintaan sebelum mencapai fungsi penanganan rute:

```php
Route::get('/admin', function () {
    // ...
})->middleware('auth');
```
- **middleware('auth')**: Menambahkan middleware `auth` pada rute.

### 7. Grup Rute
Anda dapat mengelompokkan beberapa rute dengan menggunakan grup rute untuk menerapkan middleware atau pengaturan lain secara bersamaan:

```php
Route::middleware(['auth'])->group(function () {
    Route::get('/dashboard', function () {
        // ...
    });

    Route::get('/settings', function () {
        // ...
    });
});
```
- **Route::middleware(['auth'])->group**: Menerapkan middleware `auth` pada semua rute dalam grup.
    
### 8. Rute Resource
Laravel menyediakan cara mudah untuk mendefinisikan rute CRUD dengan menggunakan rute resource:

```php
Route::resource('posts', PostController::class);
```
- **Route::resource**: Mendefinisikan rute CRUD untuk resource `posts` yang diarahkan ke `PostController`.