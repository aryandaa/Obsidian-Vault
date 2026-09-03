#cybersecurity 

Caesar Cipher adalah cipher paling sederhana dan paling tua yang masih diajarkan sampai sekarang. Namanya diambil dari Julius Caesar, kaisar Romawi yang memakai cara ini untuk mengirim pesan rahasia ke pasukannya sekitar 2000 tahun lalu.

Cara kerjanya sangat sederhana: **setiap huruf digeser beberapa langkah di dalam alfabet.**

## Analogi sederhana

Bayangkan alfabet ditulis melingkar seperti jam:

```text
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```

Kalau kita geser 3 langkah ke kanan, huruf A menjadi D, B menjadi E, C menjadi F, dan seterusnya. Setelah Z, kembali lagi ke A (karena alfabetnya melingkar).

Contoh:

```text
Pesan asli : HELLO
Geser 3    : KHOOR
```

Coba ikuti: H digeser 3 menjadi K, E menjadi H, L menjadi O, L menjadi O, O menjadi R. Hasilnya `KHOOR`.

Besar pergeseran disebut **key** atau kunci. Geser 3 artinya key = 3.

## ROT13 dan ROTn

**ROT13** adalah Caesar dengan pergeseran 13. Kenapa 13 yang terkenal? Karena alfabet ada 26 huruf, jadi ROT13 kalau diterapkan dua kali akan kembali ke huruf semula. Artinya ROT13 bisa di-encode dan di-decode dengan cara yang sama.

```text
HELLO → ROT13 → URYYB → ROT13 → HELLO
```

**ROTn** artinya Caesar dengan pergeseran bebas n. ROT17, ROT5, dan sebagainya, semuanya sama saja: tinggal ganti angka pergeserannya.

## Cara memecahkan Caesar di CTF

Karena alfabet cuma 26 huruf, kemungkinan pergeseran hanya ada 26. Kamu tinggal mencoba semuanya sampai salah satu hasilnya terbaca. Ini disebut **brute force**, dan jumlah percobaannya sangat kecil sehingga bisa dilakukan manual atau pakai script.

```python
# Brute force Caesar: coba semua 26 kemungkinan
def caesar_shift(text, shift):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += ch
    return result

cipher = "KHOOR ZRUOG"
for shift in range(26):
    print(f"shift {shift:2d}: {caesar_shift(cipher, shift)}")
```

Jalankan script itu, dan di antara 26 baris output akan ada satu yang berbunyi `HELLO WORLD`. Itu pesan aslinya.

Cara yang lebih cepat di CTF: buka [CyberChef](https://gchq.github.io/CyberChef/), cari recipe "ROT13", atau langsung pakai [dcode.fr](https://www.dcode.fr/caesar-cipher) yang bisa mencoba semua pergeseran sekaligus dan menampilkan hasil yang paling masuk akal.

## Cara mengenali Caesar

- Huruf-hurufnya masih membentuk pola huruf (spasi dan tanda baca biasanya tetap).
- Kalau kamu coba semua pergeseran, salah satunya langsung terbaca.
- Tidak ada pola rumit, hanya pergeseran.

## Latihan kecil

Coba pecahkan ini (jawabannya adalah sebuah kalimat):

```text
flag: L ORYH FUBSWR
```

Kalau sudah ketemu, coba juga buat script yang bisa menebak pergeseran otomatis dengan membandingkan hasilnya dengan kata-kata umum seperti "the", "and", atau "flag".

## Ringkasan

- Caesar = menggeser huruf sejumlah langkah tertentu.
- ROT13 = Caesar dengan geseran 13, bisa dibuka dengan cara yang sama.
- Cuma ada 26 kemungkinan, jadi brute force selalu bisa.
- Ini adalah dasar dari semua cipher substitusi yang akan kita pelajari berikutnya.
