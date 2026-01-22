#programming 
Nested if sebuah logic dari percabangan yang bersarang, yaitu pecabangan yang memiliki cabang lain sebagai verifikasi tambahan. 
sebagai analogi: 
saya memiliki 1 variable yang menyimpan nama hewan, lalu saya membuat sebuah function untuk melakukan pengecekan spesies hewan tersebut, apakah hewan itu berspesies mamalia atau bukan, jika iya maka langsung keluarkan output "hewan ini mamalia", jika tidak maka dilakukan lagi penyecekan apakah hewan itu bertelur atau ovovivivar.

contoh implementasi codenya
```python
hewan = "ayam"

if hewan == "ayam":
	print "ini hewan mamalia"
else:
	if hewan == "bertelur":
		print "ini hewan bertelur"
	elif hewan == "ular":
		print "ini hewan ovovivivar"
	else:
		print "masukan nama hewan yang ada di list"
```

jadi di dalam else ada lagi percabangan yang befungsi sebagai verifikasi, dan nested if ini tidak terbatas alias bebas menambahkannya sampai berapapun.

sebagai contoh lain:
```python
a = 50
b = 30

if a > b:
  if a > 40:
    print("WOW")
  else:
    print("HAI")
else:
  print("BYE")
```

disini saya memiliki 2 buah variable yang berisi 50 dan 30.
if pertama yaitu melakukan pengecekan apakah a lebih besar dari b? jika true maka lakukan if yang lain yaitu apakah a lebih besar dari 40? jika true lagi maka keluarkan output "wow", jika dalse "hai", dan jika dari awal hasilnya adalah false, maka langsung keluarkan output "bye".