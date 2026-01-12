di dalam aritmatika modular tidak memilliki pembagian, tapi ada yang namanya Inversting.

modular bisa di bilang invers kalo gcd(a, b) = 1, atau kedua bilangan itu prima.

ini penting di dalam Cryptograpy karena "Pembagian" di modulo itu menggunakan invers (seperti  yang sdh di sebutkan diatas, tidak ada pembagian dalam modular).

dalam Cryptography modern seperti RSA, ECC, maupun tanda tangan digital menggunakan konsep invers ini.

langsung saja saya contohkan cara mencari inverst dari 5 (mod 17):

cari x sehingga:
`5 * x = 1 (mod 17)`
menghasilkan angka ==`1`== jika hasil dari 5 * x = ... lalu di moduluskan dengan 17

cara mencek apakah 1, disini saya akan menggunakan cara manual terlebih dahulu:
5 * 1 = 5 mod 17 = 5
5 * 2 = 10 mod 17 = 10
5 * 3 = 15 mod 17 = 15
5 * 4 = 20 mod 17 = 3
5 * 5 = 25 mod 17 = 8
5 * 6 = 30 mod 17 = 13
5 * 7 = 35 mod 17 = 1

ketemu 1 di angka 7, berarti invers dari 5 (Mod 17) adalah 7.

## Rumus Euclid
5x + 17y = 1

Invers nya ada di salah satu antara x dan y.
 Langkah:
 saya akan mencari perhitungan yang menghasilkan 17 dan 5
- 17 = 3×5 + 2
- 5 = 2×2 + 1
ketemu, 1 dan 2.

lalu saya kembalikan lagi gimana caranya menghasilkan 1 dan 2 itu dari angka sebelumnya
- 1 = 5 − 2×2
- 2 = 17 − 3×5

Substitusi:
- 1 = 5 − (17 − 3×5)×2
- 1 = 7×5 − 2×17

Artinya:
x = 7 (ini invers nya)
y = -2 

Terlihat rumit, tetapi python sdh menyediakan Function untuk menghitungnya secara otomatis
## Python Untuk Inversing

```Python
pow(5, -1, 17)
#Output = 7
```
5 itu angka pertama dan 17 itu modulusnya, Function itu berfungsi seperti "Cari nilai dari 5 (mod 17)".... lalu apa itu -1?
itu adalah simbol untuk modular inversting untuk memerintahkan python agar mencari yang hasilnya 1 saja. 