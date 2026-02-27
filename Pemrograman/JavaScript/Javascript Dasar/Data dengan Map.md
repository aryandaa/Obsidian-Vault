#programming 
Map adalah tipe data yang mirip dengan object yaitu menyimpan data dengan key-value. Kalau sama seperti object, lalu apa fungsinya map? Map berfungsi untuk menutupi kekurangan dari object. Map dapat menggunakan key dengan tipe data apa pun, tidak seperti object yang hanya menerima string. Jadi perbedaan mendasarnya terletak pada key yang digunakan.

Membuat Map
Map dapat dibuat dengan mudah yaitu menggunakan object map constructor seperti berikut ini.
```js
const map = new Map();
```

Kita telah berhasil membuat map yang bernilai kosong. Selain itu, kita juga dapat menambahkan data di dalam constructor ketika menginisialisasi map seperti berikut.
```js
onst productMap = new Map([
  ['shoes', 500],
  ['cap', 350],
  ['jeans', 250]
]);

console.log(productMap);
```

### Menyimpan Nilai di Map
Untuk menyimpan nilai ke dalam map, gunakanlah method `set`. Set menerima dua nilai yang pertama adalah keynya dan yang kedua adalah valuenya. Set memiliki struktur seperti berikut: _set(key, value)_. Perhatikan contoh berikut ini.
```js
const map = new Map();
map.set('name', 'aras');
console.log(map); // Map(1) { 'name' => 'aras' }
```

Selain menggunakan string sebagai key pada Map, kita juga dapat menggunakan number sebagai key-nya seperti berikut ini.
```js
const map = new Map();
map.set(1, 'number one');
console.log(map); // Map(1) { 1 => 'number one' }
```

### Mengakses Nilai di Map
Setelah berhasil menyimpan nilai ke dalam map, kita dapat mengakses nilainya berdasarkan key tertentu dengan method `get`.
```js
const map = new Map();
map.set('name', 'aras');
console.log(map.get('name')); // Output: aras
```

