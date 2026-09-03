#cybersecurity 

Pada materi sebelumnya tentang [Vigenere Cipher](Vigenere%20Cipher.md), kita melihat bahwa kelemahan terbesarnya adalah kata kunci yang berulang-ulang secara periodik. Pengulangan ini memungkinkan penyerang mencari panjang kunci menggunakan metode Kasiski maupun Index of Coincidence.

Dua cipher klasik penting diciptakan untuk memodifikasi atau memperbaiki mekanisme Vigenere: **Autokey Cipher** dan **Beaufort Cipher**.

## Autokey Cipher

Fakta sejarah yang menarik: algoritma yang sebenarnya diciptakan oleh Blaise de Vigenere pada tahun 1586 adalah Autokey ini, sedangkan Vigenere yang kita kenal sekarang sebenarnya ditemukan oleh Giovan Battista Bellaso.

### Cara Kerja Autokey

Pada Autokey Cipher, kata kunci pendek (disebut **primer** atau seed) hanya digunakan untuk huruf-huruf pertama. Setelah primer habis, aliran kunci selanjutnya disambung langsung dengan **isi plaintext itu sendiri**.

Dengan cara ini, kunci tidak pernah berulang dalam siklus yang teratur.

Contoh:
- Plaintext : `ATTACKATDAWN`
- Primer    : `QUEEN` (5 huruf)

Aliran kunci yang terbentuk:
```text
Plaintext   : A T T A C | K A T D A W N
Primer      : Q U E E N | A T T A C K A  (diambil dari plaintext)
Aliran Kunci: Q U E E N   K A T D A W N
```

Rumus enkripsi persis seperti Vigenere:
```text
C = (P + K) mod 26
```

### Cara Dekripsi Autokey

Dekripsi Autokey harus dilakukan secara berurutan huruf demi huruf:
1. Dekripsi huruf-huruf awal menggunakan kata kunci primer: $P_i = (C_i - K_i) \bmod 26$.
2. Setiap huruf plaintext yang berhasil ditemukan langsung ditempelkan ke barisan kunci untuk mendekripsi huruf berikutnya.

## Beaufort Cipher

Diciptakan oleh Sir Francis Beaufort pada tahun 1857 (tokoh yang juga menciptakan skala kecepatan angin Beaufort).

Beaufort cipher mirip dengan Vigenere, tetapi memiliki satu perbedaan matematis mendasar: **urutan pengurangannya dibalik**.

### Rumus Beaufort

- **Enkripsi**:
  ```text
  C = (K - P) mod 26
  ```
- **Dekripsi**:
  ```text
  P = (K - C) mod 26
  ```

Perhatikan keistimewaan rumus ini: rumus enkripsi dan dekripsinya **sama persis**. Ini membuat Beaufort menjadi cipher timbal-balik (reciprocal cipher). Fungsi yang sama yang digunakan untuk menyandikan teks juga dapat digunakan untuk membuka kembali teks tersebut.

## Implementasi Script Python

Berikut script Python untuk Autokey dan Beaufort:

```python
def autokey_decrypt(cipher, primer):
    primer = primer.upper()
    cipher = [c for c in cipher.upper() if c.isalpha()]
    plain = []
    
    # Kunci awal adalah primer
    key_stream = [ord(k) - ord('A') for k in primer]
    
    for i, c in enumerate(cipher):
        c_val = ord(c) - ord('A')
        k_val = key_stream[i]
        p_val = (c_val - k_val) % 26
        plain.append(chr(p_val + ord('A')))
        # Tambahkan plaintext yang baru terungkap ke aliran kunci
        key_stream.append(p_val)
        
    return "".join(plain)

def beaufort_cipher(text, key):
    # Enkripsi dan dekripsi menggunakan fungsi yang sama
    text = [c for c in text.upper() if c.isalpha()]
    key = [c for c in key.upper() if c.isalpha()]
    result = []
    k_len = len(key)
    
    for i, ch in enumerate(text):
        c_val = ord(ch) - ord('A')
        k_val = ord(key[i % k_len]) - ord('A')
        out_val = (k_val - c_val) % 26
        result.append(chr(out_val + ord('A')))
        
    return "".join(result)

# Uji coba Autokey
cipher_autokey = "QNXEG UKXGD"
primer_key = "QUEEN"
print("Hasil Autokey:", autokey_decrypt(cipher_autokey, primer_key))

# Uji coba Beaufort
pesan = "SECRET"
kunci = "KEY"
terenkripsi = beaufort_cipher(pesan, kunci)
terbuka = beaufort_cipher(terenkripsi, kunci)
print(f"Beaufort Encrypt: {terenkripsi}, Decrypt: {terbuka}")
```

## Cara Mengenali dan Memecahkan di CTF

1. **Autokey Cipher**:
   - Jika teks terlihat seperti Vigenere tetapi analisis Kasiski atau Index of Coincidence tidak menemukan panjang periode kunci yang cocok.
   - Jika kata kunci diketahui tetapi didekripsi dengan Vigenere standar hanya huruf awal saja yang terbaca benar sedangkan sisanya rusak.
   - Tool pemecah: [dcode.fr Autokey Cipher](https://www.dcode.fr/autokey-cipher).

2. **Beaufort Cipher**:
   - Pola ciphertext mirip Vigenere.
   - Jika kunci Vigenere diketahui tetapi didekripsi menghasilkan huruf kacau, coba balik operasinya menggunakan Beaufort.
   - Tool pemecah: CyberChef (Recipe "Beaufort Decode") atau [dcode.fr Beaufort](https://www.dcode.fr/beaufort-cipher).

## Latihan Kecil

Gunakan script Beaufort di atas atau CyberChef untuk mendekripsi teks berikut dengan kunci `FLAG`:

```text
Ciphertext: T N B Q
```

Jelaskan mengapa fungsi yang sama bisa dipakai baik untuk proses enkripsi maupun proses dekripsi.

## Ringkasan

- Autokey menyambung kata kunci awal dengan isi plaintext itu sendiri untuk menghilangkan periode pengulangan kunci.
- Dekripsi Autokey harus dilakukan secara sekuensial huruf demi huruf.
- Beaufort cipher menggunakan rumus $(K - P) \bmod 26$.
- Beaufort bersifat timbal-balik (reciprocal): enkripsi dan dekripsi menggunakan operasi yang identik.
