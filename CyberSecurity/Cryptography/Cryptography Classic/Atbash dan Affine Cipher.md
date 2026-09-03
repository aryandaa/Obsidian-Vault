#cybersecurity 

Setelah Caesar, kita naik satu tingkat. Caesar cuma menggeser huruf dengan jumlah yang tetap. **Atbash** dan **Affine Cipher** adalah dua cipher substitusi yang sedikit lebih pintar, tapi tetap bisa dipecahkan dengan mudah. Keduanya sering muncul di CTF sebagai soal pembuka.

## Atbash: alfabet dibalik

Atbash bekerja dengan **membalik urutan alfabet**. Huruf pertama menjadi huruf terakhir, huruf kedua menjadi huruf kedua dari belakang, dan seterusnya.

```text
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
```

Jadi:

```text
A → Z
B → Y
C → X
...
```

Contoh:

```text
Pesan asli : HELLO
Atbash     : SVOOL
```

Coba ikuti: H berpasangan dengan S, E dengan V, L dengan O, L dengan O, O dengan L.

Mudah bukan? Dan karena ini cuma pembalikan, decode dan encode-nya sama saja. `SVOOL` di-Atbash lagi akan kembali menjadi `HELLO`.

Contoh Python:

```python
text = "SVOOL"
result = ""
for ch in text:
    if 'a' <= ch <= 'z':
        result += chr(ord('z') - (ord(ch) - ord('a')))
    elif 'A' <= ch <= 'Z':
        result += chr(ord('Z') - (ord(ch) - ord('A')))
    else:
        result += ch
print(result)  # HELLO
```

Cara mengenali Atbash: tidak ada kunci sama sekali, jadi kalau kamu membalik alfabet dan hasilnya langsung terbaca, berarti itu Atbash.

## Affine Cipher: Caesar yang pakai rumus

Affine Cipher menggabungkan dua hal: **perkalian dan penambahan**. Setiap huruf diubah dengan rumus:

```text
c = (a * huruf + b) mod 26
```

Artinya, posisi huruf (A=0, B=1, ..., Z=25) dikali dengan angka `a`, lalu ditambah angka `b`, lalu dimodulo 26 supaya hasilnya tetap di dalam alfabet.

Kunci Affine adalah dua angka: `a` dan `b`.

Contoh kecil dengan a=5 dan b=8:

```text
Huruf H = posisi 7
c = (5 * 7 + 8) mod 26 = 43 mod 26 = 17
Posisi 17 = huruf R
```

Jadi H menjadi R.

Untuk mendekripsi, kita pakai kebalikannya:

```text
huruf = (c - b) * invers_a mod 26
```

Invers dari `a` adalah angka yang kalau dikalikan dengan `a` hasilnya 1 mod 26. Konsep ini sudah kamu pelajari di materi Modular Arithmetic ([Modular Inverting](Modular%20Inverting.md)), jadi kalau terasa asing, kembali dulu ke sana.

### Syarat penting: a harus genap dan bukan kelipatan 13

Tidak semua angka boleh dipakai sebagai `a`. Angka `a` harus **coprime dengan 26**, artinya tidak punya faktor yang sama dengan 26. Kalau tidak, cipher-nya rusak: dua huruf berbeda bisa berubah menjadi huruf yang sama, dan tidak bisa dibuka kembali.

Angka yang boleh dipakai sebagai a: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.

Kalau di soal kamu melihat a yang bukan angka-angka itu, cipher-nya pasti bermasalah atau soal itu jebakan.

## Memecahkan Affine di CTF

Karena a hanya punya 12 kemungkinan dan b ada 26 kemungkinan, total kombinasi kunci cuma 12 * 26 = 312. Sangat kecil. Brute force langsung bisa:

```python
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = egcd(b % a, a)
    return g, y - (b // a) * x, x

def mod_inv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        return None
    return x % m

def affine_decrypt(cipher, a, b):
    inv = mod_inv(a, 26)
    if inv is None:
        return None
    result = ""
    for ch in cipher:
        if 'a' <= ch <= 'z':
            y = ord(ch) - ord('a')
            result += chr(((y - b) * inv) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            y = ord(ch) - ord('A')
            result += chr(((y - b) * inv) % 26 + ord('A'))
        else:
            result += ch
    return result

cipher = "MXYW DGGY"
for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
    for b in range(26):
        hasil = affine_decrypt(cipher, a, b)
        if "flag" in hasil.lower() or "the" in hasil.lower():
            print(f"a={a} b={b}: {hasil}")
```

Script ini mencoba semua kunci dan menampilkan hasil yang mengandung kata umum. Di soal sungguhan, kamu tinggal ganti `cipher` dengan teks yang kamu dapat.

Kalau malas menulis script, [dcode.fr](https://www.dcode.fr/affine-cipher) bisa mencoba semua kemungkinan a dan b secara otomatis.

## Ringkasan

- Atbash: alfabet dibalik, tidak pakai kunci.
- Affine: rumus `(a * huruf + b) mod 26`, kuncinya dua angka.
- `a` harus coprime dengan 26 supaya cipher bisa dibuka.
- Total kunci cuma 312, jadi brute force selalu menang.
- Keduanya adalah substitusi monoalfabetik: satu huruf selalu diganti dengan satu huruf lain yang sama. Kelemahan besar ini akan kita serang di materi Substitution Cipher.
