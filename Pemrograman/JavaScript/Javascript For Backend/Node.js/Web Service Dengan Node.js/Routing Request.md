#programming 
Ketika menangani request, hal yang perlu kita cek selain method adalah URL atau alamat yang dituju dari request tersebut. Sebagai contoh, ketika kita mengunjungi [dicoding.com](https://www.dicoding.com/) dan [dicoding.com/about](https://www.dicoding.com/about), tentu hasil yang kita terima dari server akan berbeda, bukan? 

Request ke [dicoding.com](https://www.dicoding.com/) akan menampilkan homepage Dicoding, sedangkan [dicoding.com/about](https://www.dicoding.com/about) akan menampilkan halaman tentang Dicoding. Teknik ini dinamakan dengan routing. Routing merupakan istilah dalam menentukan respons server berdasarkan path atau url yang diminta oleh client.

Dalam `http.clientRequest`, untuk mendapatkan nilai url sangatlah mudah, semudah kita mendapatkan nilai request method yang digunakan.
```js
const requestListener = (request, response) => {
    const { url } = request;
};
```

Properti `url` akan mengembalikan nilai path secara lengkap tanpa `host` dan `port` yang digunakan server. Contohnya, bila client meminta pada alamat **http://localhost:5000/about** atau **http://localhost:5000/about/**, maka url akan bernilai **‘/about’**; bila meminta alamat **http://localhost:5000** atau **http://localhost:5000/**, maka url akan bernilai **‘/****’**.

Dengan mendapatkan nilai `url`, kita dapat merespons client sesuai dengan path yang ia minta.
```js
const requestListener = (request, response) => {
    const { url } = request;
 
    if(url === '/') {
        // curl http://localhost:5000/
    }
 
    if(url === '/about') {
        // curl http://localhost:5000/about
    }
 
    // curl http://localhost:5000/<any>
};
```

Kita juga bisa mengombinasikan evaluasi dengan method request. Alhasil, kita dapat menentukan respons lebih spesifik lagi.
```js
const requestListener = (request, response) => {
    const { url, method } = request;
 
    if(url === '/') {
 
        if(method === 'GET') {
            // curl -X GET http://localhost:5000/
        }
 
        // curl -X <any> http://localhost:5000/
    }
 
    if(url === '/about') {
 
        if(method === 'GET') {
            // curl -X GET http://localhost:5000/about
        }
 
        if(method === 'POST') {
            // curl -X POST http://localhost:5000/about
        }
 
        // curl -X <any> http://localhost:5000/about
    }
 
    // curl -X <any> http://localhost:5000/<any>
};
```


#### Latihan Routing Request
Saatnya kita latihan lagi yuk! Karena saat ini Anda sudah paham bagaimana cara menangani request berdasarkan URL yang diminta, mari buat web server kita agar dapat menangani request yang lebih spesifik berdasarkan URL dan method request. Berikut tugas atau ketentuan yang akan kita gunakan:

- URL: ‘/’
    - Method: GET
        - Mengembalikan “Ini adalah homepage”.
    - Method: `<any>` (selain GET)
        - Mengembalikan “Halaman tidak dapat diakses dengan `<any>` request”.
- URL: ‘/about’
    - Method: GET
        - Mengembalikan “Halo! Ini adalah halaman about”.
    - Method: POST (dengan melampirkan data name pada body)
        - Mengembalikan “Halo, `<name>`! Ini adalah halaman about”.
    - Method: `<any>` (selain GET dan POST)
        - Mengembalikan “Halaman tidak dapat diakses dengan `<any>` request”.
- URL: `<any>` (selain / dan /about)
    - Method: `<any>`
        - Mengembalikan “Halaman tidak ditemukan!”.

Sudah paham? _Huft_, latihan kali ini sepertinya lebih menantang. Siapkan secangkir kopi agar Anda tetap fokus dan mari kita mulai.

Pertama, agar kita dapat fokus pada hal routing. Beri komentar dulu kode logika di dalam fungsi request listener yang sebelumnya kita buat.
```js
const requestListener = (request, response) => {
    response.setHeader('Content-Type', 'text/html');
    response.statusCode = 200;
 
    const { method } = request;
 
    // if(method === 'GET') {
    //     response.end('<h1>Hello!</h1>');
    // }
 
    // if(method === 'POST') {
    //     let body = [];
    
    //     request.on('data', (chunk) => {
    //         body.push(chunk);
    //     });
 
    //     request.on('end', () => {
    //         body = Buffer.concat(body).toString();
    //         const { name } = JSON.parse(body);
    //         response.end(`<h1>Hai, ${name}!</h2>`);
    //     });
    // }
};
```

Selanjutnya, kita ambil properti `url` dari request menggunakan teknik destructuring object seperti mendapatkan nilai `method`. Lihat kode yang ditebalkan yah.
```js
const { method, url } = request;
```

_Good!_ Sekarang kita sudah dapat nilai `url` dari `request`. Saatnya kita menentukan logika routing url sesuai dengan ketentuan menggunakan `if else`.
```js
    if(url === '/') {
        // TODO 2: logika respons bila url bernilai '/'
    } else if(url === '/about') {
        // TODO 3: logika respons bila url bernilai '/about'
    } else {
        // TODO 1: logika respons bila url bukan '/' atau '/about'
    }
```

_Nice!_ Coba lihat komentar TODO (yang harus dikerjakan) pada kode tersebut. Kita akan selesaikan TODO sesuai urutan yang ada yah. Urutan tersebut sengaja disusun dari yang paling mudah, lalu merangkak ke yang lebih sulit.

Blok `else` yang paling terakhir (TODO pertama) akan tereksekusi bila `url` bukan bernilai `‘/`**’** atau `‘/about’`. Berdasarkan ketentuan yang ada di atas, kita harus merespons dengan pesan “Halaman tidak ditemukan!”. Yuk kita langsung saja tulis responsnya.

```js
import http from 'http';
 
const requestListener = (request, response) => {
    response.setHeader('Content-Type', 'text/html');
    response.statusCode = 200;
 
    const { method, url } = request;
 
    if(url === '/') {
        if(method === 'GET') {
            response.end('<h1>Ini adalah homepage</h1>');
        } else {
            response.end(`<h1>Halaman tidak dapat diakses dengan ${method} request</h1>`);
        }
    } else if(url === '/about') {
        if(method === 'GET') {
            response.end('<h1>Halo! Ini adalah halaman about</h1>')
        } else if(method === 'POST') {
            let body = [];
    
            request.on('data', (chunk) => {
                body.push(chunk);
            });
 
            request.on('end', () => {
                body = Buffer.concat(body).toString();
                const { name } = JSON.parse(body);
                response.end(`<h1>Halo, ${name}! Ini adalah halaman about</h1>`);
            });
        } else {
            response.end(`<h1>Halaman tidak dapat diakses menggunakan ${method} request</h1>`);
        }
    } else {
        response.end('<h1>Halaman tidak ditemukan!</h1>');
    }
};
 
const server = http.createServer(requestListener);
 
const port = 5000;
const host = 'localhost';
 
server.listen(port, host, () => {
    console.log(`Server berjalan pada http://${host}:${port}`);
});
```

_Good!_ Mari kita coba dahulu perubahan yang ada. Simpan perubahan pada berkas **server.js**; jalankan ulang server dengan perintah `npm run start`; dan silakan lakukan permintaan ke alamat selain `‘/`’ atau `‘/about’`. Seharusnya, server akan merespons sesuai dengan pesan yang sudah kita tetapkan.
```shell
curl -X GET http://localhost:5000/home
// output: <h1>Halaman tidak ditemukan!</h1>

curl -X GET http://localhost:5000/hello
// output: <h1>Halaman tidak ditemukan!</h1>

curl -X GET http://localhost:5000/test
// output: <h1>Halaman tidak ditemukan!</h1>

curl -X GET http://localhost:5000
// output: <h1>Ini adalah homepage</h1>

curl -X POST http://localhost:5000
// output: <h1>Halaman tidak dapat diakses dengan POST request</h1>

curl -X DELETE http://localhost:5000
// output: <h1>Halaman tidak dapat diakses dengan DELETE request</h1>

curl -X GET http://localhost:5000/about
// output: <h1>Halo! Ini adalah halaman about</h1>

curl -X POST -H "Content-Type: application/json" http://localhost:5000/about -d "{\"name\": \"Dicoding\"}"
// output: <h1>Halo, Dicoding! Ini adalah halaman about</h1>

curl -X PUT http://localhost:5000/about
// output: <h1>Halaman tidak dapat diakses menggunakan PUT request</h1>

curl -X DELETE http://localhost:5000/about
// output: <h1>Halaman tidak dapat diakses menggunakan DELETE request</h1>
```

