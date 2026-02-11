#programming #webdev
Dalam dunia software development (pengembangan aplikasi), ada beberapa proses yang bisa diikuti untuk membuat suatu aplikasi. Dimulai dari perencanaan hingga ke pengelolaan, biasanya runtutan ini disebut dengan Software Development Life Cycle (SDLC).

![[Pasted image 20260209112531.png]]

1. Planning: Perencanaan
2. Analysis: Analisis
3. Design: Desain
4. Development: Pengembangan
5. Testing: Pengujian
6. Deployment : Penggelaran
7. Maintenance: Pemeliharaan

Setiap proses akan memberikan dampak setelahnya, Misalnya jika kita melakukan proses planning, analysis, dan design secara matang, maka proses implementasi dan testing akan bisa dieksekusi secara lebih baik dan juga lancar. Kebalikannya, jika proses implementasi dan testing tidak bisa dilakukan secara baik, maka proses maintenance (pemeliharaan) akan mengalami banyak masalah.

Dalam pengembangan aplikasi, untuk mengetahui kebutuhan pengguna secara utuh, biasanya dilakukan proses pembuatan dokumen User Requirements Specification (URS) atau User Requirement Document (URD). Dokumen ini bukan bersifat teknis, melainkan dibikin dengan format agar semua orang dapat membaca dan paham dengan gambaran besarnya.

User Requirement Specification diperlukan sebelum mengembangkan aplikasi. Lalu pertanyaannya,

1. Apa saja yang harus diperhatikan ketika membuat User Requirement Specification (URS)? 
2. Poin-poin penting apa saja yang tidak boleh terlewatkan ketika membuatnya?

URS dibuat supaya stakeholder (pemegang kepentingan) dapat memahami aplikasi yang ingin di buat dan mengurangi kesalahpahaman yang terkadang membuat proses pengembangan menjadi terhambat.

Dalam pembuatan URS tidak boleh menggunakan jargon teknis yang hanya dipahami oleh sekelompok orang saja. Misalnya, kita tidak boleh menggunakan istilah encryption (enkripsi) karena mungkin hanya pengembang aplikasi di bidang security (keamanan) saja yang mengetahui artinya.

Kemudian dalam pembuatan dokumen URS, penggunaan media seperti tabel atau diagram sangat disarankan karena dapat mempermudah penyampaian pesan asli terkait kebutuhan pengguna.

Lalu, bagaimana cara mendapatkan kebutuhan pengguna? Untuk menjawab pertanyaan tersebut, kita perlu melakukan requirement gathering. 

Requirement gathering adalah proses mendapatkan informasi dari para stakeholder (pemegang kepentingan), seperti manajer, developer, customer, dan user. Teknik yang dapat digunakan untuk requirement gathering, antara lain interview, user stories, straw man documents, dan prototyping.

### Interview
 Proses interview pada dasarnya merupakan proses tanya jawab, di mana kita menanyakan suatu pertanyaan, kemudian dijawab oleh peserta wawancara. Selain memberikan pertanyaan, kita juga perlu mencatat apa saja yang disampaikan oleh peserta wawancara.

### User Stories
User stories digunakan sebagai kriteria dalam menentukan product acceptance atau produk yang diinginkan. Selain itu, teknik ini juga dapat meningkatkan pemahaman tentang produk yang kita buat. Sebab, melalui user stories, Anda dapat menemukan berbagai kelebihan dan kekurangan dari suatu produk. Sehingga, Anda dapat mengetahui bagian manakah yang harus diperbaiki. 

User Stories dilakukan dengan menuliskan kebutuhan user sesuai dengan role dan keinginannya. Contoh format penulisan user stories adalah sebagai berikut: 
Sebagai seorang (deskripsi dari pengguna), Saya menginginkan (suatu fungsionalitas), sehingga mendapatkan (suatu kemampuan atau fitur tertentu).

### Staraw Man Documents
Teknik selanjutnya adalah Straw Man Documents. Teknik ini berguna untuk menyampaikan ide dari aplikasi tanpa menuliskan kode program apa pun. Teknik Straw Man Documents dapat dilakukan dengan berbagai macam media, misalnya storyboards, flowcharts, dan mock-up html.

### Prototyping
Teknik ini merupakan proses pembuatan prototipe program yang terbatas pada fungsionalitas utama saja. Dengan prototyping, kita bisa mendapatkan feedback yang lebih lengkap karena stakeholder sudah bisa mencoba langsung dan mendapatkan gambaran cara kerja aplikasi ketika sudah selesai nantinya. Namun, prototyping membutuhkan biaya ekstra karena mau tidak mau kita harus membuat programnya terlebih dahulu meskipun fungsionalitasnya terbatas. Selain itu, jika ada feedback dari stakeholder yang bertolak belakang, akan menyebabkan keluarnya biaya tambahan lagi untuk mengubahnya.

## Study Kasus
Supaya Anda lebih memahami tentang kebutuhan aplikasi dari sisi pengguna, mari kita coba menerapkannya berdasarkan studi kasus tertentu. Contoh studi kasus yang akan kita buat kali ini adalah User Requirement Specification terkait proses login dan logout.

Pasti Anda sudah sering mendengar proses login dan logout, bukan? Proses login dan logout sudah biasa digunakan dalam suatu aplikasi, sehingga banyak pengguna akan familier dengan proses tersebut. Walaupun sudah umum digunakan dalam suatu aplikasi, terkadang dalam proses implementasi login dan logout akan berbeda antara aplikasi satu dengan aplikasi lainnya. Oleh karena itu, kita perlu menentukan kebutuhan dari sisi pengguna terlebih dahulu.

Kali ini kita akan menggunakan teknik interview untuk mengumpulkan informasi terkait kebutuhan aplikasi yang ditujukan untuk end-user atau calon pengguna nantinya. Salah satu contoh pertanyaan yang dapat diajukan adalah sebagai berikut:

"Apa yang sebenarnya diharapkan pengguna ketika melakukan proses login atau logout?"

Setelah Anda menanyakan hal tersebut, bersiaplah untuk mencatat jawaban dari pengguna. Anggap saja Anda memperoleh beberapa jawaban seperti berikut:

Di halaman login seharusnya pengguna bisa melakukan proses login dengan memasukkan email dan password.
Ketika pengguna melakukan proses logout, ia akan secara otomatis pindah ke halaman login.
Oke, kita telah berhasil mendapat 2 user requirements.

