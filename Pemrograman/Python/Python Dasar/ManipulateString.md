#programming 
Beberapa function yang berguna untuk memanipulasi string, seperti mencari kata, menghitung, dan menggabungkan.

```Python
namaPertama = "Muhammad"
namaKedua = "Aryanda"
namaKetiga = "Sanggadiennata"
namaLengkap = namaPertama +" "+ namaKedua +" "+ namaKetiga
print(namaLengkap)
#berfngsi untuk menggabungkan string
```

1. untuk menghitung panjangnya string
```Python
panjang = len(namaLengkap)
print (panjang)
```

2. Mencari kata
```python
find = "yanda"
status = find in namaLengkap
print (status)
```
jika ada maka hasilnya true
jidak tidak ada hasilnya false
lowercase dan uppercase dianggap berbeda (case sensitive)

3. Mengulang string
```Python  
print("wk" * 20)
```

4. Mengambil huruf paling kecil
```Python
print(min(namaLengkap))
#hasilnya spasi, karena spasi dianggap nilai paling kecil
```
5. mengambil huruf paling besar
```Python
print(max(namaLengkap))
```

6. operator dalam bentuk method
```Python
jumlah = namaLengkap.count("a")
print(jumlah)
```
untuk menghitung berapa huruf yang terhandung dalam kalimat itu