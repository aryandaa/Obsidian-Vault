#cybersecurity 

ECC (Elliptic Curve Cryptography) adalah teknologi kunci publik yang lebih modern. Ia memakai matematika kurva eliptik, dan keunggulannya besar: **kunci yang lebih pendek dengan keamanan yang sama.**

```text
RSA kunci 3072 bit  ≈  ECC kunci 256 bit
```

Kunci yang lebih pendek artinya lebih cepat dan lebih hemat daya. Itu sebabnya ECC dipakai di ponsel, kartu pintar, dan sebagian besar HTTPS modern.

## Analogi sederhana: jalan di atas kurva

Bayangkan sebuah kurva berbentuk seperti huruf S yang miring (itu bentuk kurva eliptik). Ada aturan "berjalan" di atas kurva: kamu bisa menjumlahkan dua titik untuk mendapat titik ketiga, dan mengalikan titik dengan angka untuk melompat-lompat di atas kurva.

Kunci publik ECC dibangun dari:

```text
G      : titik awal yang disepakati bersama (generator)
n      : bilangan rahasia (private key)
Q = n*G : hasil "melompat" n kali dari titik G (public key)
```

Jadi public key adalah `n * G`. Masalahnya: kalau orang hanya melihat `G` dan `Q`, sulit untuk menemukan `n`. Ini disebut **elliptic curve discrete logarithm problem** (ECDLP), dan untuk kurva yang dipilih dengan benar, masalah ini sangat sulit.

Ini konsep yang sama dengan Diffie-Hellman, tapi di atas kurva:

```text
DH klasik : g^a mod p        (perkalian biasa)
ECDH      : a * G             (perkalian titik di kurva)
```

## Cara kerja ECDH (pertukaran kunci)

1. Alice dan Bob sepakat memakai kurva dan titik G yang sama.
2. Alice punya rahasia a, mengirim `a*G`.
3. Bob punya rahasia b, mengirim `b*G`.
4. Alice menghitung `a*(b*G) = ab*G`.
5. Bob menghitung `b*(a*G) = ab*G`.
6. Keduanya mendapat titik yang sama: kunci bersama.

Penyadap hanya melihat `a*G` dan `b*G`, tapi tidak bisa mendapat `ab*G` tanpa tahu a atau b.

## Parameter kurva

Kurva eliptik ditentukan oleh persamaan:

```text
y^2 = x^3 + ax + b  (mod p)
```

Parameter yang diberikan di soal:

```text
p  : bilangan prima (modulus)
a, b : koefisien kurva
G  : titik generator (x, y)
n  : orde titik generator
Q  : kunci publik (x, y)
```

Di CTF, soal ECC biasanya memakai library seperti `ecdsa` atau `cryptography` di Python, atau memberikan parameter dan meminta kamu menghitung sesuatu.

## ECC di CTF

Soal ECC tingkat pemula biasanya menyerupai ini: kurva dengan p kecil, lalu kamu harus memecahkan discrete log di atas kurva untuk menemukan private key.

```python
# pip install fastecdsa sympy
from sympy import mod_inverse

# parameter kurva
p = 0x...
a = 0x...
b = 0x...
G = (0x..., 0x...)
Q = (0x..., 0x...)

# untuk p kecil, coba semua n sampai n*G = Q
def point_add(P, Q, p, a):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if P == Q:
        m = (3 * x1 * x1 + a) * mod_inverse(2 * y1, p) % p
    else:
        m = (y2 - y1) * mod_inverse(x2 - x1, p) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def point_mul(k, P, p, a):
    R = None
    while k:
        if k & 1:
            R = point_add(R, P, p, a)
        P = point_add(P, P, p, a)
        k >>= 1
    return R

for n in range(1, 100000):
    if point_mul(n, G, p, a) == Q:
        print("private key:", n)
        break
```

Biasanya kamu tidak perlu menulis kode kurva dari nol. Library `fastecdsa` atau `ecdsa` sudah menyediakan operasi titik. Tapi memahami kode di atas membantu kamu tahu apa yang sebenarnya terjadi.

## Cara mengenali soal ECC

- Ada parameter `p`, `a`, `b`, `G`, dan `Q`.
- Ada kata "curve", "elliptic", "ECDH", "ECDSA", atau nama kurva seperti `secp256k1`.
- Perkalian titik memakai notasi `G * n` atau `scalar multiplication`.

## Ringkasan

- ECC = kriptografi kunci publik berbasis kurva eliptik.
- Keamanannya dari kesulitan memecahkan discrete log di atas kurva.
- Kunci ECC lebih pendek tapi keamanannya setara RSA yang lebih panjang.
- ECDH = Diffie-Hellman yang dijalankan di atas kurva.
- Di CTF: kalau p kecil, coba brute force private key dengan operasi titik.
- ECC adalah materi lanjutan; di CTF pemula, RSA jauh lebih sering muncul.
