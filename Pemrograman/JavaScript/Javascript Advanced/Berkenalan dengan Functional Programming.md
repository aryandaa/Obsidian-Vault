#programming 

Functional programming (selanjutnya disingkat menjadi FP) adalah paradigma pemrograman yang didasarkan pada fungsi matematika murni, yakni fungsi harus menghindari perubahan data sehingga selalu menghasilkan nilai sama ketika diberikan argumen sama. Dalam FP, fungsi adalah elemen utama yang digunakan untuk memecah kode dan membangun keseluruhan program. Dengan menerapkan konsep-konsep dalam FP, kita dapat membangun aplikasi menggunakan kode yang deklaratif (lebih simpel, tegas, dan terprediksi).

Sebagai gambaran untuk Anda yang belum tahu deklaratif dan imperatif (kebalikan dari deklaratif), simak contoh kode di bawah ini. Tujuan kode ini adalah menghasilkan nilai string baru dari nilai string yang sudah ada sebelumnya.

```js
const names = ['Harry', 'Ron', 'Jeff', 'Thomas'];

const newNamesWithExcMark = [];

for(let i = 0; i < names.length; i++) {
  newNamesWithExcMark.push(`${names[i]}!`);
}

console.log(newNamesWithExcMark); // output: [ 'Harry!', 'Ron!', 'Jeff!', 'Thomas!' ]
```

Sebagai orang yang baru belajar pemrograman, kita sering menggunakan cara for-loop untuk menyelesaikan masalah tersebut. Ketahuilah bahwa kode di atas bersifat imperatif, yakni untuk mencapai suatu tujuan, kita perlu menulis instruksi yang sifatnya langkah demi langkah. Kita perlu mendefinisikan cara melakukan perulangan, waktu perulangannya harus berhenti, hingga mengisikan nilai ke array baru. Dampaknya, kode yang ditulis menjadi banyak. Gaya imperatif memang fokusnya pada “how to solve”, bukan “what to solve”.

Lantas, bagaimana dengan gaya deklaratif?

Berikut adalah kode untuk menyelesaikan masalah yang sama, tetapi menggunakan gaya deklaratif.
```js
const names = ['Harry', 'Ron', 'Jeff', 'Thomas'];

const newNamesWithExcMark = names.map((name) => `${name}!`);

console.log(newNamesWithExcMark); // output: [ 'Harry!', 'Ron!', 'Jeff!', 'Thomas!' ]
```

Inilah bentuk dari kode deklaratif. Coba bandingkan dengan kode sebelumnya, tentu ini jauh lebih ringkas dan terlihat simpel. Inilah salah satu benefit ketika kita memecahkan masalah dengan gaya deklaratif yang notabene dianut dalam paradigma FP. Fungsi `.map()` yang Anda lihat di atas merupakan salah satu implementasi dari konsep-konsep dalam FP. Konsep utama dalam FP meliputi pure function, high-order function, recursion, dan immutability. Pada modul ini, Anda akan memahami cara kerja fungsi map yang merupakan implementasi dari konsep-konsep dalam FP.

Tantangan terberat dalam mempelajari FP adalah menghilangkan kebiasaan berpikir dari paradigma imperatif yang sudah sering kita anut. Tentu hal ini membutuhkan waktu yang panjang agar Anda benar-benar terbiasa dengan cara berpikir functional programming. Belajar FP dalam JavaScript sebetulnya bisa dilakukan secara perlahan. Anda masih bisa menggunakan konsep-konsep FP bersama paradigma yang lain, sebelum memutuskan seluruh solusi diselesaikan dengan FP.