#programming
Untuk memahami Bilangan Biner lebih lanjut, ke sesi ini terlebih dahulu 
![Binary](Binary.md)

Operasi Bitwise pada Python yaitu untuk menggeser atau membandingkan bilangan biner yang sudah di tentukan dengan cara perbit, contoh:
saya mempunyai bilangan 
10 dengan biner 00001010, dan
13 dengan biner 00001101.

lalu akan saya gunakan operasi OR untuk menghitung bitwise nya berapa dengan cara manual:

0 0 0 0 1 0 0 1 (10)
0 0 0 0 1 1 0 1 (13)

0 or 0 = 0
0 or 0 = 0
0 or 0 = 0
0 or 0 = 0
1 or 1 = 1.
1 or 0 = 1.
0 or 0 = 0.
1 or 1 = 1.

jadi 10 bitwise or 13 adalah adalah 15 (00001101) 

```Python
a = 10
b = 13

#bitwise OR ( | )
c = a | b
print(c)
```

dan begitu juga dengan operasi lainnya seperti AND, XOR, NOT, dan lain-lain. untuk logika perhitungan manualnya.
  
```Python
#bitwise AND (&)
c = a & b
print(c)
```
  
```Python
#bitwise XOR (^)
c = a ^ b
print(c)
```

```Python
#bitwise NOT (~)
c = ~a
print(c)
```
untuk not ini tidak membandingkan 2 bilangan, tetapi mencari not bit dari 1 variable saja.


lalu ada logika shift, untuk melakukan pergeseran pada bit, dengan cara:
10 = 00001010
jika di geser ke kanan 1 kali, maka akan jadi 
00000101 dan jika di desimalkan akan menjadi 5
```Python
#bitwise shift right (>>)
c = a >> 1
print(c)
#menggeser ke kanan
```
begitu pula dengan shift left 1 kali.
(10) 00001010 -> (20) 00010100

```Python
#bitwise shift left (<<)
c = a << 1
print(c)
#menggeser ke kiri
```

kita bisa mengatur jumlah pergeserannya sebanyak apapun. tetapi jika jumlah pergeserannya sudah melebihi jumlah bit, dia tidak kembali ke angka awal, tetapi terus menambahkan bit 0 di setiap ujungnya. misalnya:

```Python
c = a << 10
```
output = 10100000000000.
