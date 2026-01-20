#programming 
seperti bahasa pemrograman lain, di python juga mempunyai percabangan atau if else,
penulisannya juga hampir mirip.

susunan komponen dari if else python sebagai berikut:
1. if (kondisi jika true):
	- aksinya
2. elif (kondisi jika true):
	- aksinya
3. else : (aksi jika false)

implementasi
```python
umur = int(input("masukan umur km: "))

if umur >= 17 and umur <= 45:
    print("km sudah dewasa")
elif umur >= 46 and umur <= 60:
    print("KM SUDAH SANGAT TUA")
elif umur < 17 :
    print("km belum dewasa")
else : print ("masukan umur yang benar")
```

if pertama jika user memasukan umur dengan rasio 17 - 45.
else if pertama jika user memasukan umur dengan rasio 46 - 60.
else if kedua jika user memasukan umur dibawah 17.

dan else terakhir jika user memasukan umur yang tidak disebutkan dalam rasio maupun memasukan type data yang salah.

