#tools

ROPgadget dan ropper mencari **gadget** - potongan instruksi berakhiran `ret` yang dipakai merangkai ROP chain (lihat [[5. ROP (Return Oriented Programming)]]).

## ROPgadget

```bash
pip install ROPGadget   # atau sudah include di Kali

# Semua gadget
ROPgadget --binary chall

# Cari gadget tertentu
ROPgadget --binary chall | grep "pop rdi"
ROPgadget --binary chall | grep "pop rdi ; pop rsi ; ret"
ROPgadget --binary chall | grep "syscall"
ROPgadget --binary chall | grep "leave"

# Di libc (kalau perlu)
ROPgadget --binary /lib/x86_64-linux-gnu/libc.so.6 | grep "pop rdi"
```

## ropper

```bash
pip install ropper

ropper --file chall --search "pop rdi"
ropper --file chall --search "pop rsi"
ropper --file chall --search "syscall"
ropper --file chall --search "leave"
```

## Cari gadget dari pwntools

```python
from pwn import *

elf = ELF("./chall")
rop = ROP(elf)

# cari gadget spesifik
g = rop.find_gadget(["pop rdi", "ret"])
print(hex(g.address))

# tampilkan semua gadget
print(rop.dump())

# susun chain otomatis
rop.system(next(elf.search(b"/bin/sh")))
print(rop.dump())
print(rop.chain().hex())
```

## Gadget yang paling sering dicari

```text
pop rdi ; ret      ; argumen ke-1 (64-bit)
pop rsi ; ret      ; argumen ke-2
pop rdx ; ret      ; argumen ke-3
pop rax ; ret      ; set syscall number
syscall ; ret      ; jalankan syscall (SROP, ORW)
leave ; ret        ; stack pivot
ret                ; alignment 16-byte
```

## Tips

1. `ROPgadget --binary chall --only "pop|ret"` - filter instruksi.
2. Gadget di libc juga valid (kalau libc di-leak) - kadang lebih banyak pilihan.
3. Kalau gadget tidak ada di binary, cek `__libc_csu_init` (ret2csu) - pwntools otomatis menanganinya.
4. `ROP(elf)` pwntools otomatis menemukan gadget untuk chain yang kamu susun - coba itu dulu sebelum manual.
5. Verifikasi gadget dengan `objdump`/gdb kalau ragu (misal ada instruksi di tengah yang mengubah register).
