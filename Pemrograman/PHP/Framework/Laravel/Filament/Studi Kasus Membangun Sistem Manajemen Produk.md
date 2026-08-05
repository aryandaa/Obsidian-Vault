#programming 
Pada pembahasan sebelumnya telah dijelaskan bahwa Resource merupakan inti dari Filament. Pada pembahasan kali ini kita akan mulai membangun sebuah modul nyata, yaitu **Manajemen Produk**.

Bayangkan sebuah perusahaan memiliki gudang penyimpanan barang. Administrator membutuhkan sebuah halaman untuk mengelola seluruh produk yang dimiliki perusahaan. Setiap produk memiliki nama, kategori, harga, jumlah stok, status aktif, gambar produk, dan deskripsi.

Data tersebut nantinya akan disimpan pada database dengan struktur seperti berikut.

|Kolom|Tipe Data|Keterangan|
|---|---|---|
|id|bigint|Primary Key|
|name|varchar|Nama produk|
|category_id|bigint|Relasi ke kategori|
|price|decimal|Harga produk|
|stock|integer|Jumlah stok|
|is_active|boolean|Status produk|
|image|varchar|Path gambar|
|description|text|Deskripsi|
|created_at|timestamp|Waktu dibuat|
|updated_at|timestamp|Waktu diperbarui|

Apabila digambarkan secara sederhana, hubungan antar komponen dapat dilihat sebagai berikut.

```
Database
      │
      ▼
 Product Model
      │
      ▼
 ProductResource
      │
      ▼
+-----------------------+
| List Product          |
| Create Product        |
| Edit Product          |
| Delete Product        |
+-----------------------+
```

Pada studi kasus ini, tujuan kita bukan sekadar membuat halaman CRUD, melainkan memahami mengapa setiap sintaks ditulis dengan cara tertentu.

# Membuat Migration
Langkah pertama dalam Laravel selalu dimulai dari database. Hal ini karena seluruh data yang akan ditampilkan oleh Filament berasal dari database.

Buat migration menggunakan Artisan.
```bash
php artisan make:model Product -m
```

Perintah tersebut akan membuat dua buah file sekaligus, yaitu Model `Product` dan Migration.

Kemudian isi migration menjadi seperti berikut.

```php
public function up(): void
{
    Schema::create('products', function (Blueprint $table) {

        $table->id();

        $table->string('name');

        $table->foreignId('category_id')
            ->constrained()
            ->cascadeOnDelete();

        $table->decimal('price', 12, 2);

        $table->integer('stock')->default(0);

        $table->boolean('is_active')->default(true);

        $table->string('image')->nullable();

        $table->text('description')->nullable();

        $table->timestamps();
    });
}
```

Kode di atas belum ada hubungannya dengan Filament. Ini merupakan struktur database Laravel biasa.

Filament hanya akan membaca struktur data yang telah kita buat. Oleh karena itu, sebelum membuat antarmuka administrasi, kita harus memastikan struktur database telah dirancang dengan baik.

Setelah migration selesai, jalankan perintah berikut.

```bash
php artisan migrate
```

Kini tabel `products` telah tersedia di database.

# Membuat Resource
Setelah database selesai dibuat, langkah berikutnya adalah membuat Resource.
```shell
php artisan make:filament-resource Product
```

Saat perintah tersebut dijalankan, Filament akan menanyakan beberapa pilihan.
```
Generate resource?
```

Pilih **Generate**.

Filament kemudian akan menghasilkan beberapa file secara otomatis.

```
Products/
	ProductResource.php
	
	Pages/
	CreateProduct.php
	EditProduct.php
	ListProducts.php
	
	Schemas/
	ProductForm.php
	
	Tables/
	ProductResource.php
```
Perhatikan bahwa kita tidak pernah membuat halaman Create maupun Edit secara manual.

Inilah salah satu filosofi Filament. Developer cukup mendeskripsikan data, sedangkan Filament akan membangun antarmukanya.

## Login ke admin
jika Resource sudah dibuat, sekarang kita bisa login ke admin dengan mengetikan `localhost:8000/admin`

lalu web akan memintai password, dan gimana cara kita bisa masuk?
kita bisa mengetikan
```shell
php artisan tinker
```
lalu keluar > dan ketikan code ini di dalam interactive cli itu:
```PHP
use App\Models\User;

User::create([
    'name' => 'Admin',
    'email' => 'admin@example.com',
    'password' => bcrypt('password'),
]);
```
lalu `exit`
dan login menggunakan creds 
```
Email    : admin@example.com
Password : password
```

# Mengenal Isi ProductResource

Buka file `ProductResource.php`.

Kurang lebih isinya seperti berikut.
```php
class ProductResource extends Resource
{
    protected static ?string $model = Product::class;

    public static function form(Form $form): Form
    {

    }

    public static function table(Table $table): Table
    {

    }
}
```

Sekilas file tersebut tampak sangat sederhana. Namun sebenarnya hampir seluruh perilaku halaman CRUD akan ditentukan dari dua method tersebut.

Method `form()` mendefinisikan bagaimana pengguna memasukkan data.

Method `table()` mendefinisikan bagaimana data tersebut ditampilkan kembali.

Konsep ini disebut **declarative programming**. Kita tidak menuliskan langkah-langkah membuat form satu per satu, melainkan hanya mendeklarasikan komponen yang ingin ditampilkan.

# Membuat Form Pertama
Sekarang kita mulai mengisi method `form()`.

```php
public static function form(Form $form): Form
{
    return $form
        ->schema([
            TextInput::make('name')
                ->required()
                ->maxLength(255),

        ]);
}
```

Meskipun hanya terdiri dari beberapa baris, sebenarnya terdapat beberapa konsep penting di dalamnya.

Method `schema()` menerima sebuah array yang berisi komponen-komponen form. Setiap elemen array akan diterjemahkan menjadi sebuah komponen visual pada browser.

Komponen pertama yang kita gunakan adalah `TextInput`.

```
TextInput::make('name')
```

Sintaks tersebut memiliki arti, "buat sebuah input teks yang terhubung dengan kolom `name` pada Model Product."

Filament secara otomatis mengetahui bahwa nilai dari input tersebut nantinya akan disimpan ke atribut `$product->name`.

Tidak diperlukan penulisan atribut `name`, `id`, ataupun `value` seperti ketika menggunakan HTML biasa.

---

## Menambahkan Label
Secara default Filament akan mengubah nama field menjadi label.

```
name
```

akan menjadi
```
Name
```

Namun kita juga dapat menentukan label sendiri.

```php
TextInput::make('name')
    ->label('Nama Produk')
```

Method `label()` hanya mengubah teks yang ditampilkan kepada pengguna.

Nama kolom database tetap menggunakan `name`.

---

## Menambahkan Placeholder
Agar pengguna mengetahui data yang harus dimasukkan, kita dapat memberikan placeholder.

```php
TextInput::make('name')
    ->placeholder('Masukkan nama produk')
```

Placeholder hanya berfungsi sebagai petunjuk.

Nilainya tidak akan disimpan ke database.

---
## Menambahkan Validasi
Filament terintegrasi langsung dengan Laravel Validation.

Misalnya.
```php
TextInput::make('name')
    ->required()
    ->maxLength(255)
```
Method `required()` menghasilkan aturan validasi bahwa kolom tidak boleh kosong.
Method `maxLength(255)` membatasi jumlah karakter maksimum sebanyak 255 karakter.

Apabila pengguna mencoba menyimpan data kosong, Filament secara otomatis akan menampilkan pesan kesalahan tanpa kita menuliskan validasi secara manual.

