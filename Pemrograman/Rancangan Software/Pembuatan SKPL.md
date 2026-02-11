#programming #webdev
ini sama seperti pembahasan sebelumnya, tetapi disini saya akan memberikan contoh secara langsung berdasarkan study kasus.

## Tahapan Proses
1. Pengantar
	1. Tujuan aplikasi
		`Pengguna dapat mengakses suatu halaman web setelah melakukan proses autentikasi dengan memasukan username dan password`
	2. Sasaran pengguna
		`Semua pengguna atau masyarakat umum yang sudah memiliki hak akses dalam password`
2. Kebutuhan Pengguna
	1. Deskripsi umum dari aplikasi
		`Autentikasi dari sebuah halaman website adalah hal yang penting, Kita harus mengetahui element apa saja yang dibutuhkan untuk masuk ke halaman website seperti email, passsword, dan tombol login. Ketika pengguna berhasil melakukan autentikasi dengan memasukan email dan password yang benar, maka ia dapat mengakses konten website yang ada di dalamnya. sedangkan jika pengguna tidak berhasil melakukan proses autentikasi, pengguna tidak dapat mengakses konten yang ada dan harus memeriksa kembali apakah email dan password yang dimasukan sudah benar. supaya lebih aman, ketika penguna selesai mengakses konten website, ia dapat melakukan proses logout dengan menekan tombol logout yang ada di dalam halaman website tersebut. setelah logout, pengguna akan keluar dari konten halaman website dan harus melakukan autentikasi kembali untuk bisa masuk`
	2. Kegunaan aplikasi bagi pengguna
		- Pengguna dapat masuk (login) untuk mengaksws konten yang ada di halaman website.
		- Aplikasi dapat memeriksa penulisan format email di dalam form pengisian email.
		- Pengguna dapat memasukan password dengan aman karna antarmuka form password disamarkan tampilannya.
		- Pengguna dapat keluar (Logout) dari halaman konten website dengan menekan tombol logout
3. Spesifikasi Kebutuhan Sistem
	1. Kebutuhan Fungsional
		- Pengguna dapat memasukan email dan password pada form yang di sediakan. kemudian, pengguna yang sudah melengkapi email dan password pada form tersebut dapat menekan tombol login untuk mengases konten halaman website
		- Pengguna dapat keluar dari konten halaman website dengan menekan tombol logout
	2. Kebutuhan Non-Fungsional
		- Ketika pengguna memasukkan email di dalam form email, sistem dapat memeriksa apakah inputan tersebut sudah sesuai dengan struktur email yang benar. Jika tidak sesuai, pengguna diberi pengingat bahwa belum mengisi form email dengan benar.
		- Ketika pengguna memasukkan password di dalam form password, sistem dapat menyembunyikan setiap huruf yang diketikkan. Sehingga, pengguna akan merasa aman ketika mengetik passwordnya di tempat umum sekalipun.
	3. User Interface
		- Perangkat lunak front-end: HTML dan CSS
		- Perangkat lunak back-end: JavaScript
	4. Hardware interface
		- Komputer atau ponsel cerdas dengan browser yang sudah terinstal di dalamnya
4. Rencana Pengembangan sistem
	Dalam pengembangan sistem ke depannya, pengembang software akan menambahkan fitur sebagai berikut:
	1. Enkripsi password pada aplikasi autentikasi halaman website.
	2. Pengecekan panjang password yang harus memiliki minimal 6 karakter.

