#devops
# Membuat Container
1. untuk melihat daftar container yang ada di local kita yang sedang berjalan (running), bisa menggunakan perintah
```shell
docker container ls
```
karna masih kosong maka outputnya adalah
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

2. dan untuk melihat container yang ada di local walaupun sedang tidak jalan bisa menggunakan perintah
```shell
docker container ls --all
```
artinya dia akan menampilkan semua container yang running maupun tidak.
karna belum ada 1 pun container dilaptopku maka hasilnya sama seperti diatas itu.

3. dan sekarang akan membuat container dari image yang diinstall dari docker hub tadi:
```shell
docker container create <image>:tag
```

4. secara default docker akan memberikan random name terhadap container tersebut, dan bisa menyulitkan kalo mau menjalankan containernya karna kita harus menyebutkan nama dari container itu.

agar tidak random name, kita bisa menambahkan nama container:
```shell
docker container create --name FirstContainer <image>:tag
```

5. seperti yang sudah di jelaskan sebelumnya kalo kita bisa membuat lebih dari 1 container dari 1 image, tapi kita tidak bisa menggunakan nama yang sama, karena nama di container ini bersifat uniqe atau tidak boleh sama dengan yang lain. 

# Menjalankan Container
1. Aku sudah membuat docker containernya, sekarang akan menjalankannya dengan perintah:
```docker
docker container start FirstContainer
```
"FirstContainer" disitu adalah nama dari container yang ingin dijalankan itu, 
kalo terminal memanggil nama containernya itu berarti sukses berjalan.

2. untuk memastikan container itu sudah jalan atau belum, gunakan perintah:
```shell
docker container ls
```
kalo ada namanya berarti sudah fix jalan

sekarang containernya sudah bisa digunakan.

# Menghapus Container
untuk menghapus container cukup jalankan command ini:
```shell
docker container rm <NamaContainer> 
atau
docker container rm FirstContainer
```

tapi kita tidak bisa menghapus container yang sedang running, jadi sebelum menghapus, pastikan containernya itu sudah dimatikan dulu, gimana caranya mematikannya, gunakan perintah:
```shell
docker container stop <NamaContainer>
```
atau kita bisa mematikan sekaligus banyak seperti:
```shell
docker container stop <NamaContainer1>, <NamaContainer2>, <NamaContainer3>, ...
```

jika sudah di stop/matikan, maka container itu sudah bisa dihapus dengan perintah tadi:
```shell
docker container rm <NamaContainer>
```
bisa sekaligus banyak dengan dipisahkan koma.

>Jangan khawatir saat menghapus container, image yang sudah di install tadi akan tetap ada.

# Membuka Port Container
Container yang sudah di jalankan itu belum bisa dipakai untuk luar platform karena itu hanya bisa dipakai di dalam dockernya saja, gimana agar bisa untuk dipakai diluar juga? 
export port nya atau dibuka terlebih dahulu.

perintahnya kurang lebih sama seperti saat menjalankan, tetapi ada sedikit tambahan untuk bisa diakses dari luar, yaitu:
```shell
docker container create --name FirstContainer -p 8080:27017 <NamaImage>:tag
```
27017 = port internal container.
8080 = port untuk bisa diakses dari luar.

Saat kita membuat container yang lain, kita tidak boleh meletakan port yang sama dengan yang sudah ada untuk port akses keluarnya, contoh:
```shell
docker container create --name SecondContainer -p 8181:27017 <NamaImage>:tag
```
kenapa harus berbeda? supaya portnya tidak bentrok dengan yang sudah ada.
tetapi untuk port internal containernya tetap sama.

dan sekarang kita bisa connect ke platform docker client nya menggunakan port public itu.


