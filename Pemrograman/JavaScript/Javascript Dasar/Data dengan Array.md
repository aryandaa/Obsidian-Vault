#programming 

Array adalah struktur data spesial yang dapat menyimpan kumpulan data yang terurut. Letak perbedaan array dengan object adalah data yang disimpan di dalam array terurut, sedangkan di object tidak terurut. Di array, kita bisa menambahkan nilai di antara data yang sudah ada. Data yang ada di array dapat diakses menggunakan pola indeks. Nilai yang disimpan di dalam array disebut dengan element.

Array dapat menyimpan nilai dengan tipe data apa pun, seperti number, object, dan string. Oleh karena itu, array bersifat dinamis sehingga kita dapat menambahkan element baru di dalam array. Array juga merupakan sebuah object. Anda dapat memanfaatkan method typeof untuk melihat jenis tipe data dari array tersebut seperti berikut.
```js
const array = [1, 2];
console.log(typeof array); // Output: object
```

### Membuat Array

Membuat Array dapat dilakukan dengan tiga cara di bawah ini.

#### Menggunakan object constructor
Array dapat dibuat dengan constructor new Array() seperti berikut.
```js
const users = new Array();
const numbers = new Array(5);
```

### Mengakses Element Array
Data di dalam array terurut sehingga untuk mengaksesnya dapat dengan mudah dengan menggunakan nilai indeks-nya. Indeks merupakan angka yang digunakan untuk merujuk ke nilai di dalam array, sehingga kita bisa menambahkan, mengubah, atau menghapus nilainya. Indeks array dimulai dari angka 0. Untuk mengakses nilai di dalam array, gunakan tanda kurung siku [] yang di dalamnya berisi angka yang merupakan posisi dari nilai yang ingin diakses seperti berikut.
```js
const myArray = [42, 55, 30];
console.log(myArray[1]); // Output: 55
```
Ketika mengakses indeks di luar dari ukuran array akan menghasilkan **undefined**.

### Array Method

Perlu diketahui bahwa array memiliki banyak sekali _method_ atau fungsi bawaan yang dapat digunakan untuk memudahkan proses pengelolaan atau penggunaannya. Kita hanya akan membahas beberapa method array yang sering digunakan dalam kehidupan sehari-hari oleh programmer JavaScript.

#### Reverse
Reverse adalah method yang digunakan untuk membalikkan nilai array. Metode reverse() mengembalikan array dengan element yang dibalik.
```js
const myArray = ['Android', 'Data Science', 'Web'];
myArray.reverse();
console.log(myArray); // Output: [ 'Web', 'Data Science', 'Android' ]
```
Element pertama array akan menjadi element terakhir akhir dan sebaliknya. Method reverse tidak akan membuat array baru, tetapi mengatur ulang element tersebut di dalam array yang sudah ada.

#### Sort
Sort adalah method yang digunakan untuk mengurutkan nilai array. Loh, katanya array sudah menyimpan data secara terurut kok masih perlu mengurutkan array menggunakan sort? Memang array sudah mengurutkan data sesuai dengan indeks-nya tetapi mengurutkan berdasarkan indeks saja belum cukup. 

Terkadang, kita butuh untuk mengurutkan array berdasarkan kriteria tertentu sesuai kebutuhan aplikasi. Secara default, array akan diurutkan secara ascending. Contohnya seperti berikut.
```js
const myArray = ['Web', 'Android', 'Data Science'];
myArray.sort();
console.log(myArray); // Output: [ 'Android', 'Data Science', 'Web' ]
```
