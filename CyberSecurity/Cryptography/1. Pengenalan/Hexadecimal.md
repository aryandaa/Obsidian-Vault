#cybersecurity
Heksadesimal adalah sistem bilangan berbasis 16 yang menggunakan 16 simbol unik: angka 0-9 dan huruf A-F (A=10, B=11, C=12, D=13, E=14, F=15.. dsb).

## Python Untuk Heksadecimal
#python
Di Python, fungsi `bytes.fromhex()` bisa dipakai untuk mengubah hex menjadi byte.
sedangkan Metode `.hex()` bisa dipanggil pada byte string untuk mendapatkan representasi hex-nya.

bisa di bilang bytes.fromhex() untuk dekripsi dan .hex() untuk enkripsi:

Untuk Melakukan Dekripsi:
```python
ciphertext = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

plainteks = bytes.fromhex(ciphertext)

print (plainteks)
```
Dan hasilnya : ```crypto{You_will_be_working_with_hex_strings_a_lot}```

Untuk Melakukan Enkripsi:
```python
teks = "crypto{You_will_be_working_with_hex_strings_a_lot}"
data = teks.encode()
hasil_hex = data.hex() # bytes → hex

print(hasil_hex)
```
Hasilnya: `63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d`

kenapa saya menggunakan function .encode()? Untuk mengubah String biasa ke dalam bentuk bytes agar bisa di enkripsi ke dalam heksadecimalnya, karena kalo mentah string -> hex itu tidak bisa.
