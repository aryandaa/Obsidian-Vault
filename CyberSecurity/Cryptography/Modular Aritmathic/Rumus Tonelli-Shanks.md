#cybersecurity
ini materi lanjutan dari [[Legendre Symbol]] untuk membahas Quadratic Residue.

Di sesi sebelumnya saya sudah membahas Legandre, dengan rumus r ≡ a^((p+1)/4) (mod p), tetapi dengan syarat jika p = 3 (mod 4), (p hasilnya adalah 3 kalo di moduluskan dengan 4)

Kali ini akan membahas rumus untuk mencari akar kuadrat modulo tetapi Jika p = 1 (mod p). 
(p hasilnya 1 jika di moduluskan dengan 4) maka gunakan rumus Tonelli-Shanks 
yaitu $r^2$ = a (mod p).
tetapi rumus ini memiliki syarat wajib lagi:
- p prima ganjil
- a adalah quadratic residue dari p

Berikut adalah penjelasan rinci mengenai struktur data, langkah-langkah, dan logika di balik algoritma/rumus ini:

1. Faktorisasi Bagian Genap dari $(p - 1)$
Karena $p$ adalah bilangan prima ganjil, maka $(p - 1)$ pasti merupakan bilangan genap. 
Kita bisa memisahkan semua faktor angka 2 dari $(p - 1)$ hingga tersisa bilangan ganjil ($Q$).
Rumusnya adalah:
$$p - 1 = Q \cdot 2^S$$
- $Q$ harus berupa bilangan ganjil.
- $S$ adalah berapa kali kita bisa membagi $(p - 1)$ dengan 2.
> **Contoh:** Jika $p = 41$, maka $p - 1 = 40$.
>
> Kita bagi dengan 2 secara terus-menerus: $40 \rightarrow 20 \rightarrow 10 \rightarrow 5$ (ganjil).
> 
> Jadi, $Q = 5$ dan $S = 3$, karena $41 - 1 = 5 \cdot 2^3$.


2. Cari Elemen Bukan Kuadrat (Non-Residue)
Kita perlu mencari sebuah bilangan bulat $z$ sedemikian rupa sehingga $z$ **bukan merupakan sisa kuadrat** modulo $p$. Artinya, tidak ada bilangan yang jika dikuadratkan menghasilkan $z \pmod p$

Untuk memastikannya, kita bisa menggunakan **Simbol Legendre**. Kita cari $z$ acak sampai memenuhi kondisi:

$$z^{\frac{p-1}{2}} \equiv -1 \pmod p$$

Setelah menemukan $z$, kita hitung nilai konstanta awal:

$$c = z^Q \pmod p$$

### Langkah 3: Inisialisasi Variabel Pelacak

Sebelum masuk ke perulangan (loop), kita siapkan variabel-variabel awal berikut:

- $R \equiv a^{\frac{Q+1}{2}} \pmod p$ _(Ini adalah tebakan awal untuk akar kuadrat)_
    
- $t \equiv a^Q \pmod p$ _(Ini adalah faktor kesalahan. Jika $t = 1$, maka $R$ sudah benar)_
    
- $M = S$ _(Pelacak jumlah kuadrat yang tersisa)_

### Langkah 4: Perulangan (Looping) untuk Memperbaiki Nilai

Di sinilah inti dari algoritma Tonelli-Shanks. Kita melakukan pemeriksaan terhadap nilai $t$:

1. **Jika $t \equiv 1 \pmod p$**, maka pencarian selesai! Akar kuadratnya adalah $R$.
    
2. **Jika $t \equiv 0 \pmod p$**, maka $a \equiv 0$, artinya akarnya adalah $0$.
    
3. **Jika $t \not\equiv 1 \pmod p$**, kita harus mencari bilangan bulat terkecil $i$ (di mana $0 < i < M$) sedemikian rupa sehingga:
    $$t^{2^i} \equiv 1 \pmod p$$
Setelah menemukan nilai $i$ tersebut, kita perbarui semua variabel kita untuk iterasi berikutnya:
- $b = c^{2^{M - i - 1}} \pmod p$
    
- $R = R \cdot b \pmod p$ _(Memperbarui tebakan akar)_
    
- $t = t \cdot b^2 \pmod p$ _(Memperbarui faktor kesalahan agar mendekati 1)_
    
- $c = b^2 \pmod p$
    
- $M = i$ _(Memperkecil batas ruang pencarian)_
    

Proses ini diulangi terus sampai nilai $t$ menjadi $1$.

### Hasil Akhir (Dua Akar)
Jika algoritma selesai dan menghasilkan nilai $R$, maka persamaan tersebut sebenarnya memiliki dua solusi akar kuadrat modulo $p$, yaitu:
$$r_1 = R$$
$$r_2 = p - R$$

### Mengapa Algoritma ini Diperlukan?
Jika $p \equiv 3 \pmod 4$, kita bisa langsung menggunakan rumus cepat Fermat: $R = a^{\frac{p+1}{4}} \pmod p$. Namun, rumus cepat itu **tidak bekerja** jika $p \equiv 1 \pmod 4$. Di sinilah Tonelli-Shanks masuk dengan menggunakan variabel $t$ dan $b$ untuk "menyisir" dan mengeliminasi komponen non-kuadrat yang mengganggu perhitungan hingga akhirnya menemukan akar yang tepat.