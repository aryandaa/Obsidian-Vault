#programming 
Seluruh data di komputer dikelola dan diakses melalui _filesystem_. Ketika menjalankan kode JavaScript pada browser, sangat penting untuk melimitasi JavaScript dalam mengakses filesystem. Teknik ini dinamakan dengan _sandboxing_. Sandboxing melindungi kita dari program jahat serta tindakan pencurian yang dapat merampas privasi penggunanya.

Bagaimana dengan JavaScript yang dijalankan di back-end? Limitasi tentu tetap ada, namun tidak seketat ketika JavaScript dieksekusi pada browser. Di back-end malah filesystem menjadi fitur esensial karena dalam pengembangan back-end akan sering sekali mengakses atau menulis sebuah berkas di dalam komputer. 

Node.js menyediakan core modules `fs` yang dapat mempermudah kita dalam mengakses filesystem. Setiap method yang ada di module fs tersedia dalam dua versi, yakni versi asynchronous (default) dan versi synchronous.

Untuk mengakses berkas pada komputer kita dapat menggunakan method `fs.readFile()`. Method ini menerima tiga argumen yakni: lokasi berkas, encoding, dan callback function yang akan terpanggil bila berkas berhasil/gagal diakses.
```js
import fs from 'fs';
 
const fileReadCallback = (error, data) => {
    if(error) {
        console.log('Gagal membaca berkas');
        return;
    }
    console.log(data);
};
 
fs.readFile('todo.txt', 'UTF-8', fileReadCallback);
```

Sebagai alternatif, Anda juga bisa gunakan method versi synchronous `fs.readFileSync()`.
```js
import fs from 'fs';
 
const data = fs.readFileSync('todo.txt', 'UTF-8');
console.log(data);
```