Xor adalah operator bitwise yang mengembalikan 0 (False) jika keduanya sama, dan mengembalikan 1 (True) jika salah satunya true.
di banyak challange XOR biasanya ditulis dengan simbol caret (^).

untuk bilangan biner, dia melakukan XOR nya per bit, contoh 
0110 ^ 1010 =
0 ^ 0 = 0
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1
hasil = 1100

tapi jika ingin melakukan XOR pada integer, maka integer itu di ubah ke decimal, lalu dari decimal ke biner terlebih dahulu.
tetapi jika ingin melakukannya di String, maka kita bisa menguba tiap string tersebut menjadi integer, yang mewakili karakter unicode.

# Python Untuk XOR

```Python
txt = "label"
key = 13

hasilXor = xor(key, txt).decode()
print (f"cyrpto{{{hasilXor}}}")
```
hasil `aloha`

