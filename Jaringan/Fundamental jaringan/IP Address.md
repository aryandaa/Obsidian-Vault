#jaringan 
Ip adalah alamat global unik untuk interface suatu jaringan, yang memiliki:
	- adalah 32 bit identifier
	- mengkodekan nomor jaringan (network prefix) dan nomor host (host number). Network prefic mengidentifikasikan suatu jaringan dan host number mengidentifikasikan suatu host spesifik. nomor ini bersifat unik, dan tidak sama dengan yang lain. 

#### Notasi Dotted Decimal
- Ip address ditulis dalam bentuk dotted decimal notation. 
- Tiap byte diidentikasikan dengan nomor decimal dalam range (0....255)

contoh:
1000000 | 10001111 | 10001001 | 10010000
1st Byte  | 2nd Byte  |  3rd Byte   | 4th Byte
: 128        | : 143         | : 137          | : 144
semua itu di gabungkan menjadi = 128.143.137.144

### Terminologi IP versi 4:
1. Network Address
2. Host Address
3. Subnet Mask
	1. Subnet Mask digunakan untuk mendapatkan Network Address dengan meng-AND kan dengan alamat ip suatu host
	Alamat Ip = 202.46.249.33 = (dibinerkan) 11001010. 00011010.11111001.00100001
	Subnet mask = 255.255.255.0 = (dibinerkan) 11111111.11111111.11111111.00000000
	jadi Network address nya adalah hasil dari meng-AND kan kedua biner itu.
4. Default Gateway Address
5. Broadcast Address

