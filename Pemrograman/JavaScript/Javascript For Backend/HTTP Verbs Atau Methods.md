#programming 
Karena REST API menggunakan protokol HTTP, kita dapat memanfaatkan HTTP verbs untuk menentukan aksi.

`GET` untuk mendapatkan data, 
`POST` untuk mengirimkan data baru,
`PUT` untuk memperbarui data yang ada, 
`DELETE` untuk menghapus data. 
Verbs tersebutlah yang umum digunakan dalam operasi **CRUD**.

## HTTP Response Code
Status-Line merupakan salah satu bagian dari HTTP Response. Di dalam status line terdapat response code yang mengindikasikan bahwa permintaan yang client lakukan berhasil atau tidak. Karena itu, ketika membangun REST API kita perlu memperhatikan dan menetapkan response code secara benar.

Status code bernilai 3 digit angka. Pada REST API, berikut nilai-nilai status code yang sering digunakan:

- **200** (OK) - Permintaan client berhasil dijalankan oleh server.
- **201** (Created) - Server berhasil membuat/menambahkan resource yang diminta client.
- **400** (Bad Request) - Permintaan client gagal dijalankan karena proses validasi input dari client gagal.
- **401** (Unauthorized) - Permintaan client gagal dijalankan. Biasanya ini disebabkan karena pengguna belum melakukan proses autentikasi.
- **403** (Forbidden) - Permintaan client gagal dijalankan karena ia tidak memiliki hak akses ke resource yang diminta.
- **404** (Not Found) - Permintaan client gagal dijalankan karena resource yang diminta tidak ditemukan.
- **500** (Internal Server Error) - Permintaan client gagal dijalankan karena server mengalami eror (membangkitkan Exception).
- **503** (Service Unavailable) - Permintaan client gagal dijalankan karena server tidak dapat menangani permintaan.

Ketika permintaan client gagal dijalankan, kita harus mengembalikan status code yang sesuai dengan kesalahan yang terjadi. Penggunaan response code yang tepat dapat meminimalisir kebingungan client/user dalam memanfaatkan API.

> Untuk eksplorasi lebih detail, Anda dapat membaca mengenai status code di halaman [MDN status code](https://developer.mozilla.org/id/docs/Web/HTTP/Status).

