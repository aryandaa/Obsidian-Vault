#cybersecurity 

RSA adalah algoritma kunci publik yang paling terkenal dan paling sering muncul di CTF. Ditemukan pada tahun 1977 oleh Ron Rivest, Adi Shamir, dan Leonard Adleman. RSA memakai konsep yang sudah kamu pelajari di Modular Arithmetic: perkalian, modulo, dan invers.

## Ide besar di balik RSA

RSA berdiri di atas satu fakta sederhana: **mengalikan dua bilangan itu mudah, tetapi memfaktorkan hasilnya itu sulit.**

Contoh:

```text
61 × 53 = 3233        (mudah, hitung pakai kalkulator)
3233 = ? × ?          (butuh percobaan, apalagi untuk bilangan raksasa)
```

Kalau bilangan prima-nya sangat besar (ratusan digit), memfaktorkan kembali hasil kalinya menjadi mustahil secara praktis. Keamanan RSA bergantung pada kesulitan itu.

## Bagian-bagian RSA

RSA punya beberapa komponen yang perlu kamu kenal:

```text
p, q   : dua bilangan prima rahasia
N      : p × q (modulus, bagian dari public key)
e      : public exponent (biasanya 65537)
d      : private exponent (rahasia, dihitung dari p dan q)
```

Public key = pasangan (N, e). Private key = d (atau p, q).

## Enkripsi dan dekripsi

Rumusnya sangat pendek:

```text
Enkripsi : c = m^e mod N
Dekripsi : m = c^d mod N
```

- `m` adalah pesan yang diubah menjadi angka.
- `c` adalah ciphertext dalam bentuk angka.
- Semua operasi dilakukan modulo N.

Contoh kecil supaya terasa nyata:

```text
p = 61, q = 53
N = 61 × 53 = 3233
e = 17
d = 2753

Enkripsi pesan m = 65:
c = 65^17 mod 3233 = 2790

Dekripsi:
m = 2790^2753 mod 3233 = 65
```

Coba sendiri di Python:

```python
p, q = 61, 53
N = p * q
e = 17
d = pow(e, -1, (p-1)*(q-1))   # ini konsep modular inverting

m = 65
c = pow(m, e, N)              # enkripsi
m2 = pow(c, d, N)             # dekripsi
print(c, m2)                  # 2790 65
```

Perhatikan `pow(m, e, N)`: ini cara Python menghitung `m^e mod N` dengan cepat. Jangan pernah pakai `m ** e % N` untuk angka besar, itu lambat dan bisa membuat komputer ngelag.

## Kenapa RSA aman

Siapa pun boleh tahu N dan e. Tapi untuk mendapatkan d, kamu harus tahu p dan q. Untuk tahu p dan q, kamu harus memfaktorkan N. Dan memfaktorkan N yang besar itu mustahil secara praktis.

```text
N publik → faktorisasi sulit → p, q rahasia → d aman
```

## RSA di CTF

Di CTF, RSA hampir selalu diberikan dalam bentuk parameter, dan tugasmu menghitung atau mendekripsi dengan Python. Bentuk yang paling umum:

```python
n = 0x...
e = 65537
c = 0x...          # ciphertext dalam hex
p = 0x...          # kadang p dan q diberikan
q = 0x...
```

Langkah dasar untuk mendekripsi:

```python
n = 0x...
e = 65537
c = 0x...
p = 0x...
q = 0x...

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)          # private exponent
m = pow(c, d, n)             # pesan dalam bentuk angka

# ubah angka menjadi byte
flag = m.to_bytes((m.bit_length() + 7) // 8, 'big')
print(flag)
```

Kalau p dan q tidak diberikan, jangan panik. Ada banyak cara lain, dan itu dibahas di materi [RSA Attacks](RSA%20Attacks.md).

## Pesan ke angka dan kembali

RSA bekerja dengan angka, bukan teks. Jadi pesan harus diubah dulu menjadi angka (biasanya dari byte), dan hasil dekripsi diubah kembali menjadi teks.

```python
# teks → angka
m = int.from_bytes(b"crypto{...}", 'big')

# angka → teks
teks = m.to_bytes((m.bit_length() + 7) // 8, 'big')
```

## Ringkasan

- RSA = enkripsi kunci publik berbasis kesulitan faktorisasi.
- Komponen: p, q, N = p×q, e, d.
- Enkripsi `c = m^e mod N`, dekripsi `m = c^d mod N`.
- Di CTF: biasanya tinggal hitung d dari p, q, lalu dekripsi dengan Python.
- Kalau p dan q tidak ada, atau parameter lain terlihat aneh, lanjut ke materi RSA Attacks.
