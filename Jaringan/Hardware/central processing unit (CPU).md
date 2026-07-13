#jaringan
Apa itu Central Processing Unit (CPU) atau dalam bahasa indonesianya unit pemrosesan pusat? 
CPU adalah komponen fungsional utama dari sebuah komputer. 
CPU merupakan kumpulan sirkuit elektronik yang menjalankan sistem operasi dan aplikasi komputer serta mengelola berbagai operasi komputer lainnya.

Pada dasarnya, CPU adalah otak aktif dari komputer. CPU adalah pengelola tak terlihat di dalam komputer tempat data masukan (Input) diubah menjadi informasi keluaran (Output). Ia menyimpan dan mengeksekusi instruksi program melalui jaringan sirkuitnya yang luas.

Seperti otak manusia, CPU dapat melakukan banyak tugas sekaligus. Ini berarti CPU juga merupakan bagian komputer yang secara simultan mengatur fungsi: 
1. internal komputer, 
2. mengawasi konsumsi daya, 
3. mengalokasikan sumber daya komputasi, 
4. dan berinteraksi dengan berbagai aplikasi, program, dan jaringan.

Jika Anda masih ragu tentang betapa pentingnya CPU bagi komputasi, pertimbangkan ini: CPU adalah satu-satunya komponen yang terdapat di _setiap_ komputer, terlepas dari ukuran atau penggunaan komputer tersebut. Jika Anda membaca ini di Smartphone, laptop, atau PC, Anda sedang menggunakan CPU saat ini juga.

Meskipun istilah "CPU" terdengar seperti kita sedang berbicara tentang satu perangkat tunggal, sebenarnya bukan demikian. CPU sebenarnya adalah kumpulan berbagai komponen komputer yang bekerja bersama-sama dengan cara yang sangat terkoordinasi.

## Konsep panduan: Penyimpanan data dan memori
Sebelum membahas bagian-bagian unik dari CPU dan bagaimana mereka berinteraksi, penting untuk terlebih dahulu memahami dua konsep penting yang mendorong komputasi: penyimpanan data dan memori.

- **Penyimpanan Data atau Data Storage** merujuk pada tindakan menyimpan informasi sehingga dapat diakses dengan mudah di kemudian hari atau bahkan disimpan selamanya. Komputer bergantung pada dua jenis penyimpanan, yang diklasifikasikan sebagai penyimpanan primer atau penyimpanan sekunder. Penyimpanan primer (yang juga dikenal sebagai memori utama, atau hanya "yang utama") berisi instruksi pengoperasian atau pengambilan data. CPU secara rutin menggunakan penyimpanan primer untuk mengakses data tersebut.

- **Memori** adalah tempat penyimpanan sementara di dalam komputer yang digunakan untuk menyimpan data dan instruksi yang sedang dibutuhkan oleh sistem. Data yang tersimpan di memori dapat diakses dengan cepat oleh prosesor agar program dan sistem operasi dapat berjalan. 
Memori biasanya digunakan sebagai penyimpanan jangka pendek untuk data yang sedang aktif atau sering digunakan. Ketika sebuah data dibuka atau diproses oleh sistem operasi, data tersebut akan dimuat ke dalam **Random Access Memory (RAM)** agar dapat diakses lebih cepat dibandingkan jika langsung dibaca dari media penyimpanan seperti hard disk atau SSD.

Sekali lagi, CPU menyerupai otak manusia karena keduanya memiliki memori jangka pendek dan memori jangka panjang. Memori operasi standar CPU hanya menyimpan data RAM "pada saat itu", mirip dengan memori jangka pendek seseorang, sebelum secara berkala menghapusnya dari memori cache komputer.

Penyimpanan sekunder mirip dengan memori jangka panjang pada manusia dan melibatkan penyimpanan data secara permanen atau jangka panjang dengan mengarsipkannya pada perangkat penyimpanan sekunder, seperti hard drive. Perangkat output seperti hard drive menawarkan penyimpanan permanen. Penyimpanan permanen melibatkan memori baca saja (ROM), yang berarti data dapat diakses tetapi tidak dapat diolah atau diubah.

## Apa saja komponen yang terdapat dalam CPU?
Berikut ini adalah tiga komponen utama dalam sebuah CPU:
1. Unit kontrol
**Control Unit (CU)** atau **Unit Kontrol** adalah salah satu bagian utama dari CPU yang bertugas mengarahkan seluruh proses kerja komputer. Unit ini mengirimkan sinyal-sinyal listrik ke berbagai komponen agar setiap komponen mengetahui kapan dan bagaimana suatu instruksi harus dijalankan.

Meskipun disebut _Control Unit_, komponen ini tidak secara langsung mengendalikan aplikasi atau program yang sedang digunakan. Sebaliknya, Unit Kontrol bertugas mengatur jalannya instruksi di dalam CPU, seperti seorang manajer yang membagi tugas kepada para pekerja. Ia mengambil instruksi dari memori, menerjemahkannya menjadi sinyal kontrol, lalu mengoordinasikan komponen lain, seperti **Arithmetic Logic Unit (ALU)**, register, dan memori, agar bekerja sesuai urutan yang benar.

2. Unit aritmatika/logika
**Arithmetic Logic Unit (ALU)** atau **Unit Aritmatika dan Logika** adalah komponen utama di dalam CPU yang bertugas melakukan seluruh operasi perhitungan dan pengambilan keputusan logis.

Dalam operasi aritmatika, ALU menjalankan perhitungan dasar seperti **penjumlahan, pengurangan, perkalian, dan pembagian**. Hampir semua proses komputasi, mulai dari kalkulator hingga permainan dan aplikasi lainnya, bergantung pada kemampuan ALU untuk melakukan operasi-operasi tersebut.

Selain perhitungan matematika, ALU juga melakukan **operasi logika**, yaitu membandingkan dua nilai untuk menghasilkan keputusan. Contohnya, ALU dapat memeriksa apakah dua angka memiliki nilai yang sama, apakah suatu angka lebih besar atau lebih kecil dari angka lainnya, atau apakah suatu kondisi bernilai benar (_true_) atau salah (_false_). Hasil dari operasi logika inilah yang memungkinkan komputer mengambil keputusan, seperti menjalankan percabangan (_if-else_), perulangan (_loop_), atau memvalidasi data yang dimasukkan pengguna.

3. Unit memori
**Memory Unit (MU)** atau **Unit Memori** adalah bagian dari CPU yang bertugas mengelola pertukaran data antara prosesor dan memori utama (RAM). Komponen ini memastikan data dan instruksi yang dibutuhkan CPU dapat diambil, disimpan, dan dipindahkan dengan cepat selama proses komputasi berlangsung.

Salah satu tugas penting Unit Memori adalah mengatur aliran data antara **RAM**, **cache**, dan **CPU**. Dengan adanya pengelolaan ini, prosesor dapat memperoleh data yang diperlukan secara lebih efisien tanpa harus terus-menerus mengakses media penyimpanan yang lebih lambat. Unit Memori juga membantu mengelola penggunaan **cache memory**, yaitu memori berkecepatan tinggi yang menyimpan data atau instruksi yang sering digunakan agar proses eksekusi menjadi lebih cepat.

Selain itu, Unit Memori bertanggung jawab menjaga **perlindungan memori (memory protection)**. Mekanisme ini mencegah suatu program mengakses area memori yang bukan menjadi haknya, sehingga sistem menjadi lebih stabil, aman, dan terhindar dari kerusakan data akibat kesalahan program atau akses yang tidak sah.

### Komponen Penting Lainnya pada CPU
#### 1. Cache Memory
**Cache** adalah memori berkecepatan sangat tinggi yang berada di dalam atau sangat dekat dengan inti prosesor. Fungsinya adalah menyimpan data dan instruksi yang paling sering digunakan agar CPU dapat mengaksesnya jauh lebih cepat dibandingkan harus mengambil data langsung dari RAM.

Meskipun CPU tetap dapat mengakses RAM, pada praktiknya prosesor akan **memeriksa cache terlebih dahulu**. Jika data yang dibutuhkan tersedia di cache (_cache hit_), CPU dapat langsung menggunakannya tanpa harus menunggu akses ke RAM yang lebih lambat. Oleh karena itu, cache berperan penting dalam meningkatkan performa komputer secara keseluruhan.

#### 2. Register
**Register** adalah tempat penyimpanan data tercepat yang dimiliki CPU. Register digunakan untuk menyimpan data, alamat memori, maupun hasil perhitungan yang sedang diproses sehingga dapat diakses hanya dalam hitungan siklus clock.

Berbeda dengan media penyimpanan seperti SSD atau hard disk, register **bukan memori permanen**. Isinya akan berubah setiap saat sesuai instruksi yang sedang dijalankan dan akan hilang ketika komputer dimatikan.

#### 3. Clock (Jam CPU)
Agar seluruh bagian CPU dapat bekerja secara teratur, prosesor menggunakan **clock** atau jam internal. Clock menghasilkan sinyal listrik secara berkala yang berfungsi sebagai penanda kapan setiap instruksi harus dijalankan.

Kecepatan clock disebut **clock speed**, yang menunjukkan berapa banyak siklus kerja yang dapat dilakukan CPU setiap detik. Satuan yang digunakan adalah **Hertz (Hz)**, meskipun pada prosesor modern umumnya dinyatakan dalam **Gigahertz (GHz)**. Sebagai contoh, prosesor dengan kecepatan **3,5 GHz** mampu melakukan sekitar **3,5 miliar siklus clock setiap detik**.

#### 4. Instruction Register (IR) dan Program Counter (PC)
Saat CPU menjalankan sebuah program, setiap instruksi dieksekusi secara berurutan.

- **Program Counter (PC)** menyimpan alamat instruksi berikutnya yang akan diambil dari memori.
    
- Setelah instruksi tersebut diambil, instruksi akan disimpan sementara di **Instruction Register (IR)** untuk kemudian diterjemahkan dan dieksekusi oleh CPU.
    

Setelah satu instruksi selesai dijalankan, Program Counter akan diperbarui agar menunjuk ke instruksi berikutnya.

#### 5. Bus
**Bus** adalah jalur komunikasi yang menghubungkan CPU dengan komponen lain di dalam komputer, seperti RAM, penyimpanan, dan perangkat input/output. Melalui bus inilah data, alamat memori, dan sinyal kontrol dapat berpindah dari satu komponen ke komponen lainnya.

Lebar bus (_bus width_) menunjukkan jumlah bit yang dapat dikirim secara bersamaan dalam satu kali transfer. Misalnya, **bus 64-bit** mampu mentransfer 64 bit data sekaligus, sehingga umumnya memiliki bandwidth yang lebih tinggi dibandingkan bus 32-bit.


## Bagaimana cara kerja CPU?
Fungsi CPU ditangani oleh unit kontrol, dengan bantuan sinkronisasi yang disediakan oleh jam komputer (Clock). Kerja CPU terjadi sesuai dengan siklus yang telah ditetapkan, yang dikenal sebagai siklus instruksi CPU, yang membutuhkan sejumlah pengulangan instruksi komputasi dasar berikut, sesuai dengan kemampuan pemrosesan komputer tersebut:

- **Fetch:** Proses pengambilan data terjadi setiap kali data diambil dari memori.  
    
- **Dekode:** Dekoder di dalam CPU menerjemahkan instruksi biner menjadi sinyal listrik yang mengaktifkan bagian lain dari CPU.  
    
- **Eksekusi:** Eksekusi terjadi ketika komputer menafsirkan dan menjalankan serangkaian instruksi dari sebuah program komputer.

Kalo lebih jelasnya: Mengambil data -> Mendecode data tersebut -> dan menjalankannya.

Perlu disebutkan bahwa dengan sedikit modifikasi dasar, jam komputer di dalam CPU dapat dimanipulasi agar waktu berjalan lebih cepat dari biasanya. Beberapa pengguna melakukan ini untuk menjalankan komputer mereka dengan kecepatan lebih tinggi. Namun, praktik ini tidak disarankan karena dapat menyebabkan komponen komputer aus lebih cepat dari biasanya dan dapat melanggar garansi pabrikan CPU.