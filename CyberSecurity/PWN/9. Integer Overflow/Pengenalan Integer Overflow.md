#cybersecurity

Integer overflow terjadi saat hasil operasi aritmatika melebihi batas maksimum tipe data, dan nilai **membungkus** menjadi kecil (atau negatif).

## Batas tipe data

| Tipe | Ukuran | Min | Max |
|---|---|---|---|
| `unsigned char` | 1 byte | 0 | 255 |
| `signed char` | 1 byte | -128 | 127 |
| `unsigned short` | 2 byte | 0 | 65535 |
| `short` | 2 byte | -32768 | 32767 |
| `unsigned int` | 4 byte | 0 | 4294967295 |
| `int` | 4 byte | -2147483648 | 2147483647 |
| `size_t` | 8 byte (64-bit) | 0 | 2^64-1 |

## Contoh wrap around

```c
unsigned char x = 255;
x = x + 1;    // x = 0 (wrap around!)
```

```c
int x = 2147483647;
x = x + 1;    // x = -2147483648 (negatif!)
```

## Kode rentan - bypass cek

```c
void vuln() {
    int size;
    char buf[64];
    printf("Ukuran: ");
    scanf("%d", &size);

    if (size < 64) {          // cek ukuran...
        gets(buf);            // ...tapi gets() tidak pakai size!
    }
}
```

Atau:

```c
void copy(char *src) {
    unsigned short len = strlen(src);   // > 65535? wrap!
    char dst[100];
    strncpy(dst, src, len);             // len bisa jadi kecil
}
```

## Kode rentan - alokasi kecil, copy besar

```c
void vuln(int n) {
    char *buf = malloc(n);      // n negatif? malloc sangat besar/0
    read(0, buf, n);            // atau n besar -> overflow
}
```

Kalau `n` dihitung dari operasi yang overflow:

```c
int total = a + b;       // overflow -> total kecil/negatif
char *buf = malloc(total);
read(0, buf, total);     // baca total byte -> padahal data asli lebih besar
```

## Contoh exploit sederhana

```c
// cek: if (size > 100) return;  -> kirim -1
// scanf("%d") menerima -1; jika dipakai sebagai unsigned, jadi 4294967295
```

```python
# kirim angka negatif untuk mem-bypass cek "size < 64"
io.sendline(b"-1")       # lolos if (size < 64) tapi sebenarnya huge
```

## Bypass cek dengan signed/unsigned

```c
unsigned int size;
scanf("%u", &size);    // terima angka besar
if (size > 100) reject; 

// tapi kalau kode pakai signed:
int s = (int)size;      // 4294967295 -> -1
// cek yang memakai signed lolos!
```

Inti: **jangan percaya angka dari user** - konversi signed/unsigned dan overflow sering membuka celah.

## Deteksi

1. Cari program yang meminta angka: ukuran, jumlah, indeks, loop count.
2. Coba nilai ekstrem: `-1`, `2147483647`, `4294967295`, `65535`, `255`.
3. Lihat apakah cek bisa dilewati atau alokasi/copy jadi aneh.

## Contoh kasus CTF

```
1. Program minta "size" untuk malloc
2. size = 0x100 + 0xffffffff  -> wrap ke 0xff  (kecil)
3. lalu read(0, buf, 0x100)  -> padahal cek bilang buf kecil
4. overflow ke memory berikutnya (heap/stack) -> kontrol
```

## Catatan

- Integer overflow bukan selalu langsung RCE - sering jadi **prasyarat** (alokasi kecil + copy besar = heap overflow; ukuran negatif = stack overflow).
- Cek tipe data di source code: signed vs unsigned menentukan perilaku.
- Di CTF, cari operasi aritmatika pada input user: `size + 1`, `n * 2`, `len - 1` - itu titik rawan.
