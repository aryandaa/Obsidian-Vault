#programming 
REST API seringnya menggunakan JavaScript Object Notation atau JSON sebagai format data baik itu pada request ataupun response. JSON merupakan salah satu format standar dalam transaksi data. Bahkan, saat ini JSON menjadi format terpopuler mengalahkan pendahulunya yaitu [XML](https://id.wikipedia.org/wiki/XML).

> Sebenarnya Anda bisa menggunakan XML pada REST API, namun sebaiknya gunakan JSON agar lebih mudah dibaca dan efisien dalam transaksi data.

Agar REST API selalu merespons dengan format JSON, pastikan setiap respons terdapat properti `Content-Type` dengan nilai `application/json`.

Seperti namanya, JSON memiliki struktur seperti JavaScript Object yakni menggunakan _key-value_. Bedanya, key pada JSON selalu dituliskan menggunakan tanda kutip dua (“”). Value pada JSON dapat menampung nilai primitif seperti string, number, boolean, atau nilai non primitif seperti object atau array.

Pada latihan sebelumnya Anda sudah melihat bagaimana bentuk JSON ketika mengirimkan data pembelian kopi dan data pada body respon dari server. Berikut contoh struktur JSON ketika melakukan GET request terhadap URL [https://coffee-api.dicoding.dev/coffees](https://coffee-api.dicoding.dev/coffees):

```json
{
  "message": "Berikut daftar kopi yang tersedia",
  "coffees": [
    {
      "id": 1,
      "name": "Kopi Tubruk",
      "price": 12000
    },
    {
      "id": 2,
      "name": "Kopi Tarik",
      "price": 15000
    },
    {
      "id": 3,
      "name": "Kopi Jawa",
      "price": 18000
    }
  ]
}
```

Walaupun memiliki nama JavaScript Object Notation, bukan berarti kita harus menggunakan JavaScript untuk mengolah data dengan format JSON. Format JSON dapat digunakan oleh hampir semua bahasa pemrograman yang ada.
