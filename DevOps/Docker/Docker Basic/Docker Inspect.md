#devops 
## Apa itu Docker Inspect?
`docker inspect` adalah perintah yang digunakan untuk melihat **seluruh informasi (metadata)** mengenai object Docker.

Object tersebut bisa berupa:
- Container
- Image
- Volume
- Network

Secara sederhana, Docker Inspect adalah **identitas lengkap** dari suatu object Docker.

Misalnya sebuah container memiliki:
- Nama
- ID
- IP Address
- Network
- Environment Variable
- Volume
- Port
- Image
- Working Directory
- Restart Policy
Semuanya bisa dilihat menggunakan satu perintah.

---

# Kenapa Docker Inspect Dibutuhkan?

Misalnya kita mempunyai container:

```
app-python
```

Kita tahu container tersebut berjalan.

Tetapi muncul beberapa pertanyaan:

> Image apa yang digunakan?

> Port internalnya berapa?

> Port host berapa?

> Environment Variable sudah masuk belum?

> Container ini berada di network mana?

> IP Address-nya berapa?

> Volume-nya tersimpan di mana?

Semua jawaban tersebut bisa diperoleh dari:

```
docker inspect app-python
```

---

# Sintaks Dasar

```
docker inspect <object>
```

Contoh:
```
docker inspect app-python
```
Outputnya sangat panjang karena berbentuk **JSON**.

Contohnya:
```
[
  {
    "Id": "...",
    "Created": "...",
    "State": {...},
    "Config": {...},
    "NetworkSettings": {...},
    "Mounts": [...]
  }
]
```
JSON dipilih karena mudah dibaca oleh program maupun manusia.

---

# Informasi Penting di Dalam Docker Inspect
Sebenarnya ada puluhan informasi.
Tetapi yang paling sering digunakan hanya beberapa.

---
# 1. Container ID
Misalnya
```
"Id": "829641d61580..."
```
Ini adalah ID unik container, Sama seperti NIK manusia.

Tidak mungkin ada dua container dengan ID yang sama.

---

# 2. Nama Container
```
"Name": "/app-python"
```

Artinya nama container adalah
```
app-python
```
Nama ini biasanya diberikan saat membuat container.

```
docker run --name app-python ...
```

---

# 3. Image

Misalnya
```
"Image": "sha256:..."
```

atau
```
aryanda/app-python:compose
```

Artinya container dibuat dari image tersebut.

---

# 4. Status Container

Bagian ini sering dipakai.
```
"State": {
    "Running": true,
    "Status": "running"
}
```
Artinya container sedang berjalan.

Kalau mati.
```
"Running": false
```

---

# 5. Environment Variable

Bagian ini juga sangat sering digunakan.

Misalnya
```
"Env": [
    "NAMA=Aryanda",
    "DB_HOST=mongo",
    "DB_PORT=27017"
]
```
Dari sini kita bisa memastikan apakah ENV benar-benar masuk ke container.

Ini jauh lebih cepat daripada masuk menggunakan
```
docker exec
```

dan mengetik
```
env
```

---

# 6. Port Mapping

Misalnya
```
"PortBindings": {
    "5000/tcp": [
        {
            "HostPort": "8080"
        }
    ]
}
```

Artinya
```
Host
8080
↓

Container
5000
```

Jadi ketika membuka
```
localhost:8080
```

yang menerima request sebenarnya adalah
```
5000
```
di dalam container.

---

# 7. Network

Misalnya
```
"Networks": {
    "python_network": {}
}
```

Artinya container berada pada network
```
python_network
```

Kalau container tidak berada pada network yang sama dengan MongoDB, komunikasi tidak akan berhasil.

---

# 8. IP Address

Misalnya
```
"IPAddress": "172.19.0.3"
```

Artinya container memperoleh IP internal Docker.

Container lain pada network yang sama dapat mengakses IP tersebut, meskipun dalam praktik sehari-hari lebih disarankan menggunakan **nama service** atau **nama container** daripada IP karena IP dapat berubah ketika container dibuat ulang.

---

# 9. Volume / Bind Mount

Misalnya
```
"Mounts": [
    {
        "Type": "volume",
        "Source": "...",
        "Destination": "/data/db"
    }
]
```

atau
```
"Type": "bind"
```
Bagian ini menunjukkan apakah container menggunakan:
- Docker Volume
- Bind Mount
Sekaligus memperlihatkan lokasi penyimpanannya.

---

# Cara Membaca Informasi Tertentu

Output `docker inspect` bisa mencapai ratusan baris. Untungnya Docker mendukung **Go Template** sehingga kita bisa mengambil informasi tertentu saja.

### Melihat IP Address
```
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' app-python
```

Contoh hasil:
```
172.19.0.3
```

---

### Melihat Nama Image
```
docker inspect -f '{{.Config.Image}}' app-python
```

Hasil:
```
aryanda/app-python:compose
```

---

### Melihat Status
```
docker inspect -f '{{.State.Status}}' app-python
```

Hasil:
```
running
```

---

### Melihat Working Directory
```
docker inspect -f '{{.Config.WorkingDir}}' app-python
```

Hasil:
```
/app
```

---

### Melihat Hostname

```
docker inspect -f '{{.Config.Hostname}}' app-python
```

---

# Inspect Object Lain
Tidak hanya container.
## Image
```
docker inspect mongo:7
```
Melihat metadata image.

---

## Volume
```
docker inspect mongo_data
```

atau
```
docker volume inspect mongo_data
```
Melihat lokasi penyimpanan volume.

---

## Network
```
docker network inspect python_network
```

Melihat:

- seluruh container yang bergabung
- subnet
- gateway
- driver
- IP masing-masing container

Ini sangat berguna ketika debugging masalah jaringan antar-container.

---

# Docker Inspect vs Docker Logs

Banyak pemula tertukar.
## docker logs

Menjawab:
> Apa yang sedang dilakukan aplikasi?

Misalnya:
```
Connected MongoDB

GET /

POST /login
```

---

## docker inspect
Menjawab:
> Bagaimana container dikonfigurasi?

Misalnya:
```
Image

Volume

Port

Network

IP

Environment
```

Singkatnya:
```
docker logs
```
↓
Aktivitas aplikasi.

```
docker inspect
```
↓
Identitas dan konfigurasi container.

---

# Kapan Menggunakan Docker Inspect?
Gunakan `docker inspect` ketika kamu ingin mengetahui konfigurasi container tanpa harus masuk ke dalamnya. Beberapa contoh kasus:

- Memastikan **Environment Variable** sudah terbaca.
- Mengetahui **IP Address** container.
- Mengecek **network** yang digunakan.
- Memastikan **port mapping** sudah benar.
- Mengetahui apakah container menggunakan **Volume** atau **Bind Mount**.
- Memeriksa **working directory**, image, atau status container.

Dalam praktik sehari-hari, `docker inspect` hampir selalu menjadi pasangan dari `docker logs`. Biasanya urutannya seperti ini:

1. Cek apakah container berjalan:
    ```
    docker ps
    ```
    
2. Lihat log jika aplikasi bermasalah:
    ```
    docker logs app-python
    ```
    
3. Periksa konfigurasi container:
    ```
    docker inspect app-python
    ```
    
4. Jika perlu investigasi lebih dalam, masuk ke container:
    ```
    docker exec -it app-python sh
    ```
    

---

# Ringkasan Perintah Penting

|Perintah|Fungsi|
|---|---|
|`docker inspect app-python`|Menampilkan seluruh metadata container|
|`docker inspect -f '{{.State.Status}}' app-python`|Melihat status container|
|`docker inspect -f '{{.Config.Image}}' app-python`|Menampilkan image yang digunakan|
|`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' app-python`|Menampilkan IP Address container|
|`docker inspect -f '{{.Config.WorkingDir}}' app-python`|Menampilkan working directory|
|`docker network inspect python_network`|Menampilkan informasi jaringan beserta container yang tergabung|
|`docker volume inspect mongo_data`|Menampilkan informasi volume dan lokasi penyimpanannya|

# Kesimpulan
`docker inspect` adalah salah satu perintah paling penting dalam Docker karena menyediakan informasi lengkap mengenai konfigurasi sebuah object Docker, baik itu container, image, volume, maupun network. Dengan perintah ini, kita dapat mengetahui berbagai informasi seperti image yang digunakan, status container, environment variable, port mapping, network, IP address, volume, hingga working directory tanpa harus masuk ke dalam container. Oleh karena itu, `docker inspect` merupakan alat utama untuk melakukan inspeksi dan troubleshooting konfigurasi Docker, sedangkan `docker logs` digunakan untuk melihat aktivitas aplikasi yang sedang berjalan. Menguasai `docker inspect` berarti kamu sudah memiliki kemampuan untuk memahami bagaimana sebuah container dikonfigurasi dan berinteraksi dengan komponen Docker lainnya.