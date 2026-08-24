#cybersecurity 

**AES** (Advanced Encryption Standard) adalah cipher symmetric paling penting di dunia saat ini. Hampir semua yang kamu pakai setiap hari memakainya di dalamnya: HTTPS, WiFi, file terenkripsi, database, bahkan aplikasi chat. Kalau ada satu cipher yang harus kamu pahami dengan baik, ini dia.

AES lahir dari sayembara yang diadakan pemerintah Amerika Serikat tahun 1997. Hasilnya, sebuah algoritma bernama Rijndael (dari nama pembuatnya, Vincent Rijmen dan Joan Daemen) dipilih menjadi standar. Sejak 2001, AES menjadi standar resmi.

## Konsep inti: satu kunci, blok 16 byte

AES bekerja seperti ini:

- Pesan dipotong menjadi blok berukuran **16 byte** (128 bit) setiap kali diproses.
- Kunci bisa berukuran **16 byte (AES-128)**, **24 byte (AES-192)**, atau **32 byte (AES-256)**.
- Kunci yang sama dipakai untuk enkripsi dan dekripsi.

Jadi kalau kamu melihat "AES-256", artinya kuncinya 32 byte. Semakin panjang kunci, semakin banyak kombinasi yang harus dicoba penyerang.

## Cara kerja (tanpa bikin pusing)

Kamu tidak perlu menghafal langkah internal AES untuk bisa menggunakannya. Yang perlu kamu pahami hanyalah gambaran besarnya:

AES menganggap 16 byte sebagai kotak 4x4, lalu mengulang beberapa putaran "pengadukan":

```text
1. AddRoundKey  : campur blok dengan kunci (XOR)
2. SubBytes     : ganti tiap byte dengan byte lain dari tabel tetap
3. ShiftRows    : geser posisi baris
4. MixColumns   : campur kolom
5. kembali ke AddRoundKey, dst.
```

Jumlah putaran tergantung ukuran kunci:

```text
AES-128 → 10 putaran
AES-192 → 14 putaran
AES-256 → 14 putaran
```

Intinya: tiap putaran mengaduk data dengan aturan yang bisa dibalik. Karena aturannya bisa dibalik, dekripsi tinggal menjalankan semuanya terbalik dengan kunci yang sama. Seperti mencuci kartu: kalau kamu tahu cara mengacaknya, kamu bisa mengembalikan urutan semula.

Yang penting untuk kamu: **setiap langkah internal AES itu deterministik dan publik.** Keamanan AES tidak bergantung pada kerahasiaan cara kerjanya, melainkan pada kerahasiaan kunci. Ini prinsip Kerckhoffs yang sudah kamu lihat di materi Enigma.

## Kenapa AES dianggap aman

- Kunci 128 bit punya 2^128 kemungkinan. Angka itu sangat besar, mustahil dicoba satu per satu bahkan dengan komputer tercepat di dunia.
- Sampai hari ini, tidak ada serangan yang benar-benar praktis terhadap AES yang dipakai dengan benar.
- Yang sering diserang bukan AES-nya, tetapi **cara pakainya**: mode operasi yang salah, kunci yang pendek atau bisa ditebak, atau implementasi yang bocor. Ini akan dibahas di materi mode operasi.

## AES di CTF

Di CTF, AES biasanya sudah "jadi": soal memberikan ciphertext, dan kamu tinggal mendekripsi dengan kunci dan mode yang diberikan. Kuncinya sering ada di dalam script challenge yang disertakan.

Python pakai library `pycryptodome`:

```bash
pip install pycryptodome
```

Contoh dekripsi AES-ECB:

```python
from Crypto.Cipher import AES

key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
ciphertext = bytes.fromhex("e8d8e0f4...")

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
```

Contoh dekripsi AES-CBC (mode yang paling sering muncul):

```python
from Crypto.Cipher import AES

key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
iv = bytes.fromhex("101112131415161718191a1b1c1d1e1f")
ciphertext = bytes.fromhex("...")

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
```

Pola yang selalu sama di soal CTF: cari `key` dan `iv` di script challenge, lalu tempel ke script di atas. Flag biasanya muncul sebagai teks terbaca setelah dekripsi.

Kadang kunci atau IV ditulis dalam bentuk string biasa, bukan hex. Kalau begitu, pakai `key = b"string_kunci"` langsung.

## Cara mengenali AES di soal

- Ciphertext berupa hex yang panjangnya kelipatan 16 byte (32 karakter hex per blok).
- Script challenge memakai `AES.new(...)`, `encrypt`, `decrypt`.
- Ada `key` dan mungkin `iv` yang terlihat di script.

## Latihan kecil

Soal memberi script seperti ini:

```python
from Crypto.Cipher import AES

key = b"rahasia_super_12"
iv = b"awal_blok_16!!!!"
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
ciphertext = cipher.encrypt(b"crypto{coba_awal_aes}")
print(ciphertext.hex())
```

Tugasmu: jalankan script itu sendiri untuk mendapatkan ciphertext, lalu tulis script dekripsi yang mengembalikan pesan aslinya. Pastikan kamu bisa men-decode hasilnya menjadi `crypto{coba_awal_aes}`.

## Ringkasan

- AES = standar enkripsi symmetric modern, blok 16 byte.
- Kunci 16/24/32 byte, dipakai sama untuk enkripsi dan dekripsi.
- Keamanannya ada di kunci, bukan di kerahasiaan algoritma.
- Di CTF: cari key dan iv di script, lalu dekripsi dengan pycryptodome.
- Yang sering bocor bukan AES-nya, tapi cara pemakaiannya. Itu bahasan berikutnya.
