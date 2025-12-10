import string

plain_alph = string.ascii_uppercase
cipher_alph = "QWERTYUIOPASDFGHJKLZXCVBNM"   # custom mapping

def mono_encrypt(text):
    text = text.upper()
    return "".join(cipher_alph[plain_alph.index(c)] for c in text if c in plain_alph)

def mono_decrypt(text):
    text = text.upper()
    return "".join(plain_alph[cipher_alph.index(c)] for c in text if c in plain_alph)

print(mono_encrypt("HELLO"))
print(mono_decrypt(mono_encrypt("HELLO")))
