Komputer atau sistem tidak memahami huruf atau bahasa manusia, yang dia pahami cuman bytes.
1 byte = 8 bit dan nilainya 0 sampai 255.

kalo kita menulis "hallo", itu adalah bahasa manusia, di balik layar di sistem teks itu di ubah menjadi deretan byte berdasarkan ASCII.

begini urutaannya:
teks -> angka (kode karakter) -> byte -> lalu di proses oleh sistem.

# Python Untuk Bytes
```Python
from Crypto.Util.number import *

ciphertext = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
decode = long_to_bytes(ciphertext)

print (decode)
```