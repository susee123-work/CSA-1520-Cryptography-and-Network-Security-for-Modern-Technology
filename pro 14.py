def poly_encrypt(text, key):
    res = ""
    key = key.upper()
    i = 0
    for c in text.upper():
        if c.isalpha():
            res += chr((ord(c)-65 + ord(key[i % len(key)])-65) % 26 + 65)
            i += 1
    return res

print(poly_encrypt("HELLO", "KEY"))
