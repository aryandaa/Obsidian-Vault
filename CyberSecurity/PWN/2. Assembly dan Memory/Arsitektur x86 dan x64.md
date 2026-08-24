#cybersecurity

PWN di CTF hampir selalu menyerang program **x86 (32-bit)** atau **x64 (64-bit)** di Linux. Arsitektur menentukan ukuran register, cara argumen dikirim, dan bentuk payload.

## x86 (32-bit)

- Register 32-bit: `EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP, EIP`
- `EIP` = instruction pointer (return address disimpan di sini)
- Ukuran pointer: 4 byte → `p32()`
- Argumen fungsi dikirim lewat **stack**

## x64 (64-bit)

- Register 64-bit: `RAX, RBX, RCX, RDX, RSI, RDI, RBP, RSP, RIP, R8-R15`
- `RIP` = instruction pointer
- Ukuran pointer: 8 byte → `p64()`
- Argumen fungsi dikirim lewat **register** (RDI, RSI, RDX, RCX, R8, R9)

## Cek arsitektur

```bash
file chall
# chall: ELF 64-bit LSB executable, x86-64
```

## Cara tahu dari pwntools

```python
from pwn import *
context.arch = "amd64"   # atau "i386"
# context.binary = ELF("./chall") otomatis set arch
```

## Perbedaan yang paling terasa di exploit

| | x86 | x64 |
|---|---|---|
| Ukuran alamat | 4 byte (`p32`) | 8 byte (`p64`) |
| Alamat shellcode | Cenderung mudah (stack addr kecil) | Sulit (address acak & ada null byte) |
| ROP | Butuh `pop;ret` per argumen | Butuh gadget `pop rdi; ret` dst |
| Null byte | Alamat sering mengandung null → masalah di `strcpy` | Lebih sering |

## Instruksi yang wajib dikenal

```asm
mov  rax, rbx      ; rax = rbx
push rax           ; simpan rax ke stack
pop  rax           ; ambil dari stack ke rax
call func          ; push return addr, lompat ke func
ret                ; pop return addr, lompat ke sana
lea  rax, [rbp-0x30] ; hitung alamat
add  rax, 8        ; rax += 8
sub  rsp, 0x10     ; alokasi stack
cmp  rax, 0        ; bandingkan (set flag)
jne  label         ; lompat kalau tidak sama
xor  rax, rax      ; rax = 0
syscall            ; panggil kernel (Linux)
```

`syscall` dengan `rax=59` = `execve` - ini dasar shellcode (lihat [[7. Shellcode]]).

## Endianness

Program x86/x64 pakai **little endian**: byte paling kecil disimpan duluan. Detail di [[Little Endian dan Format Data]].
