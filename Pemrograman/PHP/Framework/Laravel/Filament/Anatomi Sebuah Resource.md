#programming 
Apabila membuka sebuah Resource, struktur yang paling penting akan terlihat seperti berikut.

```PHP
class ProductResource extends Resource
{
    protected static ?string $model = Product::class;

    public static function form(Form $form): Form
    {
        //
    }

    public static function table(Table $table): Table
    {
        //
    }
}
```

Walaupun terlihat sederhana, sebenarnya terdapat dua metode yang menjadi inti dari seluruh Resource.

Metode `form()` bertanggung jawab mendesain formulir input data. Semua komponen seperti Text Input, Select, Upload File, Date Picker, dan Checkbox diletakkan di dalam metode ini.

Sebaliknya, metode `table()` bertanggung jawab mendesain tampilan daftar data. Semua kolom, fitur pencarian, pengurutan, filter, serta aksi Edit dan Delete diatur melalui metode tersebut.

Dengan demikian, sebuah Resource dapat dipandang sebagai gabungan antara **halaman input** dan **halaman daftar data**.