#cybersecurity 

Tidak semua cipher klasik menukar huruf alfabet dengan huruf alfabet lain. Ada kelompok cipher yang menukar huruf menjadi lambang grafis, simbol visual, atau koordinat angka.

Dua yang paling populer dan hampir selalu muncul di kompetisi CTF tingkat pemula adalah **Pigpen Cipher** (Sandi Freemason) dan **Polybius Square**.

## Pigpen Cipher (Freemason's Cipher)

Pigpen Cipher adalah jenis substitusi monoalfabetik geometris yang sudah digunakan sejak abad ke-18 oleh perkumpulan rahasia Freemason untuk menjaga catatan mereka tetap rahasia.

### Pola Kisi Simbol

Pigpen membagi 26 huruf alfabet ke dalam 4 kisi gambar:
1. Dua kisi pagar / silang salib bergaris (#)
2. Dua kisi silang diagonal berbentuk huruf X

Setiap kisi terdiri dari versi **tanpa titik** dan **dengan titik**:

```text
Kisi 1 (Pagar tanpa titik):      Kisi 2 (Pagar dengan titik):
   A | B | C                         .   | .   | .
  ---+---+---                      A . B | C . D
   D | E | F                         .   | .   | .
  ---+---+---                      J . K | L . M
   G | H | I                         .   | .   | .

(Pembagian umum):
Kisi Pagar 1:                    Kisi Pagar 2:
 A | B | C                        J | K | L  (tiap sel diberi tanda titik)
---+---+---                      ---+---+---
 D | E | F                        M | N | O
---+---+---                      ---+---+---
 G | H | I                        P | Q | R

Kisi Silang 1:                   Kisi Silang 2:
    \ S /                            \ . /
   T \ / U                          W \./ X  (tiap bidang diberi titik)
     / \                              /.\
    / V \                            / Y \
                                    /  .  \
                                      Z
```

### Cara Membaca Simbol Pigpen

Bentuk simbol yang dihasilkan diambil dari garis pembatas sel tempat huruf tersebut berada:
- Huruf `E` dikelilingi oleh kotak tertutup penuh, jadi lambangnya berupa kotak `[ ]`.
- Huruf `A` berada di pojok kiri atas, jadi lambangnya sudut siku menghadap kanan-bawah `|_|` tanpa garis atas dan kiri.
- Huruf `B` berada di posisi tengah atas, lambangnya berbentuk huruf `U` terbalik.
- Huruf `J` sampai `R` memiliki bentuk garis yang sama persis dengan `A` sampai `I`, tetapi di dalam garisnya ditambahkan sebuah **titik**.
- Huruf `S`, `T`, `U`, `V` membentuk pola segitiga/sudut lancip dari silang X.
- Huruf `W`, `X`, `Y`, `Z` membentuk pola yang sama dengan silang X tetapi memiliki **titik**.

## Polybius Square

Ditemukan oleh sejarawan Yunani kuno bernama Polybius. Konsepnya sederhana: menyusun alfabet ke dalam kisi tabel 5x5, lalu setiap huruf diwakili oleh sepasang angka koordinat (nomor baris dan nomor kolom).

### Tabel Polybius 5x5

Karena tabel 5x5 hanya menampung 25 kotak, huruf `I` dan `J` biasanya disatukan di kotak yang sama.

```text
    1   2   3   4   5
  +---+---+---+---+---+
1 | A | B | C | D | E |
  +---+---+---+---+---+
2 | F | G | H | I/J | K |
  +---+---+---+---+---+
3 | L | M | N | O | P |
  +---+---+---+---+---+
4 | Q | R | S | T | U |
  +---+---+---+---+---+
5 | V | W | X | Y | Z |
  +---+---+---+---+---+
```

Setiap huruf dibaca: `(Baris, Kolom)`.

Contoh:
- `H` = Baris 2, Kolom 3 -> `23`
- `E` = Baris 1, Kolom 5 -> `15`
- `L` = Baris 3, Kolom 1 -> `31`
- `P` = Baris 3, Kolom 5 -> `35`

Pesan `HELP` menjadi: `23 15 31 35`.

### Implementasi Python untuk Polybius Square

```python
GRID = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'], # J digabung dengan I
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

def polybius_decode(numbers):
    # numbers contoh: "23 15 31 35" atau "23153135"
    digits = [c for c in numbers if c.isdigit()]
    plain = []
    for i in range(0, len(digits), 2):
        row = int(digits[i]) - 1
        col = int(digits[i+1]) - 1
        if 0 <= row < 5 and 0 <= col < 5:
            plain.append(GRID[row][col])
    return "".join(plain)

cipher_text = "23 15 31 31 34"
print("Hasil Dekripsi:", polybius_decode(cipher_text)) # HELLO
```

## Cara Mengenali Cipher Ini di CTF

### Mengenali Pigpen:
1. **Soal Berupa File Gambar**: Tantangan CTF memberikan file `.png`, `.jpg`, atau screenshot yang berisi garis-garis siku, kotak, dan silang bertitik.
2. Tidak ada teks yang bisa langsung di-copy paste ke terminal.
3. Begitu kamu melihat sudut siku-siku bertitik, kamu bisa langsung yakin 100 persen bahwa itu Pigpen.

### Mengenali Polybius Square:
1. Ciphertext hanya terdiri dari angka `1, 2, 3, 4, 5` (atau `0` sampai `4` untuk varian berbasis indeks 0).
2. Jumlah digit angka selalu genap.
3. Terkadang angka diganti menjadi huruf koordinat, misalnya varian ADFGX / ADFGVX yang menggunakan huruf tabel tertentu.

## Tools Pemecah di CTF

- **Pigpen Cipher**:
  - Buka [dcode.fr Pigpen Cipher](https://www.dcode.fr/pigpen-cipher). Di situs tersebut tersedia keyboard visual berupa simbol-simbol Pigpen. Cukup klik simbol yang sesuai dengan gambar di soal, dan dcode akan langsung menerjemahkannya ke huruf latin.
- **Polybius Square**:
  - CyberChef: Recipe "Polybius Cipher".
  - [dcode.fr Polybius Square](https://www.dcode.fr/polybius-cipher).

## Latihan Kecil

1. Pecahkan pesan koordinat Polybius berikut:
```text
43 15 13 45 42 24 44 54
```

2. Jika kamu menemukan gambar kotak persegi dengan satu titik di tengahnya pada soal bergambar, huruf apakah yang dimaksud dalam Pigpen standar?

## Ringkasan

- Pigpen Cipher adalah substitusi monoalfabetik menggunakan simbol visual geometris (kisi pagar, silang, dan titik).
- Di CTF, Pigpen hampir selalu disajikan dalam bentuk file gambar atau font khusus.
- Polybius Square mengubah huruf menjadi sepasang angka koordinat baris dan kolom pada tabel 5x5.
- Ciri khas Polybius: teks hanya tersusun dari angka 1 sampai 5 dengan panjang digit genap.
- Keduanya sangat mudah dipecahkan menggunakan tool online seperti dcode.fr atau CyberChef.
