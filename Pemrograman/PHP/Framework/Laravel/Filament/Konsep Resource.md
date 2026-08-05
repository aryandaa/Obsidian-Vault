#programming 
Konsep paling penting dalam Filament adalah **Resource**.

Resource dapat dipahami sebagai representasi sebuah Model Laravel di dalam panel administrasi. Apabila Laravel memiliki Model `Product`, maka biasanya akan terdapat `ProductResource`. Begitu pula jika terdapat Model `User`, maka biasanya terdapat `UserResource`.

Hubungan tersebut dapat digambarkan sebagai berikut.

```
Database
      │
      ▼
 Model Product
      │
      ▼
 ProductResource
      │
      ▼
Halaman CRUD
```

Resource bertugas menghubungkan Model dengan tampilan administrasi.

Pembuatan Resource dilakukan menggunakan Artisan.

```bash
php artisan make:filament-resource Product
```

Perintah tersebut akan menghasilkan berbagai file yang diperlukan, termasuk halaman daftar data, halaman tambah data, halaman edit data, serta konfigurasi navigasi.