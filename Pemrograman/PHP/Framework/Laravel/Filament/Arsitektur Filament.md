#programming 
Sebelum memahami sintaks, kita perlu memahami bagaimana Filament bekerja.

Ketika pengguna membuka sebuah halaman Filament, sebenarnya Laravel tetap menerima permintaan (request) tersebut seperti aplikasi Laravel biasa. Setelah request diterima, Livewire akan menangani komunikasi antara browser dengan server tanpa perlu melakukan refresh halaman secara penuh.

Dengan kata lain, ketika pengguna menekan tombol **Simpan**, browser tidak memuat ulang seluruh halaman. Livewire hanya mengirim data yang berubah ke server, kemudian server mengembalikan bagian tampilan yang perlu diperbarui. Hal ini membuat aplikasi terasa lebih responsif walaupun seluruh logika tetap dijalankan menggunakan PHP.

Secara sederhana hubungan antar teknologi tersebut dapat digambarkan sebagai berikut.
```
Browser
     │
     ▼
 Tailwind CSS
     │
     ▼
  Livewire
     │
     ▼
 Laravel
     │
     ▼
 Database
```

Tailwind CSS bertanggung jawab terhadap tampilan. Livewire menangani interaksi pengguna. Laravel mengelola seluruh logika aplikasi, sedangkan database menyimpan seluruh informasi.