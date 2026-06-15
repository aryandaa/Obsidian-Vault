#programming 
Mari kita berbicara mengenai teknik routing lebih lanjut. Path dalam routing bisa dikatakan sebagai alamat yang digunakan client untuk melakukan permintaan ke server. Alamat atau path yang dibuat biasanya merupakan teks verbal yang dapat dimengerti oleh client. Tak jarang hanya dengan membaca path dari sebuah tautan kita langsung mengerti apa yang client minta kepada server.

Sebagai contoh, ketika membaca tautan GitHub ini [https://github.com/dicodingacademy](https://github.com/dicodingacademy), Anda pasti mengerti bahwa client ingin meminta server untuk menampilkan profil github dari username “dicodingacademy”. 

Contoh lain, dari alamat [https://twitter.com/maudyayunda](https://twitter.com/maudyayunda), coba Anda tebak kira-kira apa yang diminta client ke server? Jika Anda berpikir client meminta profil twitter kak Maudy Ayunda, yups, Anda tepat sekali!

Twitter dan Github menggunakan pendekatan yang sama dalam menampilkan halaman profil. Mereka memanfaatkan _username_ sebagai bagian dari path untuk melakukan permintaan ke server. Terbayang tidak _sih_ bagaimana mereka melakukannya? Di saat mereka memiliki pengguna yang banyak, apakah mereka menetapkan route secara satu per satu berdasarkan username untuk setiap penggunanya? Tentu tidak!

Untuk melakukan hal tersebut, Twitter dan Github menggunakan teknik path parameter. Pada Express framework, teknik tersebut cukup mudah diterapkan. Path parameter di Express ditulis dengan awalan titik dua (`:`). Sebagai contoh:
```js
app.get(['/users', '/users/:username'], (req, res) => {
    // Jika req.params.username undefined, variabel username akan bernilai 'stranger'
    const username = req.params.username || 'stranger';    
    res.send(`Hello, ${username}!`);
});
```

Seperti yang Anda lihat di atas, bagian yang diawali dengan tanda titik dua (contohnya **`:username`**) pada properti _path_ disebut sebagai **Path Parameter**. Tanda tersebut menandakan bahwa bagian URL tersebut bersifat **dinamis**, di mana server akan menangkap nilai apa pun yang dimasukkan oleh _client_ pada posisi tersebut dan menyimpannya sebagai variabel di dalam `req.params`

Nantinya parameter ini akan disimpan sebagai properti pada dengan nama sesuai yang Anda tetapkan (username). Sebagai contoh, bila Anda melakukan permintaan ke server dengan alamat `/users/harry`, maka server akan menanggapi dengan `Hello, harry!`.

Pada contoh kode di atas, nilai path parameter wajib diisi oleh client. Bila client mengabaikannya dengan melakukan permintaan pada alamat `/users`, maka server akan mengembalikan error _Not Found_.

Tapi tenang, pada Express Anda dapat membuat path parameter bersifat opsional. Caranya dengan menambahkan tanda “?” di akhir nama parameternya. Berikut contoh yang sama namun dengan implementasi opsional path parameter:
```js
app.get('/users{/:username}', (req, res) => {
    const { username = 'stranger' } = req.params;
    res.send(`Hello, ${username}!`);
});
```

Sekarang bila client meminta pada alamat ‘`/users/dicoding`’, server menanggapi dengan ‘Hello, dicoding!’; dan bila client meminta hanya pada path ‘`/users`’, server akan menanggapinya dengan ‘Hello, stranger!’.

Anda bisa menetapkan lebih dari satu path parameter. Namun, penting untuk Anda ketahui bahwa optional path parameter hanya dapat digunakan di akhir bagian path saja. Artinya, jika Anda menetapkan optional path di tengah-tengah path parameter lain contohnya `/:one?/:two`, maka path ini dianggap tidak valid oleh Express.


#### Latihan Path Parameter
Sekarang Anda sudah tahu apa itu path parameter, saatnya kita coba praktikkan pada web server yang sudah dibuat. 

Pada latihan kali ini, kita akan membuat route baru dengan nilai path `/hello/name?`. Bila client melampirkan nilai path parameter, server harus mengembalikan dengan pesan “Hello, name!”. Namun bila tidak, server harus mengembalikan dengan nilai  
“Hello, stranger!”. Sudah paham? Yuk kita mulai!

Buka berkas **routes.js** dan tambahkan route baru seperti ini (lihat kode yang ditebalkan).
```js
router.get('/hello{/:name}', (req, res) => {
  const { name = 'stranger' } = req.params;
  res.send(`Hello, ${name}!`);
});
```

Simpan perubahan pada berkas **routes.js**; coba jalankan kembali server dengan perintah `npm run start`; dan lakukanlah permintaan melalui curl atau browser pada path **/hello/dicoding** dan **/hello**.

```shell
curl -X GET http://localhost:3000/hello/dicoding
// output: Hello, dicoding!

curl -X GET http://localhost:3000/hello
// output: Hello, stranger!
```

