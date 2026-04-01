#programming 
Salah satu tantangan terbesar ketika menggunakan JavaScript adalah sifat _weak typing_ yang dimilikinya. Bahasa pemrograman yang bersifat weak typing sangat longgar dengan penetapan tipe data. Di JavaScript, ketika membuat variabel, Anda tidak bisa mengikat nilai dengan tipe data yang spesifik. Semuanya longgar bahkan saat memberikan nilai pada parameter fungsi sekalipun.
![](Pemrograman/JavaScript/Framework/React/React%20Lanjutan/img/1.png)

JavaScript sendiri memiliki tujuh tipe data primitif, yakni Boolean, Null, Undefined, Number, String, Symbol, dan BigInt. Selain itu, ada juga tipe data Object yang dapat berisi lebih dari satu nilai primitif yang disimpan pada sebuah properti. Kesalahan dalam memberikan nilai dengan tipe data yang “tidak” diharapkan dapat menimbulkan bug.

Agar lebih paham, simak fungsi sum yang semestinya menerima dua parameter number berikut.

```js
function sum(a, b) {
  return a + b;
}
```

Fungsi **sum** di atas berguna untuk menambahkan nilai parameter a dan b. Ketika parameter diberi nilai number, fungsi akan berjalan sesuai ekspektasi.

|                         |
| ----------------------- |
| sum(5, 3); // output: 8 |

Lalu, apa jadinya bila kita memberikan tipe data string atau boolean?
```js
sum('5', 3); // output: '53'
sum(true, 3); // output: 4
```
Waduh! Ini bukan hasil yang kita harapkan. Bahayanya, bila kita tidak menyadari ada kesalahan dan aplikasi terus berjalan, pastinya kelak hal ini akan menimbulkan bug.

Sebagian besar bug yang disebabkan oleh kesalahan tipe data dapat dicegah dengan memvalidasi masukkan yang diberikan pada fungsi, class, atau apa pun yang menerima sebuah masukan. Dengan menambahkan validasi, setidaknya kita menjadi sadar terdapat kesalahan di sana sehingga dapat terhindar dari bug sedari dini.
```js
function sum(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('parameters should be a number');
  }
 
  return a + b;
}
 
console.log(sum(1, 2)); // output: 3
console.log(sum('5', 3)); // Error: parameters should be a number
console.log(sum(true, 3)); // Error: parameters should be a number
```

Cara ini umum dilakukan di JavaScript, tetapi tidak untuk bahasa pemrograman lain karena bahasa lain memiliki fitur atau sintaksis bawaan untuk menjaga kontrak dari tipe data. Sampai saat ini, tidak ada fitur bawaan di JavaScript untuk mengikat tipe data pada nilai/variabel. Namun, karena ekosistem JavaScript sangatlah luas, sudah ada tools seperti [Flow](https://flow.org/) dan [TypeScript](https://www.typescriptlang.org/) yang dibuat untuk memudahkan kita dalam memvalidasi tipe data di JavaScript. Selain itu, ada pula library semacam [Zod](https://zod.dev/) atau [Joi](https://joi.dev/) yang mempermudah kita menerapkan aturan validasi yang lebih kompleks di atas validasi tipe data. Keempat tools tersebut sangat populer, walaupun untuk menggunakannya kita perlu usaha lebih dengan mempelajari API nonstandar yang mereka tetapkan.

Validasi properti juga penting untuk diterapkan pada React component yang menerima inputan melalui _props_. Apa jadinya bila sebuah component yang menerima objek malah diberikan nilai array? Jika aplikasi terus berjalan, tentu akan menimbulkan bug. Dengan menerapkan validasi properti, jika component digunakan dengan nilai properti yang tidak sesuai, akan muncul “sinyal eror” yang mengingatkan developer bahwa penggunaan component-nya salah. Dengan begitu, Anda bisa lebih percaya diri bahwa component tersebut digunakan dengan nilai yang benar sehingga dapat berjalan sesuai harapan.

Dalam memvalidasi properti component, React merekomendasikan kita untuk menggunakan tools bernama [PropTypes](https://reactjs.org/docs/typechecking-with-proptypes.html). Melalui tools tersebut, Anda tidak perlu menulis validasi secara manual di dalam komponen sehingga tidak membuat komponen Anda menjadi “gemuk” akan kode. Penasaran? Di materi selanjutnya, kita akan mencari tahu lebih detail tentang PropTypes dan penggunaannya.

