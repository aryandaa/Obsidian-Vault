#programming 
1. Model:
	- Mengelola data dan logika bisnis aplikasi
	- berinteraksi dengan database untuk mengambil, menyimpan, dan memproses data
	- Contoh: Model user yang berisi informasi pengguna dan metode untuk mengelola data pengguna
2. View:
	- Bertanggung jawab untuk menampilkan data kepada pengguna.
	- Mengambil data dari model dan menyajikannya dalam format yang dapat dilihat dan diinteraksi oleh pengguna
	- Contoh: Halaman HTML yang menampilkan daftar pengguna.
3. Controller:
	- Mengatur aliran data antara model dan view
	- Menerima input dari pengguna melalui view, memprosesnya (dengan bantuan model), dan mengembalikan hasilnya ke view.
	- Contoh: Controller UserController yang menangani permintaan untuk menampilkan, menambah, atau mengedit pengguna.

Dengan memisahkan aplikasi menjadi tiga komponen ini, MVC membantu dalam mengorganisir kode, memudahkan pemeliharaan, dan meningkatkan skalabilitas aplikasi web.

## Model
Model dalam Laravel adalah representasi dari tabel database dan berfungsi untuk mengelola data serta logika bisnis aplikasi. Model menggunakan Eloquent ORM (Object Relational Mapping) yang memungkinkan interaksi dengan database menggunakan PHP yang sederhana dan intuitif.

### 1. Membuat model
anda dapat membuat model menggunakan perintah Artisan berikut:
```
php artisan make:model NamaModel
```

Contoh
```
php aartisan make:model user
```
yang artinya perintah ini akan membuat file model user.php di dalam folder app/Models

### 2. Structure Model
Model yang dibuat akan terlihat seperti ini
```php
namespace App\Models;

use illuminate\Database\Eloquent\Factories\HasFactory;
use illuminate\Database\Eloquent\Model;

class User extend Model{
	Use HasFactory;
	// Definisikan Properti dan metode model di sini
}
```

### 3. Properti dan Metode Model
- Table Name: Secara default Laravel mengasumsikan nama table adalah bentuk jamak dari nama model. dan dapat mengubahnya dengan mendefinisikan properti $table;
```php
protected $table = 'nama table';
```

- Primary Key: Secara default Laravel mengasumsikan primary key bernama id. dan dapat mengubahnya dengan mendefinisikan property $primarykey;
```php
protected $primarykey = 'nama_kolom';
```

- Timestamps: secara default Laravel mengelola kolom created_at dan updated_at, dan dapat menonaktifkannya dengan mendefinisikan properti $timestamps;
```php
public $timestamps = false;
```

- Fillable: Properti $fillable digunakan untuk mendefinisikan kolom yang dapat diisi secara massal
```php
protected $fillable = ['name', 'email', 'password'];
```

- Hidden: Properti $hidden digunakan untuk menyembunyikan kolom saat model dikonversi ke array atau JSON
```php
protected $hidden = ['password'];
```

### 4. Contoh Penggunaan Model
- Menyimpan data
```php
$user = new User;
$user->name = 'jhone doe';
$name->email = 'jhon@example.com';
$user->password = bcrypt('password');
$user->save();
```

- Mengambil Data
```php
$user = User::find(1); // Mengambil user dengan ID 1
$users = User::all(); // Mengambil semua User
```

- Memperbarui Data
```php
$user = user::find(1);
$user->email = 'newemail@example.com';
$user->save();
```

- Menghapus Data
```php
$user = user::find(1);
$user->delete();
```

### 5. Relasi Antar Model
Eloquent mendkung berbagai jenis relasi antar model
- One To One
```php
public function phone()
{
	return $this->hasOne(phone::class);
}
```

- One To Many
```php
public function posts()
{
	return $this->hasMany(Post::class);
}
```

- Many To Many
```php
public function roles()
{
	return $this->belongstoMany(Role::class);
}
```

- Polymorphic Relations
```php
public function imageable()
{
	return $this->morphTo();
}
```


## View
view dalam laravel bertanggung jawab untuk menampilkan data kepada pengguna. Laravel menggunakan Blade sebagai templating engine yang memungkinkan anda untuk menggunakan sintaks yang sederhana dan efisien dalam membuat tampilan

### 1. Membuat View
View di simpan di dalam folder resources/views. anda dapat membuat file view dengan ekstensi .blade.php. Contoh membuat file welcome.blade.php.
```html
<!-- resourced/views/welcome.blade.php -->
<!DOCTYPE html>
<html>
<head>
    <title>welcome</title>
</head>
<body>
    <h1>Selamat Datang di Laravel</h1>
</body>
</html>
```
Kita juga bisa membuat file view melalui php artisan cli (command line interface).
contoh berikut membuat file view app.blade.php pada folder layouts di dalam folder resources/views.
```
php artisan make:view layouts.app
```

### 2. Mengembalikan View dari Controller
Anda dapat mengembalikan view dari controller menggunakan fungsi view:
```php
// app/Http/Controllers/HomeController.php
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HomeController extends Controller
{
    public function index()
    {
        return view('welcome');
    }
}
```

****