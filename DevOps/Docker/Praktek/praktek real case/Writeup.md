## Task 1:
App.py:
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

except Exception as e:
	STATUS = f"🔴 MongoDB Disconnected <br><pre>{e}</pre>"

@app.route("/")
def home():
	return f"""
	<h1>Halo, {NAMA}</h1>
	<h2>{STATUS}</h2>
	"""

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
```

requirements.txt
```requirements.txt
Flask==3.1.1
pymongo==4.13.2
```


## Task 2:
Dockerfile:
```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
```

Build Image:
```shell
docker build -t aryanda/app-python:Task1 .
```

## Task 3:
Menjalankan Aplikasi
```shell
docker run -p 8080:5000 aryanda/app-python:Task1
```

```output
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [27/Jul/2026 12:57:00] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [27/Jul/2026 12:57:00] "GET /favicon.ico HTTP/1.1" 404 -
```

disini aplikasi sudah bisa jalan tapi belum bisa connect ke database maupun membaca environment variable.

## Task 4:
Menambahkan Environment Variable:
```shell
docker run -p 8080:5000 -e NAMA=Aryanda aryanda/app-python:Task1
```
Disini sudah bisa terhubung ke Environment Variable dengan bukti yang tadinya "Hello Guest" berganti jadi "Hello, Aryanda"

## Task 5:
Upload Image ke docker hub:
```shell 
docker push aryanda/app-python:Task1
```

disini sudah terupload dengan bukti output terminal ini:
```output
The push refers to repository [docker.io/aryanda/app-python]
062e450697fa: Layer already exists 
cd384decb927: Layer already exists 
9b72b5d0a7ee: Pushed 
bbc13f65c98a: Pushed 
463aa101532a: Layer already exists 
11125ac2c05d: Layer already exists 
f752edffc531: Pushed 
4a633c382b06: Layer already exists 
Task1: digest: sha256:589fe3c5ecd534c06df677ecac1158625278ef293713a01e671f45492c6a9bcf size: 856
```

dan jika aku hapus imagenya menggunakan perintah
`docker image rm aryanda/app-python:Task1`
lalu aku pull kembali dengan perintah:
`docker pull aryanda/app-python:Task1`
maka saya akan mendapatkan image yang sama seperti yang sudah dibuat diatas.

## Task 6:
Buat container Mongodb include dengan username dan passwordnya:
`docker run -d --name mongodb -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=123456 mongo:7 `

outputnya mengeluarkan Ascii random:
`3c0363e4e0e4f7b076306c16b91d0a38b87cd230a1084eb436817388e95a3e67`
yang berhasil untuk membuat container mongodb nya itu.

## Task 7:
Buat network:
`docker network create Real-Case`

jika saya cek menggunakan `docker network create ls`, maka akan muncul:
`98cc8e59326c   Real-Case         bridge    local`
yang berarti berhasil membuat network nya.

lalu saya hubungkan kedua container yang sudah saya buat sebelumnya dengan menggunakan flag `connect`:
`docker network connect Real-Case mongodb`
`docker network connect Real-Case app-python`

Jika diketikan perintah `docker inspect Real-Case`, maka akan muncul 2 Containers itu.

