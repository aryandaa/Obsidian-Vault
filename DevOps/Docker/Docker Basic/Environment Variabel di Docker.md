#devops 
Saat mengembangkan aplikasi, kita biasanya juga membuat konfigurasi, baik dalam bentuk file maupun database.

Namun, konfigurasi yang baik adalah konfigurasi yang **tidak di-hardcode di dalam aplikasi**, melainkan dapat diatur dari luar. Dengan begitu, ketika aplikasi sudah dibungkus menjadi Docker Image, kita tidak perlu membangun ulang image hanya untuk mengubah konfigurasi.

Docker memungkinkan kita menyuntikkan konfigurasi melalui **Environment Variables** saat container dijalankan. Dengan cara ini, image yang sama dapat digunakan di berbagai environment, seperti **development, staging, maupun production**, tanpa perlu mengubah source code atau isi image. Cukup sesuaikan nilai environment variable pada masing-masing environment.

terus gimana caranya bikin agar docker image support Environment Variabel?
disini sudah ada Dockerfile untuk aplikasi Java
![](Pasted%20image%2020260725165418.png)
disini tidak menyetting Environment Variabelnya karena EV akan di setting saat membuat Containernya. 

Untuk step pembuatan image sama seperti sebelumnya, bedanya saat pembuatan container kita harus menambahkan sedikit perintah untuk menset env nya saat docker container create:
`-e <NamaEnv> = <ValueEnv>`, misalnya
`-e NAME=Docker`
atau perintah lengkapnya
```shell
docker container create --name java-docker -p 8080:8080 -e NAME=Docker Java-docker:1.0
```

untuk memastikan apakah Environment Variabel sudah masuk ke containernya bisa gunakan perintah:
`docker container inspect <NamaCOntainer>`
dan cari apakah ada bagian bertulisan:
```
"ENV": [
	"NAME=Docker",
	...
]
```
jika ada berarti berhasil menambahkan ENV ke containernya.

jika kita butuh lebih dari 1 settingan ENV, tinggal tambahkan saja -e nya saat di create:
`-e NAME=Docker -e App=Java`

Lalu gimana caranya agar menambahkan EV ketika imagenya sudah dibuat? 
kita bisa merunnya dengan EV tambahan, misalnya:
```shell
docker run \
-e NAME=Docker \ 
-e App=Java \
-e DB_HOST=localhost \
-e DB_USER=root \
aryanda/app-golang:1.0
```
jadi ketika di jalankan itu, containernya otomatis akan menyesuaikan settingan ENV sesuai dengan command kita.

dan jika di run containernya, sistemnya sudah Sync dengan ENV kita.

saya akan melakukan praktek Environment Variabel di sini [Praktek Environment Variabel](Praktek%20Environment%20Variabel.md)
