#programming #webdev
Sebelumnya sdh mempelajari User Requirement Specification atau URS yang berguna untuk mengetahui kebutuhan pengguna sebelum membuat aplikasi, nah kali ini saya akan membahas mengenai Spesifikasi teknis dari pembuatan aplikasi, yakni dokumen yang menyimpan informasi detail mengenai fungsionalitas dari sistem/aplikasi, servis, dan juga limitasi-limitasinya.

dokumen Spesifikasi Teknis akan banyak jargon-jargon yang digunakan. Ini karena kebutuhannya sudah mengarah ke sistemnya.

Berikut ini adalah contoh spesifikasi teknis aplikasi untuk halaman checkout dari proses pembelian suatu barang:

> “Jika melakukan pembelian di atas 50 ribu rupiah maka otomatis tambahkan kupon diskon yang saat itu statusnya tersedia pada sistem, jika tidak ada kupon yang statusnya tersedia maka tampilkan tulisan tidak ada diskon yang tersedia”. 

Dari spesifikasi tersebut, bisa dilihat bahwa apa yang seharusnya sistem bisa lakukan cukuplah jelas dan detail. Dengan bahasa yang jelas dan detail akan membantu pengembang software dalam proses membuat aplikasinya.

### Cara Menentukan Spesifikasi Teknis Aplikasi
ada beberapa prinsip pada spesifikasi teknis yang bisa kita terapkan:
- Clear (jelas)
- Unambiguous (tidak ambigu)
- Mudah dipahami
- Complete (lengkap)
- Consistent (konsisten)
ketika spesifikasinya jelas dan tidak ambigu maka seorang developer dapat mengimplementasinya dengan benar. Selain itu, juga berguna bagi client di mana ekspektasi client dengan aplikasi jadi bisa selaras.


Dari berbagai macam stakeholder memang memiliki kebutuhannya masing-masing, oleh karena itu kita perlu tahu kebutuhan berdasarkan sisi pandangnya:
- **Developer**  
    Dari sisi developer tentunya yang diperlukan ada kedetailan dan kejelasan spesifikasi. Karena merekalah yang akan mengimplementasinya ke dalam aplikasi.
- **Client/User**  
    Dari sisi client meskipun spesifikasi teknis lebih mengarah ke teknis akan tetapi mereka berharap tetap bisa dimengerti. Dalam artian istilah teknis yang dipakai harus bisa dibuat semudah mungkin untuk dimengerti.
- **Legal**  
    Karena spesifikasi teknis ini bisa menjadi kontrak, maka perlu memasukkan acceptance criteria dengan jelas juga. Acceptance criteria adalah klausul kriteria yang berisi apakah suatu fitur sudah berjalan dengan baik. Jika aplikasi yang dibuat lulus semua acceptance criteria maka seharusnya tidak ada masalah dari sisi kontrak/legal.

Contingency plan adalah suatu tindakan alternatif yang dipersiapkan ketika tindakan utama yang direncanakan untuk melakukan sesuatu gagal atau terhambat oleh berbagai faktor.
Misalkan ada kebutuhan untuk menyelesaikan suatu proses dalam aplikasi, dan kita memiliki 2 solusi yang bisa digunakan, pertama adalah menggunakan layanan third party (pihak ketiga) yang memiliki fitur lengkap, kedua adalah membuat layanan sendiri meskipun adanya limitasi tapi kita punya kuasa penuh terhadapnya. 

Dalam proses implementasi kita sudah sepakat untuk memilih penggunaan third party. Akan tetapi di tengah jalan, layanan third party tersebut mengalami masalah terkait legal yang berujung pada ditutupnya layanan tersebut. Ini tentunya berdampak pada proses pengembangan aplikasi kita. Nah, ketika terjadi problem seperti ini, maka solusi kedua yang kita rencanakan di awal justru malah bisa menjadi pilihan yang cocok. 

Pada praktiknya, tentu berpindah di tengah jalan akan berdampak buruk jika kita tidak berhati-hati. Tapi yang terpenting adalah bagaimana proses pengembangan tetap terus berjalan dan tidak stuck (terhenti) atau terpaku pada suatu hal yang belum jelas kapan stabilnya.