#cybersecurity
Binary adalah sistem bilangan yang hanya menggunakan angka 0 dan 1. sistem ini juga dikenal sebagai yang dipakai oleh komputer untuk berkomunikasi dan membaca file seperti gambar, suara, teks, data, dan lain lain. 
setiap angka 0 dan 1 itu di sebut dengan "bit" atau "binary digit" dan kombinasi dari bit inilah yang merepresentasikan dari jenis data yang disebutkan diatas itu.

Misalnya, huruf “A” direpresentasikan dalam biner sebagai 01000001, sedangkan angka “5” sebagai 00110101. Dengan sistem ini, semua data yang kita masukkan ke dalam komputer atau perangkat lainnya dapat diproses dengan cepat dan efisien.

# Cara binary bekerja
Agar komputer bisa membaca biner itu sebagai data, ada beberapa cara yang digunakan:
1. Representasi data dalam bentuk biner
perangkat komputer tidak bisa memahami bahasa manusia, jadi dia membaca data dengan sinyal listrik, singkatnya 1 = hidup, dan 0 = mati. 

2. Konversi data ke format digital
setiap data yang dimasukan, akan di ubah dulu ke dalam format biner. dan proses ini biasanya dilakukan di Hardware seperti Prosesor.

3. Translator Data 
Setelah data di konversi, lalu komputer membacanya dan mengolahnya menjadi informasi yang bisa dilihat di layar.

# Cara menghitung bilangan biner
Dalam sistem biner, setiap digit memiliki posisi yang merupakan kelipatan 2 dan dimulai dari kanan.
nilai posisinya adalah 1 2 4 8 16 32, dan seterusnya, yang berarti digit paling kanan memiliki bobot $2^0$ (1), 
$2^1$ (2),
$2^2$ (4),
$2^3$ (8),
$2^4$ (16),
$2^5$ (32),
dan seterusnya.

Langsung saja saya berikan contoh cara menghitung biner ke Desimal
# Cara menghitung bilangan biner ke Desimal
### Contoh 1
Kita ambil contoh 1101, 
seperti yang sudah di jelaskan diatas kalo setiap bit itu mempunyai pangkat yang di mulai dari 0 dan seterusnya.
jadi nilai 1101 itu saya ubah dulu ke dalam bentuk pangkat dan dimulai dari kanan agar
1 = 0
0 = 1
1 = 2
1 = 3
(kalo di urutkan menjadi 1101 = 3210)

lalu saya ubah menjadi pangkat dari 2, dan menghitung hasilnya.
1 * $2^0$ = 1
0 * $2^1$ = 0 
1 * $2^2$ = 4
1 * $2^3$ = 8
dan saya mendapatkan 8 4 0 1, jika semuanya di jumlahkan 1 + 0 + 4 + 8 = 13.
jadi 1101 = 13

### Contoh 2
Biner: 1110
pangkat: 3210:
0 * $2^0$ = 0
1 * $2^1$ = 2
1 * $2^2$ = 4
1 * $2^3$ = 8
0 + 2 + 4 + 8 = 14,
jadi 1110 = 14


#### Cara cepat membaca Biner ke desimal
Cara cepat membaca Biner adalah dengan menghapal bilangan yang dipangkatkan 2. Tapi tidak ada batas maksimum yang di terapkan dalam digit biner maka akan mustahil untuk menghapalkannya, dan tetapi di dalam crypto Digit biner yang paling tinggi yang saya temui adalah 8. jadi cukup menghapali 8 digit saja.
1 2 4 8 16 32 64 128
tetapi biner dibaca dari kanan, maka;
128 64 32 16 8 4 2 1

jika sudah menghapal ini, maka akan mudah jika di berikan angka biner, contoh
0011

tinggal ubah menjadi hasil dari pangkat 2 mulai dari kanan dan dimulai dari 1, dan bit 0 tidak dihitung:
0021, dan tinggal tambahkan saja hasilnya = 3
0111 = 0421 = 4 + 2 + 1 = 7
0101 = 0401 = 4 + 1 = 5

Bisa juga di gunakan untuk selain biner digit 4:
010101 =  0160401 = 16 + 4 + 1 = 21
00111111 = 00 32168421 = 32 + 16 + 8 + 4 + 2 + 1 = 63



## Cara menghitung bilangan Desimal ke Biner
Dengan cara membagi bilangan desimal dengan 2 dengan cara berulang kali sampai mendapatkan sisa bagi 0.
## contoh 1:
saya akan mencari bilangan biner dari desimal 26:
26 / 2 = 13 sisa 0
13 / 2 = 6 sisa 1
6 / 2 = 3 sisa 0
3 / 2 = 1 sisa 1
1 / 2 = 0 sisa 1
cara menyusunnya adalah dari bawah ke atas, yaitu 11010
## contoh 2
di contoh 2 saya akan mencari biner dari desimal 32:
32 / 2 = 16 sisa 0
16 / 2 = 8 sisa 0
8 / 2 = 4 sisa 0
4 / 2 = 2 sisa 0
2 / 2 = 1 sisa 0 
1 / 2 = 0 sisa 1
jadi biner dari 32 adalah 100000

#### Cara cepat membaca Desimal ke biner
tentu saja ada cara cepatnya juga. yaitu dengan mencari hasil dari penambahan bilangan yang sudah di pangkatkan 2 menjadi desimal yang ingin dicari tersebut.

misalnya saya akan mencari bilangan 20,
dari 128 64 32 16 8 4 2 1, mana yang bisa membentuk angka 20?
16 dan 4. jadi tinggal mengubah mengubah urutan 16 dan 4 menjadi 1, dan yang lainnya 0.
00010100.
dan faktanya kita bisa menghapus angka 00 sebelum 1 terakhir dan menjadi 10100, itu tetap menghasilkan 20.

contoh lain yang lebih besar yaitu 250:
angka yang membentuk 250 yaitu:
128 64 32 16 8 2, jika di binerkan akan menjadi 11111010









