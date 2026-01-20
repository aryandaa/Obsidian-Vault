#programming 
sebuah syntax yang mengatur alignment untuk penulisan string yang mendatar di python, jadi kita tidak perlu lagi manual menggunakan spasi atau tab yang banyak untuk merapikan perlistnya, cukup menggunakan 1 syntax tambahan saja.
contoh saya mempunyai variable:
```python
nama = "yanda"
umur = "19"
berat = 56
tinggi = 160
sepatu = 31
```

biasanya kita menulis string dengan cara
```python
data_string = f"nama = {nama}, umur = {umur}, berat badan = {berat}, tinggi badan = {tinggi}, ukuran sepatu = {sepatu}"
```
ini bisa, tapi susah untuk dibaca karena tergabung semua di dalam 1 baris..

gimana dengan multiline?
```python
data_string = f"nama = {nama}, \numur = {umur}, \nberat badan = {berat}, \ntinggi badan = {tinggi}, \nukuran sepatu = {sepatu}"
```
output:
```
nama = yanda,
umur = 19,
berat badan = 56,
tinggi badan = 160,
ukuran sepatu = 31
```
ini better dari sebelumnya, tapi masih ada kekurangan yaitu ketika maintence program, code pemanggilnya menjadi 1 baris akan susah untuk dibaca.


jadi untuk mengatasi masalah itu semua, di dalam python kita bisa menyediakan yang namanya alignment, untuk merapikan pemanggilan maupun output yang keluar ketika di run, dengan menggunakan kutip triplets:

contoh belum menggunakan alignment:
```python
data_string = f"""
nama = {nama}
umur = {umur}
berat badan = {berat}
tinggi badan = {tinggi}
ukuran sepatu = {sepatu}
"""
```
output:
```
nama = yanda
umur = 19
berat badan = 56
tinggi badan = 160
ukuran sepatu = 31
```

ketika sudah menggunakan alignment;
```python
data_string = f"""
Nama            = {nama:>5}
Umur            = {umur:>5}
Berat Badan     = {berat:>5}
Tinggi Badan    = {tinggi:>5}
Ukuran Sepatu   = {sepatu:>5}
```
output:
```
Nama            = yanda
Umur            =    19
Berat Badan     =    56
Tinggi Badan    =   160
Ukuran Sepatu   =    31
```
outputnya lebih rapi dan penulisan codenya juga clean, jadi mudah untuk di maintence.

apa fungsi :>5 pada sesudah variable? 
:>5 adalah sebuah formating yang digunakan untuk menggeser isi data agar sejajar dengan atas bawahnya, jika tidak menggunakan itu, maka output yang keluar akan seperti ini:
```
Nama            = yanda
Umur            = 19
Berat Badan     = 56
Tinggi Badan    = 160
Ukuran Sepatu   = 31
```
