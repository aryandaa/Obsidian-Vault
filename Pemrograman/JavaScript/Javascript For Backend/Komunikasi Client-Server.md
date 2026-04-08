#programming 
HTTP/HTTPS merupakan salah satu protokol yang dapat digunakan untuk berinteraksi dengan web server. Protokol tersebut terkenal dengan pola _request-response_, artinya untuk mendapatkan sesuatu (_response_) kita perlu melakukan permintaan terlebih dahulu (_request_). Lagi-lagi ini menjadi pola yang sama ketika kita hendak memesan kopi di kedai kopi.

Ketika Anda ingin membeli kopi, tentu kopi yang diinginkan tidak secara ajaib datang sendiri. Anda sebagai pelanggan perlu mendatangi kasir atau pelayan untuk meminta (_request_) kopi yang diinginkan, pelayan meneruskan permintaan Anda ke barista, kemudian barista membuatkan kopi, dan memberikannya kembali (respons) ke pelayan untuk dihidangkan kepada Anda.
![](Pemrograman/JavaScript/Javascript%20For%20Backend/Img/2.png)

Pola yang sama dengan komunikasi client dengan server (untuk memudahkan pemahaman, sebutlah client adalah Front-End, server adalah Back-End) bila menggunakan protokol HTTP/S. Server tidak akan mengirimkan data apa pun apabila tidak ada permintaan dari client. Ketika client meminta sesuatu, barulah server akan menanggapi.
![](Pemrograman/JavaScript/Javascript%20For%20Backend/Img/3.png)

_Ngomong-ngomong_ tentang permintaan (_request_), ketika hendak mengajukan permintaan kepada pelayan tentu Anda harus memberikan informasi jelas perihal apa yang ingin Anda minta. Contohnya bila meminta kopi, beritahu kopi apa yang ingin dipesan. Bila ingin menanyakan lokasi toilet, ucapkan “Di mana letak toilet?” Bila permintaan yang Anda ajukan tidak memiliki keterangan yang cukup, maka pelayan tidak dapat memproses permintaan Anda.

Begitu pula dengan request pada protokol HTTP di mana request yang diajukan client harus memiliki informasi-informasi yang cukup agar dapat dieksekusi oleh server. Informasi pada request dapat mengandung:

- **Request line** : berisikan method/verb seperti GET (mengambil data), POST (menambahkan/mengirim data), PUT (memperbaharui data), atau DELETE (menghapus data); path atau alamat yang diminta; dan versi HTTP yang digunakan.
- **Header** : memuat informasi yang dilampirkan terkait request seperti format dokumen (contoh application/json, text/html, dsb), kunci akses, dsb.
- **Body (opsional)** : mengandung data yang dibutuhkan oleh server, bisa dalam bentuk teks, JSON, dll. Body tidak wajib dilampirkan bila server tidak membutuhkan data apapun.

Apabila informasi yang dilampirkan pada request tidak jelas/sesuai, maka server akan menolaknya dengan respons negatif. Respons negatif? Apa itu?

Setiap request yang dilakukan, baik dengan informasi yang sesuai ataupun tidak, akan mendapatkan respons. Respons atau tanggapan yang dikirimkan dari server untuk client juga mengandung informasi. Berikut beberapa informasi yang dilampirkan oleh respons:

- **Status line** : berisikan HTTP versi yang digunakan; status code berupa tiga digit angka yang menandakan keberhasilan dari permintaan; reason phrase atau status text yang merupakan pesan berdasarkan status code dalam bentuk teks sehingga lebih mudah dimengerti.
- **Header** : mengandung informasi yang dilampirkan terkait response seperti format dokumen.
- **Body (opsional, namun biasanya selalu dilampirkan)** : memuat data yang dikirimkan oleh server. Data dapat berupa HTML, JSON, gambar, dsb.

Kembali ke istilah respons negatif, apa maksudnya? **Respons negatif merupakan respons dari server ketika sebuah permintaan dari client gagal dipenuhi**. Sama seperti di dunia nyata, ketika kita meminta kopi tubruk di kedai, namun permintaan kita tidak dapat kedai kopi penuhi sebab alasan teknis. Alih-alih mendapatkan kopi kita hanya mendapatkan pesan “maaf stok kopi habis” atau “maaf mesin kopi sedang rusak.”

Begitu pula dengan protokol HTTP. Bila kita meminta sesuatu yang tidak dapat server proses, maka kita tidak akan mendapatkan data yang diinginkan. Server akan memberikan respons negatif dengan alasan mengapa ia tidak bisa memenuhi permintaannya, contohnya seperti “Not Found”, “Bad Request” atau pesan lainnya.

Kita dapat mengetahui sebuah request berhasil atau tidak melalui status code yang dikirim oleh response. Sebuah request berhasil bila status code response diawali dengan angka 1, 2 atau 3, selain itu request gagal dieksekusi.