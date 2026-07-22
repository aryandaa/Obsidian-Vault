Pikirkan kembali skenario kedai kopi atau lingkungan AWS kita. Proses pemesanan pada kedai kopi adalah pelanggan menyampaikan ordernya kepada kasir yang lantas meneruskannya ke barista. Proses ini seharusnya sudah berjalan lancar tanpa kendala ya.

Meskipun demikian, bagaimana jika ada beberapa pelanggan tak sabar yang coba mengabaikan kasir dan ingin memberikan pesanannya langsung ke barista? Para pelanggan penerobos antrean ini tentu akan merusak alur kedai kopi.

Yah, tak mungkin kita biarkan pelanggan terus berinteraksi dengan barista. Alih-alih menerima pesanan, sang barista harus fokus membuat kopi saja. Jadi, apa yang harus kita perbuat?

Di AWS Anda bisa menggunakan Amazon Virtual Private Cloud (Amazon VPC) untuk menuntaskan dilema ini. VPC memungkinkan Anda untuk menyediakan bagian logis dari AWS Cloud yang terisolasi, di mana Anda dapat meluncurkan sumber daya AWS di jaringan virtual sesuai kebutuhan.

Sumber daya tersebut dapat menjadi _public-facing_ yang berarti memiliki akses ke internet ataupun _private_ alias tanpa akses internet. Jenis kedua biasanya dipakai untuk layanan _backend_ seperti database atau server aplikasi.

Nah, pengelompokan sumber daya menjadi publik dan privat ini disebut dengan _subnet_ yang juga merupakan rentang alamat IP di VPC Anda.

Sekarang mari kembali ke kedai kopi dan mengimplementasikan apa yang telah kita pelajari di atas. Anda dapat menempatkan kasir dan barista di area kerja yang terpisah.

Karena kasir bertanggung jawab untuk menerima pesanan pelanggan, maka kita tempatkan ia di _subnet publik_. Sehingga, kasir dapat berkomunikasi langsung dengan pelanggan atau internet--jika kasusnya adalah _instance_.

Berbeda kasusnya untuk barista. Karena kita ingin ia fokus untuk membuat kopi dan tidak berinteraksi dengan pelanggan secara langsung, maka kita tempatkan ia di _subnet privat_. Dengan begitu, barista tetap dapat menerima pesanan dari kasir tetapi tidak langsung dari pelanggan.

