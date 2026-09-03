#cybersecurity 

Semua cipher yang kita pelajari sejauh ini bekerja dengan cara **mengganti huruf** (substitusi). Sekarang kita belajar jenis yang berbeda: **transposition**, yang bekerja dengan cara **memindahkan posisi huruf**. Hurufnya tetap sama, hanya diacak urutannya.

Analogi sederhana: substitusi itu seperti mengganti isi kardus dengan barang lain. Transposition itu seperti menata ulang posisi barang di dalam kardus. Isinya sama, tapi urutannya berantakan.

## Rail Fence Cipher

Cara kerjanya seperti menulis huruf mengikuti pola zigzag di atas pagar, lalu membacanya per baris.

Contoh pesan `WEAREDISCOVERED` dengan 3 baris:

```text
W . . . E . . . C . . . R . . .
. E . R . D . S . O . E . E .
. . A . . . I . . . V . . . D .
```

Cara membaca: tulis huruf mengikuti garis zigzag dari atas ke bawah, lalu baca per baris:

```text
Baris 1: W E C R
Baris 2: E R D S O E E
Baris 3: A I V D
```

Ciphertext:

```text
WECR ERDSOEE AIVD
```

Untuk mendekripsi, kamu perlu tahu berapa barisnya. Jumlah baris itulah kuncinya.

### Kenapa gampang dipecahkan

Jumlah baris tidak bisa terlalu banyak (biasanya 2 sampai 10). Kamu tinggal mencoba semua kemungkinan baris sampai hasilnya terbaca.

```python
def rail_fence_decrypt(cipher, rows):
    n = len(cipher)
    fence = [[''] * n for _ in range(rows)]
    r, step = 0, 1
    for c in range(n):
        fence[r][c] = '*'
        if r == 0:
            step = 1
        elif r == rows - 1:
            step = -1
        r += step
    idx = 0
    for i in range(rows):
        for j in range(n):
            if fence[i][j] == '*':
                fence[i][j] = cipher[idx]
                idx += 1
    result = []
    r, step = 0, 1
    for c in range(n):
        result.append(fence[r][c])
        if r == 0:
            step = 1
        elif r == rows - 1:
            step = -1
        r += step
    return ''.join(result)

cipher = "WECRERDSOEEAIVD"
for rows in range(2, 11):
    print(f"rows={rows}: {rail_fence_decrypt(cipher, rows)}")
```

Jalankan script itu dan lihat baris mana yang terbaca sebagai kalimat.

## Columnar Transposition

Cara kerjanya: tulis pesan dalam tabel dengan jumlah kolom tertentu, lalu baca kolom demi kolom.

Contoh pesan `ATTACKATDAWN` dengan 4 kolom:
	
```text
A T T A
C K A T
D A W N
```

Baca per kolom (dari kiri ke kanan):

```text
Kolom 1: A C D
Kolom 2: T K A
Kolom 3: T A W
Kolom 4: A T N
```

Ciphertext:

```text
ACDTKATAWTN
```

Jumlah kolom adalah kuncinya. Kalau kunci berupa kata (misalnya kolom diurutkan berdasarkan abjad kata kunci), ini disebut columnar dengan keyword, dan sedikit lebih rumit.

Untuk memecahkannya, coba semua kemungkinan jumlah kolom sampai hasilnya terbaca. Kalau pakai keyword, tool [dcode.fr columnar](https://www.dcode.fr/columnar-transposition-cipher) bisa mencoba banyak kombinasi sekaligus.

## Cara mengenali transposition

- Frekuensi huruf sangat normal (karena huruf tidak diganti, hanya dipindah). Huruf E tetap paling sering muncul.
- Kalau kamu menghitung frekuensi dan hasilnya terlihat seperti bahasa Inggris biasa, tapi teksnya tidak terbaca, itu tanda transposition.
- Brute force jumlah baris/kolom biasanya langsung berhasil karena pilihannya sedikit.

## Perbandingan cepat

```text
Substitusi   : huruf diganti → frekuensi berubah
Transposition: huruf dipindah → frekuensi tetap normal
```

Karena itu, langkah pertama dalam memecahkan cipher yang tidak dikenal: hitung frekuensi hurufnya. Kalau frekuensinya wajar, fokus ke transposition. Kalau tidak wajar, fokus ke substitusi.

## Latihan kecil

Pecahkan ciphertext berikut (rail fence, coba semua jumlah baris):

```text
CLSAOEMTRU
```

Petunjuk: hasilnya adalah satu kata berbahasa Inggris. Kalau sudah ketemu, coba jelaskan berapa baris yang dipakai.

## Ringkasan

- Transposition memindahkan posisi huruf, bukan mengganti huruf.
- Rail fence: menulis zigzag, membaca per baris.
- Columnar: menulis ke tabel, membaca per kolom.
- Frekuensi huruf tetap normal, jadi bisa dibedakan dari substitusi.
- Di CTF, coba semua jumlah baris/kolom sampai terbaca.
