#programming 

Salah satu metode untuk menangani asynchronous process adalah menggunakan callback. Namun, kita harus paham dahulu makna dari callback. Apa itu?

Callback adalah sebuah function yang dijadikan sebagai nilai argument bagi function yang lain. Ini persis dengan hal yang pernah kita pelajari pada materi Function Expression. Contoh callback yang pernah kita temui sebelumnya adalah memberikan function pada setTimeout dalam parameter pertama. Setelah mencapai nilai timeout, callback akan dibangkitkan atau dijalankan.

Jadi, bagaimana implementasi callback dalam menangani proses asinkron? Perhatikan hasil pengembangan contoh kode sebelumnya pada kode berikut.

coffee.mjs
```js
export function makeCoffee(callback) {
  const estimationTime = 5000;

  const inSecond = Math.ceil(estimationTime / 1000);
  console.log(`Mohon menunggu. Pramusaji sedang membuatkan kopi dalam ${inSecond} detik`);

  setTimeout(() => {
    // Do some tasks to make coffee...
    console.log('Pramusaji selesai membuat kopi.');

    callback();
  }, estimationTime);
}
```

main.mjs
```js
import { makeCoffee } from './coffee.mjs';

console.log('Saya memesan kopi di kafe.');

makeCoffee(() => {
  console.log('Pramusaji memberikan kopi pesanan.');
  console.log('Saya mendapatkan kopi dan menghabiskannya.');
});
```

Pada kode di atas, kita memiliki beberapa perubahan. `makeCoffee` memiliki satu parameter yang akan menerima function alias callback agar dijalankan setelah proses pembuatan kopi selesai. Function apa yang akan kita masukkan? Function tersebut adalah tugas untuk pramusaji memberikan kopi kepada customer dan kemudian customer menghabiskan kopinya. Hal yang pasti adalah kita berhasil memastikan bahwa suatu tugas benar-benar dijalankan hanya ketika proses asinkron selesai. Inilah callback untuk penanganan asynchronous process.

Mungkin ada yang berpikir bahwa proses pemberian kopi juga berupa asinkron dan kita masih bisa melanjutkan tugas lain pada waktu itu. Pramusaji tentunya membutuhkan waktu untuk memindahkan kopi ke cangkir dan mempercantiknya serta perlu waktu untuk berjalan menuju meja customer. Tepat! Mari kita sesuaikan kodenya seperti kode berikut.

coffe.mjs:
```js
export function makeCoffee(callback) {
  const estimationTime = 5000;

  const inSecond = Math.ceil(estimationTime / 1000);
  console.log(`Mohon menunggu. Pramusaji sedang membuatkan kopi dalam ${inSecond} detik`);

  setTimeout(() => {
    // Do some tasks to make coffee...
    console.log('Pramusaji selesai membuat kopi.');
    callback();
  }, estimationTime);
}

export function sendCoffee(callback) {
  const estimationTime = 2000;

  console.log('Pramusaji sedang mengantarkan kopi pesanan');

  setTimeout(() => {
    // Do some tasks to send coffee...

    console.log('Pramusaji sudah sampai ke meja.');
    callback();
  }, estimationTime);
}
```

## Penanganan Error dengan Callback

Tugas yang berjalan secara asynchronous bisa saja berjalan sesuai dengan harapan dan bisa juga memberikan hasil bertolak belakang. Ketika kita menaruh ekspektasi terhadap pihak tertentu atas suatu tugas, mungkin ada benih-benih kekecewaan yang muncul dalam hati, antara keberhasilan atau kegagalan. Ini adalah pembicaraan mengenai kehidupan kita sebagai

Kita sudah mengerti ada banyak proses asynchronous yang dapat terjadi. Dalam konteks pengembangan aplikasi, ada kalanya kita gagal berkomunikasi dengan network, menjalankan kueri pada database, membaca file system, dsb. Mungkin ada beberapa hal yang menjadi penyebab, seperti halnya tidak memiliki koneksi internet. Bagaimana kita bisa berkomunikasi dengan network?

Developer aplikasi JavaScript harus dapat memperhatikan dan mengantisipasi kemungkinan kegagalan atau keberhasilan pada proses asinkron. Perhatikan kode berikut.

caffee.mjs:
```js
export function makeCoffee(name, callback) {
  const estimationTime = 5000;
  let isSuccess = false;

  const inSecond = Math.ceil(estimationTime / 1000);
  console.log(`Mohon menunggu. Pramusaji sedang membuatkan kopi dalam ${inSecond} detik`);

  setTimeout(() => {
    // Penentuan hasil dari proses asinkron
    const number = Math.random();
    if (number > 0.3) {
      isSuccess = true;
    }

    if (!isSuccess) {
      callback(new Error('Gagal membuatkan kopi.'), null);
      return;
    }

    console.log('Pramusaji selesai membuat kopi.');
    callback(null, name);
  }, estimationTime);
}

export function sendCoffee(name, callback) {
  const estimationTime = 2000;
  let isSuccess = false;

  console.log('Pramusaji sedang mengantarkan kopi pesanan');

  setTimeout(() => {
    // Penentuan hasil dari proses asinkron
    const number = Math.random();
    if (number > 0.3) {
      isSuccess = true;
    }

    if (!isSuccess) {
      callback(new Error('Gagal mengantarkan kopi.'), null);
      return;
    }

    console.log('Pramusaji sudah sampai ke meja.');
    callback(null, name);
  }, estimationTime);
}
```

main.mjs:
```js
import { makeCoffee, sendCoffee } from './coffee.mjs';

const order = 'Kopi Espresso';

console.log(`Saya memesan ${order} di kafe.`);

makeCoffee(order, (makeCoffeeError, makeCoffeeData) => {
  if (makeCoffeeError) {
    // Do something with error
    console.error(makeCoffeeError);
    return;
  }

  sendCoffee(makeCoffeeData, (sendCoffeeError, sendCoffeeData) => {
    if (sendCoffeeError) {
      // Do something with error
      console.error(sendCoffeeError);
      return;
    }

    console.log(`Pramusaji memberikan ${sendCoffeeData} pesanan.`);
    console.log(`Saya mendapatkan ${sendCoffeeData} dan menghabiskannya.`);
  });
});
```

Mari lanjutkan studi kasus pemesanan kopi. Kita menambahkan fitur agar customer bisa memesan jenis kopi yang diinginkan. Misalnya kopi espresso. Lalu, kita menambahkan dua buah argumen pada callback function untuk membawa data jika proses asinkron berhasil atau gagal. Data error terletak pada argumen pertama dan data keberhasilan terletak pada argumen kedua.

Kemudian, bagaimana cara kita menentukan bahwa pembuatan kopi berhasil atau gagal? Silakan perhatikan potongan kode berikut.
```js
setTimeout(() => {
  // Penentuan hasil dari proses asinkron
  const number = Math.random();
  if (number > 0.3) {
    isSuccess = true;
  }
 
  if (!isSuccess) {
    callback(new Error('Gagal membuatkan kopi.'), null);
    return;
  }
 
  console.log('Pramusaji selesai membuat kopi.');
  callback(null, name);
}, estimationTime);
```

Dalam callback `setTimeout`, di sanalah penentuan hasil akan ditetapkan. Yes, `isSuccess` menjadi penentunya. Karena merupakan simulasi, kali ini kita tentukan keberhasilannya dengan meminta nilai angka random dari `Math.random`. Jika berhasil alias `isSuccess` bernilai `true`, kita bawakan data pada parameter kedua dari keberhasilan proses pembuatan kopi dan berikan `null` pada parameter pertama untuk menandakan bahwa tidak ada error yang terjadi. Jika gagal, nilai argumen akan sebaliknya.

Berikut adalah hasil jika program di atas kita jalankan.
```
Saya memesan Kopi Espresso di kafe. 
Mohon menunggu. Pramusaji sedang membuatkan kopi dalam 5 detik Pramusaji selesai membuat kopi. 
Pramusaji sedang mengantarkan kopi pesanan Pramusaji sudah sampai ke meja. 
Pramusaji memberikan Kopi Espresso pesanan. Saya mendapatkan Kopi Espresso dan menghabiskannya.
```

Apa hasil yang diperoleh jika proses pembuatan kopi gagal? Berikut output-nya.
```
Error: Gagal membuatkan kopi. at Timeout._onTimeout (file:///home/glot/coffee.mjs:16:16) at listOnTimeout (node:internal/timers:573:17) at process.processTimers (node:internal/timers:514:7)
```

Jika ingin melihatnya secara langsung, Anda bisa jalankan program di atas beberapa kali hingga mendapati `isSuccess` bernilai `false`.

_Nice!_ Itulah cara pertama untuk menangani proses asynchronous dalam JavaScript. Simulasi hanyalah simulasi, bukan sebuah kasus nyata. Supaya memiliki pengalaman yang berbeda, mari kita coba lihat penerapan callback pada proses asynchronous dengan memanfaatkan salah satu Node.js API, yaitu fs untuk membaca file system.

simple.txt:
```txt
Hello %name%, my name is %your_name%.
```
main.mjs:
```js
import { readFile } from 'fs';

readFile('./sample.txt', (error, data) => {
  if (error) {
    console.log(error);
    return;
  }

  const greeting = data.toString()
    .replace('%name%', 'Dicoding')
    .replace('%your_name%', 'JavaScript');

  console.log(greeting);
});
```

Jika dijalankan, seharusnya akan menampilkan teks berikut pada console.

```
Hello Dicoding, my name is JavaScript.
```

Mantap! Pada contoh program di atas, kita melihat program JavaScript sedang berusaha membaca berkas bernama sample.txt. Ini ditandai dengan mesin membaca method `readFile` dari module yang bernama `fs`. Ini adalah salah satu built-in module (module bawaan) dari Node.js untuk membaca berkas-berkas dalam sistem operasi.

Hal yang menjadi titik bahasan adalah method `readFile` memanfaatkan callback untuk menangani proses asinkron. Jika pembacaan berkas berhasil, kita dapat melihat isi dari **sample.txt** pada console. Inilah yang kita pelajari saat ini!