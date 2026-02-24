#programming 

Kita sudah mengetahui cara mengubah posisi dari sebuah elemen dengan menggunakan margin. Namun, ketika melakukannya akan berpengaruh terhadap posisi elemen lain di sekitarnya. Lantas bagaimana jika kita ingin memindahkan tanpa mengganggu posisi elemen lainnya? Solusinya kita perlu mengubah _positioning schema_ dengan menggunakan properti **position** dalam mengontrol letak elemen tersebut. Berikut adalah nilai dari properti **position** yang ada pada CSS.

- **Normal Flow/Static Flow**  
    Ia adalah _default behaviour_ yang dimiliki elemen, yakni setiap elemen block akan ditampilkan dalam baris baru ketika dibuat. Jadi, setiap elemen block selalu muncul di bawah dari elemen block sebelumnya. Bahkan, jika masih terdapat ruang kosong pada samping elemennya, mereka tidak akan tampak bersebelahan.
- **Relative Positioning**  
    Membuat elemen dapat melakukan perpindahan posisi ke atas, kanan, bawah, ataupun kiri dari posisi semula atau posisi seharusnya elemen tersebut berada. Perpindahan posisi ini tidak akan berpengaruh terhadap posisi elemen di sekitarnya karena ketika menggunakan relative positioning elemen tersebut akan dipindahkan dari _normal flow_.
- **Absolute Positioning**  
    Sama seperti relative, elemen akan dipindahkan keluar dari normal flow sehingga kita dapat memindahkan posisi elemen ke atas, kanan, bawah, ataupun kiri secara leluasa tanpa mengganggu elemen di sekitarnya. Namun, posisinya relatif terhadap jendela browser dan posisinya dapat relatif pada induk elemen selama induk elemen juga berada di luar dari normal flow.
- **Fixed Positioning**  
    Ia merupakan absolute position. Namun, posisinya selalu relatif pada jendela browser, bahkan ketika pengguna melakukan scrolling posisinya akan tetap tampak pada posisinya di layar.

Sebelum kita membahas satu per satu skema tersebut, mungkin kita perlu memahami lebih detail lagi pengertian sebenarnya _normal flow_ atau biasa disebut dengan _static flow_ itu, dan alasan untuk memindahkan posisi elemen kita perlu mengeluarkannya dari _static flow_.

