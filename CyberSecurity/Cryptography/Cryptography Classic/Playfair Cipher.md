#cybersecurity 

Playfair Cipher adalah cipher substitusi poligrafik praktis pertama di dunia. Ditemukan oleh Charles Wheatstone pada tahun 1854, cipher ini dipopulerkan oleh temannya, Lord Playfair, dan sempat dipakai oleh militer Inggris selama Perang Boer hingga Perang Dunia I.

Semua cipher substitusi yang kita pelajari sebelumnya (seperti Caesar atau Vigenere) bekerja pada level satu huruf (monografik). Playfair bekerja secara berbeda: **ia mengenkripsi pasangan dua huruf sekaligus (bigram atau digram)**. Karena pasangan huruf yang dienkripsi (misalnya `TH`, `HE`, `AN`), analisis frekuensi huruf tunggal langsung menjadi tidak berdaya.

## Kunci Matriks 5x5

Playfair menggunakan tabel kisi 5x5 yang diisi dengan huruf alfabet berdasarkan kata kunci (keyword).

Aturan pembuatan matriks:
1. Alfabet bahasa Inggris memiliki 26 huruf, sedangkan kisi 5x5 hanya memuat 25 ruang.
2. Huruf `I` dan `J` digabungkan ke dalam satu kotak yang sama (biasanya ditulis `I/J` atau `J` dihilangkan dan diganti `I`).
3. Masukkan kata kunci terlebih dahulu tanpa huruf duplikat.
4. Isi sisa kotak dengan huruf alfabet yang belum dipakai secara berurutan dari A sampai Z.

Contoh dengan kata kunci `MONARCHY`:

```text
M  O  N  A  R
C  H  Y  B  D
E  F  G  I  K
L  P  Q  S  T
U  V  W  X  Z
```

Perhatikan: huruf yang berulang di kata kunci dibuang, huruf `J` disatukan dengan `I`, lalu huruf sisanya diisi urut abjad.

## Menyiapkan Plaintext

Sebelum dienkripsi, pesan harus dipecah menjadi pasangan dua huruf dengan aturan berikut:

1. Hilangkan spasi dan tanda baca, ubah semua huruf menjadi kapital.
2. Jika ada pasangan huruf yang sama bersebelahan (misalnya `EE` pada kata `TREE`), sisipkan huruf pengisi (biasanya huruf `X` atau `Q`) di antaranya: `TR EX EX`.
3. Jika jumlah huruf ganjil sehingga huruf terakhir sendirian, tambahkan huruf pengisi (biasanya `X`) di akhir: `HELLO` -> `HE LL OX`.

Contoh pesan `BALLOON`:
- Pecah jadi pasangan: `BA LL OO N`
- Ada huruf kembar bersebelahan `LL`, sisipkan `X`: `BA LX LO ON`
- Total huruf genap (8 huruf, 4 pasang).

## Aturan Enkripsi dan Dekripsi

Setiap pasangan dua huruf diposisikan di dalam tabel kisi 5x5. Ada tiga skenario posisi:

### 1. Berada di Baris yang Sama
- **Enkripsi**: Geser masing-masing huruf satu langkah ke **kanan**. Jika berada di ujung kanan, putar kembali ke ujung kiri baris tersebut.
- **Dekripsi**: Geser masing-masing huruf satu langkah ke **kiri**.

Contoh matriks di atas untuk pasangan `AR`:
- `A` dan `R` berada di baris pertama.
- Hasil enkripsi: `A` -> `R`, `R` -> `M`. Menjadi `RM`.

### 2. Berada di Kolom yang Sama
- **Enkripsi**: Geser masing-masing huruf satu langkah ke **bawah**. Jika berada di baris paling bawah, putar kembali ke baris paling atas kolom tersebut.
- **Dekripsi**: Geser masing-masing huruf satu langkah ke **atas**.

Contoh matriks di atas untuk pasangan `MU`:
- `M` dan `U` berada di kolom pertama.
- Hasil enkripsi: `M` -> `C`, `U` -> `M`. Menjadi `CM`.

### 3. Membentuk Sudut Persegi Panjang (Beda Baris dan Beda Kolom)
- **Enkripsi & Dekripsi**: Tukar huruf dengan huruf yang berada pada baris yang sama tetapi di kolom huruf pasangannya (ambil sudut horizontal yang berlawanan).
- Urutan tetap: huruf pertama diganti oleh huruf sebaris dengannya di kolom huruf kedua.

Contoh pasangan `EA`:
- `E` ada di baris 3 kolom 1.
- `A` ada di baris 1 kolom 4.
- `E` diganti huruf di baris 3 kolom 4 -> `I`.
- `A` diganti huruf di baris 1 kolom 1 -> `M`.
- Hasil enkripsi: `IM`.

## Implementasi Python Sederhana

Berikut adalah script Python untuk mendekripsi Playfair jika kata kunci diketahui:

```python
def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    seen = set()
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            matrix.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.add(ch)
            matrix.append(ch)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
    return None

def playfair_decrypt(cipher, key):
    matrix = create_matrix(key)
    cipher = cipher.upper().replace("J", "I").replace(" ", "")
    plain = []
    
    for i in range(0, len(cipher), 2):
        r1, c1 = find_pos(matrix, cipher[i])
        r2, c2 = find_pos(matrix, cipher[i+1])
        
        if r1 == r2: # sebaris, geser kiri
            plain.append(matrix[r1][(c1 - 1) % 5])
            plain.append(matrix[r2][(c2 - 1) % 5])
        elif c1 == c2: # sekolom, geser atas
            plain.append(matrix[(r1 - 1) % 5][c1])
            plain.append(matrix[(r2 - 1) % 5][c2])
        else: # bentuk persegi panjang
            plain.append(matrix[r1][c2])
            plain.append(matrix[r2][c1])
            
    return "".join(plain)

# Uji coba dekripsi
ciphertext = "RMCMIM"
key = "MONARCHY"
print("Hasil dekripsi:", playfair_decrypt(ciphertext, key))
```

## Cara Mengenali Playfair di CTF

Ada karakteristik unik Playfair yang membedakannya dari cipher lain:
1. **Panjang ciphertext selalu genap**, karena dienkripsi per pasangan 2 huruf.
2. **Huruf J sangat jarang atau tidak pernah muncul**, karena dilebur menjadi I.
3. **Tidak ada pasangan bigram huruf kembar di ciphertext**. Sepasang huruf terenkripsi seperti `EE`, `LL`, atau `XX` tidak akan pernah dihasilkan oleh Playfair jika aturan pemisahan huruf kembar diterapkan.
4. Jika dibalik, pasangan `AB` yang menghasilkan `XY` akan membuat pasangan `BA` menghasilkan `YX`.

## Cara Memecahkan di CTF

1. **Jika Kunci Diberikan**:
   - Pakai CyberChef dengan operation "Playfair Decode".
   - Atau pakai dcode.fr Playfair Cipher: masukkan ciphertext dan kata kuncinya.
2. **Jika Kunci Tidak Diketahui (Brute Force / Heuristik)**:
   - Karena ada $25!$ kemungkinan susunan matriks, brute force seluruhnya mustahil.
   - Gunakan algoritma *Simulated Annealing* atau *Hill Climbing* berbasis statistik bigram/trigram bahasa Inggris.
   - Tool otomatis terbaik untuk menebak kunci Playfair tanpa bantuan adalah [dcode.fr Playfair Solver](https://www.dcode.fr/playfair-cipher).

## Latihan Kecil

Pecahkan ciphertext Playfair berikut dengan kata kunci `SECURITY`:

```text
Ciphertext: LN BF DQ
```

Petunjuk:
1. Susun matriks 5x5 dari kata `SECURITY`.
2. Dekripsi pasangan `LN`, `BF`, dan `DQ` menggunakan aturan kebalikan di atas.
3. Hasilnya adalah kata bahasa Inggris 6 huruf.

## Ringkasan

- Playfair mengenkripsi pasangan 2 huruf (bigram) menggunakan matriks kisi 5x5.
- Huruf I dan J disatukan dalam satu sel kisi.
- Ada tiga aturan posisi: sebaris (geser horizontal), sekolom (geser vertikal), dan persegi panjang (tukar sudut).
- Panjang ciphertext selalu genap dan tidak pernah ada bigram kembar identik.
- Kebal terhadap analisis frekuensi huruf tunggal standar, tetapi rentan terhadap analisis frekuensi bigram dan metode hill climbing.
