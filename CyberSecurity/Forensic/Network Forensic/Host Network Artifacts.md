#cybersecurity 

PCAP tidak selalu tersedia. Banyak investigasi berjalan tanpa packet capture sama sekali. Di sinilah **host network artifacts** menjadi penyelamat: sistem operasi menyimpan jejak komunikasi di berbagai tempat, dan jejak itu bisa dibaca jauh setelah kejadian.

Inti materi ini: sebuah mesin yang berkomunikasi dengan jaringan hampir selalu meninggalkan bekas. DNS yang pernah di-resolve, IP yang pernah terhubung, proses yang membuat koneksi, dan halaman yang pernah dibuka. Investigator yang paham di mana bekas itu berada bisa merekonstruksi komunikasi meski tanpa satu byte PCAP pun.

## Kenapa host artifacts penting

1. PCAP sering tidak direkam, tetapi host menyimpan cache secara otomatis.
2. Host artifacts menunjukkan **siapa (proses/user)** yang berkomunikasi, sedangkan PCAP hanya menunjukkan IP dan port.
3. Mereka menjembatani network forensics dan disk forensics: kamu menemukan koneksi di netstat, lalu menemukan prosesnya di tasklist, lalu menemukan binary-nya di disk.

```
PCAP menjawab "paket apa yang lewat". Host artifacts menjawab
"aplikasi apa yang membuat komunikasi itu". Gabungan keduanya
jauh lebih kuat daripada salah satu saja.
```

## Artifacts di Windows

### 1. DNS cache

Windows menyimpan hasil resolve DNS sementara:

```bash
ipconfig /displaydns
```

Output berisi nama domain, tipe record, dan alamat IP. Ini bisa menunjukkan domain yang pernah diakses, termasuk domain C2.

Untuk menghapus (jangan dilakukan pada evidence):

```bash
ipconfig /flushdns
```

### 2. File hosts

```text
C:\Windows\System32\drivers\etc\hosts
```

Mapping statis domain → IP. Penyerang kadang mengeditnya untuk redirect lalu lintas.

### 3. Tabel ARP

```bash
arp -a
```

Menampilkan mapping IP → MAC di jaringan lokal. Berguna untuk menemukan perangkat yang pernah berkomunikasi di segmen yang sama.

### 4. Netstat / tabel koneksi

```bash
netstat -ano
```

Menampilkan koneksi aktif dengan **PID**. Kolom PID adalah jembatan emas: dari PID kamu bisa cari prosesnya di tasklist.

```bash
tasklist /v
```

Atau versi PowerShell yang lebih detail:

```powershell
Get-NetTCPConnection | Where-Object {$_.State -eq "Established"}
```

Kombinasi yang klasik:

```text
netstat -ano  → temukan PID dengan koneksi mencurigakan
tasklist /v   → cari nama proses untuk PID tersebut
```

### 5. Browser history

Chrome, Firefox, dan Edge menyimpan history, download, dan cache dalam database SQLite. Halaman yang pernah dikunjungi, file yang diunduh, dan kapan itu terjadi. Ini artefak yang sangat kaya untuk merekonstruksi aktivitas pengguna.

### 6. Firewall dan event log

Windows Defender Firewall mencatat koneksi yang diizinkan/diblokir. Windows Event Log punya event ID yang relevan:

```text
5156  koneksi diizinkan (filtering platform)
5157  koneksi diblokir
3     Sysmon network connection (jika Sysmon terpasang)
```

Sysmon Event 3 bahkan mencatat process, IP tujuan, port, dan hash file yang membuat koneksi. Ini salah satu artefak network paling berharga di Windows.

### 7. Prefetch

Prefetch mencatat program yang pernah dijalankan beserta waktunya. Kalau sebuah program jahat pernah berjalan, jejaknya ada di Prefetch, dan itu bisa dikorelasikan dengan koneksi keluar yang tercatat di netstat atau firewall.

## Artifacts di Linux

### 1. File hosts

```text
/etc/hosts
```

### 2. Tabel koneksi

```bash
ss -tunap
```

atau:

```bash
cat /proc/net/tcp
```

### 3. Cache DNS

systemd-resolved:

```bash
resolvectl statistics
```

```bash
resolvectl query example.com
```

atau lihat file:

```text
/run/systemd/resolve/stub-resolv.conf
```

### 4. Log autentikasi dan service

```text
/var/log/auth.log     login, SSH, sudo
/var/log/syslog       aktivitas sistem dan service
/var/log/apache2/     access log web server
```

Access log Apache berisi IP, waktu, method, path, dan status code setiap request. Ini adalah "PCAP teks" dari sisi server.

## DHCP leases

DHCP mencatat alamat IP yang pernah diberikan ke perangkat:

- Linux: `/var/lib/dhcp/dhcpd.leases`
- Windows: registry `Dhcpip` atau log event

Lease menunjukkan perangkat mana yang pernah ada di jaringan dan IP apa yang dipakainya pada waktu tertentu. Berguna untuk menghubungkan aktivitas dengan perangkat fisik.

## Membaca artifacts dengan korelasi

Contoh alur korelasi:

```text
netstat -ano
    ↓
Ada koneksi ESTABLISHED ke 203.0.113.66:8080 dengan PID 4412
    ↓
tasklist → PID 4412 = updater_service.exe
    ↓
ipconfig /displaydns → cache berisi update-svc.kopi-senja-bot.net
    ↓
browser history → file updater_service.exe diunduh dari domain yang sama
    ↓
Kesimpulan: program updater_service.exe mengunduh dirinya lalu
berkomunikasi dengan server C2 secara berkala
```

Perhatikan bagaimana setiap artifact memberi satu potongan puzzle: koneksi, proses, domain, dan sumber unduhan.

## Catatan penting tentang volatile artifacts

Beberapa artifacts bersifat volatile dan bisa hilang:

- Tabel ARP: bertahan menit hingga jam.
- Netstat: hanya koneksi saat itu.
- DNS cache: bertahan beberapa menit hingga jam, tergantung TTL.
- Browser history: bertahan lama di disk.
- Log server: bertahan sesuai kebijakan rotasi.

Ketika mengumpulkan evidence dari mesin yang masih hidup, kumpulkan yang paling volatile dulu: koneksi aktif, proses, lalu cache, baru kemudian yang ada di disk.

Sekarang kita praktikkan korelasi artifacts host menggunakan file-file yang sudah disediakan: [Praktek 7](Praktek%20dan%20Latihan/Praktek%207.md)
