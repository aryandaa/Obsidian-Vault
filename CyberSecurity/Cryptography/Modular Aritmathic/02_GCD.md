Faktor persekutuan besar (FPB) Atau Greatest Common Divisor (GCD) adalah bilangan terbesar yang dapat membagi 2 bilangan bulat positif.

misalnya:
a = 12, b = 8
faktor dari a adalah 1, 2, 3, 4, 6, 12
dan faktor dari b adalah 1, 2, 4, 8
dan kita lihat angka tertinggi yang sama adalah 4.

### GCD dalam Cryptography
sekarang bayangkan kita punya:
a = 11, dan b = 17.
ya, keduanya adalah bilangan prima... Karena bilangan prima hanya punya dirinya sendiri dan 1 sebagai faktor,

maka gcd(a, b) = 1.

Jika nilai a dan b di FPB kan dan hasilnya 1, maka dia di sebut dengan ==coprime==, tetapi jika ingin mendapatkan 1 tersebut harus memiliki syarat mutlak, yaitu nilai keduanya harus bilangan prima,
tetapi jika a adalah bilangan prima dan b lebih kecil dari a, hasilnya juga bisa coprime.

## Contoh perhitungan GCD dengan Python
```Python
import math

# Di python ada tools untuk menghitung nilai FPB ini yaitu gcd(a, b):
a = 66528
b = 52920
hitung = math.gcd(a, b)
print (hitung) #hasilnya adalah 1512

# Contoh COprime
a = 11
b = 17
hitung = math.gcd(a, b)
print (hitung) # Hasilnya adalah 1
```