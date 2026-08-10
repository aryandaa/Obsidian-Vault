#devops 
pertama saya sudah menyiapkan 1 file aplikasi web dengan bahasa python sederhana untuk menampilkan nama:
```python
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
	nama = os.getenv("NAMA", "Guest")
	return f"<h1>Halo, {nama} 👋</h1>"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
```
Default nya adalah "Guest".
![](img/Pasted%20image%2020260726152035.png)

disini saya juga menambahkan 1 file tambahkan yaitu requirements.txt untuk meletakan semua library python yang di perlukan untuk menjalankan aplikasi tersebut, isinya cuman 1 yaitu:
`Flask==3.1.1`

dan sudah menyiapkan Dockerfile nya juga
```Dockefile
FROM python:3.13-slim

WORKDIR /app

COPY . .  

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
```
disini ada sedikit tambahan yaitu sintak untuk menginstall component yang ada di dalam requirements.txt dengan cara `RUN pip install --no-cache-dir -r requirements.txt`.

langsung saja saya eksekusi 2 file ini.

1. Pertama saya membangun Docker Image dari source code menggunakan Dockerfile. Seluruh dependency akan dipasang selama proses build sehingga image yang dihasilkan sudah siap dijalankan pada komputer mana pun yang memiliki Docker.

`docker build --tag aryanda/app-python .`
```output
IMAGE                       ID             DISK USAGE   CONTENT SIZE   EXTRA  
aryanda/app-python:latest   edd2603d3760        174MB           43MB
```

2. saya akan tes tanpa Environment Variabel terlebih dahulu
`docker run -p 8080:5000 aryanda/app-python:latest`
Dan bisa, cuman karena belum di tambahkan Environment Variabel, jadi namanya masih "Guest".

3. Dan saya menjalankan dengan menggunakan Environment Variable:
`docker run -p 8080:5000 -e NAMA=Yanda aryanda/app-python:latest`
![](imf/Pasted%20image%2020260726160109.png)

Ini adalah jika kita mengatur Environment dari luar, gimana caranya mengatur ENV dari dalam dan menjalankannya?
1. Tambahkan file .env di dalamnya yang berisi
`NAMA=Aryanda`

2. lalu run
`docker run -p 8080:5000 --env-file .env aryanda/python-env-demo:1.0`
dan hasilnya akan `Halo, Aryanda`.

Sekarang saya akan mencoba untuk menguploadnya ke dalam Docker Hub Repository,
1. Membuat Repository nya terlebih dahulu.
![](img/Pasted%20image%2020260726161018.png)
2. Terus akan saya Push image yang sudah dibuat tadi ke dalam Repo ini
`docker push aryanda/app-python:latest`
![](img/Pasted%20image%2020260726161212.png)karena sudah login sebelumnya jadi tidak perlu lagi saya mengenalkan terminal ke docker hub, dan tinggal push saja. 

dan jika orang lain ingin mengambil project kita tinggal ambil saja dengan perintah:
`docker pull aryanda/app-python:latest`.

akan saya coba itu:
1. saya menghapus semua Container dan image terlebih dahulu seolah olah tidak ada dan masih kosong:
```shell
┌─[r3x@parrot]─[~/Documents/Obsidian-Vault/DevOps/Docker/Praktek/python]
└──╼ $docker images
IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTRA
┌─[r3x@parrot]─[~/Documents/Obsidian-Vault/DevOps/Docker/Praktek/python]
└──╼ $docker container ls --all
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

2. akan saya pull dengan command diatas
`docker pull aryanda/app-python:latest `
```Output
latest: Pulling from aryanda/app-python
11125ac2c05d: Pull complete 
2b2c3e7d764f: Pull complete 
4d64b62063f6: Pull complete 
d14982accb7f: Download complete 
Digest: sha256:de4ebe1f51cf11eace50599dcd9fe288a5cb129339a2eccbe6143c5384eec412
Status: Downloaded newer image for aryanda/app-python:latest
docker.io/aryanda/app-python:latest
```

dan saya jalankan
`Docker run aryanda/app-python:latest`
```output
┌─[r3x@parrot]─[~/Documents/Obsidian-Vault/DevOps/Docker/Praktek/python]
└──╼ $docker run aryanda/app-python:latest 
 * Serving Flask app 'app'
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
```

dan sekarang semua orang bisa menjalankan Image ini.

jika orang ingin menyesuaikan dengan Environment Variable nya sendiri, bisa tambahkan -e seperti biasanya:
`docker run -e NAMA=aryanda aryanda/app-python:latest`

