#programming 
Sejauh ini kita telah membahas banyak tentang request. Kita sudah mengenal dan menggunakan method, url, body request, kemudian memberikan respons sesuai dengan karakteristik request yang ada.

Meskipun kita sudah bisa membuat server merespons permintaan, tapi sebenarnya kita belum belajar lebih dalam mengenai respons. Untuk itu, mari beranjak membahas lebih detail mengenai parameter kedua dari fungsi request listener ini. 

Seperti yang sudah Anda ketahui pada modul pengenalan back-end, respons yang dibawa oleh server dibagi menjadi tiga bagian penting. Yang pertama status line, atau bisa kita sebut response status; yang kedua response header; dan yang ketiga response body. Kita bahas mulai dari response status dahulu yah. 

Response status merupakan salah satu bagian dari respons yang berisikan tentang informasi apakah sebuah request berhasil atau gagal dilakukan. Status yang diberikan berupa kode (status code) dan pesan dari kode tersebut dalam bentuk teks (status message).

Indikasi keberhasilan request client ditentukan oleh response status code yang dikirim oleh server. Karena itu, tentu nilai status code tak bisa sembarang kita tetapkan. Status code haruslah bernilai 3 digit angka dengan ketentuan berikut:

- 100-199 : informational responses.
- **200 - 299 : successful responses.**
- 300-399 : redirect.
- **400-499 : client error.**
- **500-599 : server errors.**

Fokus terhadap poin yang ditebalkan yah karena poin itu akan sering digunakan. Silakan eksplorasi lebih detail mengenai status code pada [halaman MDN mengenai HTTP Status](https://developer.mozilla.org/id/docs/Web/HTTP/Status).

Pada Node.js, penetapan nilai status code pada response dilakukan melalui properti `response.statusCode`.
```js
const requestListener = (request, response) => {
    // memberitahu client bahwa request resource yang diminta tidak ada.
    response.statusCode = 404;
};
```

Oh ya! Dari halaman MDN yang diberikan di atas, kita juga bisa melihat bahwa status code selalu diiringi dengan status message. Contoh **200 Ok**, **400 Bad Request**, dan **404 Not Found**. Melalui status message ini kita dan juga client bisa paham maksud dari status kode.

Status message memiliki nilai standar sesuai dengan response code. Namun, kita bisa mengubahnya bila diperlukan. Untuk mengubah status message, Anda bisa gunakan properti `response.statusMessage`.
```js
const requestListener = (request, response) => {
    response.statusCode = 404;
 
    // 404 defaultnya adalah 'not found'
    response.statusMessage = 'User is not found';
};
```
Ketahuilah bahwa Anda sebaiknya tidak mengubah `statusMessage` dari nilai default bila tidak diperlukan. Walaupun hanya sekadar menerjemahkannya menjadi “Tidak ditemukan”.


#### Latihan Mengubah Response Code
Web server yang kita buat saat ini masih “cuek” dalam memberikan respons status pada client. Maksudnya, apa pun respons yang diberikan server statusnya selalu **200 OK**. Tidak percaya? Silakan lakukan request berikut pada curl.
```shell
curl -X GET http://localhost:5000/about -i
 
curl -X GET http://localhost:5000/test -i
 
curl -X DELETE http://localhost:5000/ -i
```

![](Pemrograman/JavaScript/Javascript%20For%20Backend/Node.js/Web%20Service%20Dengan%20Node.js/img/3.png)

Lihat informasi yang diberi warna kuning. Semua respons dari server berstatus 200 OK, ini membuat client mengira bahwa request berhasil dilakukan, tapi faktanya tidak.

Ada beberapa respons yang seharusnya bisa diberikan status yang lebih relevan. Seperti ketika client meminta resource yang tidak ditemukan (404 Not Found) atau menggunakan method request yang tidak tepat (400 Bad Request).

Karena Anda saat ini sudah mengetahui cara mengubah status code pada respons, mari kita perbaiki kesalahan ini.

Silakan buka kembali berkas `server.js`. Kemudian, hapus kode berikut dari fungsi request listener:
```js
response.statusCode = 200;
```

Sebagai gantinya, kita tuliskan nilai status code satu per satu sebelum perintah `response.end()`. Tentu, sesuaikan nilai status code dengan kasus-kasus yang ada. 

Contohnya, bila halaman tidak ditemukan, beri nilai **404** pada status code; bila halaman tidak bisa diakses menggunakan method tertentu, beri nilai **400** pada status code; sisanya, bila request berhasil dilakukan, beri nilai **200** pada status code. Yuk kita eksekusi!

Setelah semuanya selesai, fungsi request listener tampak seperti ini:
```js
const requestListener = (request, response) => {
    response.setHeader('Content-Type', 'text/html');
 
    const { method, url } = request;
 
    if(url === '/') {
        if(method === 'GET') {
            response.statusCode = 200;
            response.end('<h1>Ini adalah homepage</h1>');
        } else {
            response.statusCode = 400;
            response.end(`<h1>Halaman tidak dapat diakses dengan ${method} request</h1>`);
        }
    } else if(url === '/about') {
        if(method === 'GET') {
            response.statusCode = 200;
            response.end('<h1>Halo! Ini adalah halaman about</h1>')
        } else if(method === 'POST') {
            let body = [];
    
            request.on('data', (chunk) => {
                body.push(chunk);
            });
 
            request.on('end', () => {
                body = Buffer.concat(body).toString();
                const { name } = JSON.parse(body);
                response.statusCode = 200;
                response.end(`<h1>Halo, ${name}! Ini adalah halaman about</h1>`);
            });
        } else {
            response.statusCode = 400;
            response.end(`<h1>Halaman tidak dapat diakses menggunakan ${method} request</h1>`);
        }
    } else {
        response.statusCode = 404;
        response.end('<h1>Halaman tidak ditemukan!</h1>');
    }
};
```

Simpan perubahan pada berkas **server.js**; jalankan ulang server dengan perintah `npm run start`; dan coba lakukan lagi permintaan berikut menggunakan cURL:
```shell
curl -X GET http://localhost:5000/about -i
 
curl -X GET http://localhost:5000/test -i
 
curl -X DELETE http://localhost:5000/ -i
```
![](Pemrograman/JavaScript/Javascript%20For%20Backend/Node.js/Web%20Service%20Dengan%20Node.js/img/4.png)

