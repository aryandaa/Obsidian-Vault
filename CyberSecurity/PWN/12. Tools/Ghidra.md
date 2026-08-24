#tools

Ghidra adalah decompiler gratis dari NSA - mengubah binary menjadi **pseudo-code C** yang jauh lebih mudah dibaca daripada assembly. Sangat membantu menemukan bug & memahami alur program.

## Setup

```bash
# download dari https://ghidra-sre.org/
unzip ghidra*.zip
./ghidraRun
```

## Alur kerja

1. **File → New Project** → import binary (`chall`)
2. Double klik binary → analisis otomatis (Auto Analysis)
3. Buka **Symbol Tree** → cari fungsi (`main`, `vuln`, `win`)
4. Klik fungsi → lihat **Decompiler** panel (pseudo-code C)

## Yang dicari di decompiler

```c
void vuln(void) {
  char local_58 [64];
  gets(local_58);          // BUG: gets tanpa batas!
  return;
}
```

Perhatikan:
- Fungsi input berbahaya: `gets`, `strcpy`, `sprintf`, `scanf("%s")`, `read`
- Ukuran buffer (`local_58 [64]`)
- Operasi angka yang bisa overflow
- `free` lalu penggunaan ulang (UAF)
- Format string: `printf(user_input)` tanpa `%s`

## Ghidra vs objdump

| | Ghidra | objdump |
|---|---|---|
| Output | Pseudo-code C | Assembly |
| Kecepatan baca | Cepat | Lambat |
| Akurasi | Kadang "menebak" variabel | 100% sesuai instruksi |
| Untuk | Memahami logika | Verifikasi detail |

Gunakan Ghidra untuk **memahami**, objdump untuk **memastikan**.

## Fitur penting

- **Rename** - klik variabel/fungsi, rename jadi `buf`, `size`, `win`
- **Comment** - tambahkan catatan di kode
- **Search → Strings** - cari "/bin/sh", "flag"
- **Search → Memory/Instructions** - cari instruksi tertentu
- **Export** - export pseudo-code untuk dibaca di editor

## Alternatif

| Tool | Tipe |
|---|---|
| **Ghidra** | Decompiler GUI (gratis, terbaik) |
| **IDA Free** | Decompiler (lisensi terbatas) |
| **radare2/rizin + Cutter** | Reverse engineering framework |
| **retdec** | Decompiler online/CLI |
| **objdump** | Disassembler saja (lihat [[objdump dan readelf]]) |

## Tips

1. Binary **stripped** → Ghidra menamai fungsi `FUN_00401236` - cari string yang dipakai fungsi itu untuk menebak tujuannya.
2. Pseudo-code Ghidra kadang membingungkan di variabel - bandingkan dengan objdump.
3. Ghidra bisa **debug** juga (Ghidra Debugger) untuk versi terbaru.
4. Untuk challenge PWN: temukan fungsi `win`/`flag`, ukuran buffer, dan alamatnya - lalu lanjut ke pwntools.
