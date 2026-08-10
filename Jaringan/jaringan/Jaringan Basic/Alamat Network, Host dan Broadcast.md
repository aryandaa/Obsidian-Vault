#jaringan 

Dari suatu blok alamat IP Address terdiri dari Alamat Network, Host dan Broadcast. 
- Alamat Network merupakan identitas penanda suatu network. Alamat network ini digunakan oleh router dalam mencari arah network yang dituju. Alamat network ini tidak boleh digunakan sebagai alamat komputer atau perangkat karena merupakan identitas dari network nya. 
- Alamat Host merupakan alamat yang dapat digunakan oleh perangkat atau komputer sebagai alamat IP nya. 
- Alamat Broadcast merupakan alamat yang digunakan untuk mengirimkan pesan keseluruh perangkat yang berada di dalam network tersebut. Alamat broadcast juga tidak dapat digunakan sebagai alamat suatu perangkat atau komputer.

Alamat Network merupakan alamat pertama dalam suatu jaringan yang ditandai dengan nilai bit dari host portion nya bernilai 0 semua. Sedangkan alamat Broadcast merupakan alamat akhir dari suatu jaringan yang ditandai dengan nilai bit dari host portion nya bernilai 1 semua. Alamat host merupakan alamat diantara alamat network dan alamat broadcast. Contoh ada suatu alamat network 192.168.10.0/24, maka pembagian alamatnya seperti pada gambar dibawah ini.
![](img/Network%20Address.png)

Contoh: Diketahui IP 192.168.1.1, 
Tentukanlah: 
a) Jenis kelas IP, 
b) Alamat Network (Network Address/ NA), 
c) Subnet mask, 
d) Alamat Host (Host Address/ HA),
e) Alamat Broadcast

Jawab: 
a) Jenis kelas IP : Kelas C 
b) Alamat Network (Network Address/ NA) : 192.168.1.0 
c) Subnet mask : 255.255.255.0 
d) Alamat Host (Host Address/ HA) : 1 
e) Alamat Broadcast : 192.168.1.255 Prefix Notation : 192.168.1.1/24  Network prefix panjang 24 bit

