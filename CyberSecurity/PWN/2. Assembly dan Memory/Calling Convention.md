#cybersecurity

Calling convention adalah **aturan bagaimana fungsi dipanggil**: di mana argumen ditaruh, siapa yang membersihkan stack, dan di mana return value disimpan. Ini penting untuk ROP (memanggil fungsi dengan argumen yang kita kontrol).

## x86 (32-bit) - cdecl

- Semua argumen di-**push ke stack** dari kanan ke kiri
- Caller yang membersihkan stack
- Return value di `EAX`

```c
// printf("%s", buf);
push buf
push format_string
call printf
add esp, 8        ; caller cleanup
```

Payload ROP 32-bit untuk memanggil `system("/bin/sh")`:

```
[address system] [return addr] [arg1]
```

## x64 (64-bit) - System V AMD64

- Argumen 1-6 lewat register: `RDI, RSI, RDX, RCX, R8, R9`
- Argumen ke-7+ lewat stack
- Return value di `RAX`
- **Wajib** 16-byte stack alignment sebelum `call` (lihat catatan)

```c
// puts(buf);
mov rdi, buf
call puts
```

Payload ROP 64-bit untuk `system("/bin/sh")`:

```
[pop rdi; ret] [addr "/bin/sh"] [addr system]
```

Karena butuh mengisi RDI, kita perlu gadget `pop rdi; ret` - ini dasar dari [[5. ROP (Return Oriented Programming)]].

## Syscall convention (Linux x64)

Syscall dipanggil langsung dengan `syscall`:

| RAX | Fungsi |
|---|---|
| 59 | `execve` |
| 60 | `exit` |
| 0 | `read` |
| 1 | `write` |

Argumen syscall di `RDI, RSI, RDX, R10, R8, R9`. Ini dipakai shellcode ([[7. Shellcode]]) dan SROP ([[11. Advanced PWN]]).

## Stack alignment (x64)

Sebelum `call`, stack harus **16-byte aligned**. Kalau tidak, fungsi yang memakai `movaps` (SSE) akan crash.

Gejala: exploit jalan di gdb tapi crash di luar gdb - biasanya masalah alignment.

Solusi di ret2libc:

```python
# tambahkan satu ret gadget tambahan
payload = b"A"*offset + p64(ret) + p64(pop_rdi) + p64(binsh) + p64(system)
```

## Cek convention di binary

```bash
# 32-bit: call dengan push argumen
objdump -d chall | grep -A5 "<main>:"

# 64-bit: mov ke rdi/rsi/rdx
```

## Ringkasan

| | x86 | x64 |
|---|---|---|
| Argumen | Stack (push) | Register (RDI, RSI, ...) |
| ROP perlu | Alamat fungsi + arg di stack | Gadget `pop rdi; ret` dst |
| Alignment | Tidak terlalu dipedulikan | 16-byte, sering butuh ret tambahan |
| Return value | EAX | RAX |
