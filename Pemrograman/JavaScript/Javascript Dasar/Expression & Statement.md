#programming 

Instruksi yang diberikan kepada komputer berhubungan erat dengan proses komputasi. Oleh karena itu, instruksi tersebut haruslah jelas, terstruktur, dan sistematis. Contoh instruksi yang umum dilakukan pada komputer sebagai berikut.

- **Instruksi 1**: buat variabel bernama `age` dan berikan nilai 10.
- **Instruksi 2**: buat variabel bernama `name` dan berikan nilai “Dicoding”.
- **Instruksi 3**: cetak teks “Aku` [name]`, umurku `[age`] tahun.”,` [name]` diambil dari nilai variabel `name` dan `[age]` diambil dari nilai variabel `age`.

Dari contoh di atas, ada tiga instruksi yang harus dilakukan oleh komputer. Jika kita tuliskan instruksi tersebut dalam bahasa pemrograman JavaScript, kodenya akan seperti ini.
```js
const age = 10;
const name = 'Dicoding';
console.log(`Aku ${name}, umurku ${age} tahun.`);
```
outputnya:
Aku Dicoding, umurku 10 tahun.

Contoh kode di atas terdiri dari tiga baris kode. Pada pemrograman, satu instruksi umumnya ditulis dalam satu baris kode. Jadi, tiga instruksi umumnya ditulis dalam tiga baris kode. Istilah yang digunakan untuk "instruksi" dalam bahasa pemrograman adalah "statement".

Namun, penting untuk dicatat bahwa dalam bahasa pemrograman, tidak selalu satu baris hanya memiliki satu statement. Kita dapat menuliskan beberapa statement dalam satu baris kode sekaligus, seperti pada contoh berikut.

```js
const age = 10; const name = 'Dicoding'; console.log(`Aku ${name}, umurku ${age} tahun.`);
```

Penentuan akhir dari sebuah statement biasanya ditandai dengan tanda titik koma (;). Oleh karena itu, kita dapat menulis banyak statement dalam satu baris.

Selain statement, ada istilah lain yang penting untuk diketahui, yaitu _expression_. Ini merupakan bagian dari sebuah statement yang menghasilkan nilai. Setiap statement biasanya mengandung setidaknya satu expression. 
Contoh, expression dalam kode di atas adalah 
nilai age 10, 
teks “Dicoding”, 
dan teks “Aku Dicoding, umurku 10 tahun.”.

tidak hanya nilai statis, seperti angka 10 atau teks “Dicoding”. Namun, hasil operasi matematika seperti 4 + 4 yang akan menghasilkan nilai 8 atau penggabungan teks seperti “Dicoding” + “ “ + “Indonesia” yang akan menghasilkan teks “Dicoding Indonesia” juga merupakan sebuah expression.

