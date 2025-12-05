import math
for a in range(1, 26):
    if math.gcd(a, 26) != 1:
        continue
    for b in range(26):
        if (a*4 + b) % 26 == 1 and (a*19 + b) % 26 == 20:
            print("a =", a, "b =", b)
            key_a, key_b = a, b
def affine_decrypt(cipher, a, b):
    result = ""
    inv = pow(a, -1, 26)
    for ch in cipher:
        if ch.isalpha():
            c = ord(ch.upper()) - 65
            p = (inv * (c - b)) % 26
            result += chr(p + 65)
        else:
            result += ch
    return result
ciphertext = "BU..."  
print("Decrypted:", affine_decrypt(ciphertext, key_a, key_b))
