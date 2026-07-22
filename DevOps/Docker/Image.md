#devops 
Saat aplikasi kita bundle dalam Docker atau saat dibikin package nya, maka dia akan menjadi sebuah Image, jadi Image di Docker itu adalah hasil distribution file dari aplikasi kita.
image ini yang akan di deploy ke dalam Registry, dan image ini adalah aplikasi yang sudah jadi, jika di running maka sudah bisa jalan.

Image dalam bahasa sederhananya adalah **template yang bersifat read-only**.
Di dalamnya terdapat:
- Operating system minimal (Alpine, Ubuntu, Debian, dll.)
- Software
- Library
- Dependency
- Konfigurasi
- Source code (kadang)

![](img/Pasted%20image%2020260722210604.png)
di dalam docker itu sendiri hampir menyediakan semua Image yang Open source yang populer, jadi kita tidak perlu lagi membuat ulang image itu dari 0 untuk beberapa sistem. 
bahkan di docker sendiri itu bisa support multiversion, atau kita bisa menggunakan banyak versi di 1 image misalnya jika kita ingin menggunakan versi berapapun tinggal sebutkan saja tags nya.

misalnya image python ini:
![](img/Pasted%20image%2020260722214601.png)

Contohnya Image Laravel berisi:
```
Ubuntu
PHP 8.4
Composer
Laravel
Extensions PHP
Config PHP
```
	Semua sudah dibungkus menjadi satu.