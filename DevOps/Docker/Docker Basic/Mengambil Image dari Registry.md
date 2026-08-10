#devops 
untuk melihat daftar imaga yang ada di lokal computer, kita bisa menjalankan perintah
```bash
docker images
```
nanti outputnya akan seperti ini:
```Output
IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTRA
```
karna masih kosong maka tidak akan menampilkan apapun kecuali judulnya.

maka dari itu kita akan menginstall image dari https://hub.docker.com/
![](Pasted%20image%2020260723211422.png)
dari yang sudah di jelaskan disebelumnya kalo docker hub banyak menyediakan image open source yang sudah jadi, jadi kita tidak perlu membuatnya dari awal lagi, cukup mempull dari situ saja.

Misalnya aku ingin mendownload Image python, tinggal ke searchbar nya saja lalu cari "python" dan pencet card nya.
di dalam situ sudah banyak sekali informasi, salah satunya ada section untuk mempull
![](Pasted%20image%2020260723211831.png)
perintah diatas itu tinggal salin saja ke dalam terminal docker tadi, dan otomatis akan menginstall imagenya.
```output
IMAGE         ID             DISK USAGE   CONTENT SIZE   EXTRA  
python:3.13   6968f3db2567       1.62GB          430MB
```
dan muncul image yang kita install tadi.

secara default jika kita menginstall hanya dengan mengetikan
```shell
docker pull <image>
```
tanpa menyebutkan versi, maka akan terinstall versi latest atau paling terbaru,

tapi lebih baik jika kita menyebutkan versi yang spesifiknya seperti:
```shell
docker pull <image>:versi
```
dengan begitu jika ada update, aplikasi kita akan menggunakan versi itu secara terus menerus tanpa ada perubahan versi di imagenya yang mengakibatkan ribet pada saat mengupdatenya.