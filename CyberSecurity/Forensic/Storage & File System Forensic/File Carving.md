#cybersecurity 

Pada materi sebelumnya kita sudah membahas deleted file dan unallocated space. Kita mengetahui bahwa sebuah file yang dihapus tidak selalu langsung membuat seluruh byte-nya hilang. Kita juga mengetahui bahwa recovery dapat dilakukan dengan bantuan metadata filesystem apabila struktur seperti MFT masih memberikan informasi yang cukup.

Sekarang kita menghadapi kondisi yang lebih sulit.

Bayangkan sebuah file sudah dihapus, kemudian sebagian metadata filesystem-nya sudah tidak dapat digunakan. Kita tidak lagi mempunyai informasi lengkap seperti:
```text
Filename
File size
MFT record
Data runs
Directory entry
```

Tetapi data file tersebut mungkin masih tersisa di dalam unallocated space.

Pertanyaannya menjadi:
> Kalau filesystem sudah tidak memberi tahu kita file itu apa, bagaimana kita menemukan file tersebut?

Di sinilah **file carving** digunakan.

File carving adalah teknik untuk mencari dan merekonstruksi file berdasarkan karakteristik data file itu sendiri, biasanya melalui **file signature**, struktur internal, dan pola data tertentu, tanpa bergantung sepenuhnya pada metadata filesystem.

Secara sederhana:
```text
Filesystem Metadata
        ↓
      Tidak cukup
        ↓
Unallocated Space
        ↓
Search File Structure
        ↓
File Signature
        ↓
Candidate File
        ↓
Reconstruction
        ↓
Recovered File
```

Ini berbeda dengan pendekatan sebelumnya menggunakan:
```text
MFT
 ↓
Data Runs
 ↓
icat
```

Pada carving, kita mulai lebih dekat dengan **raw bytes**.

---
# Mengapa file carving diperlukan?

Misalnya kita mempunyai:
```text
secret.jpg
```

File tersebut pernah berada di disk.

Kemudian:
```text
secret.jpg
    ↓
deleted
    ↓
MFT record overwritten
    ↓
directory entry gone
```

Tetapi sebagian data masih berada di unallocated space.

Filesystem mungkin sudah tidak dapat menjawab:
```text
"Di mana secret.jpg?"
```

Tetapi byte yang membentuk JPEG mungkin masih ada:
```text
FF D8 FF E0 ...
```

Maka kita dapat mencari pola tersebut.

Jadi perbedaan pendekatannya kira-kira seperti ini:
```text
Normal filesystem analysis:

MFT
 ↓
Filename
 ↓
Data location
 ↓
File

File carving:

Raw storage
 ↓
File signature
 ↓
File structure
 ↓
Potential file
```

Inilah alasan file carving sangat berguna ketika filesystem metadata sudah rusak atau tidak tersedia.

---
# File Signature

Salah satu konsep utama dalam file carving adalah **file signature**.

Sebuah format file sering mempunyai byte tertentu yang dapat membantu mengidentifikasi awal file.

Misalnya JPEG biasanya memiliki signature awal yang dikenal sebagai:
```text
FF D8 FF
```

PNG memiliki signature:
```text
89 50 4E 47 0D 0A 1A 0A
```

PDF memiliki:
```text
25 50 44 46
```

yang jika diterjemahkan ke ASCII menjadi:
```text
%PDF
```

ZIP memiliki signature yang sering terlihat sebagai:
```text
50 4B 03 04
```

Karena itu kita dapat membayangkan proses sederhana:
```text
Raw bytes
    ↓
Search for known signature
    ↓
Found candidate
    ↓
Determine file boundaries
    ↓
Extract
```

Tetapi ada satu masalah besar.

Menemukan signature **belum berarti kita berhasil mendapatkan file yang utuh**.

---
# Header dan Footer

Dalam file carving, kita sering berbicara mengenai **header** dan **footer**.

Header berada pada bagian awal file.

Footer atau end marker dapat membantu menunjukkan bagian akhir file, tergantung formatnya.

Misalnya secara sederhana:
```text
┌──────────┬─────────────────────┬──────────┐
│ Header   │ File Content        │ Footer   │
└──────────┴─────────────────────┴──────────┘
     ↑                                ↑
    Start                             End
```

Jika kita mengetahui pola awal dan akhir, kita mempunyai peluang untuk menentukan batas file.

Misalnya secara konseptual:
```text
FF D8 FF
     ↓
JPEG DATA
     ↓
FF D9
```

`FF D9` sering digunakan sebagai JPEG End of Image marker.

Maka carving sederhana dapat mencari:
```text
Start:
FF D8 FF

End:
FF D9
```

dan mengambil byte di antara keduanya.

Tetapi jangan menganggap semua file sesederhana ini. Format modern bisa memiliki struktur kompleks, metadata tambahan, compression, container, dan fragmentasi.

---
# File Carving bukan sekadar grep

Pemula kadang membayangkan carving sebagai:
```bash
grep "signature" disk.raw
```

dan selesai? Tidak.

File carving harus mempertimbangkan struktur file dan kemungkinan adanya data yang tidak berhubungan di antara byte yang ditemukan.

Misalnya kita menemukan:
```text
JPEG Header
      ↓
Data
      ↓
Unrelated Data
      ↓
JPEG Footer
```

Apakah seluruh bagian tersebut benar-benar berasal dari satu JPEG?

Belum tentu.

Karena itu carving yang baik perlu memahami karakteristik format file.

---
# Fragmentation

Ini adalah salah satu masalah terbesar dalam file carving.

Misalnya sebuah file JPEG awalnya tersimpan secara berurutan:
```text
Cluster 100
Cluster 101
Cluster 102
Cluster 103
```

Kemudian filesystem mengalami fragmentasi:
```text
Cluster 100
Cluster 250
Cluster 102
Cluster 400
```

Data file tidak lagi contiguous.

Kalau kita hanya melakukan carving sederhana:
```text
Header
 ↓
ambil byte sampai footer
```

hasilnya bisa salah karena terdapat data file lain di antara fragment tersebut.

Secara visual:
```text
Disk:

[FILE A]
[FILE B]
[FILE A]
[FILE C]
[FILE A]
```

File A terfragmentasi.

Carver harus menentukan bagaimana potongan-potongan tersebut berhubungan.

Karena itu:
```text
File carving
≠
sekadar mencari header
```

File carving sebenarnya adalah masalah **reconstruction**.

---
# Contoh Fragmentasi

Bayangkan file:
```text
photo.jpg
```

memiliki data:
```text
A B C D E F G H
```

Filesystem menyimpannya:
```text
Cluster 10 → A B
Cluster 20 → C D
Cluster 35 → E F
Cluster 50 → G H
```

Jika metadata filesystem masih tersedia, kita dapat mengetahui hubungan:
```text
10 → 20 → 35 → 50
```

Tetapi jika metadata sudah hilang, carving harus mencoba menentukan urutan tersebut dari karakteristik data.

Semakin kompleks format file, semakin sulit prosesnya.

---
# File Carving dengan The Sleuth Kit

Kita sebelumnya menggunakan beberapa tools dari The Sleuth Kit:
```text
mmls
fsstat
fls
istat
icat
```

Untuk file carving, salah satu tool yang umum digunakan dalam ekosistem Sleuth Kit adalah:
```bash
blkls
```

`blkls` dapat digunakan untuk mengambil data dari filesystem image, termasuk area yang relevan untuk analisis unallocated space.

Misalnya secara konseptual:
```bash
blkls disk.raw > unallocated.raw
```

Sekarang kita memiliki:
```text
disk.raw
      ↓
blkls
      ↓
unallocated.raw
```

Kemudian raw unallocated data tersebut dapat dianalisis menggunakan tool carving.

Dalam praktik nanti kita juga akan mengenal tool seperti:
```text
foremost
scalpel
photorec
```

Tool-tool tersebut memiliki pendekatan carving masing-masing.

---
# Foremost

Salah satu tool klasik untuk file carving adalah **Foremost**.

Secara sederhana:
```bash
foremost evidence.raw
```

Foremost akan mencoba mengidentifikasi file berdasarkan signature yang dikenalnya.

Hasilnya dapat berupa directory:
```text
output/
├── audit.txt
├── jpg/
├── png/
├── pdf/
└── zip/
```

Jika berhasil menemukan candidate file, hasil carving akan diletakkan sesuai kategori.

Tetapi hasil carving harus dianggap sebagai **candidate evidence** sampai diverifikasi.

Misalnya tool mengatakan:
```text
1 jpg recovered
```

Jangan langsung menyimpulkan:
> "Saya berhasil mendapatkan foto asli."

Kita perlu memeriksa:
```text
Apakah file dapat dibuka?
Apakah struktur JPEG valid?
Apakah file lengkap?
Apakah data terfragmentasi?
Apakah content konsisten?
Berapa ukuran file?
Apakah hash dapat dicatat?
```

---
# Scalpel

Tool lain yang penting adalah **Scalpel**.

Scalpel menggunakan konfigurasi file signature untuk menentukan pola yang ingin dicari.

Secara konseptual:
```text
Input Image
     ↓
Scalpel
     ↓
Signature Rules
     ↓
Search
     ↓
Candidate Files
```

Ini menarik secara forensic karena kamu dapat memahami bahwa carving sebenarnya bergantung pada pengetahuan mengenai format file.

Kita tidak hanya berkata:
> "Tool ini mencari JPG."

Kita harus memahami:
> "Tool ini tahu karakteristik byte tertentu yang merepresentasikan format tersebut."

---
# PhotoRec

**PhotoRec** juga sangat terkenal dalam data recovery dan file carving.

Meskipun namanya mengandung "Photo", tool ini tidak hanya digunakan untuk gambar. PhotoRec mendukung berbagai jenis file.

Pendekatannya berfokus pada filesystem-independent recovery.

Artinya ia dapat mencari file berdasarkan struktur data tanpa terlalu bergantung pada filesystem metadata.

Secara konseptual:
```text
Filesystem Metadata
        X
        │
        │ tidak menjadi ketergantungan utama
        ↓
Raw Data
        ↓
Signature / Structure
        ↓
Recovery
```

Ini membuat carving sangat berguna ketika filesystem mengalami kerusakan atau metadata sudah tidak tersedia.

---
# File Carving vs Metadata Recovery

Ini perbedaan yang wajib kamu kuasai.

Metadata recovery:
```text
MFT
 ↓
File Record
 ↓
Data Runs
 ↓
icat
 ↓
Recovered File
```

File carving:
```text
Raw / Unallocated Data
 ↓
Signature
 ↓
File Structure
 ↓
Reconstruction
 ↓
Recovered File
```

Metadata recovery biasanya memberikan konteks lebih kaya:
```text
Filename
Timestamp
MFT Record
Path
Size
```

Sedangkan carving dapat menemukan data yang metadata filesystem-nya sudah hilang, tetapi konteks filesystem-nya mungkin tidak lengkap.

Karena itu keduanya bukan pengganti satu sama lain tetapi Keduanya saling melengkapi.

---
# Mengapa hasil carving harus diverifikasi?

Bayangkan carver menemukan:
```text
recovered_001.jpg
```

File tersebut memiliki header JPEG.

Apakah itu otomatis berarti file valid?

Belum tentu.

Kemungkinan yang terjadi:
```text
1. File benar-benar utuh
2. File sebagian corrupt
3. File terfragmentasi
4. False positive
5. File berisi data campuran
```

Misalnya header JPEG ditemukan secara kebetulan di tengah data.

Tool bisa saja menganggap:
```text
FOUND JPEG
```

padahal sebenarnya bukan file JPEG yang valid.

Karena itu kita perlu melakukan validation.

---
# Hash pada hasil recovery

Setelah sebuah file berhasil direcover, kita dapat menghitung hash:
```bash
sha256sum recovered.jpg
```

Misalnya:
```text
abc123...  recovered.jpg
```

Hash ini dapat digunakan untuk mengidentifikasi hasil recovery dan menjaga konsistensi terhadap file hasil analisis.

Workflow sederhananya:
```text
Forensic Image
      ↓
Carving
      ↓
Recovered File
      ↓
Validate
      ↓
Hash
      ↓
Analyze
```

Perhatikan bahwa hashing tetap kembali muncul.

Materi pertama kita tentang integrity ternyata tidak dibuang ke tong sampah kurikulum. Ia terus muncul di berbagai tahap forensic workflow.

---
# False Positive

Dalam file carving kita harus mengenal **false positive**.

Misalnya tool menemukan pola:
```text
50 4B 03 04
```

yang biasanya merupakan signature ZIP.

Tool berkata:
```text
ZIP found
```

Tetapi ternyata byte tersebut hanya muncul sebagai bagian dari data lain dan bukan sebuah archive yang valid.

Maka:
```text
Signature found
```

tidak sama dengan:
```text
Valid file recovered
```

Kita perlu melakukan validation terhadap hasilnya.

Ini prinsip yang sama dengan timestamp tadi:
```text
Artifact
```

tidak otomatis sama dengan:

```text
Conclusion
```

---
# Hubungan dengan Praktik Sebelumnya

Perjalanan kita sampai sini sebenarnya sangat sengaja.

Kita mulai dengan:
```text
evidence.txt
 ↓
SHA-256
```

Kemudian:
```text
disk.raw
 ↓
Hash
```

Kemudian:

```text
GPT
 ↓
Partition
```

Kemudian:
```text
NTFS
 ↓
MFT
```

Kemudian:
```text
File
 ↓
Metadata
```

Kemudian:
```text
Deleted File
 ↓
Unallocated Space
```

Sekarang:
```text
Unallocated Space
 ↓
File Carving
 ↓
Recovered File
```

Jadi seluruh materi yang kamu pelajari mulai membentuk satu rantai forensic yang nyata:
```text
Evidence
 ↓
Acquisition
 ↓
Integrity
 ↓
Disk Image
 ↓
Partition
 ↓
Filesystem
 ↓
Metadata
 ↓
Timeline
 ↓
Deletion
 ↓
Unallocated Space
 ↓
Carving
 ↓
Recovery
```

Ini sudah jauh lebih dekat dengan workflow investigation sebenarnya dibanding sekadar belajar command satu per satu.

---
# Batasan File Carving

File carving memiliki keterbatasan yang harus kamu pahami.

Kalau file sudah tertimpa:
```text
Old Data
   ↓
Overwritten
   ↓
New Data
```

carving mungkin tidak bisa mengembalikan file asli.

Kalau file terfragmentasi:
```text
Fragment A
Fragment B
Fragment C
```

carving mungkin hanya mendapatkan sebagian data atau menghasilkan file corrupt.

Kalau format file tidak memiliki signature yang jelas, identifikasi juga menjadi lebih sulit.

Kalau encryption digunakan:
```text
Encrypted Data
```

carving mungkin berhasil menemukan container atau file, tetapi tidak berarti kita bisa membaca isi file tersebut.

Jadi:
```text
Carving ≠ Guaranteed Recovery
```

Carving adalah teknik untuk **mencari dan merekonstruksi kemungkinan file dari raw data**.