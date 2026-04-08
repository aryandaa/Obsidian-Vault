#programming 
Meskipun Back-End dan Front-End terpisah dalam hal peran dan konsentrasi, namun keduanya harus saling terhubung secara lancar (_seamless_) agar aplikasi dapat berjalan dengan baik. Kembali ke analogi kedai kopi, ketika Anda memesan kopi tubruk di kasir, bagaimana informasi tersebut bisa sampai ke barista? Lalu bagaimana caranya kopi yang sudah dibuat barista sampai ke meja kita? Pasti ada perantara mengapa semuanya saling terhubung. Pada kedai kopi, penghubung itu adalah seorang pelayan.

Pelayan mencatat pesanan yang Anda inginkan kemudian mengirimnya ke barista. Setelah barista selesai membuat kopi, pelayan juga yang mengantarkan kopi dari barista ke meja Anda. Semua transaksi yang terjadi menggunakan perantara. Sebagai pelanggan, Anda tidak bisa masuk ke dapur dan meminta kopi langsung ke barista, karena hal tersebut tentu menyalahi prosedur.

Begitu pula dengan transaksi yang terjadi pada sistem aplikasi. Kita harus merancang sistem aplikasi dengan prosedur yang benar. Transaksi yang dilakukan Back-End ke Front-End harus melalui perantara. Front-End tidak boleh memiliki akses terhadap database secara langsung, begitu pula dengan Back-End yang sama sekali tidak boleh diakses secara langsung oleh pengguna (end-user). Pada sistem aplikasi, perantara tersebut dinamakan “server” yang posisinya serupa pelayan di kedai kopi.
![](Pemrograman/JavaScript/Javascript%20For%20Backend/Img/1.png)

## Apa itu Server?
Namun sebenarnya apa itu server? Server merupakan sebuah sistem yang dapat menyediakan sumber daya berupa data, layanan, atau program untuk disajikan ke komputer lain [[]](https://www.paessler.com/it-explained/server).  Ingat! Pengertian dari server bukanlah sebuah perangkat keras ataupun komputer, namun server sendiri lebih merujuk kepada sistem yang dapat membuat perangkat (termasuk komputer) dapat melayani sebuah permintaan dari perangkat lain. Jika diterjemahkan ke dalam Bahasa Indonesia, server memang berarti penyaji, atau pelayan.

Server bertugas untuk melayani sebuah layanan (services) atau jasa. Dalam dunia komputer ada banyak service yang dapat dilayani oleh server. Berikut beberapa tipe server sesuai dengan layanan yang baik untuk Anda ketahui.

- **File Server** : melayani penyimpanan dan pendistribusian berkas.
- **Application Server** : melayani hosting sebuah program atau aplikasi.
- **DNS Server** : mengubah nama domain (contoh: dicoding.com) ke dalam bentuk IP Address (contoh: 75.2.21.170).
- **Web Server** : melayani hosting sebuah program atau aplikasi (seperti Application Server) yang dapat diakses oleh client melalui internet maupun intranet.
- **Database Server** : melayani penyimpanan dan pendistribusian data terstruktur.

Sebenarnya masih banyak lagi tipe server yang tidak disebutkan, namun Anda tidak perlu mengetahui itu semua saat ini. Ada satu tipe server yang perlu kita fokuskan sekarang, yakni server yang dapat berperan sebagai pelayan kedai kopi. Server apakah itu? Mari kita berkenalan lebih dalam dengan Web Server.


