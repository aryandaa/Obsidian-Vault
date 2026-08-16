#latihan 
Setelah teori ini, praktik kita akan menggunakan **disk image yang sudah kamu buat pada latihan sebelumnya**, bukan membuat latihan yang terpisah.

Targetnya adalah membangun filesystem NTFS pada image, memasukkan beberapa file, kemudian melakukan examination menggunakan Sleuth Kit.

Workflow praktik:

```text
disk.raw
   ↓
GPT
   ↓
Partition
   ↓
NTFS
   ↓
Create files
   ↓
Delete file
   ↓
mmls
   ↓
fsstat
   ↓
fls
   ↓
istat
   ↓
MFT analysis
   ↓
icat
   ↓
Recovery
```

Dengan demikian latihan kita tetap bersambung seperti yang kamu minta sejak awal. Praktik yang sudah kamu lakukan bukan latihan sekali pakai, tetapi menjadi bagian dari satu forensic case yang terus kita bangun.