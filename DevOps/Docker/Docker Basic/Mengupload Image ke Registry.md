#devops 
1. sekarang saya akan mencoba mengupload image yang sudah dibuat sebelumnya ke dalam Registry Docker Hub, pertama buka link https://hub.docker.com/repositories/

![](img/Pasted%20image%2020260725151542.png)
Disini untuk upload image kita butuh membuat repositorynya, dengan memencet create a Repository. 
![](Pasted%20image%2020260725151849.png)
Yang harus di inputkan adalah:
1. Nama Repository, misalnya app-golang (Nama repo harus sama kaya nama image).
2. Deskripsi Optional.
3. Atur Visibility Public = bisa dilihat oleh orang lain, Private = hanya bisa dilihat oleh diri sendiri saja.
4. Dan pencet Create.
![](img/Pasted%20image%2020260725155925.png)
dan reponya sudah terbuat.

5. Lalu gimana caranya kita upload Image yang sudah dibuat ke Repository Docker Hub ini?
Simple saja kita cukup push Docker Commands yang ada di pojok atas kanan.

saat kita push
```shell
┌─[r3x@parrot]─[~]  
└──╼ $docker push aryanda/app-golang:1.0  
The push refers to repository [docker.io/aryanda/app-golang]  
tag does not exist: aryanda/app-golang:1.0
```
disitu terdapat error
```
The push refers to repository [docker.io/aryanda/app-golang]  
tag does not exist: aryanda/app-golang:1.0
```

 6. karna imaga yang ada di local kita belum di kenalkan ke repository itu, gimana caranya mengenalkan?
kirim perintah in:
`docker tag app-golang:1.0 aryanda/app-golang:1.0`
kalo kita cek `docker images`, maka kan muncul nama repository nya:
```shell
┌─[r3x@parrot]─[~]  
└──╼ $docker images  
IMAGE                    ID             DISK USAGE   CONTENT SIZE   EXTRA  
app-golang:1.0           c67a1d2dbe20        438MB          107MB    U  
aryanda/app-golang:1.0   c67a1d2dbe20        438MB          107MB    U
```

7. Tapi saat kita mencoba ngepush lagi,
`docker push aryanda/app-golang:1.0`
disitu terdapat error lagi yaitu:
`push access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed`
karena si repo docker hub ini belum mengetahui identitas kita sehingga jadi access denied. 

yang harus kita lakukan adalah kita harus login dulu ke Registry Docker Hub itu lewat terminal dengan cara:
`Docker login`
otomatis terminal akan mengirimkan link dan code OTP nya
```output
  
USING WEB-BASED LOGIN  
  
i Info → To sign in with credentials on the command line, use 'docker login -u <username>'  
  
  
Your one-time device confirmation code is: ****-**** 
Press ENTER to open your browser or submit your device code here: https://login.docker.com/activate  
  
Waiting for authentication in the browser…
```

8. sekarang docker sudah mengetahui identitas terminal kita dan sudah bisa ngepush lagi:
![](img/Pasted%20image%2020260725162127.png)

![](img/Pasted%20image%2020260725163300.png)
dan image kita sudah ada di registry nya, jadi kalo orang lain ingin mengambil Projectnya tinggal gunakan perintah
`docker pull aryanda/app-golang:tagname`