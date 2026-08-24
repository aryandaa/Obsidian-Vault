#latihan 

Praktik terakhir sebelum capstone: **timeline dan korelasi**. Kamu mendapat empat PCAP yang masing-masing merekam satu fase serangan, plus satu log host. Tugasmu: urutkan kejadian, hubungkan antar evidence, dan temukan flag.

File yang dipakai (semua di `Files/`):

```text
fase1_recon.pcap     (port scan)
fase2_exploit.pcap   (exploit dan webshell)
fase3_c2.pcap        (beacon C2)
fase4_exfil.pcap     (exfiltration data)
host_log.txt         (log dari server korban)
```

Semua file sudah diberi nama sesuai fase, tetapi tugasmu tetap membuktikan urutan waktunya dengan evidence, bukan sekadar percaya nama file.

## Langkah 1: Cek waktu tiap PCAP

```bash
cd "Network Forensic/Files"
```

```bash
capinfos fase1_recon.pcap | grep -E "Start time|End time|Duration"
```

Lakukan untuk keempat file. Catat waktu mulai dan selesai masing-masing.

Jawab:

1. Urutkan keempat fase berdasarkan waktu mulai.
2. Berapa selisih waktu antara akhir fase 1 dan awal fase 2?

## Langkah 2: Analisis fase 1 (recon)

```bash
tshark -r fase1_recon.pcap
```

Jawab:

3. IP penyerang dan IP korban?
4. Port apa saja yang di-scan? Port mana yang terbuka (mendapat SYN, ACK) dan mana yang tertutup (mendapat RST)?
5. Teknik scan apa ini (SYN scan, connect scan, dll)?

## Langkah 3: Analisis fase 2 (exploit)

```bash
tshark -r fase2_exploit.pcap -Y "http.request" -T fields -e http.request.method -e http.request.uri
```

Jawab:

6. Payload SQL injection apa yang dikirim ke login?
7. File apa yang di-upload, dan ke endpoint mana?
8. Command apa yang dieksekusi lewat webshell, dan apa output pertamanya?

## Langkah 4: Analisis fase 3 (C2)

```bash
tshark -r fase3_c2.pcap -Y "http.request" -T fields -e frame.time_relative -e http.request.uri
```

Jawab:

9. IP dan port server C2?
10. Interval beacon-nya berapa detik?

## Langkah 5: Analisis fase 4 (exfil)

```bash
tshark -r fase4_exfil.pcap -Y "dns.qry.name contains exfil && dns.flags.response == 0" -T fields -e dns.qry.name | sed 's/\..*//' | tr -d '\n' | xxd -r -p
```

Jawab:

11. Tulis flag yang dikirim lewat DNS exfiltration.
12. Selain DNS, protokol apa lagi yang dipakai untuk mengambil data, dan file apa yang diminta?

## Langkah 6: Korelasi dengan log host

Buka `host_log.txt`. Cocokkan isinya dengan timeline PCAP:

- Log jam berapa menunjukkan brute force SSH? Cocok dengan fase mana?
- Log jam berapa menunjukkan login admin dan upload file? Cocok dengan fase mana?
- Log jam berapa menunjukkan beacon? Cocok dengan fase mana?
- Log jam berapa menunjukkan sesi SFTP? Cocok dengan fase mana?

Jawab:

13. Susun kronologi lengkap serangan dari awal sampai akhir, dengan waktu dan evidence pendukung untuk setiap langkah.

## Jawab semua

1-13. Tulis jawaban lengkap.

## Pembahasan singkat

Empat PCAP + satu log ternyata bercerita satu serangan utuh: reconnaissance, exploit, command & control, lalu exfiltration. Kunci timeline adalah menyamakan waktu dan mengurutkan. Kunci korelasi adalah menemukan IP yang sama (penyerang), metode yang sama (webshell), dan waktu yang saling berurutan. Sekarang kamu siap untuk capstone: satu kasus besar dengan satu PCAP utuh dan satu syslog, tanpa nama fase yang membantu.
