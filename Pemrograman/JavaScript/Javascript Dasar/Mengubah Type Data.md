#programming 

Saat mengelola sebuah data dalam JavaScript, seringkali kita perlu mengubah nilai dari satu tipe data ke tipe data lain. Proses ini sangat penting karena dalam berbagai situasi, kita perlu menyesuaikan tipe data dengan konteks atau kebutuhan tertentu, baik untuk keperluan perhitungan, perbandingan, maupun manipulasi data.

JavaScript adalah bahasa pemrograman yang dinamis dan fleksibel, ia menyediakan berbagai cara untuk mengonversi tipe data. Konversi tipe data dapat dilakukan secara eksplisit oleh developer atau secara implisit oleh interpreter. Memahami cara konversi tipe data penting agar dapat menulis kode yang efisien, efektif, dan bebas dari kesalahan.

### Konversi Eksplisit
Konversi eksplisit adalah cara yang paling dapat diandalkan untuk mengubah tipe data karena dilakukan dengan instruksi yang jelas, alias eksplisit dari programmer. Berikut adalah beberapa metode umum yang digunakan untuk konversi tipe data secara eksplisit.

  
#### Mengubah ke String
Untuk mengubah suatu tipe data ke bentuk string umumnya dapat dilakukan dengan dua cara, yaitu menggunakan fungsi `String()` dan _method_ `.toString()`. Berikut adalah contoh dari penggunaan kedua cara tersebut.
```js
const number = 123;
const boolean = true;

const strNumber = String(number);
const strBoolean = boolean.toString();

console.log(strNumber); // output: "123"
console.log(strBoolean); // output: "true"
```

#### Mengubah ke Number
Secara umum, untuk mengubah bentuk numerik, seperti “10”, “3.14” dapat dilakukan dengan menggunakan fungsi `Number()`. Berikut contoh penggunaannya.
```js
const StrToNumber = '123';
const strTOFloat = '3.14';
const BooltoNumber = true;

const numFromString = Number(StrToNumber);
const floatFromString = Number(strTOFloat);
const numFromBoolean = Number(BooltoNumber);

console.log(StrToNumber); // output: 123
console.log(strTOFloat); // output: 3.14
console.log(BooltoNumber); // output: 1
```

>**Catatan**  
Dalam number, nilai boolean direpresentasikan dengan angka 1 dan 0. Boolean true akan diubah menjadi 1, sedangkan false diubah ke 0.

Selain dengan fungsi Number(), ada juga cara yang lebih spesifik, seperti fungsi `parseInt()` dan `parseFloat()`.

Fungsi `parseInt()` digunakan untuk mengonversi string menjadi bilangan bulat (integer). Fungsi ini memiliki kemampuan untuk membaca karakter satu per satu. Ketika menemukan karakter yang tidak bisa diubah menjadi angka, proses konversi terhenti di sana. Dengan kemampuan ini, `parseInt()` dapat digunakan untuk mengubah nilai string, seperti "20CM", "64px", atau angka dengan satuan lainnya.
```js
const cm = '20cm';
const px = '64px';

const intFromCM = parseInt(cm);
const intFromPX = parseInt(px);

console.log(intFromCM); // output: 20
console.log(intFromPX); // output: 64
```

Adapun fungsi `parseFloat()` digunakan untuk mengonversi string menjadi angka desimal (_floating-point number_). Sama seperti `parseInt()`, fungsi ini juga memiliki kemampuan membaca karakter string satu per satu sehingga dapat mengubah numerik yang mengandung satuan.
```js
const cmf = '20.55cm';
const pxf = '64.23px';

const floatFromCM = parseFloat(cmf);
const floatFromPX = parseFloat(pxf);

console.log(floatFromCM); // output: 20.55
console.log(floatFromPX); // output: 64.23
```


#### Mengubah ke Boolean
Untuk mengubah suatu nilai ke tipe data boolean, kita bisa gunakan fungsi `Boolean()`. Sama seperti fungsi sebelumnya, kita cukup memberikan nilai yang akan diubah di antara tanda kurung. Berikut adalah contoh penggunaan fungsi `Boolean()`.
```js
const stringtoBool = 'Dicoding';
const empty = null;

const boolFromNumber = Boolean(number);
const boolFromString = Boolean(stringtoBool);
const boolFromNull = Boolean(empty);

console.log(boolFromNumber); // output: true
console.log(boolFromString); // output: true
console.log(boolFromNull); // output: false
```
Sebagaimana yang sudah kita ketahui bahwa boolean hanya memiliki dua nilai, yaitu true dan false. Jadi seluruh nilai jika dikonversikan dalam boolean kemungkinan nilainya hanya ada dua, yaitu true dan false. Seluruh nilai yang dikonversi dalam boolean menghasilkan true disebut nilai [_truthy_](https://developer.mozilla.org/en-US/docs/Glossary/Truthy), sedangkan sebaliknya disebut dengan [_falsy_](https://developer.mozilla.org/en-US/docs/Glossary/Falsy).

Hampir seluruh nilai yang ada sifatnya truthy, hanya segelintir nilai yang sifatnya falsy. Berikut adalah daftar nilai falsy dalam JavaScript.
```
false
0
-0
0n
''
null
undefined
NaN
```

### Konversi Implisit

Konversi implisit terjadi ketika JavaScript secara otomatis mengubah tipe data tanpa instruksi eksplisit dari programmer. Ini biasanya terjadi dalam konteks tertentu, seperti operasi aritmetika, perbandingan, dan konteks logika. Meskipun konversi implisit bisa sangat berguna dan menghemat penulisan kode, penting untuk memahami alasan hal ini terjadi untuk menghindari bug dan perilaku yang tidak terduga dalam kode.

Berikut adalah beberapa contoh konversi implisit yang sering terjadi dalam berbagai konteks.
```js
const age = 20;
const message = 'Umurku: ' + age;

console.log(message); // output: Umurku: 20
```
Dalam contoh ini, tipe data number (age) secara otomatis dikonversi menjadi string karena operator + digunakan untuk penggabungan string.


```js
const strNumber = '123';
const result = strNumber * 2;

console.log(result); // output: 246
```
Dalam contoh ini, strNumber (yang merupakan string) dikonversi menjadi number karena operator * digunakan untuk operasi aritmetika.

Contoh lain dalam penggunaan operasi aritmetika yang mengubah nilai boolean menjadi number.
```js
const bool = true;
const result = 1 + bool;

console.log(result); // output: 2
```