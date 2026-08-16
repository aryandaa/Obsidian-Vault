#latihan 

Kita belum akan membuat image dari disk asli. Jangan mencoba eksperimen forensic pertama dengan `/dev/sda` milik komputer sendiri. Ada banyak cara untuk mengubah hard disk menjadi dekorasi meja.

Kita akan menggunakan file dummy sebagai media latihan.

Buat directory:
```bash
mkdir -p ~/forensic-lab/disk-image
cd ~/forensic-lab/disk-image
```

Buat file image berukuran 20 MB:
```bash
dd if=/dev/zero of=evidence.raw bs=1M count=20
```

Kemudian:
```bash
ls -lh evidence.raw
```

Kamu akan melihat file sekitar:
```text
20M
```

Sekarang kita memiliki:
```text
evidence.raw
```

yang akan kita perlakukan sebagai **forensic image latihan**.

---
# Menghitung Hash Image

Sekarang lakukan:

```bash
sha256sum evidence.raw
```

Hasilnya kira-kira:
```text
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  evidence.raw
```

Simpan nilai tersebut.

Misalnya:
```text
evidence.sha256
```

Kita bisa membuatnya:
```bash
sha256sum evidence.raw > evidence.sha256
```

Kemudian:
```bash
cat evidence.sha256
```

Sekarang kita memiliki:
```text
evidence.raw
evidence.sha256
```

Hash tersebut menjadi fingerprint untuk image pada saat tersebut.

---
# Verifikasi Hash

Sekarang jalankan:
```bash
sha256sum -c evidence.sha256
```

Jika tidak berubah, hasilnya akan menunjukkan:
```text
evidence.raw: OK
```

Sekarang kamu sudah melakukan salah satu proses penting dalam forensic workflow:
```text
Image
  ↓
Hash
  ↓
Verification
```

---
# Menguji Perubahan

Sekarang kita sengaja membuat perubahan pada image latihan.

Jangan lakukan ini pada evidence asli.

Kita gunakan:
```text
evidence.raw
```

yang hanya merupakan file dummy.

Tambahkan data:
```bash
echo "test" >> evidence.raw
```

Kemudian:
```bash
sha256sum -c evidence.sha256
```

Sekarang hasilnya seharusnya menunjukkan bahwa verification gagal.

Ini menunjukkan konsep:

```text
Before modification
SHA-256 = A

After modification
SHA-256 = B

A ≠ B
```

Satu perubahan saja dapat menghasilkan hash berbeda.

Itulah mengapa hash sangat berguna untuk mendeteksi perubahan terhadap evidence yang sedang diverifikasi.

Setelah selesai praktik, jangan gunakan `evidence.raw` tersebut sebagai evidence lagi karena kita memang sengaja mengubahnya.