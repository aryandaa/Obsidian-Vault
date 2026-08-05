#latihan
## Studi Kasus
Kamu baru diterima sebagai Backend Developer di sebuah startup.

Senior Developer memberikan sebuah aplikasi Flask sederhana yang terhubung ke MongoDB. Aplikasi tersebut nantinya harus bisa dijalankan oleh developer lain hanya dengan beberapa command saja.

Namun sebelum di-deploy, aplikasi harus memenuhi standar berikut:
- Aplikasi dijalankan menggunakan Docker.
- Database berjalan pada container yang berbeda.
- Kedua container saling berkomunikasi menggunakan Docker Network.
- Konfigurasi tidak boleh ditulis langsung di source code (Atur Environment nya dari luar).
- Image harus di-upload ke Docker Hub.
- Data database tidak boleh hilang ketika container dihapus.
- Build image harus efisien dan aman (dockerignore).
Seluruh tugas di bawah harus diselesaikan.

---

# Task 1 - Membuat Aplikasi
Buat aplikasi Flask sederhana yang menampilkan:
- Nama pengguna dari Environment Variable.
- Status koneksi MongoDB.

Contoh tampilan browser:
```
Halo, Aryanda

🟢 MongoDB Connected
```

---

# Task 2 - Dockerfile
Buat Dockerfile yang dapat menjalankan aplikasi tersebut.

Dockerfile harus memiliki:
- Base Image Python
- WORKDIR
- COPY
- Install dependency
- CMD

Build image.
```
docker build -t aryanda/app-python:Task1 .
```
Pastikan image berhasil dibuat.

---

# Task 3 - Menjalankan Container

Jalankan aplikasi.
```
docker run -p 8080:5000 aryanda/app-python:Task1
```
Pastikan browser bisa diakses.

---

# Task 4 - Environment Variable
Jalankan kembali container dengan nama berbeda.

```
docker run \
-p 8080:5000 \
-e NAMA=Aryanda \
aryanda/app-python:Task1
```
Pastikan nama berubah.

---

# Task 5 - Docker Hub

```
docker push aryanda/app-python:Task1
```

Lalu hapus image lokal.

```
docker rmi
```

Download kembali.
```
docker pull
```
Pastikan image tetap bisa dijalankan.

---

# Task 6 - MongoDB
Buat container MongoDB.
```
docker run
```

Gunakan:
- username
- password

Pastikan MongoDB berjalan.

---

# Task 7 - Docker Network

Buat network.

```
docker network create belajar-network
```

Hubungkan:
- MongoDB
- Flask
Pastikan aplikasi berhasil melakukan ping ke MongoDB.


---

# Task 8 - Docker Compose

Buat file `docker-compose.yml`.

Syarat:
- Flask
- MongoDB
- Network
- Environment Variable

Jalankan.
```
docker compose up -d
```
Pastikan cukup satu command untuk menjalankan seluruh aplikasi.

---

# Task 9 - Volume

MongoDB sekarang harus menggunakan Docker Volume.

Buat volume.

```
docker volume create mongo_data
```

Mount ke MongoDB.

Tambahkan sebuah database.

Hapus container MongoDB.

Buat lagi menggunakan volume yang sama.

Pastikan data masih ada.

Materi:

- Docker Volume

---

# Task 10 - Bind Mount

Sekarang jangan gunakan Volume.

Gunakan Bind Mount.

Misalnya:

```
-v ~/docker/mongodb:/data/db
```

Tambahkan data.

Hapus container.

Buat lagi.

Pastikan data tetap ada.

Materi:

- Bind Mount

---

# Task 11 - Docker Exec

Masuk ke container aplikasi.

```
docker exec -it app-python sh
```

Lakukan beberapa pengecekan:

- cek Environment Variable
- cek isi folder
- cek apakah source code ada

Materi:

- docker exec

---

# Task 12 - Docker Logs

Lihat log aplikasi.

```
docker logs app-python
```

Tambahkan request dari browser.

Lihat log kembali.

Pastikan request muncul.

Materi:

- docker logs

---

# Task 13 - Docker Inspect

Gunakan:

```
docker inspect app-python
```

Cari informasi berikut.

- IP Address
- Network
- Mount
- Image
- Environment Variable

Materi:

- docker inspect

---

# Task 14 - `.dockerignore`

Tambahkan file berikut.

- .env
- README.md
- logs
- test
- **pycache**
- bigfile.bin

Buat file dummy 500 MB.

Build tanpa `.dockerignore`.

Catat ukuran Build Context.

Tambahkan `.dockerignore`.

Build kembali.

Bandingkan hasilnya.

Materi:

- Build Context
- `.dockerignore`

---

# Task 15 - Simulasi Developer Baru

Sekarang anggap laptop benar-benar baru.

Hapus:

- seluruh container
- seluruh image
- seluruh network
- seluruh volume

Kemudian clone project.

Developer baru hanya boleh menjalankan:

```
docker compose up -d
```

Targetnya:

- Flask berjalan.
- MongoDB berjalan.
- Database otomatis terhubung.
- Data tetap ada (jika menggunakan volume/bind mount yang sesuai).
- Tidak perlu install Python.
- Tidak perlu install Flask.
- Tidak perlu install MongoDB.

Kalau semua itu berhasil, berarti project-mu benar-benar siap dibagikan ke orang lain.

---

# Bonus Challenge ⭐⭐⭐⭐⭐

Bayangkan senior developer memberikan revisi berikut:

> "Sekarang aplikasi harus bisa dijalankan oleh developer lain tanpa mengubah satu baris pun source code."

Selesaikan dengan syarat:

- Semua konfigurasi berasal dari Environment Variable.
- Semua service dijalankan melalui Docker Compose.
- Data MongoDB persisten.
- Image sudah ada di Docker Hub.
- `.env` tidak ikut masuk ke image.
- Project dapat dijalankan hanya dengan:

```
docker compose up -d
```

---

Menurutku, kalau kamu mampu menyelesaikan semua task ini **tanpa melihat catatan**, kamu sudah menguasai sekitar **90% Docker Basic**. Sisanya hanyalah command operasional (`stats`, `system`, `top`, `events`, dan sejenisnya) yang memang biasanya dicari saat dibutuhkan, bukan dihafalkan. Ini juga sudah cukup kuat sebagai fondasi sebelum masuk ke materi **Intermediate Docker** seperti Layer, Build Cache, Multi-stage Build, dan optimasi Dockerfile.