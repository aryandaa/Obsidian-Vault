Dalam aritmatika modulo, sebuah bilangan x bisa di sebut sebagai Kuadrat residu (Quadratic Residues) jika memiliki nilai a dan di kuadratkan, lalu di hasilnya di moduluskan dengan p (p adalah bilangan prima), hasilnya tersebutlah nilai x dan itu di sebut dengan "Quadratic Residue".

tapi memiliki syarat tertentu, yaitu bilangan p harus prima dan a harus -1 dari p

Quadratic Residue memiliki rumus berikut: ==$a^2$ = x mod p==. 

kalo memenuhi syarat berikut itu, berarti bilangan x mempunyai "akar kuadrat" di dunia modulo. dan sebaliknya kalo bilangan a itu tidak memenuhi syarat berarti di sebut "Quadratic Non-Residues" atau tidak memiliki akar kuadrat.
Jadi intinya, quadratic residue adalah bilangan yang **bisa muncul sebagai hasil kuadrat** dari bilangan lain dalam sistem modulo tertentu.

### Contoh
p = 29 (bilangan prima)
a = 11 (bilangan bulat apapun)
x = $a^2$ mod p

pertama saya akan menghitung a kuadrat terlebih dahulu,
$a^2$ = 11 * 11 = 121 

lalu di moduskan dengan p.
modulus 29 = 5.

berarti x nya adalah 5,
akar kuadrat dari 5 adalah 11, dan itu berarti Quadratic residue.

### Contoh Lengkap Perhitungan Quadratic Residue dan Non-Residue
p = 29

saya akan mencari bilangan yang muncul dan tidak pada perhitungan kali ini:

a = 1 = 1² = 1 mod 29 = 1  
a = 2 = 2² = 4 mod 29 = 4  
a = 3 = 3² = 9 mod 29 = 9  
a = 4 = 4² = 16 mod 29 = 16  
a = 5 = 5² = 25 mod 29 = 25  
a = 6 = 6² = 36 mod 29 = 7  
a = 7 = 7² = 49 mod 29 = 20  
a = 8 = 8² = 64 mod 29 = 6  
a = 9 = 9² = 81 mod 29 = 23  
a = 10 = 10² = 100 mod 29 = 13  
a = 11 = 11² = 121 mod 29 = 5  
a = 12 = 12² = 144 mod 29 = 28  
a = 13 = 13² = 169 mod 29 = 24  
a = 14 = 14² = 196 mod 29 = 22  
a = 15 = 15² = 225 mod 29 = 22  
a = 16 = 16² = 256 mod 29 = 24  
a = 17 = 17² = 289 mod 29 = 28  
a = 18 = 18² = 324 mod 29 = 5  
a = 19 = 19² = 361 mod 29 = 13  
a = 20 = 20² = 400 mod 29 = 23  
a = 21 = 21² = 441 mod 29 = 6  
a = 22 = 22² = 484 mod 29 = 20  
a = 23 = 23² = 529 mod 29 = 7  
a = 24 = 24² = 576 mod 29 = 25  
a = 25 = 25² = 625 mod 29 = 16  
a = 26 = 26² = 676 mod 29 = 9  
a = 27 = 27² = 729 mod 29 = 4  
a = 28 = 28² = 784 mod 29 = 1

Dari daftar ini kelihatan jelas:
- nilai yang **muncul** adalah quadratic residue,
	- 1, 4, 5, 6, 7, 9, 13, 16, 20, 22, 23, 24, 25, 28.
- nilai yang **tidak pernah muncul** adalah quadratic non-residue.
	- 0, 2, 3, 8, 10, 11, 12, 14, 15, 17, 18, 19, 21, 26, 27.


Di CryptoHack memiliki 1 soal disuruh mencari satu Quadratic residue dari tiga bilangan yaitu 6 11 dan 14, untuk membuktikan bahwak itu adalah Quadratic residue yaitu memiliki akar kuadrat, jadi perhitungan dari 3 bilangan itu adalah jawabannya...
dari list di atas saya sudah mengetahui kalo kuadrat residue nya adalah 6, tetapi saya harus membuktikan kalo 6 adalah kuadrat residue dari rumus berikut:
$a^2$ mod 29, 
nilai a yang menghasilkan 6 jika di hitung itulah jawabannya...
dari list diatas sudah bisa di ketahui kalo nilai a yang menghasilkan 6 dari perhitungan kuadrat residue adalah "8"

## Python untuk Quadratic Residue:

```Python
p = 29
for a in range(p):
    qr = (pow(a, 2, p))
    print(f"a={a} : qr={qr}")
```
jadi kode ini untuk mencari nilai a dan nilai dari Kuadrat residue dari bilangan a jika di moduluskan dengan P dengan cara di bruteforce, dan output yang keluar adalah:

![[Pasted image 20260112113540.png]]