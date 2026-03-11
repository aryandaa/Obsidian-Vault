#programming 
Salah satu upaya untuk meningkatkan kehati-hatian kita terhadap dynamic type adalah menyediakan dokumentasi kode. Dokumentasi mirip dengan kita memberi sebuah instruksi atau deskripsi mengenai tata cara penggunaan kode. Kita akan menggunakan [JSDoc](https://jsdoc.app/) sebagai alat dokumentasinya.

JSDoc adalah sebuah alat untuk menghasilkan dokumentasi kode JavaScript. Untuk memberikan deskripsi, kita akan memanfaatkan fitur komentar langsung pada sumber kodenya. Lebih tepatnya, komentar disajikan sebelum kode itu sendiri. Komentar ini sebut saja JSDoc comment.

JSDoc memiliki prosedur yang perlu kita ikuti sebelum memulai mendokumentasikan kode. Hal ini karena ada JSDoc parser yang akan menganalisis kode kita. Kerennya, JSDoc dapat menghasilkan dokumentasi dalam bentuk halaman web, _lho_. Nanti kita akan lihat.

Setiap JSDoc comment harus dimulai dengan /**. Komentar yang menggunakan /*, /***, atau lebih dari tiga bintang (*) tidak akan diproses oleh JSDoc. Mari kita lihat contoh berikut.
```js
/** Say hello to world */
function greet() {
  console.log('Hello, world!');
}
```

Dokumentasi di atas adalah contoh paling sederhana, yaitu hanya menambahkan deskripsi pada function. Bagaimana contoh yang lebih kompleks? JSDoc memiliki JSDoc tag yang dapat memberikan informasi lebih terkait function. Misalnya, sebuah function memiliki beberapa parameter dan return value. Kita bisa memberikan informasi dalam JSDoc comment tentang itu.

```js
/**
 * Get add operation of two numbers.
 * 
 * @param {number} numA - The first numeric operand
 * @param {number} numB - The second numeric operand
 * @returns {number} Sum of numA and numB
 */
function add(numA, numB) {
  return numA + numB;
}
```
JSDoc tag diawali dengan simbol @ dan diikuti dengan nama tag-nya. Kita melihat ada dua tag pada contoh kasus di atas.

- @param: menyediakan nama, tipe data, dan deskripsi untuk function parameter.
- @returns: menginformasikan nilai yang akan function keluarkan.

Ada banyak sekali tag yang tersedia untuk menghasilkan dokumentasi terbaik. Tidak hanya untuk function, JSDoc juga mampu mendokumentasikan class, object, import-export, dan sebagainya. Bahkan, JSDoc membaginya menjadi dua, yaitu block dan inline. Anda dapat bereksplorasi JSDoc tag pada [halaman dokumentasi ini](https://jsdoc.app/#block-tags).

### Bikin Dokumentasi Versi Web

Sebagaimana sudah disebutkan sebelumnya, JSDoc dapat menghasilkan dokumentasi dalam bentuk halaman web. Hal yang perlu dicatat adalah kita akan membutuhkan binary JSDoc dan mengeksekusinya melalui terminal. Pemanfaatan fitur ini harus melibatkan [package manager](https://en.wikipedia.org/wiki/Package_manager), seperti npm dan ini di luar topik pembahasan kita.

Namun, jangan khawatir. Rasa penasaran Anda dapat hilang dengan langsung melihat hasil webnya. Anda bisa membuka [halamannya di sini](https://jsdoc-web-sample.netlify.app/).

Terlihat lebih terpandu dengan adanya dokumentasi, ya. Bagi yang sering berkolaborasi dalam JavaScript, tentu ini sangat membantu agar komunikasi antar developer menjadi lancar, tanpa hambatan suatu apa pun.