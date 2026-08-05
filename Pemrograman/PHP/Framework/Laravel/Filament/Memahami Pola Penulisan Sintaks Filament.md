#programming
Hal pertama yang sering membuat pemula bingung adalah bentuk sintaks Filament.
Sebagai contoh.

```php
TextInput::make('name')
    ->required()
    ->maxLength(255);
```

Sekilas sintaks tersebut terlihat rumit karena menggunakan operator `::` dan `->` secara bersamaan. Padahal keduanya memiliki fungsi yang berbeda.

Operator `::` digunakan untuk memanggil metode statis milik sebuah class. Dalam contoh di atas, `TextInput` merupakan sebuah class yang disediakan oleh Filament. Metode `make()` dipanggil secara statis untuk membuat sebuah objek TextInput.

Setelah objek berhasil dibuat, operator `->` digunakan untuk memanggil metode milik objek tersebut. Metode seperti `required()`, `label()`, `numeric()`, atau `maxLength()` berfungsi mengubah konfigurasi objek yang telah dibuat sebelumnya.

Konsep ini dikenal sebagai **Method Chaining**. Setiap metode mengembalikan objek yang sama sehingga metode berikutnya dapat dipanggil secara berantai.

Secara konseptual, proses tersebut dapat digambarkan sebagai berikut.

```
TextInput

↓

make()

↓

Objek TextInput

↓

required()

↓

label()

↓

numeric()

↓

maxLength()
```

Karena seluruh komponen Filament menggunakan pola yang sama, seorang developer cukup memahami satu pola tersebut untuk dapat menggunakan hampir seluruh komponen yang tersedia.