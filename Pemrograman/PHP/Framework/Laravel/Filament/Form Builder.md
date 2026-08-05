#programming 
Form Builder merupakan fitur yang digunakan untuk menyusun tampilan formulir.

Misalkan sebuah tabel produk memiliki kolom sebagai berikut.
```
id
name
price
stock
```

Form yang dibuat tidak perlu menulis HTML secara manual. Developer cukup mendeskripsikan komponen apa saja yang dibutuhkan.

```php
public static function form(Form $form): Form
{
    return $form
        ->schema([
            TextInput::make('name'),
            TextInput::make('price'),
            TextInput::make('stock'),
        ]);
}
```

Kata **schema** dapat dipahami sebagai cetak biru (blueprint) dari formulir. Setiap elemen di dalam array tersebut akan diterjemahkan oleh Filament menjadi komponen antarmuka yang siap digunakan.

Dengan pendekatan ini, developer tidak lagi memikirkan bagaimana cara membuat `<input>`, `<label>`, maupun validasi HTML. Seluruh proses tersebut ditangani secara otomatis oleh Filament.