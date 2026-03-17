#programming 
Web storage terbagi menjadi 2 yakni local storage dan session storage. Sebelum menggunakan Web Storage baik sessionStorage atau localStorage, kita perlu memastikan browser support terhadap fitur tersebut, dengan cara menjalankan perintah berikut pada console browser:

```js
typeof(storage);
```
Output yang dihasilkan semestinya tidak bertuliskan "undefined".

Seharusnya browser yang ada saat ini sudah mendukung kedua fitur tersebut, seperti Google Chrome dan Mozilla Firefox.

Data yang tersimpan dalam _sessionStorage_ atau _localStorage_ adalah nilai dengan tipe data primitif seperti **number**, **boolean**, atau **string**. Namun, kita juga dapat menyimpan data berbentuk JavaScript objek dengan mengubahnya ke dalam **string (JSON)** terlebih dahulu, begitu pula sebaliknya ketika kita ingin menggunakan datanya kembali.

Metode yang dapat digunakan untuk menyimpan dan mengakses data pada storage adalah _key-value_. Di sini _key_ menjadi sebuah kunci untuk mengakses data pada storage. Ibarat sebuah loker, jika Anda ingin menyimpan sebuah benda pasti memerlukan kunci unik untuk loker tersebut. Sama halnya jika Anda ingin mengambil kembali barang tersebut, yakni membukanya dengan kunci yang tepat.

Data yang disimpan pada Web Storage dapat kita lihat menggunakan DevTools pada _tab_**Application** (Google Chrome) atau _tab_**Storage** (Mozilla Firefox).