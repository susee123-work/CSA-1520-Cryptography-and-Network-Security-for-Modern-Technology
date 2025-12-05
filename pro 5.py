def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m=26):
    for i in range(26):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b):
    cipher = ""
    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - 65
            c = (a * p + b) % 26
            cipher += chr(c + 65)
        else:
            cipher += ch
    return cipher

def affine_decrypt(cipher, a, b):
    a_inv = mod_inverse(a)
    if a_inv is None:
        return "Invalid 'a'! No modular inverse exists."

    plain = ""
    for ch in cipher:
        if ch.isalpha():
            c = ord(ch) - 65
            p = (a_inv * (c - b + 26)) % 26
            plain += chr(p + 65)
        else:
            plain += ch
    return plain

# ---------------------------
# Main program
# ---------------------------

text = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Check if valid 'a'
if gcd(a, 26) != 1:
    print("Error: Invalid value of 'a'! gcd(a, 26) must be 1.")
else:
    cipher = affine_encrypt(text, a, b)
    print("Ciphertext:", cipher)
    print("Decrypted text:", affine_decrypt(cipher, a, b))
