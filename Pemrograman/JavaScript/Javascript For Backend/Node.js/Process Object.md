#programming 
Salah satu global objek yang penting untuk diketahui adalah process. Dalam ilmu komputer, process adalah sebuah program yang dijalankan pada satu atau lebih thread. Anda bisa melihat proses yang sedang berjalan pada komputer Anda melalui Task Manager (Windows), System Monitor (Ubuntu), atau Activity Monitor (macOS).

Pada Node.js, global objek `process` memiliki fungsi dan properti yang dapat memberikan informasi mengenai proses yang sedang berjalan.

Salah satu yang sering digunakan adalah properti `process.env`. Melalui properti ini kita dapat menyimpan nilai atau mendapatkan informasi mengenai _environment_ yang digunakan selama proses sedang berlangsung. Contoh, `process.env` memiliki properti `process.env.PWD` yang menyediakan informasi mengenai lokasi di mana proses dijalankan; properti `process.env.USER` menyimpan informasi nama user pada komputer Anda; dan masih banyak properti lainnya. Anda bisa lihat daftar lengkap properti yang ada pada halaman [dokumentasi Node.js mengenai process.env](https://nodejs.org/dist/latest-v8.x/docs/api/process.html#process_process_env).

Anda juga bisa secara manual menyimpan nilai di dalam `process.env`. Hal ini berguna untuk menentukan alur code seperti if-else dalam program berdasarkan _environment_ yang Anda berikan. Contohnya, ketika Anda ingin nilai variabel `host` berbeda di kala pengembangan (_development_) dan produksi (_production_), Anda bisa membuat properti `NODE_ENV` pada `process.env`. Jadi, Anda bisa menentukan nilai host berdasarkan kondisi `NODE_ENV`.

```js
import http from 'http';
const hostname = process.env.NODE_ENV !== 'production' ? 'localhost' : 'dicoding.com';
const port = 3000;
const requestHandler = (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
};
const server = http.createServer(requestHandler);
server.listen(port, hostname, () => {
  console.log(`Server berjalan pada http://${hostname}:${port}/`);
});
```

Untuk memberikan nilai pada properti `process.env`, kita dapat memberikannya ketika mengeksekusi berkas JavaScript. Caranya seperti ini:
`
untuk Mac / Linux:
`NODE_ENV=development node app.js`

untuk Windows:
`SET NODE_ENV=development && node app.js`

Nilai yang ada pada process.env hanya dapat diakses di dalam cakupan proses Node.js. Itu berarti Anda tidak dapat menggunakan nilainya pada program lain seperti menampilkan nilainya melalui program `echo`.

```node
// perintah ini tidak akan berjalan
node -e 'process.env.foo = "bar"' && echo $foo
```

Selain untuk menetapkan dan mendapatkan informasi mengenai environment, objek `process` memiliki kegunaan lain. Salah satunya adalah mendapatkan informasi tentang penggunaan memory ketika proses berjalan. Anda dapat mengakses informasi tersebut melalui fungsi `process.memoryUsage()`.

```node
const memoryInformation = process.memoryUsage();
 
console.log(memoryInformation);
 
/* output
{
  rss: 14569472,
  heapTotal: 2654208,
  heapUsed: 1788896,
  external: 855681,
  arrayBuffers: 9898
}
*/
```

Yang terakhir dan tak kalah pentingnya adalah properti `process.argv`. Properti ini dapat menampung nilai baris perintah dalam bentuk array ketika menjalankan proses. Contoh jika kita menjalankan baris perintah berikut:
```node
node app.js "harry" "potter"
```

Maka array `process.argv` akan bernilai:

- Elemen pertama : Alamat (path) lengkap dari lokasi node yang menjalankan prosesnya. 
- Element kedua : Alamat (path) berkas JavaScript yang dieksekusi (app.js)
- Element ketiga : “harry”
- Element keempat : “potter”

Bila **app.js** memiliki kode seperti ini:
```js
const firstName = process.argv[2];
const lastName = process.argv[3];
 
console.log(`Hello ${firstName} ${lastName}`);
```

Maka output yang dihasilkan tampak seperti ini:
`Hello harry potter`

Kita hanya membahas sedikit tentang properti dan fungsi yang ada pada `process` objek. Anda bisa mendalaminya dengan membaca [dokumentasi tentang objek process](https://nodejs.org/api/process.html).