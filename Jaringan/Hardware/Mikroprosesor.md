#jaringan 
UNIVAC merupakan salah satu terobosan besar dalam sejarah komputer. Namun, komputer tersebut masih memiliki ukuran yang sangat besar dan membutuhkan banyak komponen elektronik untuk menjalankan berbagai fungsi.

Seiring berkembangnya teknologi transistor dan **Integrated Circuit (IC)**, berbagai komponen elektronik mulai dapat ditempatkan dalam chip yang jauh lebih kecil. Motherboard kemudian menggunakan berbagai chip khusus untuk menangani fungsi tertentu dalam sistem komputer.

Perkembangan teknologi semikonduktor memungkinkan semakin banyak transistor dan rangkaian elektronik ditempatkan dalam satu chip. Pada akhirnya, komponen utama CPU dapat digabungkan ke dalam sebuah Integrated Circuit berukuran kecil yang disebut **microprocessor atau mikroprosesor**.

**Mikroprosesor** adalah sebuah chip yang berisi unit pemrosesan utama komputer. Di dalamnya terdapat berbagai komponen CPU, seperti Control Unit, Arithmetic Logic Unit (ALU), register, dan cache.

CPU modern bahkan dapat memiliki beberapa **core atau inti pemrosesan** di dalam satu mikroprosesor.

### CPU Core

**Core** adalah unit pemrosesan yang mampu menjalankan instruksi. Setiap core memiliki komponen pemrosesan yang memungkinkannya melakukan proses **fetch, decode, dan execute** terhadap instruksi.

Karena itu, core sering digambarkan sebagai **"prosesor kecil di dalam sebuah prosesor."**

Sebagai contoh, sebuah CPU dengan 4 core memiliki empat unit pemrosesan yang dapat menangani pekerjaan secara bersamaan.

Seluruh core tersebut berada dalam satu paket prosesor dan biasanya menggunakan satu soket CPU pada motherboard. Beberapa sumber daya, seperti cache tertentu dan jalur komunikasi dengan memori, dapat digunakan bersama oleh beberapa core.

### Mikroprosesor dan Mikrokontroler

Istilah **microprocessor** tidak boleh disamakan dengan **microcontroller atau mikrokontroler**.

Mikroprosesor pada dasarnya berfokus pada fungsi pemrosesan. Untuk membentuk sebuah sistem komputer lengkap, mikroprosesor biasanya bekerja bersama komponen eksternal seperti RAM, media penyimpanan, dan perangkat Input/Output.

Sementara itu, **mikrokontroler adalah sebuah komputer kecil yang terintegrasi dalam satu chip**. Di dalam sebuah mikrokontroler biasanya sudah terdapat:

- CPU
- Memori, seperti RAM dan Flash Memory
- Perangkat Input/Output (I/O) yang dapat diprogram
- Timer dan komponen pendukung lainnya

Mikrokontroler banyak digunakan pada perangkat yang menjalankan fungsi tertentu, seperti mesin cuci, sistem kontrol kendaraan, perangkat IoT, robot, dan berbagai perangkat elektronik lainnya.

### Jenis Prosesor Berdasarkan Jumlah Core

#### 1. Single-Core Processor

**Single-core processor** memiliki satu inti pemrosesan fisik. CPU jenis ini hanya memiliki satu core untuk menjalankan instruksi program.

Satu core tetap dapat menjalankan banyak program melalui mekanisme **multitasking** yang dikelola oleh sistem operasi. Sistem operasi membagi waktu penggunaan CPU kepada berbagai proses dengan sangat cepat sehingga beberapa program terlihat berjalan secara bersamaan.

Namun, pada tingkat pemrosesan fisik, hanya terdapat satu core yang menangani pekerjaan tersebut.

#### 2. Dual-Core Processor

**Dual-core processor** memiliki dua inti pemrosesan dalam satu prosesor.

Kedua core dapat menjalankan pekerjaan secara bersamaan. Sebagai contoh, satu core dapat memproses sebuah aplikasi sementara core lainnya menangani proses sistem operasi.

Dual-core dapat meningkatkan performa dibandingkan single-core, terutama pada aplikasi yang dirancang untuk menggunakan beberapa core.

Namun, penggunaan dua core **tidak selalu membuat komputer dua kali lebih cepat**. Peningkatan performa bergantung pada kemampuan software dalam membagi pekerjaan ke beberapa core.

#### 3. Quad-Core Processor

**Quad-core processor** memiliki empat inti pemrosesan dalam satu prosesor.

Keempat core dapat menangani beberapa tugas secara paralel. Hal ini sangat berguna untuk pekerjaan yang membutuhkan banyak proses, seperti rendering video, kompilasi program, menjalankan virtual machine, dan beberapa jenis permainan.

Namun, quad-core **tidak otomatis menghasilkan performa empat kali lebih cepat dibandingkan single-core**. Performa tetap dipengaruhi oleh arsitektur CPU, clock speed, cache, RAM, dan kemampuan software dalam memanfaatkan banyak core.

#### 4. Multi-Core Processor

**Multi-core processor** adalah prosesor yang memiliki dua atau lebih core dalam satu chip atau paket prosesor.

Contohnya meliputi:

**2 core → Dual-Core**

**4 core → Quad-Core**

**6 core → Hexa-Core**

**8 core → Octa-Core**

**12, 16, 24 core atau lebih → Multi-Core Processor**

Penggunaan banyak core memungkinkan CPU membagi pekerjaan ke beberapa unit pemrosesan. Dengan cara ini, komputer dapat menjalankan banyak tugas secara bersamaan dan menyelesaikan pekerjaan yang mendukung pemrosesan paralel dengan lebih efisien.

Selain meningkatkan performa, desain multi-core juga membantu meningkatkan efisiensi energi. Daripada terus meningkatkan clock speed satu core yang dapat menghasilkan panas dan konsumsi daya sangat tinggi, produsen CPU dapat menggunakan beberapa core untuk membagi beban pemrosesan.