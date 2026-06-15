#programming 
Sebelum membuat Web Server, buatlah proyek Node.js terlebih dahulu. 

1. Silakan buat folder baru di dalam **_C -> javascript-projects_** **(Windows)** atau **_home -> javascript-project_** **(Linux dan Mac)** dengan nama “nodejs-web-server”. 
2. Setelah itu, buka folder tersebut menggunakan VSCode.
3. Buka Terminal dan tuliskan perintah

`npm init --y`

> “Mungkin Anda bertanya mengapa terdapat --y di akhir perintahnya? **--y pada akhir perintah tersebut berfungsi untuk menjawab seluruh pertanyaan yang diberikan NPM ketika membuat proyek baru dengan jawaban/nilai default.**
> 
> Jika Anda lebih suka menjawab pertanyaan-pertanyaan tersebut secara manual, silakan hapus --y pada perintah tersebut.”

4. Setelah membuat proyek Node.js, pastikan di dalam proyek **nodejs-web-server** terdapat berkas **package.json**.
5. Lanjut kita buat berkas JavaScript baru, karena kita hendak membuat server, maka beri nama berkas tersebut **server.js**.
6. Di dalamnya tuliskan kode JavaScript berikut:
```js
console.log('Halo, kita akan belajar membuat server');
```
7. Kemudian buka berkas **package.json** dan tambahkan runner script seperti ini:
```js
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "start": "node server.js"
}
```
Sebenarnya Anda bisa menghapus runner script test. Karena script tersebut tidak kita gunakan. Jadi, runner script hanya memiliki nilai start saja.
8. Setelah itu, tambahkan baris kode berikut sebelum baris scripts.
```js
"type": "module"
```
Berikut kode lengkap dari package.json.
```js
{
  "name": "nodejs-web-server",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "type": "module",
  "scripts": {
    "start": "node server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```
Menambahkan "type": "module" di dalam file package.json memberi tahu Node.js bahwa proyek Anda menggunakan modul ECMAScript (ESM) secara default.

9. Simpan seluruh perubahan pada berkas yang ada. Kemudian buka terminal dan jalankan perintah:
```
npm run start
```
Bila konsol menampilkan pesan “Halo, kita akan belajar membuat server”, Selamat! Persiapan proyek kita sudah selesai.
