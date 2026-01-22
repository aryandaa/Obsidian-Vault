#programming 
Ada 2 error dalam python, yaitu:
1. Syntax Error
2. Runtime Error

## Syntax Error
Syntax error terjadi karena kesalahan penulisan dalam code python, baik lupa menaruh petik, atau ada yang typo saat menuliskan perintahnya.
untuk mengatasi error ini dengan cara menghapal cara penulisan yang benar pada syntax maupun pada function di python.

contoh Syntax error adalah:
```python
print ("hello)
fpr x in world:
	print(x)
```
kesalahan diatas itu adalah lupa menaruh titik koma, dan typo menulis function,
penulisan yang benar adalah:
```Python
print ("hello")
for x in world:
	print(x)
```

## Runtime Error
ini adalah jenis error yang terjadi ketika code sedang berjalan, berbeda dengan syntax error, error ini di akibatkan oleh user itu sendiri, misalnya ada sebuah program meminta inputan yang berbentuk integer, contohnya umur, tetapi si user menginput string dengan value "dua puluh", maka code tersebut akan menolak inputan user itu dan akan error.

untuk mengatasi error ini adalah mempertimbangkan kemungkinan kesalahan dari user dan membuat code antisipasinya, sebagai contoh:
untuk mengatasi user salah input tipe data seperti diatas, maka dibuatkan sebuah percabangan yang tidak membolehkan user menginputkan tipe data apapun selain yang di pilih.
