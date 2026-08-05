#programming 
Setelah Filament diinstal, Laravel akan memiliki sebuah folder baru bernama **Filament** di dalam direktori `app`.

```
app
│
├── Models
│
├── Http
│
└── Filament
      ├── Resources
      ├── Widgets
      ├── Pages
      ├── Clusters
      └── Providers
```

Masing-masing folder memiliki fungsi yang berbeda.

Folder **Resources** merupakan bagian yang paling sering digunakan karena hampir seluruh operasi CRUD dibuat melalui folder ini. 

Folder **Widgets** digunakan untuk membuat dashboard statistik, grafik, maupun ringkasan data. 

Folder **Pages** digunakan apabila developer ingin membuat halaman khusus yang tidak berhubungan dengan CRUD. 

Sementara itu, **Clusters** digunakan untuk mengelompokkan menu agar sidebar menjadi lebih rapi ketika aplikasi sudah memiliki banyak modul.

Dalam praktiknya, seorang developer dapat menghabiskan sebagian besar waktunya hanya di dalam folder Resources karena hampir seluruh kebutuhan administrasi data dapat diselesaikan melalui Resource.