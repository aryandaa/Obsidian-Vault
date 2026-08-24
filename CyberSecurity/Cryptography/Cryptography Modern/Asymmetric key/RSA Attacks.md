#cybersecurity 

RSA yang dipakai dengan benar sangat sulit diserang. Tapi di CTF, RSA hampir selalu dipakai dengan cara yang "salah", dan itulah inti soalnya. Materi ini mengajarkan serangan-serangan RSA yang paling sering muncul, plus cara menebaknya dari parameter yang diberikan.

Pola pikirnya: **setiap parameter yang terlihat aneh adalah petunjuk serangan.** Jangan langsung menyerah kalau p dan q tidak diberikan.

## Langkah 0: selalu cek yang paling mudah dulu

Urutan cek ini menyelesaikan sebagian besar soal RSA di CTF:

```text
1. Apakah p dan q diberikan langsung? → hitung d biasa
2. Apakah n kecil? → faktorisasi dengan factordb atau sympy
3. Apakah e kecil dan c kecil? → akar pangkat tiga
4. Apakah e = 1? → c langsung terbaca
5. Apakah dua soal memakai n yang sama? → common modulus
6. Apakah d kecil? → Wiener attack
7. Apakah m kecil tapi e = 3? → cube root attack
```

## Serangan 1: n kecil (faktorisasi langsung)

Kalau n hanya puluhan atau ratusan digit kecil, kamu bisa memfaktorkannya langsung.

Cara pertama: coba [factordb.com](http://factordb.com). Situs ini punya database faktorisasi. Tempel n, dan kalau sudah pernah difaktorkan orang, hasilnya langsung keluar.

Cara kedua: pakai sympy di Python.

```bash
pip install sympy
```

```python
from sympy import factorint

n = 0x...
print(factorint(n))   # menghasilkan {p: 1, q: 1}
```

Cara ketiga: coba faktorisasi kecil-kecilan manual.

```python
n = 0x...
for i in range(2, 100000):
    if n % i == 0:
        print(i, n // i)
        break
```

Setelah p dan q ketemu, lanjut dekripsi seperti di materi RSA.

## Serangan 2: e kecil (cube root attack)

Kalau `e = 3` dan pesan `m` kecil, maka `m^3` bisa jadi **lebih kecil dari n**. Kalau itu terjadi, operasi modulo tidak mengubah apa pun:

```text
c = m^3 mod n = m^3 (karena m^3 < n)
```

Artinya ciphertext `c` adalah pangkat tiga murni. Tinggal akar pangkat tiga:

```python
import gmpy2

c = 0x...
m = gmpy2.iroot(c, 3)[0]      # akar pangkat 3
flag = int(m).to_bytes((int(m).bit_length() + 7) // 8, 'big')
print(flag)
```

Cara cepat mendeteksi: e = 3 dan panjang ciphertext jauh lebih pendek dari n.

## Serangan 3: common modulus

Kalau dua soal (atau dua ciphertext) memakai **n yang sama** tetapi e yang berbeda, dan gcd dari kedua e itu 1, kamu bisa mendekripsi tanpa memfaktorkan n sama sekali.

```python
# e1, c1 dan e2, c2 memakai n yang sama
# cari a, b sehingga a*e1 + b*e2 = 1 (extended GCD, sudah dipelajari)
g, a, b = ..., ..., ...
m = (pow(c1, a, n) * pow(c2, b, n)) % n
```

Konsep ini memakai extended GCD yang sudah kamu pelajari di Modular Arithmetic. Kalau kedua ciphertext berasal dari pesan yang sama, ini langsung berhasil.

## Serangan 4: Wiener attack (d kecil)

Kalau private exponent `d` terlalu kecil, RSA bisa diserang dengan Wiener attack menggunakan pecahan lanjut (continued fraction). Ini sudah diimplementasikan di library.

```bash
pip install owiener
```

```python
import owiener

n = 0x...
e = 0x...
c = 0x...

d = owiener.attack(e, n)
if d:
    m = pow(c, d, n)
    print(int(m).to_bytes((int(m).bit_length() + 7) // 8, 'big'))
```

Cara mendeteksi: `e` sangat besar (mendekati n). Itu biasanya penanda d kecil.

## Serangan 5: m yang sama dikirim ke beberapa orang (broadcast)

Kalau pesan yang sama dikirim ke 3 orang dengan e = 3 dan n yang berbeda-beda:

```text
c1 = m^3 mod n1
c2 = m^3 mod n2
c3 = m^3 mod n3
```

Dengan Chinese Remainder Theorem (sudah dipelajari di Modular Arithmetic), kamu bisa menemukan `m^3` persis, lalu akar pangkat tiga.

```python
from sympy.ntheory.modular import crt

# crt([n1,n2,n3], [c1,c2,c3]) → m^3 yang sebenarnya
```

Ini disebut Hastad broadcast attack. Di CTF biasanya muncul sebagai "3 orang mengirim pesan sama".

## Serangan 6: e = 1

Kalau `e = 1`, maka `c = m^1 mod n = m`. Ciphertext-nya langsung pesan aslinya. Ini sering jadi jebakan soal "gampang".

```python
flag = int.to_bytes(c, (c.bit_length() + 7) // 8, 'big')
```

## Alur lengkap saat menghadapi soal RSA

```text
Baca parameter: n, e, c, dan apa pun yang ada
    ↓
Apakah p, q ada? → dekripsi biasa
    ↓
Tidak. Apakah n kecil / ada di factordb? → faktorisasi
    ↓
Tidak. Apakah e = 3 dan c kecil? → cube root
    ↓
Tidak. Apakah ada n yang sama dipakai dua kali? → common modulus
    ↓
Tidak. Apakah e sangat besar? → Wiener
    ↓
Tidak. Apakah ada beberapa ciphertext dengan e = 3? → broadcast (CRT)
    ↓
Masih tidak? → periksa pola lain, baca lagi soalnya, cari petunjuk
```

Sebagian besar soal RSA pemula selesai di langkah faktorisasi atau cube root.

## Latihan kecil

Diberikan:

```text
n = 3233
e = 17
c = 2790
```

Faktorisasi 3233 (bilangan kecil), hitung d, lalu dekripsi. Hasilnya harus angka 65, yang kalau diubah ke ASCII adalah huruf `A`. Coba juga di factordb untuk memastikan kamu tahu cara pakainya.

## Ringkasan

- RSA yang "salah pakai" bisa diserang tanpa memfaktorkan n.
- Cek urutan: p/q ada, n kecil, e kecil, common modulus, Wiener, broadcast.
- factordb dan sympy menyelesaikan banyak kasus dalam hitungan detik.
- Parameter aneh = petunjuk serangan.
- Extended GCD dan CRT dari sesi Modular Arithmetic adalah senjata utama.
