#devops 
Sebelumnya untuk mendapatkan image harus mendownload langsung lewat registry nya, sekarang belajar untuk membuat image kita sendiri, untuk membuat image di docker kita butuh 1 file bernama Dockerfile.

1. bisa buka text editor, seperti vscode.

![](Pasted%20image%2020260724212703.png)
disini saya sudah menyiapkan 1 code go sederhana untuk web yang cuman menampilkan "Hello World!"
![](Pasted%20image%2020260724213112.png)

2. Lalu dibawahnya saya akan menambahkan 1 file bernama "Dockerfile",
yang perlu di highlight adalah, para developer sangat jarang sekali membuat image dari kosongan, biasanya mereka akan menggunakan image yang sudah ada ke image yang akan dibuat.

sebagai contoh, disini saya akan membuat aplikasi golang, dibandingkan membuat image manual dari 0 akan sangat ribet sekali, lebih baik saya akan memakai image golang yang sudah di siapkan di registry Docker Hub. 
![](Pasted%20image%2020260724213806.png)

3. jika ingin menggunakan Image itu, kita bisa tambahkan ini di Dockerfile nya
```Dockerfile
FROM golang:tip-alpine3.23
```
yang akan kita lakukan adalah membuild image dari image yang sudah ada yaitu golang. 

4. selanjutnya adalah kita harus mengcopy semua file aplikasi kita dimasukan ke dalam image nya dengan cara:
```Dockerfile
COPY main.go /app/main.go
```
`/app/main.go` adalah alamat directori yang ingin kita copy file nya 

5. tahapan terakhir yang dilakukan setelah mengambil semua file aplikasi, kita akan memberitahu ke image gimana cara running si aplikasi ini.
karna saya menggunakan go maka cara runningnya adalah dengan cara 
`go run <nama file>`,  maka perintah itulah yang diketikan di Docker file:
```Dockerfile
CMD ["go", "run", "/app/main.go"]
```
`CMD` adalah syntax agar si dockerfile nya tau kalo perintah setelahnya akan dikirimkan ke terminal command.
`["go", "run", "main.go"]` adalah command yang akan dikirim, dengan dipisah dengan array.
kenapa menggunakan `"/app/main.go"` bukan `main.go` nya langsung? karena di sintak atas kita sudah mencopy semua aplikasi ke dalam directory `/app`.

dan ini adalah code full Dockerfile nya:
```Dockerfile
FROM golang:tip-alpine3.23

COPY main.go /app/main.go

CMD ["go", "run", "/app/main.go"]
```

6. sekarang saya akan mencoba membuild image dari dockerfile yang sudah dibuat itu, cara ngebuildnya cukup gampang, cukup gunakan perintah:
```shell
docker build --tag <NamaApp>:<tag> <Directory Dockerfile>
```
`--tag <NamaApp>:<tag>` adalah nama aplikasi yang ingin dibuat dan tag itu adalah versi dari aplikasinya, misalnya "app-golang:1.0" atau jika ada update jadi "app-golang:1.1".

`<Directory Dockerfile>` di isi dengan letak directori dari Dockerfile tersebut, jika terminal sudah berada di directori yang sama, cukup tambahkan titik "." saja.

contoh perintah finalnya:
```shell
docker build --tag app-golang:1.0 .
```

7. kirim dan tunggu sampai selesai,
![](Pasted%20image%2020260724220551.png)

step dari prosessnya itu sesuai dengan isi dari Dockerfile, yaitu:
1. Installasi Image
2. Copy aplikasi ke /app/main.go
3. Dan menjalankan command` "CMD ["go", "run", "/app/main.go"]"`

jika kita cek dengan perintah `docker images` di terminal, maka disitu akan muncul image buatan kita tadi
```output
IMAGE            ID             DISK USAGE   CONTENT SIZE   EXTRA
app-golang:1.0   c67a1d2dbe20        438MB          107MB        
```

8. sekarang saya akan membuat container dari image yang sudah dibuat diatas, dengan perintah 
```shell
docker container create --name app1 -p 8080:8080 app-golang:1.0
```
jika di cek `Docker container ls --all`, maka akan muncul nama container app1 

9. lalu jalankan container itu dengan perintah
```shell
docker container start app1
```

10. jika kita buka di browser dengan port 8080, maka webnya berhasil muncul:
![](Pasted%20image%2020260724221824.png)
Yang artinya kita berhasil membuat image kita sendiri, dan membuatkan containernya. 