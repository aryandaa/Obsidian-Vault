#programming 

Setelah memahami apa itu program dan siapa yang disebut programmer, sekarang kita masuk ke bagian yang sedikit lebih dekat dengan "mesin"-nya. Kita tidak perlu langsung menyelam ke transistor, instruction set, atau arsitektur CPU sampai kepala berasap. Tujuan materi ini adalah membangun gambaran mental tentang **apa yang terjadi ketika sebuah program dijalankan oleh komputer**.

Ini penting karena programmer sebenarnya sedang menulis instruksi untuk sebuah mesin. Kalau kita tidak tahu sama sekali bagaimana mesin tersebut bekerja, kita hanya akan mengenal programming dari permukaannya saja. Nanti ketika belajar memory, performance, database, networking, concurrency, cybersecurity, dan debugging, pemahaman ini akan mulai terasa manfaatnya.

---
## Komputer sebenarnya melakukan apa?

Pada tingkat paling dasar, komputer melakukan sesuatu yang sangat sederhana: **menerima data, memproses data berdasarkan instruksi, kemudian menghasilkan hasil**.

Secara umum:
```text
Input
  ↓
Process
  ↓
Output
```

Misalnya kamu menjalankan kalkulator dan memasukkan:
```text
10 + 20
```

Komputer menerima angka `10`, operator `+`, dan angka `20` sebagai input.

Kemudian komputer menjalankan instruksi untuk melakukan operasi penjumlahan.

Hasilnya:
```text
30
```

Secara sederhana:
```text
10 + 20
   ↓
Processor
   ↓
  30
```

Walaupun komputer modern jauh lebih kompleks daripada contoh tersebut, konsep dasarnya tetap seperti ini.

---
# Komputer Tidak "Mengerti" Program Seperti Manusia

Ketika kamu menulis:
```javascript
const total = price * quantity;
```

kita sebagai manusia dapat memahami maksudnya.

Kita tahu:
> ambil `price`, kalikan dengan `quantity`, lalu simpan hasilnya ke `total`.

Komputer tidak membaca kode tersebut dengan cara yang sama seperti manusia membaca kalimat.

Komputer pada akhirnya membutuhkan **instruksi tingkat mesin** yang dapat diproses oleh hardware.

Inilah alasan mengapa terdapat beberapa lapisan antara kode yang kita tulis dengan hardware komputer.

Secara sederhana:
```text
Kode yang ditulis programmer
        ↓
Bahasa Pemrograman
        ↓
Compiler / Interpreter / Runtime
        ↓
Machine Code
        ↓
CPU
        ↓
Hardware
```

Jadi ketika kamu menulis:
```php
$total = $price * $quantity;
```

tidak berarti CPU secara langsung memahami tulisan `$total`.

Ada proses yang menerjemahkan atau mengeksekusi kode tersebut sampai akhirnya CPU mendapatkan instruksi yang sesuai dengan arsitektur mesin.

---
# Hardware dan Software

Untuk memahami komputer, kita harus membedakan dua hal besar: **hardware** dan **software**

Hardware adalah bagian fisik komputer.

Contohnya:
```text
CPU
RAM
SSD
GPU
Keyboard
Mouse
Monitor
Network Card
Motherboard
```

Software adalah instruksi dan perangkat lunak yang berjalan menggunakan hardware tersebut.

Contohnya:
```text
Operating System
Browser
VS Code
PHP
Python
JavaScript Runtime
Database
Game
Application
```

Hubungannya sederhana.
```text
Software
   ↓
memberikan instruksi
   ↓
Hardware
   ↓
melakukan pekerjaan
```

Misalnya kamu menjalankan browser, Browser adalah software lalu Browser meminta komputer melakukan berbagai pekerjaan seperti:
```text
Ambil data dari internet
Decode data
Render halaman
Menampilkan gambar
Memproses JavaScript
```

Hardware kemudian melakukan pekerjaan tersebut menggunakan CPU, RAM, GPU, network interface, storage, dan komponen lainnya.

---
# CPU: Bagian yang Menjalankan Instruksi

CPU atau **Central Processing Unit** adalah salah satu komponen paling penting dalam komputer karena bertugas menjalankan instruksi program.

Kalau kita menyederhanakannya secara ekstrem, CPU dapat dianggap sebagai bagian yang melakukan:
```text
Ambil instruksi
↓
Pahami instruksi
↓
Jalankan instruksi
↓
Lanjut ke instruksi berikutnya
```

Proses ini sering dijelaskan dengan istilah:
```text
Fetch
Decode
Execute
```

CPU mengambil instruksi dari memory, melakukan decoding terhadap instruksi tersebut, kemudian menjalankannya.

Misalnya program membutuhkan operasi:
```text
5 + 10
```

CPU akan mendapatkan instruksi yang sesuai untuk melakukan operasi tersebut.

Sekali lagi, jangan membayangkan CPU membaca:
```text
"tolong tambahkan 5 dan 10"
```

CPU bekerja menggunakan instruksi mesin yang sangat jauh lebih rendah levelnya.

Untuk sekarang cukup pahami:
> **CPU adalah komponen yang mengeksekusi instruksi.**

---

# RAM: Tempat Data yang Sedang Digunakan

Sekarang kita masuk ke RAM.

RAM atau **Random Access Memory** adalah memory yang digunakan untuk menyimpan data dan program yang sedang aktif digunakan komputer.

Misalnya kamu membuka browser.

Program browser perlu berada di memory agar CPU dapat mengakses data dan instruksinya dengan cepat.

Secara sederhana:
```text
SSD
 ↓
Program disimpan
 ↓
Program dijalankan
 ↓
RAM
 ↓
CPU mengakses data/instruksi
```

Misalnya kamu membuka aplikasi:
```text
VS Code
```

File aplikasi awalnya tersimpan di storage seperti SSD.

Ketika dijalankan, sistem operasi memuat bagian yang diperlukan ke RAM.

Kemudian CPU dapat bekerja dengan data dan instruksi tersebut.

Itulah sebabnya RAM sangat penting dalam performa komputer.

Kalau RAM terlalu terbatas dan komputer menjalankan terlalu banyak program, sistem dapat mengalami tekanan memory dan menggunakan storage sebagai bagian dari mekanisme virtual memory, yang umumnya jauh lebih lambat dibanding akses RAM.

---
# Storage: Tempat Menyimpan Data

Kalau RAM digunakan untuk data yang sedang aktif digunakan, storage seperti SSD atau HDD digunakan untuk menyimpan data secara lebih permanen.

Misalnya:
```text
project/
├── index.php
├── config.php
└── database.sql
```

File-file tersebut berada di storage jadi Ketika komputer dimatikan, file tersebut tetap ada.

Berbeda dengan RAM yang bersifat volatile. Ketika daya hilang, isi RAM tidak dipertahankan seperti data pada storage.

Secara sederhana:
```text
Storage
    ↓
Menyimpan data secara permanen

RAM
    ↓
Menyimpan data yang sedang digunakan

CPU
    ↓
Menjalankan instruksi
```

Ketiganya bekerja bersama.

---
# Hubungan CPU, RAM, dan Storage

Kita bisa membayangkan seperti ini.

Storage adalah tempat menyimpan barang.
RAM adalah meja kerja.
CPU adalah orang yang melakukan pekerjaan.

Misalnya kamu mempunyai file:
```text
program.js
```
File tersebut berada di storage.

Ketika program dijalankan:
```text
Storage
   ↓
Program dimuat
   ↓
RAM
   ↓
CPU mengambil instruksi/data
   ↓
Program dijalankan
```

Analogi ini tentu tidak sempurna, tetapi cukup bagus untuk membangun mental model, Kalau meja kerja terlalu kecil, kamu sulit mengerjakan banyak barang sekaligus, Kalau orang yang bekerja lebih cepat, pekerjaan dapat dilakukan lebih cepat, Kalau lemari penyimpanan lambat, mengambil barang membutuhkan waktu lebih lama. Begitu juga komputer.

---
# Lalu Apa Peran Operating System?

Sekarang kita masuk ke komponen yang sangat penting bagi programmer: **Operating System atau OS**.

Contohnya:
```text
Windows
Linux
macOS
Android
iOS
```

Operating system bertindak sebagai lapisan yang mengatur penggunaan hardware dan menyediakan berbagai layanan yang digunakan aplikasi.

Misalnya sebuah program ingin membaca file.

Program tidak perlu mengendalikan SSD secara langsung dengan mengatur sinyal listrik ke hardware.

Program cukup meminta operating system:
```text
"Berikan saya isi file ini."
```

OS kemudian menangani detail yang lebih rendah.

Secara sederhana:
```text
Application
     ↓
Operating System
     ↓
Hardware
```

Misalnya:
```text
PHP Application
     ↓
Operating System
     ↓
File System
     ↓
SSD
```

Begitu juga dengan networking:
```text
Application
     ↓
Operating System
     ↓
Network Stack
     ↓
Network Interface
     ↓
Internet
```

Ini disebut **abstraction**.

Programmer tidak harus berurusan langsung dengan seluruh detail hardware setiap kali ingin melakukan sesuatu.

---
# Apa yang Terjadi Saat Program Dijalankan?

Sekarang kita gabungkan semuanya.

Misalnya kita mempunyai program sederhana:

```javascript
const a = 10;
const b = 20;

const result = a + b;

console.log(result);
```

Ketika program dijalankan, secara konseptual terjadi sesuatu seperti ini.

Pertama, source code berada di storage.
```text
SSD
 ↓
program.js
```

Kemudian JavaScript runtime seperti Node.js memproses program tersebut.

Runtime memerlukan memory.
```text
program.js
   ↓
Runtime
   ↓
RAM
```

Kemudian instruksi yang diperlukan dieksekusi oleh CPU.
```text
RAM
 ↓
CPU
 ↓
Execute instructions
```

Program menghasilkan nilai:
```text
30
```

Kemudian `console.log()` menyebabkan hasil tersebut dikirim ke output yang sesuai, misalnya terminal.

```text
CPU
 ↓
Runtime
 ↓
Terminal
 ↓
30
```

Kita sengaja menyederhanakan prosesnya karena implementasi sebenarnya jauh lebih kompleks. Tetapi model ini cukup untuk memahami hubungan antara source code dan hardware.

---
# Apa Itu Machine Code?

Sekarang kita turun satu tingkat lagi, CPU tidak menjalankan:
```javascript
const result = a + b;
```

CPU menjalankan instruksi yang sesuai dengan **instruction set architecture**, atau ISA.

Contoh arsitektur CPU yang terkenal:
```text
x86-64
ARM64
RISC-V
```

Setiap arsitektur memiliki kumpulan instruksi yang dapat dimengerti CPU tersebut, Machine code adalah representasi instruksi yang dapat dieksekusi oleh CPU.

Kita tidak perlu menulis machine code secara manual untuk membuat aplikasi modern.

Bahasa pemrograman, compiler, interpreter, runtime, dan berbagai layer lainnya menangani proses tersebut.

Gambaran sederhananya:
```text
High-Level Language
       ↓
Compiler / Runtime
       ↓
Lower-Level Representation
       ↓
Machine Instructions
       ↓
CPU
```

Semakin tinggi level bahasa, semakin dekat syntax-nya dengan cara manusia berpikir.
Semakin rendah levelnya, semakin dekat dengan hardware.

---
# High-Level dan Low-Level

Bahasa seperti Python, JavaScript, PHP, Java, dan C# biasanya dianggap lebih **high-level** dibanding assembly atau machine code.

Misalnya:
```python
result = a + b
```

Sangat mudah dibaca manusia.

Sedangkan pada level yang jauh lebih rendah, instruksi CPU bisa direpresentasikan dalam bentuk assembly yang jauh lebih dekat dengan operasi mesin.

Contohnya secara ilustratif:
```asm
ADD RAX, RBX
```

Kita tidak perlu mempelajari assembly sekarang.

Yang perlu dipahami adalah konsep **abstraction level**:
```text
High Level
│
├── Python
├── JavaScript
├── PHP
├── Java
│
├── C / C++
│
├── Assembly
│
└── Machine Code
       ↓
     CPU
Low Level
```

Ini bukan ranking bahwa bahasa high-level lebih bagus daripada low-level tetapi menunjukan bahwa masing-masing memiliki tujuan dan trade-off yang berbeda.

---
# Bagaimana CPU Menjalankan Program?

Sekarang kita kembali ke siklus CPU.

Secara sederhana:
```text
Fetch
  ↓
Decode
  ↓
Execute
  ↓
Fetch
  ↓
Decode
  ↓
Execute
  ↓
...
```

**Fetch** berarti CPU mengambil instruksi dari memory.

**Decode** berarti CPU menentukan apa arti instruksi tersebut.

**Execute** berarti CPU melakukan operasi yang diminta.

Misalnya ada instruksi yang secara konseptual berarti:
```text
Tambahkan nilai A dan B.
```

CPU melakukan operasi tersebut.

Kemudian mengambil instruksi berikutnya.

Program modern tentu tidak sesederhana ini karena CPU memiliki cache, pipeline, branch prediction, out-of-order execution, multiple cores, dan berbagai optimisasi lain.

Tetapi untuk fundamental, model:
```text
Fetch → Decode → Execute
```

sudah merupakan fondasi yang bagus.

---
# Apa Itu Process?

Ketika kamu menjalankan sebuah program, program tersebut dapat menjadi **process** yang sedang berjalan di sistem operasi.

Misalnya kamu membuka:
```text
VS Code
```

OS membuat dan mengelola process untuk aplikasi tersebut.

Process memiliki resource seperti:
```text
Memory
CPU time
File handles
Network resources
```

Misalnya kamu membuka browser dan terminal.

Bisa saja terdapat beberapa process yang berjalan secara bersamaan.
```text
Operating System
│
├── Browser Process
├── Terminal Process
├── VS Code Process
└── Other Processes
```

OS bertugas mengatur bagaimana process-process tersebut mendapatkan resource dari komputer.

---
# Process dan Program Bukan Hal yang Sama

Ini perbedaan yang bagus untuk mulai dikenali.

**Program** adalah sekumpulan instruksi yang tersimpan.

**Process** adalah program yang sedang dijalankan beserta state dan resource yang terkait dengan eksekusinya.

Analogi sederhananya:
```text
Program
=
Resep masakan

Process
=
Resep yang sedang benar-benar digunakan untuk memasak
```

Satu program bahkan dapat dijalankan lebih dari satu kali dan menghasilkan beberapa process atau execution context, tergantung model aplikasi dan operating system.

Misalnya kamu menjalankan aplikasi tertentu beberapa kali.

Secara konsep:
```text
Program
  ↓
Execution 1
  ↓
Process

Program
  ↓
Execution 2
  ↓
Process
```

Ini akan menjadi penting ketika nanti kamu belajar operating system, backend, concurrency, networking, dan security.

---
# Mengapa Memory Penting bagi Programmer?

Sekarang kamu mungkin bertanya:
> "Bukannya saya cuma perlu tahu coding?"

Untuk programming dasar, mungkin belum terasa, Tetapi semakin jauh kamu belajar, memory menjadi sangat penting.

Misalnya:
```javascript
const user = {
    name: "Yanda",
    age: 20
};
```

Data tersebut membutuhkan memory.

Ketika kamu membuat:
```javascript
const users = [];
```

kemudian memasukkan ribuan object ke dalamnya, memory yang digunakan juga meningkat.

Atau ketika aplikasi mengalami:
```text
Memory Leak
```

program dapat menggunakan memory semakin banyak sampai akhirnya performanya buruk atau process dihentikan.

Nanti ketika belajar programming lebih lanjut, kamu akan bertemu konsep seperti:
```text
Stack
Heap
Reference
Value
Memory Allocation
Garbage Collection
Pointer
Memory Leak
```

Sekarang belum perlu dipelajari semuanya, Cukup pahami bahwa:
> **Program membutuhkan memory untuk menyimpan data dan state selama program berjalan.**

---
# Program Tidak Berjalan Sendirian

Sebuah aplikasi modern hampir tidak pernah benar-benar bekerja sendirian.

Misalnya aplikasi web:
```text
Browser
   ↓
HTTP Request
   ↓
Web Server
   ↓
Application
   ↓
Database
   ↓
Application
   ↓
HTTP Response
   ↓
Browser
```

Di sini terdapat banyak komponen:
```text
Browser
Operating System
Network
Web Server
Runtime
Application
Database
Storage
CPU
RAM
```

Semuanya bekerja bersama.

Inilah alasan fundamental programming sebaiknya tidak berhenti pada syntax. Semakin kamu berkembang menjadi programmer, kamu akan mulai memahami bagaimana berbagai komponen tersebut saling berhubungan.

---

# Contoh: Apa yang Terjadi Saat Membuka Website?

Misalnya kamu membuka:

```text
https://example.com
```

Secara sederhana prosesnya dapat digambarkan seperti ini:

```text
Browser
   ↓
DNS
   ↓
Mencari IP server
   ↓
Network connection
   ↓
HTTP/HTTPS request
   ↓
Web Server
   ↓
Application
   ↓
Database jika diperlukan
   ↓
Response
   ↓
Browser
   ↓
Render halaman
```

Kemudian browser menggunakan CPU, RAM, GPU, network interface, dan berbagai software untuk menghasilkan tampilan yang kamu lihat.

Jadi ketika kamu melihat sebuah halaman web, sebenarnya ada banyak lapisan komputer yang sedang bekerja.

Kita belum perlu mempelajari semuanya sekarang.

Tetapi kamu harus mulai memiliki mental model bahwa:

> **Aplikasi hanyalah satu bagian dari sistem komputer yang lebih besar.**

---
# Kenapa Programmer Perlu Memahami Ini?

Karena nantinya ketika terjadi masalah, kamu harus mengetahui kira-kira masalah tersebut berada di layer mana.

Misalnya aplikasi lambat.

Kemungkinan masalahnya bisa berasal dari:
```text
Frontend
↓
Backend
↓
Database
↓
Network
↓
CPU
↓
Memory
↓
Storage
```

Kalau kamu hanya mengetahui syntax PHP atau JavaScript, kamu mungkin hanya melihat satu bagian kecil dari masalah.

Tetapi programmer yang memiliki fundamental kuat mulai berpikir:
```text
"Apakah application code yang lambat?"

"Apakah query database?"

"Apakah network latency?"

"Apakah memory pressure?"

"Apakah CPU usage?"

"Apakah storage I/O?"
```

Inilah yang nantinya membedakan programmer yang hanya bisa membuat kode dengan programmer yang memahami **sistem**.

---
# Mental Model yang Harus Kamu Miliki

Untuk sekarang, jangan mencoba menghafal seluruh arsitektur komputer.

Cukup simpan gambaran besar ini di kepala:
```text
                 USER
                  ↓
             APPLICATION
                  ↓
            OPERATING SYSTEM
                  ↓
        ┌─────────┼─────────┐
        ↓         ↓         ↓
       CPU       RAM      STORAGE
        ↓
   EXECUTE INSTRUCTIONS
```

Kalau aplikasinya membutuhkan internet:
```text
APPLICATION
     ↓
OPERATING SYSTEM
     ↓
NETWORK STACK
     ↓
NETWORK INTERFACE
     ↓
NETWORK
     ↓
SERVER
```

Dan pada sisi server:
```text
REQUEST
   ↓
SERVER
   ↓
APPLICATION
   ↓
DATABASE
   ↓
RESPONSE
```

Ini adalah fondasi mental model yang nanti akan terus kita gunakan ketika belajar backend, networking, Linux, database, cybersecurity, dan cloud.

---
# Kesimpulan Bab

Komputer pada dasarnya adalah mesin yang menjalankan instruksi dan memproses data.

Programmer menulis program menggunakan bahasa pemrograman. Program tersebut kemudian diproses oleh compiler, interpreter, runtime, atau kombinasi berbagai komponen lain, sampai akhirnya CPU dapat menjalankan instruksi yang sesuai.

Hardware dan software bekerja bersama.

CPU bertugas mengeksekusi instruksi.

RAM menyediakan tempat untuk data dan program yang sedang digunakan.

Storage menyimpan data dan program secara persisten.

Operating system menjadi lapisan penting yang mengatur resource hardware dan menyediakan layanan bagi aplikasi.

Dan ketika sebuah program dijalankan, program tersebut menjadi bagian dari execution environment yang dikelola oleh operating system, sering kali dalam bentuk process.

Gambaran besarnya:
```text
Programmer
    ↓
Source Code
    ↓
Compiler / Interpreter / Runtime
    ↓
Operating System
    ↓
CPU + RAM + Storage + Network
    ↓
Program Execution
    ↓
Output
```

Yang paling penting bukan menghafal istilah-istilah tersebut. Kamu harus memahami **hubungan antarbagian**.

Ketika nanti kamu menulis:
```php
echo "Hello World";
```

jangan melihatnya hanya sebagai syntax PHP.

Di balik satu baris sederhana itu terdapat bahasa pemrograman, runtime, operating system, process, memory, CPU, dan output mechanism yang bekerja bersama. Kita sengaja belum membongkar semuanya sampai level terdalam karena itu bukan tujuan bab ini. Untuk sekarang kita sedang membangun peta dunia terlebih dahulu sebelum mulai menjelajahinya.

