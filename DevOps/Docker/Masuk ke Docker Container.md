#devops 
Pada kondisi tertentu, kita perlu masuk ke dalam sebuah container yang sedang berjalan. Misalnya untuk:
- Melihat isi file di dalam container.
- Mengecek Environment Variable.
- Menjalankan perintah Linux.
- Melakukan debugging aplikasi.
- Mengakses database secara langsung.
- Menginstal package sementara (hanya untuk keperluan debugging).

Docker menyediakan perintah **`docker exec`** untuk menjalankan sebuah perintah di dalam container yang sedang aktif.

Sintaks dasarnya adalah:
```
docker exec [OPTIONS] <container> <command>
```

Contohnya:
```
docker exec app-python ls
```
Perintah di atas akan menjalankan perintah `ls` di dalam container `app-python`.

# Masuk ke Terminal Container
Agar dapat menggunakan container layaknya sebuah komputer Linux, kita dapat membuka terminal interaktif menggunakan opsi `-it`.
```
docker exec -it app-python sh
```

atau jika image tersebut memiliki Bash:
```
docker exec -it app-python bash
```

Keterangan:
- **-i (interactive)** → menjaga input terminal tetap aktif sehingga kita dapat mengetik perintah.
- **-t (tty)** → membuat terminal virtual sehingga tampilannya seperti terminal Linux biasa.

Setelah berhasil masuk, prompt terminal akan berubah, misalnya:
```
root@829641d61580:/app#
```
Artinya kita sedang berada **di dalam container**, bukan lagi di komputer (host).

# Mengapa Menggunakan `sh` dan Bukan `bash`?
Tidak semua image Docker memiliki Bash.

Misalnya image:
```
FROM python:3.13-slim
```
Image **Slim** dibuat sekecil mungkin sehingga banyak package yang dihilangkan, termasuk `bash`.

Karena itu kita menggunakan:
```
docker exec -it app-python sh
```

Jika memaksa menggunakan Bash:
```
docker exec -it app-python bash
```

kemungkinan akan muncul:
```
exec: "bash": executable file not found
```
Sedangkan image Ubuntu atau Debian versi lengkap biasanya sudah memiliki Bash.

---

# Contoh Penggunaan

### Melihat isi folder
```
ls
```
atau
```
ls -la
```

---

### Melihat direktori saat ini
```
pwd
```
Contoh hasil:
```
/app
```
---

### Melihat seluruh Environment Variable
```
env
```
atau
```
printenv
```

---

### Mencari Environment Variable tertentu
Misalnya hanya ingin melihat konfigurasi database:

```
env | grep DB
```
Hasilnya:
```
DB_HOST=mongo
DB_PORT=27017
DB_USER=root
DB_PASS=123456
```

---

### Menjalankan Python
Karena container kita menggunakan Python, kita juga dapat langsung menjalankan interpreter Python.
```
python
```

Prompt akan berubah menjadi:
```
>>>
```

Misalnya:
```
print("Halo Docker")
```
Hasil:
```
Halo Docker
```

Untuk keluar:
```
exit()
```

atau tekan
```
Ctrl + D
```

---

### Mengakses MongoDB

Jika masuk ke container MongoDB:
```
docker exec -it mongo mongosh
```
Kita dapat langsung menjalankan perintah MongoDB.

Contohnya:
```
show dbs
```

atau
```
db.runCommand({ ping: 1 })
```

---

# Keluar dari Container

Untuk keluar dari terminal container cukup jalankan:
```
exit
```

atau tekan
```
Ctrl + D
```

Setelah keluar, prompt akan kembali menjadi terminal komputer (host), misalnya:

```
r3x@parrot:~$
```

---

# Kapan `docker exec` Digunakan?

Perintah `docker exec` biasanya digunakan ketika ingin melakukan debugging atau pemeriksaan terhadap container yang sedang berjalan. Contohnya seperti mengecek file konfigurasi, memastikan Environment Variable sudah terbaca, menjalankan perintah Linux, atau mengakses database secara langsung tanpa harus membuat image baru. Oleh karena itu, `docker exec` merupakan salah satu perintah yang paling sering digunakan oleh developer maupun DevOps Engineer saat melakukan troubleshooting aplikasi yang berjalan di dalam Docker.

> **Kesimpulannya**, `docker exec` memungkinkan kita menjalankan perintah atau membuka terminal interaktif di dalam container yang sedang berjalan. Fitur ini sangat berguna untuk debugging, inspeksi, maupun administrasi container tanpa perlu menghentikan atau membuat ulang container tersebut.