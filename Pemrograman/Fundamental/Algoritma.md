#programming 
Algoritma membantu membuat structure dari suatu masalah, dengan begitu kita bisa mudah membuat alur problem solvingnya secara terurut, masuk akal, dan sistematis.

Ketika menyusun algoritma, terdapat beberapa hal yang harus diperhatikan, seperti:

- **Finiteness (Keterbatasan)**  
    Algoritma yang berjalan dan memproses setiap langkah-langkahnya memiliki sifat terbatas, sehingga ia harus berhenti ketika semua langkah-langkahnya selesai dikerjakan. Jangan membuat algoritma yang panjang dan tidak ada akhirnya karena akan bertentangan dengan sifat finiteness ini.
    
- **Definiteness (Kepastian)**  
    Setiap langkah algoritma harus jelas, detail, dan tidak ambigu (makna ganda). Dengan kata lain, pembaca harus mengerti apa tujuan yang dimaksud. Misalnya Anda ingin membuat algoritma untuk menghitung luas persegi. Dari sana penggunanya harus tahu kalau yang diinputkan hanya berupa angka, bukan teks.  
      
    
- **Effectiveness (Efektivitas)**  
    Setiap algoritma harus dibuat secara efektif. Langkah-langkah yang ada di dalamnya juga harus sesuai kebutuhan dan tidak perlu berlebihan. Dengan langkah yang efektif, waktu yang dibutuhkan pun akan lebih singkat atau masih dalam batas wajar.  
      
    
- **Input (Masukan)**  
    Algoritma pasti membutuhkan nol atau lebih masukan (input) sebelum prosesnya dimulai. Misalnya algoritma untuk menghitung luas persegi panjang. Anda harus memasukkan dua input berupa angka untuk panjang dan lebarnya.  
      
    
- **Output (Keluaran)**  
    Setiap input yang diproses oleh algoritma pasti memiliki satu atau lebih keluaran (output). Keluaran adalah besaran nilai yang memiliki hubungan dengan masukan (input). Keluaran harus berupa solusi atau penyelesaian dari suatu masalah. Jika sebuah algoritma tidak menemukan solusi, setidaknya harus menunjukkan pesan eror yang jelas. Misalnya dalam algoritma menghitung luas persegi panjang, pengguna melakukan kesalahan dengan memasukkan input berupa teks. Sehingga algoritma yang Anda buat harus bisa menangani hal tersebut dengan menampilkan pesan eror dan mengatakan inputnya harus berupa angka.


Masih ingat cerita diskon 20% yang ingin Anda dapatkan di supermarket pada materi sebelumnya? Sebelumnya mari kita segarkan kembali ingatan tentang cerita diskon 20% tersebut.

Ketika Anda melihat plakat yang bertuliskan diskon 20%, seketika jiwa shopping Anda bergejolak. Setelah membaca lebih lanjut ternyata syarat mendapat diskon adalah total belanja minimal 300 ribu untuk segala jenis barang. Di sini Anda berpikir, “Jika jumlah harga barang yang saya beli lebih dari atau sama dengan 300 ribu, maka saya berhak mendapat diskon 20%.” Nah, itulah yang dimaksud dengan penerapan logika pemrograman.

Kemudian Anda memutuskan untuk belanja kebutuhan rumah tangga sekaligus produk lainnya supaya mendapat diskon 20%. Nah, untuk mendapatkan diskon tersebut kita bisa menerapkan algoritma seperti berikut.

1. Anda harus masuk ke supermarketnya terlebih dahulu.
2. Ambil keranjang atau troli belanja.
3. Pilih barang-barang yang ingin Anda beli.
4. Lihat harga yang tercantum di setiap rak tempat Anda mengambil barang.
5. Setelah semua barang sudah masuk ke dalam troli dan totalnya masih belum mencapai 300 ribu, cari barang lainnya.
6. Ketika total harga barang yang Anda beli sudah mencapai 300 ribu atau lebih dan dirasa cukup, berjalanlah menuju meja kasir.
7. Tunggu kasir menghitung kembali semua barang belanjaan Anda.
8. Keluarkan dompet Anda dan bayarkan sesuai total harga belanjaan yang sudah dihitung oleh kasir.
9. Periksa kembali struk yang diberikan oleh kasir dan pastikan sudah mendapat diskon 20%.
10. Ketika pembayaran selesai, jangan lupa ambil belanjaan Anda.
11. Keluar supermarket dan selesai.

Nah, contoh urutan langkah di atas itulah yang dinamakan algoritma untuk menyelesaikan sebuah permasalahan. Sama halnya jika diterapkan pada ilmu pemrograman. Ketika Anda sudah memikirkan bagaimana logika berjalannya suatu program, tulislah dalam bentuk algoritma atau kode yang berurutan untuk mewujudkannya.