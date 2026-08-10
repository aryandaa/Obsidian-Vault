#devops 
Apa itu Container Registry? container registry adalah tempat yang digunakan untuk menyimpan Image, saat kita membuat Image maka akan di simpan di dalam Registry Ini, sebelum di deploy tiap server dockernya.

Kenapa tidak langsung simpan ke servernya saja dan harus ke registry dulu? karena pada saat di prodoction kita tidak mungkin akan menginstall 1 node/server saja pada sebuah docker, dan pasti akan menginstallnya sekaligus banyak, dan kalo kita memasukan imagenya ke dalam banyak server pasti akan sangat ribet, kita cukup install di 1 registry nanti docker server production yang akan mengambil data dari registry ini, dan akan bisa dipakai untuk berulang kali. 

Fungsi lain yaitu untuk share Image antar Developer tanpa perlu menginstall/membuat ulang dari Registry itu.

contoh beberapa Platform Registry untuk docker:
![](Pasted%20image%2020260723194804.png)
Docker Hub adalah Registry bawaan dari docker itu sendiri, di docker hub ini untuk yang open source itu gratis dan untuk private berbayar.

Google container registry itu bagian dari google cloud, jadi jika ingin deploy ke google cloud bisa menggunakan registry itu, dan begitupula dengan AWS elastic container registry.

