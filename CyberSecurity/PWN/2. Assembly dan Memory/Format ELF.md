#cybersecurity

ELF (Executable and Linkable Format) adalah format binary Linux. Memahami struktur dasarnya membantu membaca binary dan memahami mengapa teknik tertentu (GOT overwrite, ret2plt) bekerja.

## Bagian utama ELF

```
+----------------------+
| ELF Header           |  arsitektur, entry point, dll
+----------------------+
| Program Headers      |  segmen (LOAD, GNU_STACK, dll)
+----------------------+
| Section Headers      |  section (.text, .data, .bss, .plt, .got)
+----------------------+
```

## Section yang penting

| Section | Isi | Relevansi PWN |
|---|---|---|
| `.text` | Kode program (instruksi) | Alamat fungsi, gadget ROP |
| `.data` | Variabel global yang diinisialisasi | Kadang target overwrite |
| `.bss` | Variabel global tanpa inisialisasi | Tempat menaruh data (misal "/bin/sh") |
| `.plt` | Stub untuk lazy binding | Memanggil fungsi libc tanpa tahu alamat |
| `.got` | Alamat fungsi libc | Target GOT overwrite |
| `.rodata` | String konstan | Mencari "/bin/sh", format string |
| `.interp` | Path dynamic loader | Info libc |

## Cara membaca

```bash
# Header ELF
readelf -h chall

# Section
readelf -S chall

# Symbol (fungsi)
readelf -s chall | grep FUNC

# Dynamic (import)
readelf -d chall | grep -i needed
#  0x0000000000000001 (NEEDED) Shared library: [libc.so.6]

# Disassembly
objdump -d chall | less

# String
strings chall | grep -i flag
```

## Dengan pwntools

```python
from pwn import *

elf = ELF("./chall")

elf.sym["win"]          # alamat fungsi win
elf.plt["puts"]         # alamat puts@plt
elf.got["puts"]         # alamat puts@got (isi: alamat puts di libc)
elf.search(b"/bin/sh")  # generator alamat string
elf.address             # base address (set kalau PIE + leak)
```

## Dynamic vs Static

- **Dynamic** - pakai libc (`ldd chall`), exploit bisa ret2libc
- **Static** - semua kode di dalam binary, tidak butuh libc; ROP biasanya harus dari binary sendiri

```bash
file chall
# ... dynamically linked ...  -> bisa ret2libc
# ... statically linked ...   -> ROP dalam binary
```

## Stripped vs unstripped

- **Unstripped** - nama fungsi ada (`win`, `vuln`, `main`) → mudah
- **Stripped** - nama hilang → cari lewat `objdump`, string, atau signature

```bash
# cek
file chall  # "not stripped" / "stripped"
```

## Mengapa ini penting?

- Kalau tahu ada fungsi `win` (dari `elf.sym`), ret2win tinggal lompat ke sana.
- Kalau tahu binary dynamic, kita bisa ret2libc.
- GOT overwrite butuh tahu alamat `puts@got` (dari `elf.got`).
- PIE butuh base address yang di-leak, lalu `elf.address = base`.

Materi lanjutan: [[8. GOT dan PLT]], [[5. ROP (Return Oriented Programming)]].
