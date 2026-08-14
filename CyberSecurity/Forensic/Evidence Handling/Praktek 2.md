#latihan 

Sekarang kita mulai praktik yang benar-benar berhubungan dengan konsep integrity.

Buat directory:
```bash
mkdir forensic-integrity
cd forensic-integrity
```

Buat evidence:
```bash
echo "CASE-01: Original Evidence" > evidence.txt
```

Sekarang lakukan hashing:
```bash
sha256sum evidence.txt
```

Misalnya hasilnya:
```text
<hash-1>  evidence.txt
```

Simpan hash tersebut:
```bash
sha256sum evidence.txt > evidence.sha256
```

Sekarang kita memiliki:
```text
forensic-integrity/
├── evidence.txt
└── evidence.sha256
```

File `evidence.sha256` berisi hash referensi.

Sekarang verifikasi:
```bash
sha256sum -c evidence.sha256
```

Jika tidak berubah, hasilnya akan seperti:
```text
evidence.txt: OK
```

Sekarang kita sengaja mengubah evidence:
```bash
echo "MODIFIED DATA" >> evidence.txt
```

Kemudian lakukan verifikasi lagi:
```bash
sha256sum -c evidence.sha256
```

Sekarang hasilnya akan menunjukkan bahwa verification gagal.

Inilah simulasi sederhana dari konsep:
```text
Original Evidence
       ↓
      Hash
       ↓
Reference Hash
       ↓
Evidence Analysis
       ↓
Verification
       ↓
OK / FAILED
```

# Praktik kedua: memahami authenticity

Sekarang buat dua file:
```bash
echo "CASE-01 Evidence A" > evidence-a.txt
echo "CASE-01 Evidence B" > evidence-b.txt
```

Hitung hash:
```bash
sha256sum evidence-a.txt evidence-b.txt
```

Hash berbeda karena isi berbeda.

Sekarang bayangkan seseorang mengirimkan file:
```text
evidence-a.txt
```

tetapi ternyata file tersebut bukan berasal dari sumber evidence yang sebenarnya.

Hash-nya tetap valid.

Di sinilah kamu harus memahami batasan hash.

Hash dapat membantu:
```text
Detect modification
```

tetapi hash sendirian tidak dapat membuktikan:
```text
Provenance
```

atau asal-usul evidence.

Untuk membuktikan provenance, kita membutuhkan proses acquisition dan dokumentasi evidence yang baik.

---
# Mini Investigation

Sekarang kita buat simulasi kecil.

Misalkan investigator menemukan:
```text
case01/
├── evidence.txt
├── evidence.sha256
└── notes.txt
```

Isi `evidence.txt`:
```text
User downloaded suspicious-file.zip
```

Kemudian hash evidence tersebut sudah dicatat sebelumnya.

Ketika analyst menerima evidence, dia melakukan:
```bash
sha256sum -c evidence.sha256
```

Hasil:
```text
evidence.txt: OK
```

Artinya evidence masih konsisten dengan hash referensi.

Kemudian analyst melakukan analisis.

Setelah selesai, hash diperiksa lagi:
```bash
sha256sum -c evidence.sha256
```

Jika tetap:
```text
evidence.txt: OK
```

maka evidence tidak mengalami perubahan yang terdeteksi oleh hash selama proses tersebut.

Sekarang bandingkan dengan skenario:
```text
Before analysis
      ↓
Hash = ABC123
      ↓
Analysis
      ↓
File modified
      ↓
Hash = XYZ789
```

Sekarang ada discrepancy yang harus diselidiki.

Forensic analyst tidak boleh sekadar berkata:
> “Hash beda, ya sudah.”

Pertanyaannya menjadi:

> Kapan berubah?

> Apa yang menyebabkan perubahan?

> Siapa yang melakukan perubahan?

> Apakah perubahan terjadi pada evidence asli atau analysis copy?

> Apakah evidence tersebut masih dapat digunakan?

Ini sudah mulai masuk ke pola berpikir forensic yang sebenarnya.

---
# Kesalahan yang harus kamu hindari

Ada beberapa kesalahan yang ingin aku hentikan sejak awal.

Pertama, **menganggap hash sebagai bukti bahwa file aman**. Salah. Hash digunakan untuk verification dan identification, bukan menentukan apakah file berbahaya.

Kedua, **menganggap evidence yang tidak berubah otomatis autentik**. Salah. Integrity dan authenticity berbeda.

Ketiga, **menganalisis evidence asli secara sembarangan**. Dalam workflow forensic yang benar, kita berusaha mempertahankan evidence asli dan bekerja pada forensic image atau working copy.

Keempat, **mengabaikan volatile evidence**. Kalau sistem masih hidup dan RAM relevan terhadap kasus, mematikan sistem secara sembarangan bisa menghilangkan evidence penting.

Kelima, **percaya sepenuhnya kepada satu artifact**. Sebuah timestamp atau file saja jarang cukup untuk membuat kesimpulan kuat. Kita akan selalu berusaha melakukan **correlation**.

---