def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    cipher = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            p = ord(ch) - 65
            k = ord(key[j % len(key)]) - 65
            cipher += chr((p + k) % 26 + 65)
            j += 1
        else:
            cipher += ch
    return cipher

pt = input("Enter plaintext: ")
key = input("Enter key: ")

print("Ciphertext:", vigenere_encrypt(pt, key))
