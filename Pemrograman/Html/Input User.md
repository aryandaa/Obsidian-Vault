#programming 
### Input Element

Elemen `<input>` merupakan elemen yang sangat sering dipakai untuk mendapatkan data dari user. Mengapa hal tersebut terjadi? Hal ini karena elemen input memiliki banyak sekali tipe-tipenya, mulai dari teks, password, email, search, file, dsb. Tidak hanya itu, dari sekian tipe input, masing-masingnya juga didukung oleh atribut khusus sehingga pembuatan formulir semakin _powerful_.

Berikut adalah contoh penerapan dari input element.
```html
<div>
  Text:
  <input type="text" />
</div>
<div>
  Number:
  <input type="number" />
</div>
<div>
  Email:
  <input type="email" />
</div>
<div>
  Password:
  <input type="password" />
</div>
```
output:
<div>
  Text:
  <input type="text" />
</div>
<div>
  Number:
  <input type="number" />
</div>
<div>
  Email:
  <input type="email" />
</div>
<div>
  Password:
  <input type="password" />
</div>

Selain tipe-tipe input di atas, ada banyak tipe lainnya yang tersedia. Selengkapnya, Anda dapat lihat pada tabel berikut.
  
|                                                              |                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tipe**                                                     | **Deskripsi**                                                                                                                                                                                                                                                                            |
| `<input type="text">` <input type="text">                    | Input teks yang berisi satu baris. Ini adalah tipe default dari input elemen. Jika tidak menentukan tipenya, tipe **text**-lah yang akan diterapkan.                                                                                                                                     |
| `<input type="number">`<input type="number">                 | Input teks yang hanya mengizinkan format angka.                                                                                                                                                                                                                                          |
| `<input type="password">`<input type="password">             | Sama seperti input text, tetapi setiap karakter akan ditampilkan sebagai bintang.                                                                                                                                                                                                        |
| `<input type="email">`<input type="email">                   | Sama seperti teks biasa, tetapi input ini dikhususkan untuk format email. Jika tidak, error akan muncul.                                                                                                                                                                                 |
| `<input type="search">`<input type="search">                 | Input untuk melakukan pencarian berdasarkan kata kunci. Input ini memiliki ikon ✕ di tepi kanan elemen untuk melakukan clear text.                                                                                                                                                       |
| `<input type="date">`<input type="date">                     | Untuk mengambil data tanggal. Tipe ini akan menyediakan popup penanggalan untuk mempermudah pengisian.                                                                                                                                                                                   |
| `<input type="time">`<input type="time">                     | Menentukan waktu (jam) yang ingin user isi. Tipe input ini juga akan menampilkan visual dari jam.                                                                                                                                                                                        |
| `<input type="datetime-local">`<input type="datetime-local"> | Sama seperti tipe date, tetapi ia menambahkan data waktu (jam).                                                                                                                                                                                                                          |
| `<input type="checkbox">`<input type="checkbox">             | Di-render sebagai sebuah kotak yang dapat dicek untuk active.                                                                                                                                                                                                                            |
| `<input type="radio">`<input type="radio">                   | Pada umumnya, ini digunakan untuk melakukan pemilihan dari sekian opsi (radio button) yang ada. Untuk melakukannya, input ini akan dikelompokkan dalam sebuah radio group. Bukan merupakan suatu elemen, kita dapat memberikan value yang sama pada atribut name di setiap elemen radio. |
| `<input type="range">`<input type="range">                   | Menentukan nilai angka berdasarkan jangkauan nilai yang ditentukan. User tidak akan bisa mengambil nilai diluar yang ditentukan.                                                                                                                                                         |
| `<input type="color">`<input type="color">                   | User dapat menentukan warna dengan tipe ini, baik menggunakan color picker atau memasukkan format nilai warna secara manual.                                                                                                                                                             |
| `<input type="file">`<input type="file">                     | Melakukan input satu atau lebih berkas dari penyimpanan data perangkatnya.                                                                                                                                                                                                               |
| `<input type="submit">`<input type="submit">                 | Input yang di-render sebagai tombol submit. Jika tombol ini ditekan, formulir akan ter-submit dan dikirimkan ke tujuan pengiriman (atribut action).                                                                                                                                      |
| `<input type="hidden">`<input type="hidden">                 | Biasanya, tipe ini tidak terlihat oleh user. Namun, input ini akan sangat berguna bagi developer untuk memasukkan suatu data.                                                                                                                                                            |

### Label Element

Pembuatan elemen input sudah umum jika dijajarkan dengan elemen label. Ada banyak sekali keuntungan jika memberikan keterangan–dengan kata lain, kita bisa menyebutnya caption–pada masing-masing elemen input. Tidak hanya elemen input, elemen lainnya seperti textarea juga perlu disandingkan dengan elemen label.

Beberapa keuntungan penerapan label untuk elemen input sebagai berikut.

- Elemen input yang berasosiasi dengan elemen label akan memberikan kemampuan bagi _screen reader_ untuk menjelaskan fungsi dari elemen input tersebut. Dalam hal ini, ia akan meningkatkan aksesibilitas. Tentunya, ini akan sangat bermanfaat bagi penyandang disabilitas.
- Memberikan kemampuan bagi browser untuk mengalihkan langsung pada elemen input saat elemen label yang berasosiasi dengannya ditekan atau klik.

Ada dua langkah untuk menghubungkan elemen label dan input. Pertama, menambahkan atribut id pada elemen input beserta value-nya. Kedua, menambahkan atribut for pada elemen label dan value-nya. Apakah sudah selesai sampai sini? Jawabannya, belum. Kita perlu memberikan value yang **sama** pada kedua atribut (id dan for). Dengan cara ini, elemen label akan berasosiasi dengan elemen input dan kita akan mendapatkan dua keuntungan yang telah dibahas sebelumnya.
```html
<div>
  <label for="email">Email</label>
  <br>
  <input type="email" id="email" />
</div>

<div>
  <label for="password">Password</label>
  <br>
  <input type="password" id="password" />
</div>
```
output:
<div>
  <label for="email">Email</label>
  <br>
  <input type="email" id="email" />
</div>
<div>
  <label for="password">Password</label>
  <br>
  <input type="password" id="password" />
</div>

## Atribut pada Elemen Input

Banyak sekali tipe dari elemen input yang dirancang untuk mengatasi beragam kasus data. Bahkan, pewarnaan pun disediakan oleh HTML dengan berbagai variasi nilai (RBG, Hex, dsb.). Pembahasan tentang input element tidak hanya sampai di situ. Ada hal lain yang perlu dibahas dan diketahui untuk memaksimalkan pembuatan formulir di website. 

Sebelumnya, kita sempat menyinggung bahwa atribut yang didukung sangat beragam selain tipe elemen input. Ada atribut yang bekerja untuk semua tipe input dan ada atribut yang hanya dikhususkan bagi satu tipe.

Berikut adalah contoh penerapan atribut placeholder dan required.
```html
<div>
  <label for="email">Email</label>
  <br />
  <input type="email" id="email" placeholder="example@mail.com" required />
</div>

<div>
  <label for="password">Password</label>
  <br />
  <input type="password" id="password" placeholder="********" required />
</div>
```
hasilnya akan seperti ini:
<div>
  <label for="email">Email</label>
  <br />
  <input type="email" id="email" placeholder="example@mail.com" required />
</div>
<div>
  <label for="password">Password</label>
  <br />
  <input type="password" id="password" placeholder="********" required />
</div>


Dua atribut di atas merupakan atribut yang sering dimanfaatkan ketika membuat formulir. Atribut placeholder digunakan untuk memberikan contoh atau referensi data sebagai panduan user mengisi data, sedangkan atribut required menandakan bahwa elemen input tersebut wajib diisi.

> **Catatan:**  
> Elemen label tidak dapat digantikan oleh atribut placeholder. Kedua hal ini memiliki peranannya sendiri dalam membuat formulir. Placeholder berfungsi sebagai petunjuk user dalam mengisi data, bukan untuk memberi keterangan atau caption elemen input.

Berikut adalah beberapa atribut yang menurut kami sering digunakan ketika membangun formulir.

|**Atribut**|**Tipe**|**Deskripsi**|
|---|---|---|
|name|semua tipe|Menamai elemen input. Data yang diisikan oleh user akan dikirimkan saat formulir di-submit. Atribut ini memiliki peran yang sangat penting. Jika tidak menyertakannya, data input tidak akan dikirim ke server.|
|placeholder|text, search, url, tel, email, password, number|Teks “samar” yang muncul pada kolom input. Teks ini biasanya digunakan sebagai petunjuk atau contoh data yang perlu diisi.|
|required|semua tipe, kecuali hidden, range, color, dan button|Atribut ini menyebabkan elemen input wajib diisi untuk di-submit. Ia merupakan atribut boolean.|
|value|semua tipe, kecuali image|Memberikan data awal atau default pada elemen input.|
|autocomplete|semua tipe, kecuali checkbox, radio, dan button|Fitur melengkapi input secara otomatis. Biasanya, ini terjadi ketika kita pernah meng-input sesuatu dan pada kesempatan berikutnya, data tersebut akan ditampilkan lagi oleh browser sebagai autocomplete.|
|maxlength|text, search, url, tel, email, password|Menentukan maksimal panjang karakter yang diperbolehkan pada kolom input.|
|max|date, month, week, time, datetime-local, number, range|Menentukan maksimal nilai yang diperbolehkan.|
|minlength|text, search, url, tel, email, password|Menentukan minimal panjang karakter yang diperbolehkan pada kolom input.|
|min|date, month, week, time, datetime-local, number, range|Menentukan minimal nilai yang diperbolehkan.|
|checked|checkbox, radio|Mengaktifkan atau mencentangkan input checkbox.|
|accept|file|Panduan atau batasan format berkas apa yang diperbolehkan pada input berkas.|
|multiple|email, file|Memungkinkan pemilihan ganda pada elemen input.|
|pattern|text, search, url, tel, email, password|Menentukan pola yang wajib dipatuhi pada data yang diisi agar dapat valid.|
|readonly|semua tipe, kecuali hidden, range, color, checkbox, radio, dan button|Tidak memiliki akses edit nilai.|
|disabled|semua tipe|Memberikan efek tidak aktif pada elemen input.|

  
Ada banyak sekali atribut-atribut yang tersedia. Tidak hanya memberikan fitur lebih, beberapa atribut lainnya dapat mengaktifkan proses validasi terhadap data yang dimasukkan user, seperti required, pattern, max, maxlength, dsb.

Jika Anda ingat, menentukan tipe pada elemen input merupakan salah satu penerapan validasi. Contohnya, jika Anda menerapkan tipe email dan tidak mengisi data dengan email valid, sebuah popup error akan muncul untuk memberi petunjuk pada user agar data yang dimasukkan valid.

Itulah beberapa atribut pada elemen input yang dapat dimanfaatkan untuk memberikan kemampuan yang lebih dari sekadar input biasa.