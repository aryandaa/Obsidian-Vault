#programming 
URL, Path, atau Endpoint merupakan salah satu bagian terpenting yang harus diperhatikan ketika membangun REST API. Dengan merancang endpoint yang baik, penggunaan API akan lebih mudah dipahami. Dalam merancang endpoint, ikutilah aturan umum atau convention agar penggunaan API kita memiliki standar yang diharapkan oleh banyak developer. Lalu, seperti apa standar dalam merancang endpoint?

### Gunakan Kata Benda daripada Kata Kerja pada Endpoint Path
Hindari penggunaan kata kerja dalam menetapkan nama endpoint (titik akhir path). Contohnya `/getArticles` atau `/addArticles`. Karena aksi dapat ditentukan secara jelas melalui HTTP Verb, kita tidak perlu lagi menambahkan kata kerja di endpoint. Dengan adanya HTTP verbs Anda cukup memberikan endpoint `GET /articles` untuk mendapatkan data artikel atau `POST /articles` untuk menambahkan artikel.


### Gunakan Kata Jamak pada Endpoint untuk Resource Collection
Selalu gunakan kata jamak (plural) saat memberikan nama endpoint. Ini karena jarang ada data yang hanya memiliki satu item. Dengan menggunakan kata jamak, kita menjadi konsisten dengan apa yang ada di database. Karena tabel pada database pun biasanya memiliki lebih dari satu record (data).

Lalu, bagaimana bila ingin mengakses satu data saja? Contohnya mendapatkan satu artikel secara spesifik?

Gunakan path parameter untuk mendapatkan data spesifik. Endpoint `/articles/:id` merupakan contoh yang baik untuk mendapatkan artikel secara spesifik berdasarkan `id`. Kita akan membahas dan menggunakan path parameter nanti ketika latihan membuat web server.


### Gunakan Endpoint berantai untuk resource yang memiliki hirarki/relasi
Endpoint dari resource yang memiliki hirarki/relasi sebaiknya dituliskan secara berantai. Contohnya untuk mendapatkan daftar komentar dari sebuah artikel, endpoint `GET /articles/:id/comments` merupakan contoh yang tepat.

Penggunaan endpoint tersebut masuk akal karena untuk mendapatkan `comments` pada respons, kita perlu tahu komentar pada artikel mana yang akan ditampilkan. Prinsip ini juga memperjelas permintaan dari client hanya dengan melihat endpoint yang dituju.

Tidak hanya `GET`, prinsip ini juga cocok diterapkan pada HTTP verb `POST`, `PUT`, maupun `DELETE`.

