def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = egcd(b % a, a)
    return g, y - (b // a) * x, x

def mod_inv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        return None
    return x % m

def affine_decrypt(cipher, a, b):
    inv = mod_inv(a, 26)
    if inv is None:
        return None
    result = ""
    for ch in cipher:
        if 'a' <= ch <= 'z':
            y = ord(ch) - ord('a')
            result += chr(((y - b) * inv) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            y = ord(ch) - ord('A')
            result += chr(((y - b) * inv) % 26 + ord('A'))
        else:
            result += ch
    return result

cipher = "MXYW DGGY"
for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
    for b in range(26):
        hasil = affine_decrypt(cipher, a, b)
        if "flag" in hasil.lower() or "the" in hasil.lower():
            print(f"a={a} b={b}: {hasil}")