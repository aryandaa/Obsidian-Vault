#cybersecurity 

Bayangkan kamu menemukan teks seperti ini di sebuah soal CTF:

```text
Gur frperg pbqr vf urnira
```

Hurufnya aneh, tapi pola hurufnya terlihat seperti bahasa Inggris biasa. Kemungkinan besar ini cipher substitusi. Materi ini mengajarkan senjata utamanya: **frequency analysis**, alias analisis seberapa sering sebuah huruf muncul.

## Apa itu substitusi monoalfabetik

Cipher substitusi sederhana mengganti setiap huruf dengan huruf lain secara tetap. Misalnya:

```text
A → Q
B → X
C → Z
...
```

Setiap huruf A di plaintext selalu menjadi Q di ciphertext. Caesar, Atbash, dan Affine sebenarnya adalah kasus khusus dari cipher ini. Yang membedakan hanyalah aturan penggantiannya.

Contoh:

```text
Plaintext : THE QUICK BROWN FOX
Substitusi: XYZ ... (satu huruf diganti satu huruf lain)
```

Kalau aturannya acak, brute force tidak mungkin (ada 26! kemungkinan, jumlahnya sangat besar). Tapi kita tidak perlu mencoba semuanya, karena ada pola yang bisa dimanfaatkan.

## Bahasa manusia itu tidak acak

Dalam bahasa Inggris, huruf-huruf tidak muncul dengan frekuensi yang sama. Huruf E jauh lebih sering muncul daripada Z. Urutan kira-kira seperti ini:

```text
E (paling sering)
T
A
O
I
N
S
H
R
...
Z (paling jarang)
```

Kalau di sebuah ciphertext huruf Q paling sering muncul, besar kemungkinan Q menggantikan huruf E di plaintext.

## Frequency analysis step by step

Langkah 1: hitung frekuensi tiap huruf di ciphertext.

```python
from collections import Counter

cipher = "GUR FRPERG PBQR VF URINRA"
cipher = cipher.replace(" ", "")
freq = Counter(cipher)
for huruf, jumlah in freq.most_common():
    print(huruf, jumlah)
```

Output akan menunjukkan huruf yang paling sering muncul. Di contoh ini, huruf R paling sering muncul, dan itu petunjuk kuat bahwa R menggantikan huruf E.

Langkah 2: ganti huruf yang paling sering dengan E, lalu tebak pola huruf berikutnya berdasarkan kata pendek.

Kata pendek sangat membantu:

```text
1 huruf  → A atau I
2 huruf  → of, to, in, it, is, be, as, at, so, we, he, by, or
3 huruf  → the, and, for, are, but, not, you, all
```

Kalau kamu melihat kata 3 huruf yang berulang di ciphertext, coba tebak itu "the". Itu akan langsung membuka 3 huruf sekaligus.

Langkah 3: ulangi sampai seluruh pesan terbaca. Ini seperti menyelesaikan puzzle silang.

Contoh lengkap, teks dari soal CTF:

```text
Gur frperg pbqr vf urnira
```

Kalau kamu analisis frekuensi dan tebak pola, hasilnya adalah:

```text
The secret code is hidden
```

Kebetulan contoh ini sebenarnya ROT13, tapi prosesnya sama.

## Tool otomatis

Di CTF, jangan ragu pakai tool:

- [dcode.fr Monoalphabetic](https://www.dcode.fr/monoalphabetic-substitution): analisis otomatis dengan kamus.
- [quipqiup.com](https://www.quipqiup.com): solver substitusi terbaik, tempel ciphertext dan langsung dapat solusi.
- CyberChef: recipe "Substitution".

Kalau di soal ada beberapa kalimat, quipqiup hampir selalu langsung benar.

## Bigram dan trigram

Selain frekuensi huruf tunggal, pola pasangan dan tiga huruf juga membantu:

```text
Bigram umum : th, he, in, er, an, re, on, at, en, nd
Trigram umum: the, and, tha, ent, ion, tio, for, nde
```

Kalau ciphertext mengandung pasangan yang sangat sering muncul, coba tebak itu "th" atau "he".

## Cara mengenali cipher substitusi

- Hanya huruf, tanpa pola pergeseran yang jelas.
- Panjang kata sama dengan plaintext (spasi tetap).
- Frekuensi huruf tidak merata (ada yang menonjol).
- Caesar/Atbash/Affine tidak berhasil membukanya.

## Latihan kecil

Pecahkan ciphertext berikut (kalimat pendek, pakai quipqiup atau analisis manual):

```text
Vjku ku c pqf g curgtvc o gcuwig
```

Petunjuk: huruf yang paling sering muncul kemungkinan menggantikan huruf E. Kalau sudah ketemu, tuliskan plaintextnya.

## Ringkasan

- Substitusi monoalfabetik mengganti tiap huruf dengan satu huruf lain yang tetap.
- Bahasa manusia tidak acak: huruf E paling sering muncul.
- Frequency analysis memetakan huruf yang sering muncul di ciphertext ke huruf yang sering muncul di bahasa aslinya.
- Kata pendek (the, and, of) adalah kunci untuk menebak lebih cepat.
- Di CTF, quipqiup dan dcode menyelesaikan ini dalam hitungan detik.
