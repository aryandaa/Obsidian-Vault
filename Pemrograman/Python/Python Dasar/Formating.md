#programming 
di dalam python ada yang namanya formating untuk memudahkan dalam penulisan code.
syntax formating yang paling umum ialah f"", dengan cara penggunaan:
```python
namadepan = "Muhammad"
namatengah = "aryanda"
namabelakang = "sanggadiennata"
tahunlahir = 1945
```

dengan formating kita bisa menggabungkan teks biasa dengan variable type data apapun
```python
teks = f"nama depan saya {namadepan}, nama tengah saya {namatengah}, nama belakang saya {namabelakang}, dan saya lahir pada tahun {tahunlahir}"
```

di dalam python juga menyediakan format untuk penulisan angka yang dipisah oleh koma, cocok digunakan untuk penulisan mata uang dengan format ribuan, ratusan maupun jutaan.
```python
uang = 2000000000
print(f"uang = {uang:,} \n")
```
dengan menambahkan :, ketika memanggil variable tersebut.

dan ada formating yang digunakan untuk penulisan float, `:.2f`, 
output yang keluar jika float diberikan formating itu ketika dipanggil adalah mengeluarkan 2 angka setelah koma, dan membulatkan angka terakhirnya, contoh:
```python
x = 2.678
print(f"{x:.2f}")
```
output yang keluar adalah `2.68`, kenapa 2.68? bukan 2.67, kan di belakang koma?...
karena pembulatan dari 78. 

dan lebih banyak lagi trik memformat seperti ini
`:+d` menampilkan minus - di sebelah kiri angka
`:+` menampilkan plus
`:%` menampilkan persentase
`:0` menampilkan angka tanpa koma

Dalam Python Cryptography juga ada formating yang dikhususkan untuk cryptography, yaitu untuk menulis binary, octal, hexa

```python
angka = 192006

binary = f"binary = {bin(angka)}"
octal = f"octal = {oct(angka)}"
hexa = f"hexa = {hex(angka)}"

print(binary,"\n",octal,"\n",hexa,"\n")
```
output:
```
binary = 0b101110111000000110
octal = 0o567006
hexa = 0x2ee06
```
jadi kita mengconvert ketika bentuk bilangan itu bisa dengan mudah.

dan untuk ngedecodenya tinggal tuliskan ulang outputnya itu, dan bisa kembali ke bilangan awal tanpa formating apapun:
```python
binary = 0b101110111000000110
octal = 0o567006
hexa = 0x2ee06

print ("binary =", binary, "\n", "octal =", octal, "\n", "hexa =", hexa, "\n")
```
output:
```
binary = 192006
octal = 192006
hexa = 192006
```
kenapa bisa kembali tanpa syntax decode tambahan? karena kita menuliskan 2 formating diawal itu:
0b = binary
0o = octal
0x = hex
tanpa menuliskan ini, maka output yang keluar akan sama seperti variable, tidak di decode apapun.

