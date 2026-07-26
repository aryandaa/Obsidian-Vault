#devops 
## Apa itu Docker Logs?
**Docker Logs** adalah fitur yang digunakan untuk melihat seluruh output (stdout dan stderr) yang dihasilkan oleh aplikasi yang berjalan di dalam container.

Dengan kata lain, semua yang biasanya muncul di terminal ketika menjalankan aplikasi akan direkam oleh Docker.

Misalnya aplikasi Flask:
```
print("Server berjalan...")
```

atau
```
print("Database Connected")
```

atau ketika terjadi error:
```
ModuleNotFoundError
Connection Refused
Permission Denied
```

Semuanya akan disimpan oleh Docker dan dapat dilihat kapan saja menggunakan `docker logs`.

Ilustrasinya:
```
             Flask App
                 │
         print("Hello")
         print("Connected")
         print("Error...")
                 │
                 ▼
           Docker Engine
                 │
                 ▼
          Docker Log Driver
                 │
                 ▼
docker logs app-python
```

---

# Kenapa Docker Logs Dibutuhkan?
Bayangkan aplikasi berjalan sebagai container.
```
app-python
```
Container tersebut berjalan di background.

Kamu tidak melihat output apa pun, Suatu saat browser menampilkan:
```
500 Internal Server Error
```
Bagaimana cara mengetahui penyebabnya?

Jawabannya:
```
docker logs app-python
```
Dari sana biasanya akan muncul error sebenarnya.

Contoh:
```
Traceback (most recent call last):
ModuleNotFoundError:
No module named flask
```
Tanpa logs, kita hanya tahu aplikasi gagal.
Dengan logs, kita tahu **kenapa** aplikasi gagal.

---

# Melihat Log
Sintaks paling sederhana:
```
docker logs <container>
```

Misalnya:
```
docker logs app-python
```

Output:
```
* Serving Flask app 'app'
* Running on http://0.0.0.0:5000
172.17.0.1 - - [26/Jul/2026] "GET / HTTP/1.1" 200 -
```

---

# Mengikuti Log Secara Real Time

Perintah paling sering dipakai:
```
docker logs -f app-python
```
`-f` berarti Follow
Artinya Docker akan terus menampilkan log baru seperti:

```
GET /
GET /
GET /
POST /login
GET /dashboard
```

Mirip:
```
tail -f logfile.log
```
di Linux.

Contoh:
Browser di-refresh.
Terminal langsung menampilkan:
```
172.17.0.1 GET /
172.17.0.1 GET /
172.17.0.1 GET /
```
Sangat berguna saat debugging.

---

# Menampilkan 10 Log Terakhir
Kadang log sangat banyak, kita Tidak perlu melihat semuanya, jadi cukup Gunakan:
```
docker logs --tail 10 app-python
```

Hanya muncul:
```
...
...
10 baris terakhir
```

Misalnya:
```
GET /
GET /
POST /login
Connected MongoDB
```

---

# Mengikuti Log Mulai 20 Baris Terakhir

Ini kombinasi yang paling sering dipakai.
```
docker logs -f --tail 20 app-python
```

Artinya:
```
Tampilkan 20 log terakhir

↓

Lalu terus ikuti log baru
```
Ini jauh lebih nyaman daripada membaca ribuan baris log lama.

---

# Menampilkan Log Berdasarkan Waktu
Misalnya hanya ingin melihat log dalam satu jam terakhir.
```
docker logs --since 1h app-python
```
atau
```
docker logs --since 30m app-python
```

atau
```
docker logs --since 10s app-python
```

Contoh:
```
Request Login
Insert MongoDB
User Logout
```

---

# Sampai Waktu Tertentu
```
docker logs --until 5m app-python
```

Artinya hanya tampilkan log hingga lima menit yang lalu.
Biasanya dipakai bersama `--since`.

---

# Menampilkan Timestamp

Supaya tahu kapan log dibuat.
```
docker logs -t app-python
```

Output:
```
2026-07-26T14:21:11 GET /
2026-07-26T14:21:13 GET /
```
Ini penting ketika mencocokkan waktu kejadian dengan monitoring atau laporan pengguna.

---

# Docker Compose Logs
Kalau memakai Compose, Misalnya ada:
```
Mongo
Redis
Python
Nginx
```

Semua log:
```
docker compose logs
```

Output:
```
mongo      |
mongo      |
app-python |
nginx      |
```
Setiap service diberi nama sehingga mudah dibedakan.

---

## Log Satu Service

Misalnya hanya Python.

```
docker compose logs app-python
```

atau MongoDB.
```
docker compose logs mongo
```

---

## Follow Compose

```
docker compose logs -f
```
Kalau browser di-refresh.
Log langsung muncul.

---

# Contoh Nyata Debugging

Misalnya browser.
```
Halo Aryanda

MongoDB Disconnected
```
Tidak tahu penyebabnya.

Lihat log.
```
docker logs app-python
```

Muncul.
```
Authentication Failed
```
Berarti username/password salah.

Contoh lain.
```
Connection Refused
```
Berarti MongoDB belum hidup.

Atau.
```
No module named pymongo
```
Berarti lupa install dependency.
Hanya dari logs, penyebab masalah bisa langsung diketahui.

---

# Docker Logs vs docker exec

Banyak orang baru sering tertukar.
## docker logs
Hanya membaca output aplikasi.
```
docker logs app-python
```
Tidak masuk ke dalam container.
Tidak bisa mengetik perintah.

---

## docker exec

Masuk ke dalam container.
```
docker exec -it app-python sh
```

Di sini kamu bisa:
```
ls

pwd

env

python
```

Jadi:
```
docker logs
```
↓
Membaca cerita.

Sedangkan

```
docker exec
```
↓
Masuk ke dalam rumah.

---

# Best Practice

Ketika container mengalami masalah, urutan troubleshooting yang umum adalah:

1. Pastikan container berjalan.
```
docker ps
```

2. Lihat log aplikasi.
```
docker logs app-python
```

3. Jika masih belum jelas, masuk ke container.
```
docker exec -it app-python sh
```

4. Periksa konfigurasi, file, atau environment variable secara langsung.
Pendekatan ini jauh lebih efisien daripada langsung menebak-nebak penyebab error.

---

# Ringkasan Perintah Penting

|Perintah|Fungsi|
|---|---|
|`docker logs app-python`|Melihat seluruh log container|
|`docker logs -f app-python`|Mengikuti log secara real time|
|`docker logs --tail 20 app-python`|Menampilkan 20 log terakhir|
|`docker logs -f --tail 20 app-python`|Menampilkan 20 log terakhir lalu mengikuti log baru|
|`docker logs --since 1h app-python`|Menampilkan log sejak 1 jam terakhir|
|`docker logs -t app-python`|Menampilkan log beserta timestamp|
|`docker compose logs`|Melihat log semua service dalam Compose|
|`docker compose logs app-python`|Melihat log satu service|
|`docker compose logs -f`|Mengikuti log semua service secara real time|

# Kesimpulan
`docker logs` adalah perintah yang digunakan untuk melihat output aplikasi yang berjalan di dalam container tanpa harus masuk ke dalam container tersebut. Perintah ini menjadi alat utama dalam proses debugging karena hampir semua informasi penting, seperti pesan sukses, aktivitas aplikasi, peringatan, hingga error, akan direkam oleh Docker. Dengan memanfaatkan opsi seperti `-f`, `--tail`, `--since`, dan `-t`, kita dapat memantau log secara lebih efisien sesuai kebutuhan. Dalam praktik DevOps, `docker logs` biasanya menjadi langkah pertama saat melakukan troubleshooting, sedangkan `docker exec` digunakan jika kita perlu masuk ke dalam container untuk melakukan pemeriksaan lebih lanjut. Menguasai `docker logs` berarti kamu sudah memiliki kemampuan dasar yang sangat penting untuk menganalisis dan menyelesaikan masalah pada aplikasi yang berjalan di dalam Docker.