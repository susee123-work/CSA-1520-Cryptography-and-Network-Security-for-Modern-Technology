import string
keyword = "CIPHER"
alphabet = string.ascii_uppercase
cipher_alpha = ""
for ch in keyword:
    if ch not in cipher_alpha:
        cipher_alpha += ch
for ch in alphabet:
    if ch not in cipher_alpha:
        cipher_alpha += ch
plain = alphabet
cipher = cipher_alpha
print("Plain :", plain)
print("Cipher:", cipher)
def encrypt(msg):
    result = ""
    for ch in msg.upper():
        if ch in plain:
            idx = plain.index(ch)
            result += cipher[idx]
        else:
            result += ch
    return result
print("Encrypt 'HELLO' →", encrypt("HELLO"))
