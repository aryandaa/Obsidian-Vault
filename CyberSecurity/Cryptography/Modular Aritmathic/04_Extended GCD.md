Misalkan a dan b adalah bilangan bulat positif.
Algoritma Euclid versi extended adalah cara yang efisien untuk mencari bilangan bulat u, v
sehingga:
`a ⋅ u + b ⋅ v = gcd(a,b)`

langsung saja saya mengerjakan soal ini:
Menggunakan dua bilangan prima:
p = 26513
q = 32321

cari bilangan bulat u dan v sehingga

p ⋅ u + q ⋅ v = gcd(p,q)

note : saya tidak bisa menghitungnya manual karena angkanya terlalu banyak, jadi disini saya akan menggunakan python saja:
```Python
from sympy import gcdex
from sympy import gcd

p = 26513
q = 32321

u, v, g = gcdex(p, q)
print(f"u = {u}\nv = {v}")
print (f"{p * u + q * v} hasilnya akan sama dengan {gcd(p, q)}")
```
di dalam python ada function untuk menjadi nilai U dan V dengan mudah, yaitu menggunakan gcdex dari sympy.

### penjelasan:
Ada dua angka u dan v, sehingga kalau p dikali u lalu ditambah q dikali v,
hasilnya tepat sama dengan gcd-nya.

ini namanya "extended GCD"
Karena p dan q adalah bilangan prima yang berbeda, maka kalo di gcd kan hasilnya "1"

Jadi sebenarnya kita cuma lagi nyari cara nulis angka 1 sewbagai:

1 = (kelipatan p) + (kelipatan q)  

Kok bisa 1 ditulis dari p dan q?
Karena algoritma Euclid.

Waktu melakukan gcd(p, q), kamu sebenernya melakukan ini:
q = p·a + r1
p = r1·b + r2
r1 = r2·c + r3
...(bla bla bla)