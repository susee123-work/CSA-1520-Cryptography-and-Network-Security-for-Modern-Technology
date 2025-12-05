import string

# Build 5x5 Playfair Matrix
def build_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key + string.ascii_uppercase:
        if ch not in used and ch != 'J' and ch.isalpha():
            used.add(ch)
            matrix.append(ch)
            if len(matrix) == 25:
                break
    return [matrix[i:i+5] for i in range(0, 25, 5)]

# Find letter position
def find_pos(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

# Encrypt digrams
def playfair_encrypt(pt, key):
    pt = pt.upper().replace("J", "I")
    pt = pt.replace(" ", "")

    # Form digrams
    pairs = []
    i = 0
    while i < len(pt):
        a = pt[i]
        b = pt[i+1] if i+1 < len(pt) else 'X'
        if a == b:
            b = 'X'
            i += 1
        else:
            i += 2
        pairs.append((a, b))

    matrix = build_matrix(key)
    cipher = ""

    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1+1) % 5]
            cipher += matrix[r2][(c2+1) % 5]
        elif c1 == c2:
            cipher += matrix[(r1+1) % 5][c1]
            cipher += matrix[(r2+1) % 5][c2]
        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher

key = input("Enter keyword: ")
pt = input("Enter plaintext: ")
print("Ciphertext:", playfair_encrypt(pt, key))
