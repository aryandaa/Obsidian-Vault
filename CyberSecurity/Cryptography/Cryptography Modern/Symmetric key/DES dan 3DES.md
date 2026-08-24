#cybersecurity 

Sebelum AES, ada **DES** (Data Encryption Standard). DES adalah standar enkripsi resmi Amerika Serikat dari tahun 1977 sampai digantikan oleh AES. Di CTF, DES jarang dipakai untuk hal yang serius, tetapi tetap perlu kamu kenal karena:

1. Banyak soal lama atau soal "custom cipher" yang meniru gaya DES.
2. Banyak sistem lama yang masih memakai turunannya.
3. Cerita kelemahannya mengajarkan pelajaran penting tentang ukuran kunci.

## Cara kerja DES secara singkat

DES termasuk block cipher, sama seperti AES: pesan dipotong menjadi blok, lalu tiap blok dienkripsi dengan kunci.

Perbedaan utamanya dengan AES:

```text
DES : blok 8 byte (64 bit), kunci efektif 7 byte (56 bit)
AES : blok 16 byte, kunci 16/24/32 byte
```

Proses internalnya mirip dengan AES secara konsep: campur blok dengan kunci, acak posisi, ganti byte, ulang beberapa putaran. DES memakai 16 putaran. Kamu tidak perlu hafal detailnya.

## Kelemahan DES: kunci terlalu pendek

Ini pelajaran paling penting dari materi ini.

Kunci DES cuma 56 bit. Artinya ada 2^56 kemungkinan kunci. Pada tahun 1977 itu terlihat mustahil, tetapi pada tahun 1998 sebuah mesin bernama Deep Crack (dibangun Electronic Frontier Foundation) berhasil memecahkan DES dalam 56 jam. Pada tahun 1999, memecahkannya dalam 22 jam.

Intinya: **56 bit tidak cukup di era komputer modern.** Kunci harus cukup panjang supaya penyerang tidak bisa mencoba semua kemungkinan.

## 3DES (Triple DES)

Karena DES sudah lemah tetapi masih banyak dipakai, orang membuat **3DES**: menjalankan DES tiga kali dengan dua atau tiga kunci.

```text
Enkripsi : E_K1(D_K2(E_K3(pesan)))
```

3DES memperpanjang kunci efektif menjadi 112 atau 168 bit, jadi jauh lebih kuat daripada DES biasa. Tetapi 3DES lambat dan akhirnya juga ditinggalkan. Sejak 2023, 3DES resmi tidak dianjurkan lagi.

## DES di CTF

DES muncul di CTF dalam beberapa bentuk:

1. **Soal dekripsi langsung**: script challenge memakai DES, kunci ada di script.

```python
from Crypto.Cipher import DES

key = b"8bytekey"   # kunci DES harus tepat 8 byte!
cipher = DES.new(key, DES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
```

2. **Soal brute force kunci kecil**: kadang kunci DES hanya 3 atau 4 byte (sisanya nol). Karena ruang kuncinya kecil, kamu bisa mencoba semua kemungkinan:

```python
from Crypto.Cipher import DES
import itertools

ciphertext = bytes.fromhex("...")

# coba semua kunci 4 byte, sisanya nol
for i in range(2**32):
    key = i.to_bytes(8, 'big')   # 4 byte angka, 4 byte nol
    if b'crypto{' in DES.new(key, DES.MODE_ECB).decrypt(ciphertext):
        print(key)
        break
```

3. **Soal yang memakai DES sebagai "obfuscation"**: hasilnya tetap bisa dibuka dengan kunci yang diberikan di soal.

## Cara mengenali DES di soal

- Kunci harus tepat 8 byte (kalau tidak, bukan DES).
- Script memakai `DES.new(...)`.
- Bloknya 8 byte, jadi panjang ciphertext kelipatan 8 byte (16 karakter hex per blok).

## Ringkasan

- DES = block cipher lama dengan kunci 56 bit.
- Kunci 56 bit terlalu pendek dan sudah bisa dipecahkan dengan mesin khusus.
- 3DES = DES dijalankan tiga kali, lebih kuat tapi ditinggalkan juga.
- Di CTF: cek dulu apakah kuncinya kecil dan bisa di-brute force.
- Pelajaran utamanya: ukuran kunci menentukan keamanan. Ini alasan AES-128/256 dipakai sekarang.
