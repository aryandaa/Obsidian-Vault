#programming 
### Keyword
Anda pasti pernah membaca Kamus Bahasa Indonesia. Tahukah Anda berapa jumlah kosakata atau _keywords_ yang ada dalam kamus Bahasa Indonesia? Kurang lebih ada 111.000 kosakata dan 127.000 makna kata di dalamnya. Bayangkan jika Anda harus menghafal semuanya, pasti sedikit menyulitkan, bukan? Sedangkan, keywords dalam bahasa pemrograman jauh lebih sedikit dari itu. Kita ambil contoh satu bahasa pemrograman yaitu Java yang memiliki 50 keywords. Bahkan bahasa Python hanya memiliki kurang lebih 33 keywords. Semakin sering kita _ngoding_, pasti akan hafal dengan sendirinya.

contoh keyword dalam python:

| Keyword dalam Python |         |        |
| -------------------- | ------- | ------ |
| and                  | exec    | not    |
| assert               | finally | or     |
| break                | for     | pass   |
| class                | from    | print  |
| continue             | global  | raise  |
| def                  | if      | return |
| del                  | import  | try    |
| elif                 | in      | while  |
| else                 | is      | with   |
| except               | lambda  | yield  |
Kita tidak bisa memberi nama variabel yang sama dengan nama keyword. Misal kita ingin membuat sebuah variabel _int if_ atau _string for_, maka kompiler akan mengirimkan pesan eror karena Anda menggunakan keyword sebagai nama variabel.

### Pseudocode
Pseudocode merupakan istilah dalam pemrograman untuk menuliskan sebuah sintaks, statement, algoritma, dan lainnya dalam bahasa yang bisa dipahami oleh manusia. Sederhananya, pseudocode adalah bentuk representasi dari kode kita nantinya dengan versi yang human readable, bukan computer readable.

pseudocode sangat penting sekali sebelum memulai sebuah program. Itu akan melatih kita tentang bagaimana program tersebut berjalan dan berpikir.

### Contoh pembuatan Pseudocode

Sebagai contoh kita ingin membuat aplikasi login. Ketika pengguna memasukkan email dan password yang sesuai dengan data yang tersimpan di database, ia dapat masuk ke halaman utama. Jika tidak sesuai, maka pengguna dipersilakan untuk memasukkan email dan password kembali.

Tenang saja, dalam Pseucode tidak ada standar khusus dalam hal penulisan. Namun, kita harus tetap membuatnya sederhana dan mudah dipahami.

Sebagai contoh, hasilnya seperti di bawah ini.
```
Get input email from user.
Get input password from user.

Check input user.
IF (email and password) equals to data on database
     Go to homepage
 ELSE
     PRINT login gagal, silakan ulangi kembali
     User input email and password again
 END IF
```
Oke, kita mulai dari yang pertama, alurnya adalah membuat aplikasi login yang berasal dari input email dan password pengguna. Untuk mendapatkan data email dan password, kita dapat menuliskan `get input email from user`. Untuk mengambil email dan password kita harus mendapatkannya satu per satu. Karena itulah kita menuliskan email terlebih dahulu di sini, kemudian baru langkah yang selanjutnya yaitu kita mendapatkan password. Kita bisa menggunakan kata-kata `get input password from user`. Jadi, di sini tidak ada hal khusus yang harus diperhatikan, yang terpenting adalah alur dan isi dari yang kita buat. Oke?

Nah, langkah selanjutnya yaitu kita akan melakukan pengecekan, yaitu pengecekan jika email dan password yang dimasukkan pengguna sesuai dengan data yang tersimpan di database. Untuk melakukan pengecekan, kita bisa menggunakan percabangan. Salah satu percabangan yang bisa kita gunakan yaitu **If-Else**. Jadi, kita tuliskan terlebih dahulu `check input user` karena di sini kita akan melakukan pengecekan.