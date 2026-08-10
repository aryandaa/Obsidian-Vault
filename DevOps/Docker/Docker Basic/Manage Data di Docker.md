#devops 
Saat membangun aplikasi, sebisa mungkin aplikasi dibuat **stateless**, yaitu aplikasi yang **tidak menyimpan data penting di dalam dirinya sendiri**. Dengan begitu, jika aplikasi dimatikan, dihapus, atau dibuat ulang, tidak ada data yang hilang. Konsep ini membuat aplikasi lebih mudah di-scale, dipindahkan, maupun di-deploy.

Namun, tidak semua aplikasi bisa bersifat stateless. Salah satu contohnya adalah **database**. Database seperti MongoDB, MySQL, atau PostgreSQL termasuk aplikasi **stateful** karena tugas utamanya adalah menyimpan data. Oleh karena itu, data yang ada di dalam database harus tetap ada meskipun container dihentikan atau dihapus.

Masalahnya, secara default setiap data yang disimpan di dalam container akan ikut hilang ketika container tersebut dihapus. Misalnya kita menjalankan MongoDB di dalam Docker, kemudian menjalankan perintah:
`docker rm -f mongodb`
maka seluruh data yang berada di dalam filesystem container juga akan ikut terhapus.

Untuk mengatasi masalah tersebut, Docker menyediakan fitur **data management**. Konsepnya adalah **data tidak disimpan di dalam container**, melainkan disimpan di media penyimpanan yang terpisah dari container. Dengan begitu, container dapat dihapus atau dibuat ulang kapan saja tanpa menghilangkan data.

Docker menyediakan beberapa cara untuk mengelola penyimpanan data, namun yang paling umum digunakan adalah **Volume**.

**Docker Volume** dapat diibaratkan sebagai sebuah media penyimpanan khusus yang dikelola langsung oleh Docker. Saat menjalankan container, kita dapat menghubungkan (mount) sebuah folder di dalam container ke sebuah volume. Misalnya, folder `/data/db` milik MongoDB dapat dihubungkan ke sebuah volume bernama `mongo-data`.

Ilustrasinya seperti berikut:
```
Container MongoDB
┌─────────────────────────┐
│ /data/db ───────────────┼──────────────┐
└─────────────────────────┘              │
                                         ▼
                               Docker Volume
                           ┌──────────────────┐
                           │    mongo-data    │
                           └──────────────────┘
```
Dengan cara ini, jika container MongoDB dihapus lalu dibuat kembali, Docker hanya akan memasang (mount) kembali volume `mongo-data` ke dalam container yang baru. Akibatnya, seluruh data database tetap tersimpan dan tidak hilang.

> **Kesimpulannya**, container sebaiknya dianggap sebagai sesuatu yang bersifat **sementara (ephemeral)**, sedangkan data penting harus disimpan di tempat yang bersifat **persisten**, seperti Docker Volume. Inilah alasan mengapa hampir semua aplikasi database yang dijalankan di Docker selalu menggunakan volume untuk menyimpan datanya.


# Tanpa Volume
Sekarang saya akan mencoba menjalankan MongoDB **tanpa menggunakan Docker Volume** untuk melihat apa yang terjadi pada data ketika container dihapus.

Pertama, saya membuat container MongoDB dengan perintah:

```
docker container create --name mongo -p 27017:27017 mongo:7
```

Kemudian saya menjalankan container tersebut:

```
docker container start mongo
```

Selanjutnya saya menghubungkan MongoDB ke aplikasi MongoDB Compass menggunakan host dan port dari container yang telah dibuat. Setelah berhasil terhubung, saya membuat sebuah database beserta beberapa data di dalamnya.

![](img/Pasted%20image%2020260726230404.png)

Data berhasil tersimpan dan dapat diakses selama container masih berjalan.

Setelah itu, saya menghentikan dan menghapus container:

```
docker container stop mongo
docker container rm mongo
```

Kemudian saya membuat container MongoDB baru dengan konfigurasi yang sama. Hasilnya, seluruh database dan data yang sebelumnya telah dibuat sudah tidak ada lagi.

Hal ini terjadi karena seluruh data database sebelumnya disimpan di dalam filesystem container. Ketika container dihapus, filesystem tersebut ikut terhapus sehingga seluruh data juga ikut hilang.

# Dengan Volume
Sekarang saya akan mencoba menyimpan data MongoDB menggunakan **Docker Volume** agar data tetap tersimpan meskipun container dihapus.

Docker menyediakan perintah bawaan `docker volume` untuk mengelola volume, seperti membuat, melihat, maupun menghapus volume.

Pertama, saya membuat sebuah volume baru dengan nama **mongo_data**:

```
docker volume create mongo_data
```

Selanjutnya saya membuat container MongoDB dan menghubungkan volume tersebut ke direktori penyimpanan data MongoDB, yaitu **`/data/db`**.

```
docker container create \
  --name mongo \
  -p 27017:27017 \
  -v mongo_data:/data/db \
  mongo:7
```

Opsi `-v mongo_data:/data/db` berarti Docker akan memasang (mount) volume **mongo_data** ke direktori **`/data/db`** di dalam container. Dengan demikian, seluruh data MongoDB tidak lagi disimpan di filesystem container, melainkan di dalam Docker Volume.

Setelah container dijalankan dan saya kembali menghubungkannya ke MongoDB Compass, saya membuat database beserta beberapa data seperti sebelumnya.

Kemudian saya menghentikan dan menghapus container:

```
docker container stop mongo
docker container rm mongo
```

Selanjutnya saya membuat kembali container MongoDB dengan konfigurasi yang sama dan tetap menggunakan volume **mongo_data**.

Hasilnya, seluruh database dan data yang sebelumnya dibuat masih tetap ada. Hal ini membuktikan bahwa Docker Volume mampu menyimpan data secara persisten meskipun container dihapus dan dibuat ulang.

## Mengapa lebih disarankan menggunakan Docker Volume?

Docker Volume merupakan media penyimpanan yang dikelola langsung oleh Docker sehingga lebih aman dan mudah dikelola dibandingkan menyimpan data di dalam filesystem container. Selain itu, Docker Volume memiliki beberapa keunggulan, antara lain:

- Data tetap tersimpan meskipun container dihapus.
- Dapat digunakan kembali oleh container baru.
- Memudahkan proses **backup** dan **restore** data.
- Memudahkan proses **migrasi** data ke server atau host lain.
- Memiliki performa yang lebih baik dibandingkan menyimpan data langsung di dalam filesystem container.

Oleh karena itu, hampir semua aplikasi yang bersifat **stateful**, seperti MongoDB, MySQL, PostgreSQL, Redis, maupun database lainnya, umumnya menggunakan Docker Volume untuk menyimpan data secara persisten.

--- 
# Menyimpan Data ke Direktori Komputer (Bind Mount)
Pada contoh sebelumnya, data MongoDB disimpan menggunakan **Docker Volume** yang dikelola langsung oleh Docker. Lokasi penyimpanannya berada di dalam direktori internal Docker sehingga kita tidak mengetahui secara langsung letak folder tersebut.

Namun, terkadang kita ingin data disimpan **langsung di dalam folder komputer kita sendiri**. Misalnya agar lebih mudah diakses, dibackup, atau dimasukkan ke dalam project tertentu.

Untuk kebutuhan tersebut, Docker menyediakan fitur **Bind Mount**.

Dengan Bind Mount, kita dapat menghubungkan sebuah folder di komputer (host) ke sebuah folder di dalam container.

Ilustrasinya seperti berikut:
```
Komputer (Host)
┌─────────────────────────────────────┐
│ /home/r3x/docker-data/mongodb       │
└──────────────────┬──────────────────┘
                   │
                   ▼
Container MongoDB
┌─────────────────────────────────────┐
│ /data/db                            │
└─────────────────────────────────────┘
```

Artinya, setiap data yang ditulis MongoDB ke dalam folder `/data/db` sebenarnya akan langsung disimpan ke folder:
```
/home/r3x/docker-data/mongodb
```
di komputer kita.
### 1. Membuat Folder
Sebelum menjalankan container, buat terlebih dahulu folder tujuan.

```
mkdir -p ~/docker-data/mongodb
```

atau jika ingin menggunakan path absolut:
```
mkdir -p /home/r3x/docker-data/mongodb
```

### 2. Membuat Container

Kemudian buat container MongoDB dengan Bind Mount.
```
docker container create \
  --name mongo \
  -p 27017:27017 \
  -v /home/r3x/docker-data/mongodb:/data/db \
  mongo:7
```

Lalu jalankan:
```
docker container start mongo
```

### 3. Menguji

Hubungkan MongoDB menggunakan MongoDB Compass, kemudian buat sebuah database dan beberapa data.

Setelah itu, lihat isi folder:
```
ls /home/r3x/docker-data/mongodb
```

Akan muncul file-file database MongoDB, misalnya:
```
WiredTiger
WiredTiger.lock
collection-0.wt
collection-1.wt
diagnostic.data
journal
```
Artinya data benar-benar disimpan di komputer, bukan di dalam filesystem container.

### 4. Menghapus Container

Sekarang hentikan dan hapus container.
```
docker container stop mongo
docker container rm mongo
```

Lalu buat kembali container dengan perintah yang sama:
```
docker container create \
  --name mongo \
  -p 27017:27017 \
  -v /home/r3x/docker-data/mongodb:/data/db \
  mongo:7
```

Jalankan kembali:
```
docker container start mongo
```
Database yang sebelumnya dibuat akan tetap ada karena seluruh data tersimpan di folder komputer.

---

# Docker Volume vs Bind Mount

Baik **Docker Volume** maupun **Bind Mount** sama-sama digunakan untuk menyimpan data di luar container agar data tidak hilang ketika container dihapus. Namun, keduanya memiliki tujuan penggunaan yang berbeda.

## Docker Volume
Docker Volume merupakan media penyimpanan yang **dikelola langsung oleh Docker**. Lokasi penyimpanannya berada di dalam direktori internal Docker sehingga pengguna tidak perlu mengatur sendiri letak penyimpanannya.

Contoh penggunaannya:

```
docker container create \
  --name mongo \
  -v mongo_data:/data/db \
  mongo:7
```

### Keunggulan Docker Volume
- Data tetap tersimpan meskipun container dihapus.
- Dikelola langsung oleh Docker sehingga lebih aman dan stabil.
- Mudah digunakan untuk proses **backup** dan **restore** data.
- Mudah dipindahkan (migrasi) ke server lain.
- Dapat digunakan oleh beberapa container sekaligus jika diperlukan.
- Memiliki performa yang lebih baik dibandingkan Bind Mount, terutama pada Docker Desktop (Windows dan macOS).
- Sangat cocok digunakan pada lingkungan **production**.

### Kekurangan Docker Volume
- Lokasi penyimpanan data tidak terlihat secara langsung sehingga sedikit lebih sulit diakses.
- Untuk melihat isi data, biasanya perlu menggunakan perintah Docker atau masuk ke dalam container.

---

## Bind Mount
Bind Mount menghubungkan sebuah folder yang ada di komputer (host) ke dalam container. Dengan demikian, seluruh data yang ditulis container akan langsung tersimpan pada folder tersebut.

Contohnya:
```
docker container create \
  --name mongo \
  -v /home/r3x/docker-data/mongodb:/data/db \
  mongo:7
```

Pada contoh di atas, semua data MongoDB akan disimpan langsung di folder:
```
/home/r3x/docker-data/mongodb
```

### Keunggulan Bind Mount
- Data dapat diakses langsung melalui File Explorer atau File Manager.
- Mudah diedit menggunakan editor seperti VS Code atau Neovim.
- Sangat praktis untuk proses development karena setiap perubahan langsung terlihat tanpa perlu membangun ulang image.
- Memudahkan proses belajar karena kita dapat melihat secara langsung file yang dibuat oleh aplikasi.
- Sangat cocok untuk menyimpan source code, file konfigurasi, maupun hasil log selama proses pengembangan.

### Kekurangan Bind Mount
- Bergantung pada struktur direktori sistem operasi host, sehingga kurang portabel.
- Jika project dipindahkan ke komputer lain, path direktori harus disesuaikan kembali.
- Pengaturan permission file terkadang dapat menimbulkan masalah, terutama pada Linux.

---

# Kapan Menggunakan Keduanya?

|Docker Volume|Bind Mount|
|---|---|
|Menyimpan data database|Menyimpan source code saat development|
|Environment production|Environment development|
|Backup dan restore lebih mudah|Mengedit file secara langsung|
|Migrasi data antar server|Belajar Docker dan testing|
|Data aplikasi yang bersifat persisten|Sinkronisasi file dengan komputer host|

## Kesimpulan
Secara umum, **Docker Volume** lebih direkomendasikan untuk menyimpan data penting seperti database karena dikelola langsung oleh Docker, lebih aman, serta mendukung proses backup, restore, dan migrasi dengan lebih baik. Oleh karena itu, Docker Volume lebih banyak digunakan pada lingkungan **production**.

Sementara itu, **Bind Mount** lebih cocok digunakan selama proses **development** atau pembelajaran. Dengan Bind Mount, file dapat langsung diakses dan diedit dari komputer tanpa harus masuk ke dalam container. Hal ini membuat proses debugging, pengembangan aplikasi, maupun belajar Docker menjadi lebih mudah dan praktis.

Singkatnya, jika tujuan utamanya adalah **menyimpan data aplikasi secara aman dan persisten**, gunakan **Docker Volume**. Namun, jika tujuan utamanya adalah **mengembangkan aplikasi dan sering mengubah file**, maka **Bind Mount** merupakan pilihan yang lebih tepat.