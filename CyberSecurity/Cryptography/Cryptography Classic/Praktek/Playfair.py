def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    seen = set()
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            matrix.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.add(ch)
            matrix.append(ch)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
    return None

def playfair_decrypt(cipher, key):
    matrix = create_matrix(key)
    cipher = cipher.upper().replace("J", "I").replace(" ", "")
    plain = []
    
    for i in range(0, len(cipher), 2):
        r1, c1 = find_pos(matrix, cipher[i])
        r2, c2 = find_pos(matrix, cipher[i+1])
        
        if r1 == r2: # sebaris, geser kiri
            plain.append(matrix[r1][(c1 - 1) % 5])
            plain.append(matrix[r2][(c2 - 1) % 5])
        elif c1 == c2: # sekolom, geser atas
            plain.append(matrix[(r1 - 1) % 5][c1])
            plain.append(matrix[(r2 - 1) % 5][c2])
        else: # bentuk persegi panjang
            plain.append(matrix[r1][c2])
            plain.append(matrix[r2][c1])
            
    return "".join(plain)

if __name__ == "__main__":
    key = "MONARCHY"
    cipher = "RMCMIM"
    print(f"Key       : {key}")
    print(f"Ciphertext: {cipher}")
    print(f"Plaintext : {playfair_decrypt(cipher, key)}")
