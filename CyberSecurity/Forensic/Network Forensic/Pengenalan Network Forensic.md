#cybersecurity 

Network Forensic adalah cabang digital forensics yang fokus pada **pengumpulan, pemeriksaan, dan analisis bukti yang berasal dari jaringan komputer**. Kalau disk forensics membedah hard disk dan memory forensics membedah RAM, maka network forensics membedah **komunikasi antar perangkat**: siapa bicara ke siapa, kapan, lewat protokol apa, dan data apa yang dikirim.

Kenapa ini penting? Karena hampir semua serangan di dunia nyata **melibatkan jaringan**. Malware harus berkomunikasi dengan command & control (C2), attacker harus masuk melalui port yang terbuka, data curian harus dikirim keluar, dan phishing harus melewati jaringan dulu sebelum sampai ke email. Bahkan ketika file sudah dihapus dari disk dan memory sudah dimatikan, jejak komunikasi bisa tetap tersimpan di packet capture, log server, atau firewall.

Sederhananya: kalau disk forensic menjawab "apa yang ada di komputer ini?", network forensic menjawab "apa yang terjadi di antara komputer-komputer ini?".

## Sumber evidence di jaringan

Evidence di jaringan tidak selalu berbentuk file. Ia bisa berupa:

1. **Packet capture (PCAP)**: rekaman mentah paket yang lewat di sebuah interface. Ini sumber evidence yang paling kaya karena berisi seluruh komunikasi.
2. **NetFlow / IPFIX**: ringkasan aliran komunikasi (siapa ke siapa, port, berapa banyak data). Tidak berisi isi paket, tetapi sangat berguna untuk melihat pola.
3. **Log server**: Apache/Nginx access log, DNS log, proxy log, firewall log, IDS/IPS alert.
4. **Log endpoint**: Windows Event Log, Sysmon, atau auth.log yang mencatat koneksi keluar dari sebuah mesin.
5. **Artefak host**: DNS cache, ARP cache, netstat, dan browser history yang menunjukkan komunikasi yang pernah terjadi.

Dalam lomba CTF, sumber yang paling sering muncul adalah PCAP. Karena itu modul ini akan sangat fokus pada membaca dan menganalisis PCAP.

## Apa itu PCAP?

PCAP adalah format file untuk menyimpan paket yang ditangkap. Nama resminya "packet capture". File ini berisi:

- Timestamp setiap paket.
- Data mentah paket (frame Ethernet, IP, TCP/UDP, dan payload aplikasi).
- Metadata capture seperti ukuran snaplen dan tipe link layer.

Format lama bernama **pcap**, format baru bernama **pcapng** (menyimpan metadata lebih banyak, mendukung beberapa interface). `tshark` dan Wireshark bisa membaca keduanya.

PCAP adalah evidence yang sangat berharga karena ia seperti **rekaman CCTV jaringan**: apa yang lewat, terekam apa adanya. Sayangnya, PCAP juga sangat sensitif terhadap waktu: kalau tidak di-capture saat kejadian berlangsung, maka tidak akan pernah ada lagi.

## Volatile evidence

Ingat konsep order of volatility dari materi Digital Evidence? Network traffic adalah salah satu evidence yang paling volatile.

Data di hard disk bisa bertahan bertahun-tahun. Memory bertahan sampai komputer dimatikan. Tetapi **paket yang lewat di jaringan hanya ada selama beberapa milidetik**. Kalau tidak ditangkap saat itu juga, paket tersebut hilang selamanya.

Ini alasan kenapa incident responder menangkap traffic secepat mungkin, dan kenapa organisasi memasang sensor yang merekam traffic secara terus menerus.

```
Jangan pernah berasumsi PCAP akan tersedia. Dalam investigasi nyata,
packet capture sering tidak ada, dan investigator harus bergantung
pada log dan artefak host.
```

## Evidence, Artifact, dan Finding di jaringan

Pola berpikir yang sudah kamu tanam di materi Evidence Handling tetap berlaku.

- **Evidence**: `traffic.pcap` atau `access.log`.
- **Artifact**: sebuah DNS query ke domain mencurigakan, sebuah TCP connection ke port aneh, sebuah HTTP POST dengan payload terenkode.
- **Finding**: hasil interpretasi, misalnya "mesin korban melakukan beacon ke server C2 setiap 8 detik selama 2 jam".

Satu paket sendirian sering tidak berarti. Tetapi serangkaian paket yang berkorelasi bisa membentuk cerita: scanning, exploit, beacon, exfiltrasi.

## Empat tahap dalam Network Forensic

Prosesnya mengikuti kerangka yang sama: **collection, examination, analysis, reporting**.

1. **Collection**: menangkap atau mengumpulkan evidence (PCAP, log, NetFlow). Pastikan waktu capture dan timezone tercatat.
2. **Examination**: memproses evidence agar informasi bisa ditemukan. Membuka PCAP, memfilter, mengikuti stream, mengekstrak file.
3. **Analysis**: memberi konteks. Menyusun timeline, mengkorelasikan antar artefak, mengidentifikasi pola serangan.
4. **Reporting**: menjelaskan temuan. Siapa yang bicara ke siapa, kapan, protokol apa, dan apa kesimpulannya.

## Tantangan dalam Network Forensic

1. **Volume**: satu hari traffic perusahaan bisa berisi miliaran paket. Tanpa filter dan triage, kamu tenggelam.
2. **Enkripsi**: HTTPS, SSH, dan VPN membuat isi komunikasi tidak terbaca. Yang tersisa hanyalah metadata (siapa, kapan, kemana, berapa besar).
3. **Spoofing**: IP bisa dipalsukan, MAC bisa diubah. Investigasi harus hati-hati sebelum menyimpulkan identitas.
4. **Timezone**: timestamps dari banyak sumber bisa berbeda zona. Selalu catat timezone setiap evidence.
5. **Fragmentasi**: paket yang terpecah perlu di-reassemble sebelum bisa dibaca isinya.

## Tool utama

Modul ini fokus pada tool command line yang sudah tersedia:

- **tshark**: command line Wireshark. Membaca, memfilter, dan mengekstrak dari PCAP.
- **Wireshark**: versi GUI untuk eksplorasi visual.
- **capinfos**: melihat informasi file PCAP.
- **mergecap / editcap**: menggabung dan memotong PCAP.
- **strings, xxd, base64**: untuk memproses payload yang sudah diekstrak.

Tool lain yang dikenal di dunia nyata: `tcpdump` (menangkap traffic live), NetworkMiner (ekstraksi file otomatis), Zeek (analisis jaringan berbasis event), dan tshark dengan script.

## Workflow dasar

```text
capinfos traffic.pcap
    ↓
tshark -r traffic.pcap (daftar kasar paket)
    ↓
Analisis percakapan (tshark -z conv,tcp)
    ↓
Filter protokol mencurigakan (dns, http, ftp)
    ↓
Follow stream / ekstrak payload
    ↓
Korelasi dengan log dan artefak host
    ↓
Timeline dan laporan
```

Mulai dari pandangan luas, lalu persempit ke detail. Jangan langsung membaca isi satu paket sebelum tahu gambaran besarnya.

## Kaitan dengan modul lain

Network Forensic berdiri di antara disk, memory, dan browser forensics. Satu insiden biasanya meninggalkan jejak di banyak tempat: PCAP menunjukkan komunikasi, disk menunjukkan file yang diunduh, memory menunjukkan proses yang berjalan, dan host artifacts menunjukkan cache DNS dan history. Investigator yang baik menggabungkan semuanya.

Sekarang kita mulai praktik pertama menggunakan file PCAP yang sudah disediakan: [Praktek 1](Praktek%20dan%20Latihan/Praktek%201.md)
