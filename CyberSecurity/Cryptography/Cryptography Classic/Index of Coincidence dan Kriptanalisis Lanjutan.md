#cybersecurity 

Saat menghadapi tantangan kriptografi klasik di CTF, sering kali kamu hanya diberikan sepotong teks acak tanpa petunjuk cipher apa yang digunakan. Menebak satu per satu secara membabi buta akan membuang banyak waktu.

Para kriptanalis menggunakan metode matematika dan statistik untuk mengidentifikasi jenis cipher dalam hitungan detik. Dua senjata utamanya adalah **Index of Coincidence (IoC)** dan **Analisis N-gram**.

## Apa itu Index of Coincidence (IoC)

Index of Coincidence ditemukan oleh kriptografer militer Amerika Serikat, William F. Friedman, pada tahun 1922.

Secara sederhana, **IoC mengukur probabilitas bahwa dua huruf yang diambil secara acak dari sebuah teks adalah huruf yang sama.**

### Rumus Matematis IoC

Jika sebuah teks memiliki panjang $N$ huruf, dan setiap huruf ke-$i$ (dari A sampai Z) muncul sebanyak $f_i$ kali, maka rumusnya adalah:

```text
        sum( f_i * (f_i - 1) )
IoC = --------------------------
              N * (N - 1)
```

Di mana:
- $f_i$ adalah frekuensi kemunculan masing-masing huruf (A sampai Z).
- $N$ adalah total jumlah seluruh huruf di dalam teks.

## Nilai Patokan (Benchmark) IoC

Bahasa manusia memiliki distribusi huruf yang tidak merata (huruf E, T, A sangat sering muncul, sedangkan Q, Z jarang). Sebaliknya, teks yang benar-benar acak memiliki probabilitas huruf yang sama rata ($1/26$).

Nilai patokan IoC:
1. **Bahasa Inggris Normal**: $\approx 0.0667$ (sering dibulatkan $0.067$)
2. **Bahasa Indonesia Normal**: $\approx 0.075$
3. **Teks Acak Murni (Distribusi Seragam)**: $1 / 26 \approx 0.0385$

## Pohon Keputusan: Menentukan Jenis Cipher dengan IoC

Dengan menghitung nilai IoC ciphertext, kamu bisa langsung mengetahui kategori cipher yang dihadapi:

```text
                      [ Hitung Nilai IoC ]
                               |
            +------------------+------------------+
            |                                     |
     IoC tinggi (~0.067)                   IoC rendah (~0.038 - 0.052)
            |                                     |
    +-------+-------+                      [ Polialfabetik ]
    |               |                             |
Frekuensi huruf   Frekuensi huruf          - Vigenere
tetap normal?     berantakan?              - Beaufort
    |               |                      - Autokey
    v               v                      - Enigma
[Transposisi]    [Substitusi Mono]
- Rail Fence     - Caesar / ROT
- Columnar       - Atbash / Affine
                 - Simple Substitution
```

Penjelasan alur:
1. **Jika IoC tinggi ($\approx 0.067$) dan distribusi frekuensi huruf normal**: Huruf hanya dipindahkan posisinya, bukan diganti. Ciphertext ini adalah **Transposisi**.
2. **Jika IoC tinggi ($\approx 0.067$) tetapi distribusi huruf berantakan**: Huruf diganti dengan pemetaan satu-ke-satu yang konsisten. Ciphertext ini adalah **Substitusi Monoalfabetik**.
3. **Jika IoC rendah ($\approx 0.038 - 0.052$)**: Huruf yang sama diganti menjadi berbagai huruf berbeda. Ciphertext ini adalah **Substitusi Polialfabetik**.

## Menebak Panjang Kunci Vigenere Menggunakan IoC

Jika kamu sudah tahu teks tersebut adalah polialfabetik (seperti Vigenere), kamu bisa menemukan panjang kuncinya secara otomatis:

1. Asumsikan panjang kunci adalah $k$ (misal coba $k = 1, 2, 3, \dots, 20$).
2. Bagi ciphertext menjadi $k$ kolom (huruf ke-1, $1+k$, $1+2k$, dst masuk ke kolom 1).
3. Setiap kolom sebenarnya adalah teks monoalfabetik Caesar tersendiri.
4. Hitung nilai IoC untuk masing-masing kolom, lalu ambil nilai rata-ratanya.
5. Panjang kunci yang benar adalah nilai $k$ pertama yang membuat rata-rata IoC **melonjak naik mendekati angka 0.067**.

## Analisis N-gram (Bigram, Trigram, Quadgram)

Frekuensi satu huruf saja terkadang tidak cukup, terutama untuk teks pendek atau cipher poligrafik seperti Playfair. Kriptanalisis tingkat lanjut menggunakan frekuensi pasangan huruf:

- **Monogram**: frekuensi huruf tunggal (`E`, `T`, `A`).
- **Bigram**: frekuensi pasangan 2 huruf (`TH`, `HE`, `IN`, `ER`, `AN`).
- **Trigram**: frekuensi susunan 3 huruf (`THE`, `AND`, `THA`, `ENT`, `ION`).
- **Quadgram**: frekuensi susunan 4 huruf (`THAT`, `THER`, `WITH`, `TION`).

Program pemecah cipher otomatis modern (seperti yang digunakan oleh situs dcode.fr atau tool Python otomatis) menggunakan *fitness score* berbasis log probabilitas Quadgram bahasa Inggris untuk menguji jutaan kunci per detik.

## Script Python: Penghitung IoC dan Detektor Kunci

Script berikut menghitung nilai IoC sebuah teks dan menguji kemungkinan panjang kunci Vigenere dari 1 sampai 10:

```python
from collections import Counter

def calculate_ioc(text):
    if isinstance(text, list):
        text = "".join(text)
    clean_text = [c for c in text.upper() if c.isalpha()]
    N = len(clean_text)
    if N <= 1:
        return 0.0
    counts = Counter(clean_text)
    numerator = sum(f * (f - 1) for f in counts.values())
    denominator = N * (N - 1)
    return numerator / denominator

def find_vigenere_key_length(ciphertext, max_len=10):
    clean = [c for c in ciphertext.upper() if c.isalpha()]
    print(f"Total huruf: {len(clean)}")
    print(f"IoC teks utuh: {calculate_ioc(clean):.4f}\n")
    
    print("Mencoba perkiraan panjang kunci (rata-rata IoC):")
    for k in range(1, max_len + 1):
        # Bagi menjadi k kolom potongan
        slices = [clean[i::k] for i in range(k)]
        avg_ioc = sum(calculate_ioc(s) for s in slices) / k
        status = "<- KEMUNGKINAN KUNCI!" if avg_ioc >= 0.060 else ""
        print(f"Panjang k={k:2d}: IoC rata-rata = {avg_ioc:.4f} {status}")

# Contoh uji coba
sample_cipher = (
    "QPWKALVRXCQZIKGRBPWFAOMMYVGNKCLGHSJBYVGNKCLGHSJBY"
    "QPWKALVRXCQZIKGRBPWFAOMMYVGNKCLGHSJBYVGNKCLGHSJBY"
)
find_vigenere_key_length(sample_cipher, max_len=6)
```

## Tools Otomatis di CTF

- [dcode.fr Cipher Identifier](https://www.dcode.fr/cipher-identifier): Menganalisis teks misterius dan memberikan rekomendasi jenis cipher berdasarkan IoC dan statistik frekuensi.
- [CyberChef](https://gchq.github.io/CyberChef/): Recipe "Index of Coincidence".

## Latihan Kecil

Hitung IoC dari teks berikut menggunakan script Python di atas:
```text
Text A: "BEEF IS DELICIOUS AND HEALTHY FOOD FOR DINNER TONIGHT"
Text B: "XQZJK VBLPT MNWFR ZTXQY LPKMN BVXZQ JKLMN PQRST VWXYZ"
```

Perhatikan mana yang memiliki IoC mendekati 0.067 dan mana yang mendekati 0.038.

## Ringkasan

- Index of Coincidence mengukur seberapa tidak meratanya sebaran huruf dalam sebuah teks.
- Patokan IoC: Bahasa Inggris $\approx 0.067$, teks acak murni $\approx 0.038$.
- IoC tinggi dengan susunan kata acak menandakan cipher monoalfabetik atau transposisi.
- IoC rendah menandakan cipher polialfabetik.
- Dengan memecah teks per perioda $k$, IoC dapat menentukan panjang kunci Vigenere secara presisi sebelum kunci itu sendiri ditebak.
