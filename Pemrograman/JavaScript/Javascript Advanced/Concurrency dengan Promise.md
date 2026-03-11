#programming 

Kita sering berhadapan dengan banyak proses asynchronous sekaligus dalam kehidupan nyata. Apakah Anda sadar? Contohnya kita memiliki tiga buah tugas yang perlu diselesaikan.

1. Mencuci pakaian kotor dengan mesin cuci.
2. Menyapu lantai dengan robot pembersih.
3. Membuat kopi.

Kita tahu bahwa dua tugas pertama didelegasikan ke mesin. Lalu, kita bisa mengerjakan tugas ketiga sembari dua pekerjaan tersebut dalam proses penyelesaian. Ini bisa kita sebut dengan proses _concurrency_ karena banyak proses asynchronous berjalan secara bersamaan.

Untuk melakukan hal ini, objek Promise memiliki beberapa static method, seperti Promise.all dan Promise.allSettled. Keduanya memiliki kemiripan. Hal yang membedakan adalah Promise.all akan memasuki kondisi rejected jika salah satu Promise saja terjadi kegagalan. Namun, ini tidak berlaku dengan Promise.allSettled.

Perhatikan contoh pemanfaatan Promise.all jika salah satu Promise gagal.
```js
const promise1 = new Promise((resolve) => setTimeout(() => resolve(1), 1000));
const promise2 = new Promise((resolve, reject) => setTimeout(() => reject(new Error('Ups!')), 2000));
const promise3 = new Promise((resolve) => setTimeout(() => resolve(3), 3000));

Promise.all([promise1, promise2, promise3])
  .then((values) => {
    console.log('Success');
    console.log(values);
  })
  .catch((error) => {
    console.log('Failed');
    console.log(error.message);
  });

/* Output:
Failed
Ups!
*/
```

Yap, kode masuk ke method catch. Ini tidak akan terjadi dengan `Promise.allSettled`. Semua Promise akan dikembalikan meskipun ada yang gagal.
```js
const promise1 = new Promise((resolve) => setTimeout(() => resolve(1), 1000));
const promise2 = new Promise((resolve, reject) => setTimeout(() => reject(new Error('Ups!')), 2000));
const promise3 = new Promise((resolve) => setTimeout(() => resolve(3), 3000));

Promise.allSettled([promise1, promise2, promise3])
  .then((values) => {
    console.log('Success');
    console.log(values);
  })
  .catch((error) => {
    console.log('Failed');
    console.log(error.message);
  });

/* Output:
Success
[
  { status: 'fulfilled', value: 1 },
  {
    status: 'rejected',
    reason: Error: Ups!
        at Timeout._onTimeout (file:///home/nurrizkiadip/static-method.mjs:2:75)
        at listOnTimeout (node:internal/timers:573:17)
        at process.processTimers (node:internal/timers:514:7)
  },
  { status: 'fulfilled', value: 3 }
]
*/
```

Hal yang perlu kita tahu adalah tipe parameter static method, yaitu array berisi sejumlah Promise. Oleh karena itu, static method Promise dapat menjalankan banyak Promise.

Demikian materi mengenai _concurrency_ dengan Promise. Jadi, kita bisa menangani proses asynchronous sekaligus. _No ribet!_