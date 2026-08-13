#latihan 

Sekarang praktik pertama kita akan dibuat sederhana dulu. Belum ada malware, belum ada memory dump, belum ada kasus yang membuatmu mempertanyakan pilihan hidup.

Kita akan membuat beberapa file evidence sendiri dan mengamati bagaimana evidence dapat diverifikasi.

Di Linux, buat sebuah directory:

```bash
mkdir forensic-lab
cd forensic-lab
```

Kemudian buat sebuah file:

```bash
echo "Digital Forensics Lab" > evidence.txt
```

Sekarang lihat file tersebut:

```bash
cat evidence.txt
```

Kemudian hitung SHA-256:

```bash
sha256sum evidence.txt
```

Kamu akan mendapatkan hash seperti:

```text
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  evidence.txt
```

Nilai persisnya akan berbeda berdasarkan isi file.

Sekarang buat salinan:

```bash
cp evidence.txt evidence-copy.txt
```

Kemudian hash keduanya:

```bash
sha256sum evidence.txt evidence-copy.txt
```

Hash keduanya harus sama.

Sekarang kita sengaja mengubah evidence copy:

```bash
echo "modified" >> evidence-copy.txt
```

Kemudian:

```bash
sha256sum evidence.txt evidence-copy.txt
```

Sekarang hash-nya berbeda.

Di sinilah kamu mulai melihat hubungan antara **integrity dan evidence**. Kalau sebuah evidence berubah, hash dapat membantu kita mendeteksi perubahan tersebut.

Praktik kecil ini memang terlihat sederhana, tetapi konsepnya akan kita bawa terus sampai nanti kamu menerima forensic image berukuran gigabyte. Bedanya nanti bukan `evidence.txt`, melainkan sesuatu seperti:

`Windows-Forensic-Image.E01`

dan ukurannya mungkin membuat storage laptop ikut mempertanyakan keputusan hidup.