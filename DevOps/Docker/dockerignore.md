#devops 
# Apa itu `.dockerignore`?
`.dockerignore` adalah file konfigurasi yang digunakan untuk memberi tahu Docker file atau folder mana yang **tidak boleh ikut dikirim** ketika proses build image berlangsung.

Konsepnya sebenarnya sangat mirip dengan `.gitignore`. Bedanya, kalau `.gitignore` digunakan agar Git tidak meng-upload file tertentu ke repository, maka `.dockerignore` digunakan agar Docker tidak mengirim file tersebut ke **Build Context** saat menjalankan proses build.

---

# Apa itu Build Context?
Sebelum memahami fungsi `.dockerignore`, kita perlu memahami terlebih dahulu apa itu **Build Context**.

Banyak orang mengira ketika menjalankan perintah berikut, Docker langsung membaca Dockerfile dan mulai membuat image.

```
docker build .
```

Padahal prosesnya tidak seperti itu.

Hal pertama yang dilakukan Docker adalah mengumpulkan **seluruh isi folder project** yang menjadi lokasi build. Seluruh file dan folder tersebut akan dikirim ke Docker Engine terlebih dahulu. Kumpulan file inilah yang disebut **Build Context**.

Sebagai contoh, misalkan project kita memiliki struktur seperti ini.

```
project/
│
├── Dockerfile
├── app.py
├── requirements.txt
├── .env
├── node_modules/
├── .git/
├── README.md
├── logs/
└── test/
```

Saat menjalankan perintah berikut,

```
docker build .
```

Docker akan mengirim **semua isi folder project** tersebut ke Docker Engine, bukan hanya Dockerfile.

Artinya file seperti `.env`, folder `.git`, `node_modules`, folder `logs`, hingga folder `test` semuanya ikut dikirim, meskipun nantinya belum tentu digunakan selama proses build.

---

# Kenapa Ini Menjadi Masalah?
Bayangkan kamu sedang mengembangkan aplikasi React. Folder source code mungkin hanya berukuran beberapa megabyte, tetapi folder `node_modules` bisa mencapai ratusan megabyte bahkan lebih dari 1 GB.

Ketika menjalankan proses build, Docker tetap akan mengirim seluruh folder `node_modules`, padahal di dalam Dockerfile biasanya sudah terdapat perintah untuk meng-install dependency kembali.

```
RUN npm install
```

Artinya folder `node_modules` sebenarnya tidak dibutuhkan selama proses build, tetapi tetap ikut dikirim karena Docker belum diberi tahu untuk mengabaikannya.

Akibatnya proses build menjadi lebih lama, cache build menjadi lebih besar, dan image juga berpotensi membawa file yang sebenarnya tidak diperlukan.

---

# Solusinya
Solusinya adalah membuat file bernama `.dockerignore`.

Misalnya isi filenya hanya seperti berikut.
```
node_modules
```

Sekarang saat menjalankan proses build, Docker akan mengabaikan folder `node_modules`. Build Context menjadi jauh lebih kecil sehingga proses build berlangsung lebih cepat.

---

# Cara Membuat
Cukup buat sebuah file bernama `.dockerignore` di folder yang sama dengan Dockerfile.

Misalnya struktur project menjadi seperti berikut.

```
project/
│
├── Dockerfile
├── .dockerignore
├── app.py
└── requirements.txt
```

Docker akan otomatis membaca file tersebut setiap kali menjalankan `docker build`.

---

# Contoh Isi `.dockerignore`
Isi `.dockerignore` sebenarnya sangat sederhana. Setiap baris mewakili satu file atau satu folder yang ingin diabaikan.

```
node_modules
.git
.env
```

Artinya Docker tidak akan mengirim ketiga item tersebut ke Build Context.

Kita juga bisa menggunakan pola (pattern) seperti pada `.gitignore`.

```
logs/
```
Artinya seluruh isi folder `logs` akan diabaikan.

```
*.log
```
Artinya semua file dengan ekstensi `.log` akan diabaikan.

```
__pycache__/
```
Mengabaikan folder cache Python.

```
*.pyc
```
Mengabaikan seluruh file cache Python.

---

# Kenapa `.env` Harus Di-ignore?
Salah satu file yang hampir selalu dimasukkan ke dalam `.dockerignore` adalah `.env`.

Biasanya file ini berisi konfigurasi penting seperti password database, JWT Secret, API Key, token layanan pihak ketiga, dan berbagai informasi sensitif lainnya.

Contohnya:
```
DB_PASSWORD=123456
JWT_SECRET=xxxxxxxx
API_KEY=xxxxxxxx
```

Kalau file `.env` ikut masuk ke Build Context, lalu image tersebut di-push ke Docker Hub atau registry lain, ada kemungkinan informasi sensitif tersebut ikut terbawa ke dalam image.

Karena itu, praktik yang baik adalah **jangan pernah memasukkan `.env` ke dalam image**. Sebagai gantinya, gunakan Environment Variable saat menjalankan container atau gunakan file `.env` di sisi deployment.

---

# Implementasi Nyata (Project Python)

Misalkan kita memiliki aplikasi Flask sederhana dengan Dockerfile berikut.
```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
```

Kemudian kita membuat `.dockerignore`.
```
# Python Cache
__pycache__/
*.pyc

# Git
.git
.gitignore

# Virtual Environment
venv/

# Secret
.env

# Log
logs/
*.log

# Editor
.vscode/
.idea/

# Testing
tests/
coverage/

# OS
.DS_Store
Thumbs.db

# Documentation
README.md
```

Selanjutnya build image seperti biasa.
```
docker build -t python-demo .
```

Docker hanya akan mengirim file yang benar-benar diperlukan untuk membangun image.

---

# Cara Membuktikan `.dockerignore` Bekerja

Cara paling mudah adalah membuat file dummy yang ukurannya sangat besar.

```
dd if=/dev/zero of=bigfile.bin bs=1M count=500
```

Kemudian lakukan build tanpa `.dockerignore`.

```
docker build .
```

Perhatikan output awalnya.
```
Sending build context to Docker daemon 501MB
```

Sekarang tambahkan file tersebut ke dalam `.dockerignore`.
```
bigfile.bin
```

Lalu build ulang.

```
docker build .
```

Output akan berubah menjadi seperti berikut.
```
Sending build context to Docker daemon 12kB
```

Padahal aplikasi sama sekali tidak berubah. Yang berubah hanyalah jumlah file yang dikirim ke Docker Engine. Ini merupakan cara paling mudah untuk memahami manfaat `.dockerignore` secara langsung.

---

# Kesalahan yang Sering Dilakukan

## Mengabaikan file yang sebenarnya dibutuhkan
Misalnya memasukkan `requirements.txt` ke dalam `.dockerignore`.
```
requirements.txt
```

Padahal Dockerfile membutuhkan file tersebut.
```
RUN pip install -r requirements.txt
```

Akibatnya proses build akan gagal karena Docker tidak pernah menerima file `requirements.txt`.

## Mengira `.dockerignore` mengecilkan image
Ini adalah salah satu kesalahpahaman yang paling sering terjadi.

`.dockerignore` **tidak secara langsung mengecilkan ukuran image**. Yang sebenarnya diperkecil adalah **Build Context**.

Ukuran image baru akan ikut mengecil jika file yang sebelumnya ikut disalin melalui `COPY . .` kini sudah tidak lagi dikirim ke Docker Engine.

## Tetap menggunakan `COPY . .` tanpa berpikir
Perintah berikut memang praktis.

```
COPY . .
```

Namun jika `.dockerignore` tidak disusun dengan baik, maka semua file yang tidak diabaikan tetap akan ikut masuk ke image. Oleh karena itu, `.dockerignore` dan `COPY . .` selalu berjalan beriringan.

---

# Best Practice
Untuk project Python, umumnya `.dockerignore` berisi:

```
__pycache__/
*.pyc
.env
.git
.vscode/
.idea/
logs/
tests/
coverage/
README.md
```

Untuk project Node.js, biasanya ditambahkan:
```
node_modules/
npm-debug.log
yarn-error.log
```

Sedangkan pada project Laravel biasanya ditambahkan:
```
vendor/
node_modules/
storage/logs/
.env
.git
```

---

# Ringkasan

|Tanpa `.dockerignore`|Dengan `.dockerignore`|
|---|---|
|Build Context besar|Build Context lebih kecil|
|Build lebih lambat|Build lebih cepat|
|Risiko file sensitif ikut terkirim|File sensitif dapat dikecualikan|
|Cache build lebih besar|Cache lebih efisien|
|Image dapat membawa file yang tidak diperlukan|Image lebih bersih dan optimal|

# Kesimpulan
`.dockerignore` berfungsi untuk mengontrol **Build Context**, yaitu kumpulan file yang dikirim Docker ke Docker Engine sebelum proses build dimulai. Dengan mengecualikan file dan folder yang tidak diperlukan, proses build menjadi lebih cepat, penggunaan cache menjadi lebih efisien, dan risiko membawa file sensitif seperti `.env`, `.git`, atau file log ke dalam image dapat dihindari. Walaupun hanya berupa satu file kecil, `.dockerignore` merupakan salah satu praktik terbaik yang hampir selalu digunakan dalam pengembangan aplikasi menggunakan Docker karena membantu menghasilkan image yang lebih aman, lebih bersih, dan lebih efisien.