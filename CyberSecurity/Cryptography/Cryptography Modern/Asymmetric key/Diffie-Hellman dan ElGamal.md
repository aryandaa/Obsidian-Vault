#cybersecurity 

Diffie-Hellman dan ElGamal adalah dua algoritma kunci publik yang saling berhubungan. Diffie-Hellman dipakai untuk **bertukar kunci** (dua orang membuat kunci rahasia yang sama tanpa mengirimkannya), dan ElGamal memakai ide yang sama untuk **enkripsi** langsung.

## Masalah yang dipecahkan Diffie-Hellman

Ingat masalah symmetric key: dua orang butuh kunci yang sama, tapi bagaimana mengirim kuncinya tanpa ketahuan orang lain? Mengirim kunci lewat jaringan itu berbahaya, karena siapa pun bisa menyadapnya.

Diffie-Hellman (disingkat DH, ditemukan 1976 oleh Whitfield Diffie dan Martin Hellman) memecahkan masalah ini: Alice dan Bob bisa membuat kunci yang sama **tanpa pernah mengirim kuncinya**.

## Analogi warna

Cara paling gampang memahami DH adalah dengan analogi cat warna:

1. Alice dan Bob sepakat memakai satu warna dasar yang sama (misal kuning). Ini boleh diketahui semua orang.
2. Alice mencampur kuning dengan warna rahasianya (misal merah) menjadi oranye, lalu mengirim oranye ke Bob.
3. Bob mencampur kuning dengan warna rahasianya (misal biru) menjadi hijau, lalu mengirim hijau ke Alice.
4. Sekarang Alice mencampur hijau yang dia terima dengan warna rahasianya (merah), dan Bob mencampur oranye yang dia terima dengan warna rahasianya (biru).

Hasilnya: keduanya mendapat warna yang sama! Alice mendapat hijau + merah, Bob mendapat oranye + biru. Keduanya sama-sama kuning + merah + biru.

Si penyadap hanya melihat kuning, oranye, dan hijau. Dia tidak pernah melihat merah atau biru, jadi dia tidak bisa membuat warna akhir.

## DH dalam matematika

Versi matematikanya memakai pangkat dan modulo (konsep yang sudah kamu pelajari di Modular Arithmetic):

```text
1. Alice dan Bob sepakat: p (bilangan prima besar) dan g (generator)
2. Alice pilih rahasia a, kirim A = g^a mod p
3. Bob pilih rahasia b, kirim B = g^b mod p
4. Alice hitung: B^a mod p = g^(b*a) mod p
5. Bob hitung: A^b mod p = g^(a*b) mod p
6. Keduanya mendapat nilai yang sama: g^(ab) mod p
```

Nilai `g^(ab) mod p` itu menjadi kunci rahasia bersama.

Kenapa aman? Penyadap melihat `g^a` dan `g^b`, tetapi untuk mendapat `a` atau `b` dia harus memecahkan **discrete logarithm**, yang sulit untuk p yang besar.

## DH di CTF

Di CTF, soal DH biasanya seperti ini:

```text
p = 0x... (prima)
g = 2
A = 0x... (nilai Alice)
B = 0x... (nilai Bob)
```

Kunci bersama = `pow(A, b, p)` atau `pow(B, a, p)`. Kalau `a` atau `b` kecil, kamu bisa memecahkan discrete log:

```python
from sympy import discrete_log

p = 0x...
g = 2
A = 0x...

# cari a sehingga g^a mod p = A
a = discrete_log(p, A, g)
print(a)
```

Kalau p-nya kecil, discrete log langsung ketemu. Kalau p besar tapi a kecil (misal cuma 20 bit), brute force juga bisa:

```python
# cari a dengan mencoba semua kemungkinan kecil
for a in range(2**20):
    if pow(g, a, p) == A:
        print(a)
        break
```

Setelah dapat a, hitung kunci bersama, lalu dekripsi pesan yang dienkripsi dengan kunci itu (biasanya XOR atau AES).

## ElGamal: enkripsi berbasis DH

ElGamal memakai ide DH untuk enkripsi langsung. Strukturnya:

```text
Public key : p, g, h = g^x mod p
Private key: x (rahasia)
```

Untuk mengenkripsi pesan m:

```text
1. Pilih angka acak y
2. c1 = g^y mod p
3. c2 = m * (h^y) mod p
4. Ciphertext = (c1, c2)
```

Untuk mendekripsi:

```text
m = c2 * (c1^x)^-1 mod p
```

Dengan kata lain: pengirim menyembunyikan pesan dengan cara mengalikannya dengan "kunci sementara" yang dibuat dari public key, dan penerima bisa menghapus kunci sementara itu karena dia tahu x.

## ElGamal di CTF

Soal ElGamal biasanya memberikan p, g, h, c1, c2, dan kadang y yang terlalu kecil atau x yang terlalu kecil.

Kalau y kecil, brute force:

```python
p = 0x...
g = 0x...
h = 0x...
c1, c2 = 0x..., 0x...

for y in range(2**20):
    if pow(g, y, p) == c1:
        s = pow(h, y, p)
        m = (c2 * pow(s, -1, p)) % p
        print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))
        break
```

Kalau x kecil, cari dulu x dari h, lalu dekripsi.

## Cara mengenali soal DH/ElGamal

- Ada `p` dan `g` (parameter publik).
- Ada nilai `A` dan `B` (DH) atau `h`, `c1`, `c2` (ElGamal).
- Sering ada pesan terenkripsi yang harus didekripsi setelah kunci bersama ketemu.

## Ringkasan

- DH memungkinkan dua pihak membuat kunci bersama tanpa mengirim kunci.
- Keamanannya bergantung pada kesulitan discrete logarithm.
- ElGamal = enkripsi yang memakai ide DH.
- Di CTF: kalau p kecil atau a/y/x kecil, discrete log atau brute force langsung menang.
- sympy punya `discrete_log` yang siap pakai.
