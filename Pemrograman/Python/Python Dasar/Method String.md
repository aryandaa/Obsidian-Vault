#programming 
Bebagai macam function yang berfungsi memanipulasi case dari string, seperti:
lowercase: huruf kecil.
uppercase: huruf besar.
mix: gabungan huruf kecil dan huruf besar.
contoh:
```Python
lowercase = "python adalah bahasa pemrograman yang mudah dipahami"
uppercase = "BELAJAR KONSISTEN MEMBUAT KEMAMPUAN SEMAKIN MAHIR"
mix = "hArI iNi CuAcA cErAh dAn AnGiN sEpOi-SePoI"
```

Cara penggunaan functionnya:
```python
#merubah semua kalimat menjadi uppercase
print(lowercase.upper())

#merubah semua kalimat menjadi lowercase
print(uppercase.lower())
print(mix.lower())
```

ada juga function yang berfungsi untuk melakukan pengecekan apakah string itu upper ataupun lower, dan outputnya berbentuk boolean, false atau true.
```Python
#ngecek apakah ada lower: true
print(lowercase.islower())

#mencek apakah ada upper: false (karena lowersemua)
print(lowercase.isupper())

#mencek apakah ada lowe: false (karena ada uppernya juga)
print(mix.islower())
```


ada juga function lain yang bisa melakukan pengecekan lain selain case:
# isalpha() = Huruf

# isdigit() = Angka

# isalnum() = Huruf dan Angka

# isdecimal() = Decimal

# isspace() = spasi, tab, newline

# istitle() = semua kata dimuai dengan huruf besar

# startswith("") = mengecek apakah kata itu dimulai dari ...

# endswith("") = apakah kata itu diakhiri dengan ...
