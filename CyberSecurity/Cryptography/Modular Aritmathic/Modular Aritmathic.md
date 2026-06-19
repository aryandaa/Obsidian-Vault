#cybersecurity
Modular adalah sisa bagi dari 2 bilangan
### contoh manual:

misalnya 16 dan 28 = 12
  
cari pembagian 16 yang hasilnya mendekati 28
16 x 1 = 16 hasilnya 1
16 x 2 = 32 (salah karna melebihi)
1 x 16 = 16
28 (nilai tertinggi di awal) - 16 (sisa di atas) = 12

kita buktikan dengan python
`print (28 % 16)` dan hasilnya sama yaitu 12

Nah sekarang bayangkan kalo kita memiliki sebuah modulus P, dan kita membatasi pembahasan pada kasus ketika **p adalah bilangan prima**.

Bilangan bulat modulo **p** membentuk sebuah **field (lapangan)**, yang dinotasikan sebagai **Fₚ**.
> Jika modulusnya bukan bilangan prima, maka himpunan bilangan bulat modulo **n** membentuk sebuah **ring (gelang)**.

Jika sebuah field hingga (**finite field**) **Fₚ** adalah himpunan bilangan bulat, maka cara mencari N nya dengan cara berikut: 
**0, 1, ..., p − 1**

contohnya adalah jika Fp dan p-nya adalah 5, maka N adalah 0, 1, 2, 3, 4 (P-1), artinya semua angka yang boleh dipakai cuma yang di sebutkan saja.

Jadi kalau hasil perhitungan keluar dari daftar itu, kita "putar balik" pakai modulo 5.
contoh:
```
- 1 mod 5 = 1
    
- 2 mod 5 = 2
    
- 3 mod 5 = 3
    
- 4 mod 5 = 4
    
- 5 mod 5 = 0
    
- 6 mod 5 = 1
    
- 7 mod 5 = 2
    
- 8 mod 5 = 3
    
- 9 mod 5 = 4
    
- 10 mod 5 = 0
```

kalo kita lihat diatas, hasilnya mulai dari 0 lalu terakhir 4 dan tidak pernah 5 persis seperti yang sudah di sebutkan diatas kalo 0,1,2,3...P-1

### 1. Invers Penjumlahan (b+)
Rumus dari invers Penjumlahan adalah:
```
a + b₊ = 0
```

atau artinya cari angka jika di tambah dengan A hasilnya jadi 0 jika di moduluskan dengan P diawal (5)

Contoh
a = 2
rumus = 2 + ? = 0 mod 5
kalo di coba dengan 3 jadi:
```
2 + 3 = 5 mod 5 = 0 (Berhasil)
```
kesimpulan: Jadi Inverst Penjumlahan dari 2 adalah 3

Contoh lain:
```
1 + 4 = 5
5 mod 5 = 0
```
Kesimpulan jadi inverse penjumlahan dari 1 adalah 4.

jadi itulah alasan kenapa kita tidak boleh memakai nominal yang melebihi dari 5.


### 2. Invers Perkalian (b*)
Rumus dari Invers Perkalian adalah:
```
a · b* = 1
```
cari angka yang jika dikalikan dengan a hasilnya 1 jika di moduluskan dengan P diawal (5).

Cara pengerjaannya sama saja kaya invers Perjumlahan

Contoh 1:
```
a = 2

jika cari satu satu:
2×1 = 2
2×2 = 4
2×3 = 6 ≡ 1 mod 5
```
Kesimpulan: Invers perkalian dari 2 adalah 3.

Contoh 2:
```
a = 4

4x1 = 4
4x2 = 8
4x3 = 12
4x4 = 16 = 1 mod 5
```
Kesimpulan: Invers perkalian dari 4 adalah 16.



jadi kenapa field harus bilangan prima?
supaya semua angka yang di invers jumlah maupun invers kali akan memiliki invers nya sendiri.
misalnya seperti tadi saya memilih modulo 5:
```
1 punya invers
2 punya invers
3 punya invers
4 punya invers
kecuali 0.
```
jadi itulah kenapa syarat field harus prima.

coba sekarang yang non-prima, contohnya '6', angka yang tersedia adalah "0,1,2,3,4,5".
kita ambil 2.
lalu kita coba invers perkalian:
```
rumus: 2 × ? ≡ 1 mod 6

2×1 = 2
2×2 = 4
2×3 = 0
2×4 = 2
2×5 = 4
```
Tidak ada yang pernah dapat 1.
artinya: 2 tidak punya invers.

### sekarang saya memiliki soal dari cryptohack, yaitu

 1. 11 = x mod 6
 2. 8146798528947 = y mod 17
 3. carilah x dan y, lalu dimoduluskan

disini karna sudah ada teknologi python, jadi saya akan menggunakan python untuk solved.
gampang saja tinggal pakai simbol % untuk modulus, moduluskan 11 dengan 6 dan 8146798528947 dengan 17, lalu kedua hasilnya itu di bitwise and kan dengan simbol &, dan itu jawabannya.

```Python
soal1 = 11 % 6
soal2 = 8146798528947 % 17

print (soal1 & soal2)
#jawabannya adalah "4"
```
