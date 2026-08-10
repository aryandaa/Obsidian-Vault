#devops 
Sekarang saya akan mencoba untuk menghubungkan 2 atau lebih container yang berbeda ke dalam 1 aplikasi utuh, misalnya saya mempunyai container aplikasi dan container.
dan gimana caranya menghubungkan container aplikasi jadi mempunyai database yang berasal dari container berbeda?

Saya akan membuat container databasenya terlebih dahulu dan untuk aplikasinya saya akan memakai aplikasi python yang kemaren saja.

1. pertama saya akan membuat structure foldernya seperti ini:
```
database/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── .env
```

requirements.txt:
```txt
Flask==3.1.1
pymongo==4.13.2
```
ini berisi library dari python yang perlu di install lewat dockernya.

app.py:
```python
from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

NAMA = os.getenv("NAMA", "Guest")

DB_HOST = os.getenv("DB_HOST", "mongodb")
DB_PORT = int(os.getenv("DB_PORT", "27017"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "123456")

try:
    client = MongoClient(
        f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/",
        serverSelectionTimeoutMS=3000
    )

    client.admin.command("ping")
    STATUS = "🟢 MongoDB Connected"

except Exception:
    STATUS = "🔴 MongoDB Disconnected"


@app.route("/")
def home():
    return f"""
    <h1>Halo, {NAMA}</h1>
    <h2>{STATUS}</h2>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
code python ini sudah bisa terintegrasi dengan mongo db dan yang dilakukan aplikasi:
- mengambil nama dari Environment Variable
- mengambil host database dari Environment Variable
- mencoba koneksi
- melakukan `ping`
- menampilkan status koneksi

Dockerfile:
```Dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
```

.env:
```env
NAMA=Yanda

DB_HOST=mongodb
DB_PORT=27017

DB_USER=root
DB_PASS=123456
```
semua nama di env sini harus sama dengan settingan di container yang ingin di hubungkan. contohnya disini saya memakai db_host nya adalah mongodb dan port nya 27017 agar menyesuaikan dengan container mongodb nya.

Sekarang semua file sudah siap, dan saya pertama akan membuat imagenya dari semua file itu:
`docker build -t aryanda/app-python:network .`

lalu mempushnya ke repository yang sama dengan yang kemaren, yang membedakan cuman di tag:
`docker push aryanda/app-python:network`

Disinilah pembedanya, saya akan membuat network untuk Container ini, dengan cara:
`docker network create belajar-network`
sekarang sudah ada
```output
NETWORK ID     NAME              DRIVER    SCOPE
4de41eaa829f   belajar-network   bridge    local
```

lalu saat run saya menambahkan --network agar container tersebut connect ke network yang sudah dibuat tadi:
`docker run -d --name mongodb --network belajar-network -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=123456 mongo:latest`

sekarang saya akan pull image mongodb nya:
![](Pasted%20image%2020260726172514.png)

```shell
docker run -d \
--name mongodb \
--network belajar-network \
-e MONGO_INITDB_ROOT_USERNAME=root \
-e MONGO_INITDB_ROOT_PASSWORD=123456 \
mongo:7
```

--name = nama databasenya.
-network = nama network nya agar bisa terhubung ke aplikasi.
-e MONGO_INITDB_ROOT_USERNAME = username database.
-e MONGO_INITDB_ROOT_PASSWORD = password database.

Pertanyaannya kenapa saya bisa langsung run tanpa pull terlebih dahulu? karena **`docker run` akan otomatis melakukan `docker pull` jika image yang diminta belum ada di lokal.**

dan alurnya seperti ini
```
docker run mongo:7
        │
        ▼
Apakah image ada di lokal?
        │
   ┌────┴────┐
   │         │
  Ada      Tidak Ada
   │         │
   ▼         ▼
 Langsung   docker pull
 dijalankan     │
                ▼
          Image berhasil di-download?
                │
           ┌────┴────┐
           │         │
         Ya        Tidak
           │         │
           ▼         ▼
     Jalankan     Error
     container
```

dan jika di cek dengan `docker ps`, maka akan muncul databasenya:
```output
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS       NAMES
25a948fe9a50   mongo:7   "docker-entrypoint.s…"   18 seconds ago   Up 17 seconds   27017/tcp   mongodb
```

sekarang image database sudah run, sekarang saya akan menjalankan image aplikasinya dengan perintah:
```shell
docker run -d \
--name app-python \
--network belajar-network \
-p 8080:5000 \
--env-file .env \
aryanda/app-python:network
```
disini sama, saya juga menambahkan --network untuk memasukan container aplikasi ke dalam network itu.

sekarang crosscheck apakah apakah container berjalan di network yang sama dengan:
`docker network inspect belajar-network`

dan cari di bagian "Container: { ... }", jika ada keduanya maka berhasil, disini punya saya ada keduanya.
```output
"Containers": {
            "829641d61580e2c5bc73d10ff9a7a1559332650dbf38781c9fa6ba500b1ddc6c": {
                "Name": "app-python",
                "EndpointID": "4300d713b0e9a4d15b8e4e1e9b251f42c00ef8a60fdca7916349919717664b36",
                "MacAddress": "02:1e:3c:db:64:7a",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            },
            "b1fa9368bd2e96261e0086079286020a821f6caf2db59d0f71bf86f0767ae1a9": {
                "Name": "mongodb",
                "EndpointID": "616a6900e15b177930a140271c1ccf1fbe4dfbef66ca96dcd3ce4376f237778e",
                "MacAddress": "9a:5b:4b:89:c9:81",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
```

dan ketika dibuka aplikasinya maka akan berhasil connect:
![](Pasted%20image%2020260726203051.png)


> Jika km lupa untuk menambahkan --network ketika nge run container, km bisa menconnect-kannya di akhir dengan cara
> `docker network connect <NamaContainer>`
