#jaringan 
IP Address merupakan alamat setiap komputer. Dalam jaringan komputer dikenal ada alamat MAC Address dan juga IP Address. IP Address ini ibarat nama seseorang sedangkan MAC Address ibarat tampang atau muka dari seseorang. Nama dan tampilan muka seseorang merupakan identitas yang digunakan sebagai pembeda antara orang yang satu dengan orang yang lain. Ibarat muka seseorang, MAC Address merupakan alamat bawaan dari lahir yang seharusnya tidak berubah-ubah. Sedangkan IP Address merupakan pemberian yang menunjukkan identitas dari perangkat tersebut ketika terhubung ke jaringan. IP Address terdiri dari 32 bit untuk versi 4 (IPv4) dan 128 bit (IPv6).

IP Address merupakan pengenal yang digunakan untuk memberi alamat pada tiap-tiap komputer dalam jaringan. Format IP address adalah bilangan 32 bit yang tiap 8 bit-nya dipisahkan oleh tanda titik. Adapun format IP Address dapat berupa bentuk ‘biner’ (xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx dengan x merupakan bilangan biner 0 atau 1). Atau dengan bentuk empat bilangan desimal yang masing-masing dipisahkan oleh titik, bentuk ini dikenal dengan ‘dotted decimal’ (xxx.xxx.xxx.xxx adapun xxx merupakan nilai dari 1 oktet yang berasal dari 8 bit). Dikenal dua cara pembagian IP Address, yakni: classfull dan classless addressing.

### 1) Classfull Addressing
Classfull merupakan metode pembagian IP address berdasarkan kelas, dimana IP address (yang berjumlah sekitar 4 milyar) dibagi kedalam lima kelas yakni:
1. Kelas A:
	1. HOB : 0
	2. NET ID Bits: 8
	3. Host Id Bits: 24
	4. No Of Network: 2$^7$ = 128
	5. Host Per Network: 2^24 = 26.777,216.
	6. Start Address: 0.0.0.0 
	7. End Address: 127.255.255.255
2. Kelas B:
	1. HOB : 10
	2. NET ID Bits: 16
	3. Host Id Bits: 16
	4. No Of Network: 2^14 = 16,384
	5. Host Per Network: 2^16 = 65,536
	6. Start Address: 128.0.0.0.0 
	7. End Address: 191.255.255.255
3. Kelas C:
	1. HOB : 110
	2. NET ID Bits: 24
	3. Host Id Bits: 8
	4. No Of Network: 2^21 = 2,097,152
	5. Host Per Network: 2^8 = 256
	6. Start Address: 192.0.0.0 
	7. End Address: 223.255.255.255
4. Kelas D:
	1. HOB : 1110
	2. NET ID Bits: -
	3. Host Id Bits: -
	4. No Of Network: -
	5. Host Per Network: -
	6. Start Address: 224.0.0.0 
	7. End Address: 239.255.255.255
5. Kelas E:
	1. HOB : 1111
	2. NET ID Bits: -
	3. Host Id Bits: -
	4. No Of Network: -
	5. Host Per Network: -
	6. Start Address: 240.0.0.0 
	7. End Address: 255.255.255.255


### 2) Classless Addressing
Metode classless addressing (pengalamatan tanpa kelas) saat ini mulai banyak diterapkan, yakni dengan pengalokasian IP Address dalam notasi Classless Inter Domain Routing (CIDR). Istilah lain yang digunakan untuk menyebut bagian IP address yang menunjuk suatu jaringan secara lebih spesifik, disebut juga dengan Network Prefix. Biasanya dalam menuliskan network prefix suatu kelas IP Address digunakan tanda garis miring (Slash) “/”, diikuti dengan angka yang menunjukan panjang network prefix ini dalam bit. Gambar dibawah ini menunjukkan contoh penulisan Prefix Length.
![](img/Classless%20Addressing.png)

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

