Algoritma Euclides itu adalah cara sederhana dan sistematis untuk mencari FPB (Faktor Persekutuan Terbesar) dari dua bilangan. algoritma ini bekerja dengan prinsip bahwa FPB dua bilangan tidak berubah walaupun bilangan yang lebih besar diganti dengan sisa hasil pembagiannya oleh bilangan yang lebih kecil.

Jadi daripada mengecek satu-satu faktor dari angka kecil sampai besar yang capek dan ribet,
algoritma Euclides memilih jalan cerdas:
bagi, ambil sisa, tukar posisi, lalu ulangi. Proses ini dilakukan terus sampai sisanya menjadi nol, dan pada saat itu bilangan terakhir yang digunakan untuk membagi adalah FPB yang dicari.

Karena langkahnya sedikit, cepat, dan selalu pasti berhenti, algoritma Euclides jadi salah satu algoritma klasik paling efisien dan masih dipakai sampai sekarang, termasuk di matematika, pemrograman, dan kriptografi.

## Cara penggunaan:

Misal mempunyai 2 angka
48 dan 18
### Langkah 1: Di organisasikan besar dan kecil terlebih dahulu
- Besar : 48
- Kecil : 18
### Langkah 2: yang besar dibagi dengan yang kecil, lalu ambil sisanya
48 ÷ 18 = 2 sisa 12

kenapa dapat 12?
18 × 1 = 18
18 × 2 = 36
18 × 3 = 54 ❌
(mentok di 2, karena 3 itu kebesaran)
48 (angka pertama tadi) - 36 (hasil dari 18 x 2) = 12
ini bisa juga di sebut dengan modulus atau sisa bagi yang sdh di pelajari sebelumnya.
  
### Langkah 3: tidak berhenti di 12, karena masih bisa di bagi lagi
18 ÷ 12 = 1 sisa 6
(karena 18 - 12 = 6)
### Langkah 4: ulangi lagi:
18 tadi sdh habis di bagi 12, jadi sisa 12 dan 6(sisanya tadi) yang bekerja

12 ÷ 6 = 2 sisa 0 (habis)
# Finish:
angka tertinggi terakhir sebelum 0 adalah PFB nya, yaitu 6

### Contoh soal 2
Cari FPB dari 56 dan 98:

### Organisasikan:
besar = 98
kecil = 56

### Hitung sisa bagi
98 ÷ 56 = 1 sisa 42

karena:
56 x 1 = 56
56 x 2 = 112 (bukan 2 karena kelebihan dari 98)
98 - 56 = 42
### Ulangi:
56 ÷ 42 = 1 sisa 14

karena:
56 x 1 = 56
56 - 42 = 14
### Finish 
FPB dari 56 dan 98 adalah 14, karena tertinggi dan tidak bisa dibagi lagi