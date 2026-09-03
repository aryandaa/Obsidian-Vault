def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = egcd(b % a, a)
    return g, y - (b // a) * x, x

def mod_inv(a, m=26):
    g, x, _ = egcd(a % m, m)
    if g != 1:
        return None
    return x % m

def hill_decrypt_2x2(cipher, K):
    det = (K[0][0] * K[1][1] - K[0][1] * K[1][0]) % 26
    det_inv = mod_inv(det, 26)
    if det_inv is None:
        raise ValueError("Matriks kunci tidak punya invers modulo 26!")

    K_inv = [
        [( K[1][1] * det_inv) % 26, (-K[0][1] * det_inv) % 26],
        [(-K[1][0] * det_inv) % 26, ( K[0][0] * det_inv) % 26]
    ]

    plain = []
    cipher_clean = [ord(c) - ord('A') for c in cipher.upper() if c.isalpha()]
    for i in range(0, len(cipher_clean), 2):
        c1, c2 = cipher_clean[i], cipher_clean[i+1]
        p1 = (K_inv[0][0] * c1 + K_inv[0][1] * c2) % 26
        p2 = (K_inv[1][0] * c1 + K_inv[1][1] * c2) % 26
        plain.append(chr(p1 + ord('A')))
        plain.append(chr(p2 + ord('A')))
    return "".join(plain)

if __name__ == "__main__":
    K = [[3, 3], [2, 5]]
    cipher = "HIAT"
    print(f"Kunci Matriks: {K}")
    print(f"Ciphertext   : {cipher}")
    print(f"Hasil Dekripsi: {hill_decrypt_2x2(cipher, K)}")
