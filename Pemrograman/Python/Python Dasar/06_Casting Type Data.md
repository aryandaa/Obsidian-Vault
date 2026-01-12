Casting Type data berfungsi untuk Merubah tipe data dari suatu tipe ke tipe lain
Misalnuy dari int ke str, 
dari str ke int, 
atau dari int ke float, dll

contoh penggunaan casting dari integer ke float

```Python
#===INT KE FLOAT===
data_int = 9
print("data = ", data_int, "type = ", type(data_int))

data_float = float(data_int)
print("data = ", data_float, "type = ", type(data_float))
#Outputnya = (9.0)
```

```Python
#===BOOL KE INT===
data_bool = True
print("data = ", data_bool, "type = ", type(data_bool))

data_int = int(data_bool)
print("data =", data_int, "type =", type(data_int))
#Output = 1
```

```Python
#===STR KE BOOL==

data_str = "ucup"
print("data =", data_str, "type =", type(data_str))

data_bool = bool(data_str)
print("data =", data_bool, "type =", type(data_bool))
#Output = True
```
  
Cara penggunannya Tinggal ketik nama type data lalu diberikan tanda kurung yang di dalamnya berisi data atau variable yang ingin di ubah..

misalnya:
int(data),
bool(data),
str(data),
float(data),
dan lain lain...