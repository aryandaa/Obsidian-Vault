#latihan 

Praktik ini berbeda dari sebelumnya: **tidak ada PCAP**. Kamu hanya punya artifacts dari dalam host. Tugasmu merekonstruksi komunikasi jaringan mesin korban berdasarkan jejak yang tersimpan. Ini persis situasi investigasi nyata ketika packet capture tidak tersedia.

File yang dipakai (semua di `Files/`):

```text
praktek7_dns_cache.txt        cache DNS (ipconfig /displaydns)
praktek7_arp_cache.txt        tabel ARP (arp -a)
praktek7_netstat.txt          koneksi aktif (netstat -ano)
praktek7_process_list.txt     daftar proses (tasklist)
praktek7_browser_history.json history dan download Chrome
praktek7_hosts_file.txt       isi file hosts
```

Evidence diambil dari mesin korban pada tanggal 2026-08-14 09:15:00 UTC.

## Langkah 1: Baca cache DNS

Buka `praktek7_dns_cache.txt`. Catat semua domain yang ada di cache.

Jawab:

1. Domain apa saja yang tersimpan di cache DNS?
2. Domain mana yang paling mencurigakan, dan IP apa yang di-resolve?

## Langkah 2: Baca koneksi aktif

Buka `praktek7_netstat.txt`. Perhatikan kolom `Foreign Address` dan `PID`.

Jawab:

3. Koneksi ke IP mana saja yang statusnya ESTABLISHED?
4. PID berapa yang melakukan koneksi ke `203.0.113.66:8080`?
5. Koneksi ke `8.8.8.8:53` dengan PID yang sama menandakan apa?

## Langkah 3: Hubungkan PID ke proses

Buka `praktek7_process_list.txt`. Cari PID yang kamu temukan di netstat.

Jawab:

6. Nama proses apa yang punya PID tersebut?
7. Apakah nama proses itu wajar? (Petunjuk: lihat nama-nama proses lain di daftar.)

## Langkah 4: Baca history browser

Buka `praktek7_browser_history.json`.

Jawab:

8. Kapan `updater_service.exe` diunduh, dan dari URL apa?
9. Halaman apa saja yang dikunjungi pada pagi itu? Susun urutannya berdasarkan `visit_time`.
10. Hubungan apa antara history browser dan proses `updater_service.exe`?

## Langkah 5: Korelasikan semua

Sekarang gabungkan semua temuan. Perhatikan bahwa:

- DNS cache berisi `update-svc.kopi-senja-bot.net` → `203.0.113.66`.
- Browser history menunjukkan download `updater_service.exe` dari `update-svc.kopi-senja-bot.net/update`.
- Netstat menunjukkan PID 4412 (updater_service.exe) terhubung ke `203.0.113.66:8080`.
- File hosts juga memetakan `update-svc.kopi-senja-bot.net` ke `203.0.113.66`.

Jawab:

11. Susun cerita lengkap: dari mana program jahat datang, kapan diinstal, dan ke mana ia berkomunikasi.
12. Cari flag di `praktek7_dns_cache.txt`. Perhatikan record TXT.

## Jawab semua

1-12. Tulis jawaban lengkap dengan evidence pendukung untuk setiap kesimpulan.

## Pembahasan singkat

Tanpa PCAP pun, jejak komunikasi bisa direkonstruksi: cache DNS menunjukkan domain yang diakses, netstat menunjukkan koneksi yang aktif beserta PID, process list memberi nama proses, dan browser history menunjukkan sumber unduhan. Kunci dari praktik ini adalah korelasi: satu artifacts hanya memberi satu potongan, tetapi bersama-sama mereka membentuk cerita. Di praktik terakhir, kamu menggabungkan PCAP dan log untuk membangun timeline.
