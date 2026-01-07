ASCII merupakan singkatan dari "American Standard Code for Information Interchange".
adalah sebuah standar internasional dalam kode huruf dan simbol seperti hex dan unicode, Namun ASCII memiliki sifat yang lebih universal, contohnya adalah 012 = A.

Pada dasarnya mewakili karakter-karakter angka maupun huruf di dalam komputer, misalnya 1 2 3 A B C dan sebagainya.

Table Ascii Bisa dilihat disini: https://www.ascii-code.com/

kode ASCII sebenarnya memiliki komposisi bilangan biner sebanyak 8 bit dimulai dari  00000000 hingga 11111111, total kombinasi yang dihasilkan ada sebanyak 256, dimulai dari 0 hingga 255 dalam sistem Desimal .

pada umumnya kode-kode ascii ini merepresentasikan kode-kode untuk:
- angka 0-9
- huruf A-Z (uppercase)
- huruf a-z (lowercase)
- simbol & ^ % $ @ # ! dan sebagainya.
- tombol eter, esc, backspace, space, tab, shift, dll.
- Karakter grafis (kode ASCII standar nomor 128 s/d 255)
- Kode komunikasi ETX< STX, ENQ. ACK...

penggunaan ASCII dalam kriptografi biasanya digunakan untuk mengubah karakter menjadi bilangan numerik.
## Python Untuk Ascii
#python
Disini di sediakan sebuah variable yang menyimpan ASCII nya dalam bentuk decimal

```python

ciphertext = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
```

di dalam python ada function `chr()` yang bisa digunakan untuk mengubah bilangan ASCII menjadi karakter, sedangkan `ord()` melakukan sebaliknya

disini saya menggunakan `''.join() `yang berfungsi untuk menggabungkan banyak element dalam list jadi 1 string utuh

```python
join = ''.join(chr(x)
               for x in ciphertext)

print (join)
```

Logika dari code ini:
menggabungkan semua isi list jadi 1 bilangan ascii utuh menggunakan `''.join(),`

lalu di decode menggunakan chr(x),
variable x ini berfungsi untuk looping buat mengdecode chiphertext dengan 1 1.

dan keluarkan hasilnya:
```crypto{ASCII_pr1nt4bl3}```

