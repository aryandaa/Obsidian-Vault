#devops 
untuk menghapus docker image yang kita punya, kita bisa menggunakan perintah
```shell
docker image rm <NamaImage>:tag
```

tapi terkadang saat menghapus, kita mendapatkan error conflict karena ada salah satu container yang memakai image tersebut, contoh errornya seperti ini:
![](img/Pasted%20image%2020260724203413.png)

jika mendapati error seperti itu, kita harus menghapus container yang mengandung image itu terlebih dahulu, dengan cara yang sudah di sebutkan sebelumnya:
```shell
docker container stop <NamaContainer>  
docker container rm <NamaContainer>  
```

jika sudah, maka kita sudah bisa menghapus image tersebut..