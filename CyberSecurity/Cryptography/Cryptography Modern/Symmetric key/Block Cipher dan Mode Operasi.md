#cybersecurity 

Block cipher seperti AES bekerja per blok 16 byte. Pertanyaannya: bagaimana caranya mengenkripsi pesan yang lebih panjang dari 16 byte? Jawabannya: pesan dipotong menjadi blok-blok, lalu blok-blok itu disusun dengan sebuah **mode operasi**.

Pemilihan mode operasi ini sangat penting. Mode yang salah bisa membuat cipher yang kuat sekalipun menjadi bocor. Materi ini menjelaskan mode yang paling sering muncul di CTF: **ECB** dan **CBC**.

## ECB: mode paling sederhana dan paling berbahaya

**ECB** (Electronic Codebook) bekerja dengan cara yang paling polos: setiap blok dienkripsi sendiri-sendiri dengan kunci yang sama.

```text
Blok 1 → AES(kunci) → Blok 1 terenkripsi
Blok 2 → AES(kunci) → Blok 2 terenkripsi
Blok 3 → AES(kunci) → Blok 3 terenkripsi
```

Masalahnya: **blok yang sama akan menghasilkan ciphertext yang sama.** Kalau dua blok plaintext identik, dua blok ciphertext-nya juga identik. Ini bocoran informasi yang sangat besar.

### Contoh terkenal: pinguin ECB

Ada gambar pinguin yang terkenal di dunia kriptografi. Kalau gambar itu dienkripsi dengan AES-ECB, hasilnya masih terlihat seperti pinguin! Pola warna yang sama tetap terlihat karena blok yang sama menghasilkan output yang sama. Gambar yang sama dienkripsi dengan mode lain (seperti CBC) berubah menjadi noise acak.

Inilah alasan ECB dilarang untuk data yang lebih dari satu blok.

### Mendeteksi ECB di CTF

Karena blok yang sama menghasilkan ciphertext yang sama, kamu bisa mendeteksi ECB dengan cara: hitung blok-blok yang berulang di ciphertext.

```python
from Crypto.Cipher import AES

ciphertext = bytes.fromhex("...")
blok = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
unik = set(blok)
print(f"total blok: {len(blok)}, blok unik: {len(unik)}")

# kalau jumlah blok unik jauh lebih sedikit dari total, kemungkinan besar ECB
if len(unik) < len(blok):
    print("Kemungkinan ECB: ada blok yang berulang!")
```

Di soal CTF, ini sering jadi langkah pertama: cek apakah ciphertext punya blok berulang. Kalau iya, itu ECB, dan ada serangan khusus yang bisa dipakai (lihat di bawah).

### Serangan ECB copy-paste

Karena blok dienkripsi independen, kamu bisa **memindahkan blok** antar ciphertext tanpa merusak dekripsi. Misalnya sebuah aplikasi mengenkripsi data pengguna yang berisi role, kamu bisa menyalin blok dari ciphertext pengguna admin ke ciphertext pengguna lain. Serangan ini disebut ECB cut-and-paste, dan muncul cukup sering di CTF tingkat menengah.

## CBC: mode yang lebih aman

**CBC** (Cipher Block Chaining) memperbaiki kelemahan ECB dengan merantai blok: setiap blok di-XOR dengan ciphertext blok sebelumnya sebelum dienkripsi.

```text
Blok 1 di-XOR dengan IV, lalu dienkripsi → C1
Blok 2 di-XOR dengan C1, lalu dienkripsi → C2
Blok 3 di-XOR dengan C2, lalu dienkripsi → C3
```

Karena setiap blok bergantung pada blok sebelumnya, blok yang sama di plaintext menghasilkan ciphertext yang berbeda. Pola pinguin hilang.

Komponen penting CBC:

```text
IV (Initialization Vector) : blok awal 16 byte untuk memulai rantai
Kunci                      : sama untuk semua blok
```

Dekripsi CBC kebalikannya: dekripsi blok, lalu XOR dengan ciphertext blok sebelumnya.

### Di CTF: cari key dan IV

Mode CBC adalah yang paling sering muncul di soal AES. Script challenge biasanya seperti ini:

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b"..."        # 16/24/32 byte
iv = b"..."         # 16 byte
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
ciphertext = cipher.encrypt(pad(flag, 16))
```

Untuk mendekripsi:

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b"..."
iv = b"..."
ciphertext = bytes.fromhex("...")

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
plaintext = unpad(cipher.decrypt(ciphertext), 16)
print(plaintext)
```

Perhatikan `unpad`: karena blok harus pas 16 byte, pesan ditambal dengan padding sebelum enkripsi, dan harus dibuka lagi setelah dekripsi.

## Mode lain yang perlu kamu kenal namanya

```text
CTR : blok berubah menjadi stream dengan counter, tidak butuh padding
GCM : mode modern dengan autentikasi, dipakai di HTTPS
OFB : mirip CBC tapi tanpa chaining blok
CFB : varian lain dari CBC
```

CTR dan GCM adalah mode yang paling dipakai di dunia nyata sekarang. Di CTF menengah ke atas, GCM dan CTR juga muncul, terutama untuk serangan nonce reuse.

## Cara menentukan mode dari soal

Lihat script challenge:

```text
MODE_ECB   → tidak ada iv, blok independen
MODE_CBC   → ada iv, blok dirantai
MODE_CTR   → ada nonce, bekerja seperti stream
MODE_GCM   → ada nonce dan tag
```

Kalau tidak yakin, coba dekripsi dengan ECB dulu. Kalau hasilnya berantakan tapi sebagian terbaca, coba CBC dengan iv.

## Ringkasan

- Block cipher butuh mode operasi untuk pesan panjang.
- ECB: blok independen, bocor karena blok sama menghasilkan ciphertext sama. Dilarang untuk data panjang.
- CBC: blok dirantai dengan IV, lebih aman, paling sering muncul di CTF.
- Di CTF: tentukan mode dari script, cari key dan iv, lalu dekripsi dengan pycryptodome.
- Jangan lupa `pad` dan `unpad` saat blok tidak pas 16 byte.
