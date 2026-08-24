#cybersecurity 

Block cipher memotong pesan menjadi blok. **Stream cipher** bekerja dengan cara yang berbeda: ia menghasilkan aliran kunci (keystream) dan meng-XOR-nya dengan pesan byte demi byte.

```text
Pesan    :  H E L L O
Keystream:  K1 K2 K3 K4 K5
Cipher   :  (H^K1) (E^K2) (L^K3) (L^K4) (O^K5)
```

Kalau kamu sudah belajar XOR di sesi Pengenalan, ini terasa familier: XOR adalah operasi yang bisa dibalik, jadi ciphertext di-XOR dengan keystream yang sama akan mengembalikan pesan asli.

## Kenapa pakai stream cipher

- Tidak butuh padding, karena bekerja per byte, bukan per blok.
- Cocok untuk data yang panjangnya tidak pasti, seperti video atau chat.
- Cepat di hardware.

Contoh stream cipher yang terkenal: **RC4** (dipakai WiFi lama dan TLS lama) dan **ChaCha20** (dipakai di aplikasi modern seperti WhatsApp dan Google).

## One-Time Pad: stream cipher yang sempurna

Bayangkan keystream-nya **benar-benar acak, sepanjang pesan, dan hanya dipakai sekali**. Ini disebut One-Time Pad (OTP), dan secara matematis terbukti **tidak bisa dipecahkan**. Ini satu-satunya cipher yang aman tanpa syarat.

```text
Pesan  : ATTACK (dalam biner)
Kunci  : 101100 (acak, sekali pakai)
Hasil  : XOR dari keduanya
```

Masalahnya: untuk mengirim pesan sepanjang 1 MB, kamu harus mengirim kunci sepanjang 1 MB juga, dan kunci itu hanya bisa dipakai sekali. Distribusi kunci menjadi masalah besar. Itu sebabnya OTP jarang dipakai praktis, tapi konsepnya jadi fondasi pemahaman stream cipher.

## Masalah besar: keystream dipakai ulang

Stream cipher menjadi sangat lemah kalau **keystream yang sama dipakai untuk dua pesan berbeda**. Ini disebut keystream reuse, dan ini adalah topik favorit di CTF.

Kalau kamu punya dua ciphertext dari pesan yang di-XOR dengan keystream yang sama:

```text
C1 = P1 XOR K
C2 = P2 XOR K
```

Maka:

```text
C1 XOR C2 = P1 XOR P2
```

Keystream-nya hilang! Yang tersisa hanyalah XOR dari dua pesan asli. Kalau kamu bisa menebak salah satu pesan (misalnya salah satunya adalah teks dengan pola standar), kamu bisa membuka yang lainnya.

Contoh klasik di CTF: beberapa flag dienkripsi dengan keystream yang sama.

```python
# C1 XOR C2 menghilangkan kunci
c1 = bytes.fromhex("...")
c2 = bytes.fromhex("...")
x = bytes(a ^ b for a, b in zip(c1, c2))
print(x)  # ini P1 XOR P2
```

Kalau salah satu pesan diketahui (misalnya berisi kata "flag{" di awal), kamu bisa memulihkan potongan keystream:

```python
known = b"crypto{"
keystream = bytes(a ^ b for a, b in zip(known, c1))
```

Lalu gunakan keystream itu untuk mendekripsi bagian lain dari c2.

## RC4 di CTF

RC4 dulu sangat populer, sekarang sudah dianggap lemah. Di CTF, RC4 muncul dengan dua cara:

1. **Dekripsi langsung** dengan kunci yang diberikan:

```python
from Crypto.Cipher import ARC4

key = b"kunci_rahasia"
cipher = ARC4.new(key)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
```

2. **Keystream reuse**, seperti di atas: dua ciphertext yang memakai keystream sama dari kunci yang sama.

## Cara mengenali stream cipher di soal

- Tidak ada padding, tidak ada blok.
- Panjang ciphertext sama persis dengan plaintext.
- Script memakai `ARC4.new(...)`, `ChaCha20.new(...)`, atau melakukan XOR manual dengan keystream.
- Kalau ada dua ciphertext dengan panjang sama dan sepertinya "dari kunci yang sama", curigai keystream reuse.

## Latihan kecil

Dua pesan dienkripsi dengan keystream yang sama:

```text
C1 = 1c1c0104...
C2 = 1e1a0000...
```

Kamu tahu bahwa P1 diawali dengan `crypto{`. Tulis script untuk menghitung keystream dari potongan awal C1, lalu gunakan untuk mendekripsi awal C2. Petunjuk: XOR `crypto{` dengan 7 byte pertama C1.

## Ringkasan

- Stream cipher = XOR pesan dengan keystream byte demi byte.
- One-Time Pad sempurna tapi tidak praktis karena kunci sepanjang pesan.
- Keystream reuse adalah bencana: C1 XOR C2 menghilangkan kunci.
- Di CTF, keystream reuse adalah salah satu soal stream cipher paling umum.
- RC4 sudah lemah, ChaCha20 yang dipakai sekarang.
