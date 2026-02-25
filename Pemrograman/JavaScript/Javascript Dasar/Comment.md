#programming 
Kita sudah mengetahui bahwa kode yang kita tulis dianggap sebagai instruksi dan interpreter akan menjalankan instruksi tersebut. Namun, dalam menulis kode, kita sering sekali menyisipkan sebuah catatan. Kita tidak ingin catatan tersebut ikut tereksekusi oleh interpreter. Pada kondisi ini, kita bisa menyisipkan catatan dalam bentuk komentar.

Komentar adalah teks bersifat penjelasan yang dapat dibaca oleh programmer dan ditulis dalam berkas kode. Pada JavaScript, untuk menuliskan teks komentar, ada dua cara, yaitu menggunakan tanda // dan /* */. Teks yang ditulis dengan tanda tersebut dianggap bukan instruksi dan tidak akan dijalankan oleh interpreter.

Berikut adalah contoh komentar yang ditulis dengan tanda //.
```js
// Teks ini akan diabaikan oleh interpreter
console.log('Hai, Readers!');
console.log('Hai, JavaScript!');
// console.log('Hai, Dicoding!');
```
Jika Anda jalankan kode di atas, hanya akan tampil teks "Hai, Readers!” dan “Hai, JavaScript!”. Kode yang ditulis pada baris pertama dan terakhir akan diabaikan karena dianggap sebagai komentar.

Berikut adalah contoh dari komentar yang ditulis dengan tanda /* */.
```js
/*
 * TODO
 * 1. Buatlah variabel bernama `PI` dan isikan dengan nilai 3.14
 * 2. Cetak nilai variabel PI di terminal menggunakan console.log
 */

const PI = '3.14';
console.log(PI);
```

Tanda /* */ memudahkan kita untuk menuliskan komentar lebih dari satu baris_._ Pasalnya, teks apa pun (termasuk baris baru) yang ditulis di antara tanda _/*_  dan diakhiri dengan tanda */ akan dianggap sebagai komentar. Hal ini berbeda dengan tanda // yang tidak mendukung baris baru.

Maka dari itu, tanda // biasanya disebut dengan _single line comment_, sedangkan tanda /* */ disebut dengan multi line comment.