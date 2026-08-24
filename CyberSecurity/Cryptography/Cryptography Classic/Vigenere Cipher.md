#cybersecurity 

Caesar, Atbash, dan Affine punya satu kelemahan besar: **satu huruf selalu diganti dengan huruf yang sama**. Huruf H di dalam pesan selalu menjadi huruf yang sama di ciphertext. Itu disebut substitusi monoalfabetik, dan mudah dipecahkan dengan analisis frekuensi.

Vigenere Cipher datang untuk memperbaiki masalah ini. Ia menggunakan **kata kunci** sehingga huruf yang sama bisa berubah menjadi huruf yang berbeda tergantung posisinya. Ini disebut **polyalphabetic substitution**, dan selama ratusan tahun cipher ini dianggap tidak bisa dipecahkan.

## Cara kerja

Bayangkan tabel alfabet yang disusun seperti berikut (disebut tabel Vigenere atau tabula recta):

```text
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
...
```

Cara pakainya: setiap huruf pesan digeser, tetapi **besar pergeserannya ditentukan oleh huruf kata kunci** yang bersesuaian.

Contoh:

```text
Pesan     : HELLOWORLD
Kata kunci: KEYKEYKEYK
```

- Huruf H digeser sebesar huruf K (K = pergeseran 10). H + 10 = R.
- Huruf E digeser sebesar E (pergeseran 4). E + 4 = I.
- Huruf L digeser sebesar Y (pergeseran 24). L + 24 = J.
- Dan seterusnya.

Hasilnya:

```text
HELLOWORLD dengan kunci KEY → RIJVS UYVJN (contoh)
```

Perhatikan: huruf L yang muncul dua kali di pesan menjadi huruf yang berbeda di ciphertext. Itulah keunggulan Vigenere.

## Kunci harus diulang

Kata kunci diulang-ulang sampai sepanjang pesan:

```text
Pesan     : HELLOWORLD
Kunci     : KEYKEYKEYK
```

Kelemahan inilah yang akhirnya membuat Vigenere bisa dipecahkan: pola perulangan kunci bisa dideteksi.

## Memecahkan Vigenere

Ada dua teknik utama, dan keduanya sudah otomatis ada di tool:

1. **Kasiski examination**: mencari pola yang berulang di ciphertext untuk menebak panjang kunci.
2. **Index of coincidence**: cara statistik untuk menebak panjang kunci.

Setelah panjang kunci ketemu, ciphertext bisa dipecah menjadi beberapa bagian (masing-masing bagian adalah Caesar dengan pergeseran tetap), lalu masing-masing dipecahkan dengan analisis frekuensi.

Untungnya, kamu tidak perlu melakukan ini manual di CTF. Tool sudah menyelesaikan semuanya:

- [dcode.fr Vigenere](https://www.dcode.fr/vigenere-cipher): tempel ciphertext, otomatis cari kunci.
- CyberChef: recipe "Vigenere Decode".
- Python pakai library:

```python
# pip install pycipher
from pycipher import Vigenere

# Kalau kunci sudah ketahuan
cipher = "RIJVS UYVJN"
print(Vigenere("KEY").decipher(cipher))
```

Untuk menebak kunci secara otomatis, pakai tool seperti [pygenere](https://github.com/atomicobject/pygenere) atau dcode.

## Cara mengenali Vigenere

- Tidak terbaca dengan Caesar/Atbash biasa.
- Ciphertext-nya huruf semua, spasi tetap ada.
- Kalau huruf yang sama di plaintext menjadi huruf beda di ciphertext, besar kemungkinan ini polialfabetik.
- Panjangnya kira-kira sama dengan plaintext.

## Latihan kecil

Coba pecahkan ciphertext berikut (kunci berupa kata bahasa Inggris, dan hasilnya mengandung kata "flag"):

```text
VFLQ HPEJ XWDB
```

Kalau mentok, gunakan dcode dan biarkan ia menebak kuncinya. Setelah ketemu, coba jelaskan mengapa huruf yang sama bisa terenkripsi menjadi huruf yang berbeda di ciphertext ini.

## Ringkasan

- Vigenere = beberapa Caesar yang bergantian sesuai kata kunci.
- Huruf yang sama bisa menjadi huruf berbeda, karena pergeseran berubah-ubah.
- Kelemahan: kunci diulang, dan pola perulangan bisa dideteksi.
- Di CTF, cukup pakai tool untuk memecahkannya; yang penting kamu paham kenapa cara ini dulu dianggap kuat.
