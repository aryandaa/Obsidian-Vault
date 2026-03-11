#programming 

Penanganan Promise benar-benar memudahkan programmer JavaScript. Kode menjadi makin simpel dan enak dibaca. Namun, proses asynchronous tetaplah tidak akan mencegah eksekusi kode setelahnya.

Perhatikan contoh berikut.

utils.mjs:
```js
function promiseExecutor(resolve, reject) {
  setTimeout(() => {
    resolve('You did it!');
  }, 2000);
}

export function doSomething() {
  return new Promise(promiseExecutor);
}
```

main.mjs
```js
import { doSomething } from './utils.mjs';

console.log('Start.');

doSomething()
  .then((value) => {
    console.log(value);
  });

console.log('End.');

/* Output:
Start.
End.
You did it.
*/
```

Misalnya Anda tetap ingin memiliki pengalaman kode yang berjalan secara sekuensial. Mari kita sebut ini sebagai gaya synchronous. Dengan harapan, berikut adalah output yang diharapkan jika kode di atas dijalankan ulang.

1. Start.
2. You did it.
3. End.

Untuk mencapai gaya synchronous, JavaScript memiliki fitur async-await untuk menangani Promise. Mari kita belajar implementasinya.

Istilah “async-await” terdiri dari dua keyword JavaScript, yaitu `async` dan `await`. Kita perlu menggunakan mereka berdua secara bersamaan dan tidak bisa mencederai salah satunya. Hal yang perlu dicatat adalah fitur ini hanya bisa dipakai jika menggunakan function.

Berikut adalah hasil perubahan contoh kode di atas.
```js
import { doSomething } from './utils.mjs';
 
async function promiseWithAsyncAwait() {
  console.log('Start.');
 
  const result = await doSomething();
  console.log(result);
 
  console.log('End.');
}
 
promiseWithAsyncAwait();
 
/* Output:
Start.
You did it.
End.
*/
```

Lihat! Kode dalam function benar-benar dibaca secara urut dari atas ke bawah. Data yang dikembalikan dari proses asynchronous akan dikeluarkan dari function dan dapat kita simpan dalam variabel. Ini terjadi berkat async-await. Keren!

Ada pertanyaan besar yang seharusnya muncul dalam benak kita, yaitu tentang cara penanganan error-nya jika menggunakan async-await. Ini menandakan Anda bisa berpikir kritis. Jawabannya adalah memanfaatkan try-catch. Error yang terjadi dari proses asynchronous akan langsung memasuki block catch.

Jika diterapkan, berikut hasil perubahan kodenya.

utils.mjs:
```js
function promiseExecutor(resolve, reject) {
  setTimeout(() => {
    resolve('You did it!');
  }, 2000);
}

export function doSomething() {
  return new Promise(promiseExecutor);
}
```

main.mjs:
```js
import { doSomething } from './utils.mjs';

async function promiseWithAsyncAwait() {
  try {
    console.log('Start.');

    const result = await doSomething();
    console.log(result);

    console.log('End.');
  } catch (error) {
    console.log(error.message);
  }
}

promiseWithAsyncAwait();

/* Output:
Start.
You did it.
End.
*/
```

Kami pun merasa nyaman dengan adanya fitur ini. Anda juga merasakan hal yang sama, kan? Kita jadi makin percaya diri jika berhadapan dengan proses asynchronous.