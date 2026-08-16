#latihan 

Sekarang kita gunakan kembali konsep dari praktik sebelumnya.

Kita memiliki:
```text
~/forensic-lab/disk-image/evidence.raw
```

Namun perlu diingat, image yang kita buat sebelumnya dengan:
```bash
dd if=/dev/zero of=evidence.raw bs=1M count=20
```

hanya berisi zero dan **belum memiliki partition table sungguhan**.

Jadi kita akan membuat image latihan baru.

Buat directory:
```bash
mkdir -p ~/forensic-lab/partition-lab
cd ~/forensic-lab/partition-lab
```

Buat image:
```bash
dd if=/dev/zero of=disk.raw bs=1M count=100
```

Sekarang kita memiliki:
```text
disk.raw
```

Kita dapat memeriksanya dengan:
```bash
file disk.raw
```

Karena image masih kosong, tool mungkin hanya mengenalinya sebagai data biasa.

Sekarang kita perlu membuat partition table pada image.

Gunakan:
```bash
fdisk disk.raw
```

Di dalam `fdisk`, kita dapat menggunakan menu bantuan:
```text
m
```

Untuk membuat partition table baru, gunakan:
```text
g
```

Ini akan membuat GPT partition table.

Kemudian:
```text
n
```

untuk membuat partition baru.

Gunakan default values ketika ditanyakan agar kita tidak perlu menghitung manual dulu.

Kemudian:
```text
w
```

untuk menulis perubahan.

Setelah selesai:
```bash
fdisk -l disk.raw
```

Kamu seharusnya mendapatkan informasi mengenai partition yang baru dibuat.

---
# Membaca Partition Secara Forensic

Tool yang sangat berguna untuk melihat partition adalah:
```bash
mmls disk.raw
```

`mmls` merupakan bagian dari **The Sleuth Kit**.

Output-nya akan menunjukkan struktur partition berdasarkan sector.

Misalnya secara konsep:
```text
Slot    Start       End         Length
000:    0000000000  0000000000  ...
001:    0000002048  ...
```

Yang paling penting untuk sekarang adalah memahami:
```text
Start
End
Length
```

Informasi tersebut akan menjadi dasar ketika kita nanti melakukan filesystem analysis.

