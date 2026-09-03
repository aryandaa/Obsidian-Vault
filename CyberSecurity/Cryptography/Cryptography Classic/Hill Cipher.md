#cybersecurity 

Hill Cipher diciptakan oleh matematikawan Lester S. Hill pada tahun 1929. Cipher ini menjadi titik balik penting dalam sejarah kriptografi karena merupakan cipher klasik pertama yang menggabungkan konsep aljabar linier murni ke dalam enkripsi teks.

Jika cipher sebelumnya mengandalkan pergeseran huruf atau tabel alfabet buatan, Hill Cipher bekerja dengan **perkalian matriks modulo 26**. Materi ini berhubungan langsung dengan materi yang sudah kamu pelajari di [Modular Aritmatika](../Modular%20Aritmathic/Modular%20Aritmatika.md) dan [Modular Inverting](../Modular%20Aritmathic/Modular%20Inverting.md).

## Cara Kerja

Hill Cipher membagi plaintext menjadi blok berukuran $n$ huruf. Setiap huruf diubah menjadi angka sesuai posisinya di alfabet ($A=0, B=1, \dots, Z=25$).

Kunci enkripsinya adalah sebuah matriks persegi $K$ berukuran $n \times n$:

```text
K = [ k11  k12 ]
    [ k21  k22 ]
```

Pesan plaintext $P$ dibentuk menjadi vektor kolom berukuran $n \times 1$:

```text
P = [ p1 ]
    [ p2 ]
```

### Rumus Enkripsi

Vektor ciphertext $C$ dihitung dengan mengalikan matriks kunci dengan vektor plaintext, lalu dimodulo 26:

```text
C = (K * P) mod 26
```

Atau dalam bentuk sistem persamaan:
- $c_1 = (k_{11} \cdot p_1 + k_{12} \cdot p_2) \bmod 26$
- $c_2 = (k_{21} \cdot p_1 + k_{22} \cdot p_2) \bmod 26$

### Rumus Dekripsi

Untuk mengembalikan ciphertext menjadi plaintext, kita mengalikan vektor ciphertext dengan invers matriks kunci:

```text
P = (K^(-1) * C) mod 26
```

### Syarat Matriks Kunci: Harus Memiliki Invers Modulo 26

Tidak sembarang matriks bisa dijadikan kunci. Sebuah matriks $K$ hanya bisa didekripsi jika determinannya memenuhi dua syarat:
1. $\det(K) \neq 0$
2. $\gcd(\det(K), 26) = 1$ (determinan harus coprime terhadap 26).

Jika determinan bernilai genap atau kelipatan 13, matriks tersebut tidak memiliki invers modulo 26, sehingga pesan tidak akan pernah bisa didekripsi kembali.

Untuk matriks 2x2:
- Determinan: $d = (k_{11} \cdot k_{22} - k_{12} \cdot k_{21}) \bmod 26$
- Cari modular inverse dari determinan: $d^{-1} \pmod{26}$
- Matriks invers:
```text
K^(-1) = d^(-1) * [  k22  -k12 ]  mod 26
                  [ -k21   k11 ]
```

## Contoh Perhitungan Nyata

Misalkan matriks kunci $K$ ukuran 2x2:
```text
K = [ 3  3 ]
    [ 2  5 ]
```

Kita ingin mengenkripsi pesan `HELP`:
1. Ubah jadi angka: `H=7, E=4, L=11, P=15`
2. Blok pertama `HE` = $[7, 4]^T$:
   - $c_1 = (3 \cdot 7 + 3 \cdot 4) \bmod 26 = (21 + 12) \bmod 26 = 33 \bmod 26 = 7$ (`H`)
   - $c_2 = (2 \cdot 7 + 5 \cdot 4) \bmod 26 = (14 + 20) \bmod 26 = 34 \bmod 26 = 8$ (`I`)
   - Hasil blok 1: `HI`
3. Blok kedua `LP` = $[11, 15]^T$:
   - $c_1 = (3 \cdot 11 + 3 \cdot 15) \bmod 26 = (33 + 45) \bmod 26 = 78 \bmod 26 = 0$ (`A`)
   - $c_2 = (2 \cdot 11 + 5 \cdot 15) \bmod 26 = (22 + 75) \bmod 26 = 97 \bmod 26 = 19$ (`T`)
   - Hasil blok 2: `AT`
4. Ciphertext akhir: `HIAT`

## Implementasi Script Python

Berikut script Python mandiri untuk enkripsi dan dekripsi Hill Cipher 2x2:

```python
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = egcd(b % a, a)
    return g, y - (b // a) * x, x

def mod_inv(a, m=26):
    g, x, _ = egcd(a % m, m)
    if g != 1:
        return None
    return x % m

def hill_decrypt_2x2(cipher, K):
    # Hitung determinan
    det = (K[0][0] * K[1][1] - K[0][1] * K[1][0]) % 26
    det_inv = mod_inv(det, 26)
    if det_inv is None:
        raise ValueError("Matriks kunci tidak punya invers modulo 26!")

    # Hitung invers matriks 2x2 modulo 26
    K_inv = [
        [( K[1][1] * det_inv) % 26, (-K[0][1] * det_inv) % 26],
        [(-K[1][0] * det_inv) % 26, ( K[0][0] * det_inv) % 26]
    ]

    plain = []
    cipher_clean = [ord(c) - ord('A') for c in cipher.upper() if c.isalpha()]
    for i in range(0, len(cipher_clean), 2):
        c1, c2 = cipher_clean[i], cipher_clean[i+1]
        p1 = (K_inv[0][0] * c1 + K_inv[0][1] * c2) % 26
        p2 = (K_inv[1][0] * c1 + K_inv[1][1] * c2) % 26
        plain.append(chr(p1 + ord('A')))
        plain.append(chr(p2 + ord('A')))
    return "".join(plain)

# Contoh uji coba dekripsi
K = [[3, 3], [2, 5]]
cipher = "HIAT"
print("Hasil Dekripsi:", hill_decrypt_2x2(cipher, K))  # HELP
```

## Kelemahan Fatal: Known Plaintext Attack (KPA)

Meskipun kebal terhadap frekuensi huruf tunggal, Hill Cipher sangat rapuh jika musuh mengetahui sedikit potongan plaintext dan ciphertext yang bersesuaian.

Karena hubungan enkripsinya linear ($C = K \cdot P$), jika kita mengetahui $n$ pasang vektor plaintext dan ciphertext, kita bisa menyusun matriks plaintext $P$ dan matriks ciphertext $C$:

```text
K = C * P^(-1) mod 26
```

Cukup ketahui 4 huruf plaintext beserta 4 huruf ciphertext yang bersesuaian pada matriks 2x2, kunci $K$ langsung bisa dihitung secara pasti dengan perkalian matriks invers!

## Cara Mengenali Hill Cipher di CTF

- Panjang ciphertext biasanya kelipatan ukuran blok (kelipatan 2 untuk matriks 2x2, kelipatan 3 untuk matriks 3x3).
- Soal sering menyertakan petunjuk berupa angka matriks atau menyebutkan ordo matriks tertentu.
- Teks tampak acak dan tidak terbaca dengan Vigenere maupun substitusi monoalfabetik.
- Sering diberikan format flag yang sudah diketahui di awal (misalnya `picoCTF{...}` atau `flag{...}`), yang sengaja disediakan pembuat soal untuk diserang menggunakan Known Plaintext Attack.

## Tools untuk CTF

- [dcode.fr Hill Cipher](https://www.dcode.fr/hill-cipher): Mendukung pemecahan dengan kunci atau dengan known plaintext attack secara otomatis.
- CyberChef: Operation "Hill Cipher Decode".
- Python dengan library `sympy.matrices` jika membutuhkan matriks ordo 3x3 atau lebih besar modulo 26.

## Latihan Kecil

Diketahui ciphertext `PO` dihasilkan oleh matriks kunci:
```text
K = [ 5  8 ]
    [ 17  3 ]
```

Dapatkan determinan dari matriks kunci, cari modular inversnya, dan dekripsi dua huruf tersebut menjadi plaintext aslinya.

## Ringkasan

- Hill Cipher menggunakan perkalian matriks modulo 26 pada blok berukuran $n$ huruf.
- Kunci adalah matriks $n \times n$ dengan syarat determinan harus coprime terhadap 26.
- Dekripsi menggunakan invers matriks modulo 26.
- Sangat rentan terhadap Known Plaintext Attack (KPA) karena sifat relasi matematisnya yang linier.
