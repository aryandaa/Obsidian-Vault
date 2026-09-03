GRID = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'], # J disatukan dengan I
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

def polybius_decode(numbers):
    digits = [c for c in numbers if c.isdigit()]
    plain = []
    for i in range(0, len(digits), 2):
        row = int(digits[i]) - 1
        col = int(digits[i+1]) - 1
        if 0 <= row < 5 and 0 <= col < 5:
            plain.append(GRID[row][col])
    return "".join(plain)

def polybius_encode(text):
    text = text.upper().replace("J", "I")
    coords = []
    for ch in text:
        for r in range(5):
            for c in range(5):
                if GRID[r][c] == ch:
                    coords.append(f"{r+1}{c+1}")
    return " ".join(coords)

if __name__ == "__main__":
    msg = "HELLO"
    encoded = polybius_encode(msg)
    decoded = polybius_decode(encoded)
    print(f"Pesan Asli: {msg}")
    print(f"Encoded   : {encoded}")
    print(f"Decoded   : {decoded}")
