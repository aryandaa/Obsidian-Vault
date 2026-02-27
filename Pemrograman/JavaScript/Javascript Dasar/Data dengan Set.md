#programming 
Terakhir, struktur data yang kita bahas adalah set. Set adalah struktur data yang spesial dibandingkan dengan map, array, dan object. Kenapa dikatakan spesial?

Jawabannya adalah karena set tidak memiliki key dan indeks ketika menyimpan data. Selain itu, data yang disimpan di dalam set akan bernilai unik artinya tidak akan ada data yang duplikat.

### Membuat Set
Set dapat dibuat dengan cara menuliskan object constructor set seperti contoh berikut ini.
```js
const set = new Set();
```

Set juga dapat dibuat beserta dengan nilainya seperti berikut ini.
```js
const mySet = new Set([1, 2, 3]);
console.log(mySet);
```

### Menyimpan Nilai di Set
Untuk menambahkan nilai set setelah diinisialisasi dapat menggunakan method add.

```js
const set = new Set();
set.add(1);
set.add(2);
```
Method add hanya menerima satu argument sebagai nilai yang ingin kita tambahkan ke dalam set. Jika kita memberikan nilai yang sama, set hanya akan menyimpan sekali saja. Oleh karena itu, data yang ada di dalam set tidak akan terduplikat.

```js
const set = new Set();
set.add(1);
set.add('Apple');
set.add(1);
set.add('Apple');

console.log(set); // Output: Set { 1, 'Apple' }
```
Dalam contoh kode di atas, perhatikan bahwa ketika menambahkan data yang sama, seperti 'Apple' dan '1' ke dalam set, hanya satu data yang tersimpan.

