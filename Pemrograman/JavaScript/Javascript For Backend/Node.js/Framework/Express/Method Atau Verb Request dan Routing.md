#programming 
Setelah membuat dan menjalankan server, selanjutnya adalah menambahkan routing agar server dapat merespons permintaan sesuai dengan method dan url yang diminta oleh client.

Routing pada Express tidak dilakukan di dalam request handler seperti cara native. Namun, ia memanfaatkan method dari objek `app`. Objek app merupakan instance dari `express`.

Perhatikan kode yang ditebalkan.
```js
import express from 'express';
 
const app = express();
const port = 3000;
const host = 'localhost';
 
app.get('/', (req, res) => {
  res.send('Hello World!')
})
 
app.listen(port, () => {
  console.log(`Server running at http://${host}:${port}`);
});
```

Untuk mendefine route menggunakan struktur seperti berikut.
```js
app.METHOD(PATH, HANDLER)
```
- `METHOD` merupakan sebuah [HTTP request method](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods) yang dituliskan dalam bentuk lowercase.
- `PATH` merupakan alamat yang dituju.
- `HANDLER` merupakan function yang dieksekusi ketika route dipanggil.

Lalu, bagaimana cara menetapkan lebih dari satu route? Mudah! 

Sebenarnya, kita bisa secara mudah menambahkan route seperti ini:
```js
import express from 'express';
 
const app = express();
const port = 3000;
const host = 'localhost';
 
app.get('/', (req, res) => {
  res.send('Hello World!')
})
 
app.post('/', (req, res) => {
  res.send('POST request to the homepage')
})
 
app.listen(port, () => {
  console.log(`Server running at http://${host}:${port}`);
});
```

Namun, cara tersebut tidak kami rekomendasikan. Sebaiknya, route dipisahkan pada berkas JavaScript berbeda. Dengan begitu, satu berkas JavaScript hanya memiliki satu fungsi atau tanggung jawab saja (single responsibility principle).

routes.js
```js
import express from 'express';
 
const router = express.Router();
 
router.get('/', (_, res) => {
  res.send('Homepage');
});
 
router.get('/about', (_, res) => {
  res.send('About page');
});
 
export default router;
```

server.js
```js
import express from 'express';
import routes from './routes.js'
 
const app = express();
const port = 3000;
const host = 'localhost';
 
app.use('', routes);
 
app.listen(port, () => {
  console.log(`Server running at http://${host}:${port}`);
});
```

#### Latihan Routing

Setelah mengetahui cara menspesifikasikan route pada Express, sekarang saatnya kita terapkan apa yang sudah kita ketahui pada web server yang sudah dibuat sebelumnya. 

Pada latihan kali ini, kita akan membuat routes configuration dengan ketentuan berikut:

- URL: ‘/’
    - Method: GET
        - Mengembalikan pesan “Homepage”.
    - Method: `<any>` (selain method GET)
        - Mengembalikan pesan “Halaman tidak dapat diakses dengan method tersebut”.
- URL: ‘/about’
    - Method: GET
        - Mengembalikan pesan “About page”.
    - Method: `<any>` (selain method GET)
        - Mengembalikan pesan “Halaman tidak dapat diakses dengan method tersebut”.
- URL: `<any>` (selain “/’ dan “/about”)
    - Method: `<any>`
        - Mengembalikan pesan “Halaman tidak ditemukan”.

Agar kode lebih terkelompok, tulis route configuration pada berkas JavaScript terpisah. Silakan buat berkas JavaScript baru pada proyek express-web-server dengan nama “**routes.js**”. Kemudian, tuliskan kumpulan routes configuration dalam bentuk array sesuai dengan ketentuan.
```js
import express from 'express';
 
const router = express.Router();
 
router.get('/', (_, res) => {
  res.send('Homepage');
});
 
router.get('/about', (_, res) => {
  res.send('About page');
});
 
router.all('/', (_, res) => {
  res.status(405).send('Halaman tidak dapat diakses dengan method tersebut');
});
router.all('/about', (_, res) => {
  res.status(405).send('Halaman tidak dapat diakses dengan method tersebut');
});
router.use((_, res) => {
  res.send('Halaman tidak ditemukan');
});
 
export default router;
```

Tunggu, sepertinya ada beberapa hal baru yang belum Anda ketahui.  
Mari kita bedah kode yang ditebalkan yah.  
  
Anda bisa lihat beberapa properti method menggunakan **`.all()`**. Nah, `.all()` ini artinya route dapat diakses menggunakan [seluruh method HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) (GET, POST, PUT, DELETE, dll). Jadi, meskipun method yang digunakan berbeda, Express akan tetap mengeksekusi handler tersebut. Dalam kasus ini, semua method selain GET untuk `/` dan `/about` akan ditolak dengan status **405 Method Not Allowed**. 

Kemudian, `router.use()`. Fungsinya adalah menangani permintaan masuk pada path yang **belum Anda tentukan** sebelumnya. Teknik ini sering digunakan untuk membuat routing dinamis di Express, biasanya untuk menampilkan halaman **404 Not Found**.

Oke, sudah paham? Jika sudah, mari kita lanjutkan.

Setelah menetapkan routes configuration, gunakan nilainya menggunakan `app.use('', routes);` pada berkas `server.js`.

```js
import express from 'express';
import routes from './routes.js';
 
const app = express();
const port = 3000;
const host = 'localhost';
 
app.use('/', routes);
 
app.listen(port, () => {
  console.log(`Server running at http://${host}:${port}`);
});
```
Kode tersebut digunakan untuk **mendaftarkan router** (`routes`) ke dalam aplikasi utama Express (`app`).

- Nilai `'/'` artinya router dipasang langsung di **root path** (`/`). Jadi, semua path di dalam `routes` bisa diakses tanpa prefix tambahan.
- Kalau nilainya `/api`, maka semua path di dalam `routes` otomatis punya prefix `/api`.

Simpan seluruh perubahan yang ada baik pada berkas routes.js dan **server.js**; jalankan ulang server dengan perintah `npm run start`; dan coba lakukan permintaan ke server. Seharusnya server sudah bisa merespons sesuai dengan yang diharapkan.

```shell
curl -X GET http://localhost:3000
// output: Homepage
curl -X GET http://localhost:3000/about
// output: About page
curl -X GET http://localhost:3000/test
// output: Halaman tidak ditemukan
curl -X POST http://localhost:3000
// output: Halaman tidak dapat diakses dengan method tersebut
```