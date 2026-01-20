#cybersecurity
Modular adalah sisa bagi dari 2 bilangan
### contoh manual:

misalnya 16 dan 28 = 12
  
cari pembagian 16 yang hasilnya mendekati 28
16 x 1 = 16 hasilnya 1
16 x 2 = 32 (salah)
1 x 16 = 16
28 (nilai tertinggi di awal) - 16 (sisa di atas) = 12

kita buktikan dengan python
`print (28 % 16)` dan hasilnya sama yaitu 12
### sekarang saya memiliki soal dari cryptohack, yaitu

 1. 11 = x mod 6
 2. 8146798528947 = y mod 17
 3. carilah x dan y, lalu dimoduluskan

```Python
soal1 = 11 % 6
soal2 = 8146798528947 % 17

print (soal1 & soal2)
#jawabannya adalah "4"
```
