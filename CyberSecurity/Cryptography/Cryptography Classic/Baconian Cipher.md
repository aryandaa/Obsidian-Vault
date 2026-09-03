#cybersecurity 

Baconian Cipher (dikenal juga sebagai Bacon's Cipher) diciptakan oleh filsuf dan negarawan Inggris, Sir Francis Bacon, pada tahun 1605. Cipher ini sangat istimewa karena merupakan salah satu bentuk paling awal dari penggabungan antara **kriptografi** (penyandian pesan) dan **steganografi** (penyembunyian keberadaan pesan itu sendiri).

Pesan tidak dienkripsi dengan menggeser atau mengacak huruf, melainkan dengan mengubah setiap huruf menjadi kode biner sepanjang 5 karakter yang hanya terdiri dari dua pilihan simbol (biasanya dilambangkan dengan huruf `A` dan `B`).

## Cara Kerja dan Tabel Baconian

Setiap huruf alfabet diwakili oleh urutan 5 karakter biner:

### 1. Varian Klasik 24 Huruf (I = J dan U = V)
Pada zaman Francis Bacon, alfabet Latin kuno menyatukan huruf `I` dengan `J`, serta `U` dengan `V`.

```text
A = AAAAA    G = AABBA    N = ABBAA    T = BAABA
B = AAAAB    H = AABBB    O = ABBAB    U/V = BAABB
C = AAABA    I/J = ABAAA  P = ABBBA    W = BABAA
D = AAABB    K = ABAAB    Q = ABBBB    X = BABAB
E = AABAA    L = ABABA    R = BAAAA    Y = BABBA
F = AABAB    M = ABABB    S = BAAAB    Z = BABBB
```

### 2. Varian Modern 26 Huruf Penuh
Setiap huruf dari A sampai Z memiliki kode uniknya masing-masing tanpa ada huruf yang digabungkan:
- A = AAAAA, B = AAAAB, C = AAABA, D = AAABB, E = AABAA ... Z = BABBA.

Nilai ini persis seperti representasi biner angka 0 sampai 25, di mana `A = 0` dan `B = 1`.

## Penyamaran Steganografi (Ciri Utama Baconian)

Kelebihan utama Baconian adalah dua simbol `A` dan `B` bisa disembunyikan ke dalam media teks apa pun yang terlihat biasa saja. Orang yang melihatnya mengira teks itu hanya paragraf biasa, padahal di dalamnya tersimpan pesan rahasia.

Contoh metode penyamaran yang sering dipakai di soal CTF:
1. **Huruf Kapital vs Huruf Kecil**:
   - Huruf kecil dianggap `A`, huruf kapital dianggap `B`.
   - Contoh: `tHis IS A nORmAl tEXt` -> uraikan besar kecilnya menjadi untaian A dan B.
2. **Gaya Font (Tebal / Miring)**:
   - Font reguler = `A`, font miring (italic) atau tebal (bold) = `B`.
3. **Dua Jenis Karakter Apapun**:
   - Spasi ganjil/genap, dua jenis tanda baca, atau dua pilihan kata.

## Contoh Dekripsi Sederhana

Misalkan kamu mendapatkan ciphertext:
```text
AABAA  ABABB  ABABA  ABABA  ABBAB
```

Mari cocokkan dengan tabel varian modern:
- `AABAA` = `E` (desimal 4)
- `ABABB` = `M` (desimal 11)
- `ABABA` = `L` (desimal 10)
- `ABABA` = `L` (desimal 10)
- `ABBAB` = `O` (desimal 14)

Pesan asli: `EMLLO` (atau `HELLO` tergantung offset/tabel yang dipakai).

## Implementasi Script Python

Berikut script Python untuk mendekripsi teks Baconian langsung dari format huruf besar-kecil atau format A/B:

```python
BACON_DICT_26 = {
    format(i, '05b').replace('0', 'A').replace('1', 'B'): chr(i + ord('A'))
    for i in range(26)
}

def bacon_decode_ab(text):
    # Bersihkan hanya ambil huruf A dan B
    clean = [c for c in text.upper() if c in ('A', 'B')]
    result = []
    for i in range(0, len(clean) - 4, 5):
        chunk = "".join(clean[i:i+5])
        result.append(BACON_DICT_26.get(chunk, '?'))
    return "".join(result)

def bacon_decode_case(text):
    # Mengubah teks campuran kapital: kecil = A, besar = B
    ab_stream = []
    for ch in text:
        if ch.isalpha():
            ab_stream.append('B' if ch.isupper() else 'A')
    return bacon_decode_ab("".join(ab_stream))

# Uji coba 1: format AB langsung
cipher1 = "AAAAA AAAAB AAABA AAABB AABAA"
print("Dekripsi AB:", bacon_decode_ab(cipher1)) # ABCDE

# Uji coba 2: steganografi kapitalisasi teks
cipher2 = "aLl thE WoRLd iS a StAgE"
print("Dekripsi Stego:", bacon_decode_case(cipher2))
```

## Cara Mengenali Baconian Cipher di CTF

1. **Pola Biner 2 Simbol**: Ciphertext hanya terdiri dari dua huruf (biasanya `A` dan `B`), dua digit angka (`0` dan `1`), atau dua emoji berbeda.
2. **Panjang Teks Kelipatan 5**: Jumlah karakter adalah kelipatan 5 (misalnya 25, 40, atau 100 karakter).
3. **Kapitalisasi Teks Aneh**: Diberikan sebuah kalimat atau lirik lagu berbahasa Inggris dengan huruf besar dan kecil yang acak-acakan tidak beraturan.
4. **Format Font Khusus**: Soal berupa dokumen PDF atau halaman web yang jika diperiksa kode HTML-nya ada tag `<b>` atau `<i>` berselang-seling.

## Tools untuk CTF

- **CyberChef**: Recipe "Bacon Cipher Decode". CyberChef memiliki opsi untuk otomatis menerjemahkan varian 24 huruf atau 26 huruf.
- **dcode.fr**: [dcode.fr Baconian Cipher](https://www.dcode.fr/bacon-cipher). dcode sangat fleksibel karena bisa otomatis mendeteksi apakah `A` mewakili huruf besar atau sebaliknya.

## Latihan Kecil

Perhatikan teks berikut:
```text
thE qUIcK BrOwn fOx jUmPs
```

Ambil pola kapitalisasinya (huruf kecil = A, huruf kapital = B), bagi setiap 5 huruf menjadi satu blok, dan terjemahkan pesan rahasia yang tersembunyi di dalamnya.

## Ringkasan

- Baconian Cipher merepresentasikan setiap huruf alfabet menjadi kode biner 5 huruf (A dan B).
- Ada dua standar: varian klasik 24 huruf (I=J, U=V) dan varian modern 26 huruf.
- Sering digunakan sebagai teknik steganografi teks di CTF (huruf besar/kecil atau font tebal/miring).
- Panjang teks selalu kelipatan 5.
- CyberChef dan dcode.fr dapat menyelesaikannya secara instan.
