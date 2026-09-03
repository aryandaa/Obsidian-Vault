def rail_fence_decrypt(cipher, rows):
    n = len(cipher)
    fence = [[''] * n for _ in range(rows)]
    r, step = 0, 1
    for c in range(n):
        fence[r][c] = '*'
        if r == 0:
            step = 1
        elif r == rows - 1:
            step = -1
        r += step
    idx = 0
    for i in range(rows):
        for j in range(n):
            if fence[i][j] == '*':
                fence[i][j] = cipher[idx]
                idx += 1
    result = []
    r, step = 0, 1
    for c in range(n):
        result.append(fence[r][c])
        if r == 0:
            step = 1
        elif r == rows - 1:
            step = -1
        r += step
    return ''.join(result)

cipher = "CLSAOEMTRU"
for rows in range(2, 11):
    print(f"rows={rows}: {rail_fence_decrypt(cipher, rows)}")