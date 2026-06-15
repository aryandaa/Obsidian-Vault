#programming 
Sebelum membuat Web Server, kita akan membuat proyek baru.

1. Mari kita awali dengan membuat proyek baru. Silakan buat folder di _C -> javascript-projects_ (Windows) atau _home -> javascript-projects_ (Linux dan macOS) dengan nama “**express***-**web-server**”.
2. Buka folder menggunakan VSCode, kemudian inisialisasi proyek pada Terminal dengan menggunakan perintah:  
    `npm init --y`
3. Lanjut, kita atur NPM runner pada package.json menjadi seperti ini:
```js
"scripts": {
   "start": "node server.js"
},
```
4. Setelah itu, tambahkan type module ke package.json.
```js
{
  "name": "express-web-server",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "type": "module",
  "scripts": {
    "start": "node server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^5.1.0"
  }
}
```

5. Lalu, buatlah berkas JavaScript baru dengan nama server.js. Kemudian, tuliskan kode berikut:
```js
console.log('Halo, kita akan belajar membuat server menggunakan Express');
```

6. Simpan perubahan pada berkas server.js dan coba jalankan perintah berikut pada Terminal:
```shell
npm run start
```

Bila Anda melihat pesan “Halo, kita akan belajar membuat server menggunakan Express”, maka proyek telah siap digunakan.

