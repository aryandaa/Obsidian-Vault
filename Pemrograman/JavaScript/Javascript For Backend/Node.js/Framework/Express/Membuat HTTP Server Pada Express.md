#programming 
Untuk membuat HTTP server menggunakan Express, kita tidak lagi menggunakan core module `http` secara langsung. Namun, kita akan membuat server dengan dependencies pihak ketiga yaitu Express. Untuk menggunakannya, kita perlu memasang terlebih dahulu melalui NPM dengan perintah.
```shell
npm install express
```

Setelah proses pemasangan berhasil, barulah kita bisa menggunakan modul tersebut.
```js
import express from 'express';
```

Pembuatan server menggunakan Express memiliki struktur kode yang berbeda dari cara asli. Berikut adalah dasar kode dalam membuat HTTP server pada Express:
```js
const app = express();
const port = 3000;
 
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
```
Mari kita bedah kodenya.

HTTP server sendiri dibuat melalui fungsi `express()`. Fungsi ini mengembalikan instance aplikasi Express yang siap dikonfigurasi. Instance aplikasi ini disimpan dalam variabel app yang akan menjadi fondasi dari web server kita.

Konfigurasi port dilakukan secara terpisah dengan mendefinisikan variabel port yang bernilai 3000. Berbeda dengan framework lain yang menerima konfigurasi dalam satu objek, Express memisahkan konfigurasi port dari pembuatan aplikasi.

Proses menjalankan server (`app.listen()`) dilakukan secara synchronous namun dengan callback function. Method `listen()` menerima dua parameter: port number dan callback function yang akan dieksekusi ketika server berhasil berjalan.


#### Latihan membuat HTTP Server
Ayo kita mulai!  
Sekarang praktikan pada server express-web-server yang telah kita siapkan sebelumnya. 

Pertama, kita pasang dahulu expresss dengan cara eksekusi perintah berikut pada Terminal proyek:
```shell
npm install express
```

Untuk memastikan express berhasil terpasang, lihat berkas **package.json**. Pastikan di sana terdapat properti dependencies dan menampung express beserta versi yang digunakan.
```json
"dependencies": {
   "express": "^5.1.0"
}
```

Proses instalasi modul selesai! Kita lanjut ke penulisan kode pada berkas **server.js**.

Silakan hapus kode yang ada pada **server.js**, lalu ganti dengan kode dasar dalam pembuatan server menggunakan Express berikut ini:
```js
import express from 'express';
 
const app = express();
const port = 3000;
const host = 'localhost';
 
app.listen(port, () => {
  console.log(`Server running at http://${host}:${port}`);
});
```

Simpan perubahan pada berkas **server.js**. Kemudian jalankan perintah `npm run start` pada Terminal. Jika server berhasil dijalankan, maka Anda akan melihat pesan ‘Server berjalan pada [http://localhost:3000](http://localhost:3000/)’.

Silakan lakukan permintaan ke [http://localhost:3000](http://localhost:3000/) melalui cURL. Perhatikan, server akan merespons seperti ini:
![](Pemrograman/JavaScript/Javascript%20For%20Backend/Node.js/Framework/Express/img/1.png)
