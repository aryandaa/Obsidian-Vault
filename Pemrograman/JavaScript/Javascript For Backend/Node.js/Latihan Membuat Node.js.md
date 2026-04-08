#programming 
Setelah mengenal Node.js kini saatnya kita belajar cara menggunakannya. Kita akan mulai dari membuat proyek Node.js, menjalankan kode JavaScript menggunakan Node.js, hingga mempelajari berbagai API yang ada di dalamnya. Jadi sekali lagi pastikan prasyarat yang ada sudah Anda penuhi yah. Siapkan Text Editor, dan kita akan mulai menuliskan kode JavaScript.

Ikuti langkah-langkah berikut untuk membuat proyek Node.js.

1. Sebelum membuat proyek, buatlah folder baru terlebih dahulu. Folder ini akan digunakan sebagai tempat penyimpanan berkas proyek dan JavaScript yang kita tulis nanti. Kami sarankan, Anda buat folder tersebut di alamat:
- C -> javascript-projects -> nodejs-basic bagi pengguna Windows; 
- home -> javascript-projects -> nodejs-basic bagi pengguna Linux atau macOS.


2. Selanjutnya, buka folder nodejs-basic menggunakan VSCode. Caranya, pada Visual Studio Code pilih menu File -> Open Folder -> [pilih foldernya]. Folder pun berhasil terbuka melalui VSCode.


3. Untuk membuat proyek JavaScript, silakan buka Terminal pada VSCode. Pilih menu Terminal -> New Terminal, kemudian tuliskan perintah:
	`npm init`

>   
> NPM alias Node Package Manager merupakan JavaScript Package Manager bawaan dari Node.js. Melalui NPM ini kita dapat membuat Node.js package (proyek) dan mengelola penggunaan package eksternal yang digunakan. Kita akan membahas NPM lebih detail nanti.

Jika Anda yang tidak menggunakan Visual Studio Code, gunakan Terminal/Command Prompt usungan OS Anda. Namun, sesuaikan lokasinya pada folder proyek ya.

4. Setelah menuliskan perintah di atas, Anda akan diberikan beberapa pertanyaan untuk mengisi nilai package name, version, description. Semua itu merupakan informasi dasar dari aplikasi yang Anda buat.  
	Nilai yang berada di dalam tanda kurung merupakan nilai default. Anda dapat menggunakan nilainya dengan langsung menekan tombol Enter. Untuk saat ini, cukup berikan semua pertanyaan dengan nilai default.


5. Setelah mengisi seluruh pertanyaan yang diberikan, Anda akan diberitahu untuk melihat hasil akhir yang dibuat pada berkas package.json.
![](Pemrograman/JavaScript/Javascript%20For%20Backend/Node.js/img/1.png)

6. Dalam latihan kelas ini kita akan fokus menggunakan modularisasi ESM, maka dari itu perlu ada sedikit penyesuaian kode di dalam package.json. Silakan buka package.json dan tambahkan property "type" dengan nilai "module" seperti potongan kode yang diberikan tanda tebal di bawah ini.
```json
{
  "name": "nodejs-basic",
  "version": "1.0.0",
  "description": "",
  "license": "ISC",
  "author": "",
  "type": "module",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  }
}
```
Voila! Anda berhasil membuat proyek Node.js. Harap diingat dan dipahami cara membuat proyek Node.js ini ya karena ke depannya kita akan membuat beberapa proyek Node.js dengan langkah yang sama.

