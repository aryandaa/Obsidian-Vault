#programming 
Selain path parameter, terdapat cara lain yang sering digunakan dalam mengirimkan data melalui URL, yakni dengan query parameter. Teknik ini umum digunakan pada permintaan yang membutuhkan kueri dari client, contohnya seperti pencarian dan filter data. 

Data yang dikirim melalui query memiliki format **key=value**. Contohnya:
```url
localhost:3000?name=harry&location=bali
```

Contoh di atas memiliki dua query parameter. Yang pertama adalah `name=harry` dan `location=bali`. Di Express, Anda bisa mendapatkan nilai query parameter melalui `req.query`. Contoh:
```js
app.get('/', (req, res) => {
    const { name, location } = req.query;
    res.send(`Hello, ${name} from ${location}`);
});
```

Jika client melakukan permintaan ke:
```url
http://localhost:3000?name=harry&location=bali
```

 Server akan menanggapi dengan:
 ```output
 Hello, harry from bali
 ```

#### Latihan Query Parameters
Saatnya latihan!

Pada latihan kali ini kita akan menambahkan dukungan bahasa terhadap path `/hello/:name?` yang sudah kita buat. 

- Bila path tersebut memiliki kueri `lang` dengan nilai `id`, maka server akan menanggapi dengan pesan “Hai, {name}!”. 
- Selain itu, biarkan pesan tetap sama seperti latihan sebelumnya. 

Ayo kita mulai!

Buka berkas routes.js dan ubah route /hello/{name}. Dapatkan nilai path parameter melalui req.params dan query parameter melalui req.query.
```js
router.get('/hello/:name?', (req, res) => {
  const { name = 'stranger' } = req.params;
const { lang } = req.query;
 
  res.send(`Hello, ${name}!`);
});
```

Lalu, sesuaikan pesan kembalian handler berdasarkan evaluasi nilai `lang` seperti ini:
```js
if (lang === 'id') {
    return res.send(`Hai, ${name}!`);
}
```

Simpan perubahan pada berkas **routes.js**; jalankan kembali server dengan perintah `npm run start`; dan lakukan permintaan pada path `/hello/dicoding` dengan dan tanpa melampirkan kueri `lang=id`.
```shell
curl -X GET http://localhost:3000/hello/dicoding?lang=id
// output: Hai, dicoding!

curl -X GET http://localhost:3000/hello/dicoding
// output: Hello, dicoding!
```
