from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# --- Simple Padding (1 bit + 0 bits) ---
def pad(text):
    data = text.encode()
    data += b'\x80'  # 1 bit followed by zeros (10000000)
    while len(data) % 16 != 0:  # pad until multiple of 16 bytes
        data += b'\x00'
    return data

def unpad(data):
    return data.rstrip(b'\x00').rstrip(b'\x80').decode(errors='ignore')

# --- ECB Mode ---
def ecb_mode(key, text):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(text)
    ct = cipher.encrypt(padded)
    pt = unpad(cipher.decrypt(ct))
    print("\n--- ECB MODE ---")
    print("Ciphertext:", ct.hex())
    print("Decrypted :", pt)

# --- CBC Mode ---
def cbc_mode(key, text, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(text)
    ct = cipher.encrypt(padded)
    pt = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ct))
    print("\n--- CBC MODE ---")
    print("Ciphertext:", ct.hex())
    print("Decrypted :", pt)

# --- CFB Mode ---
def cfb_mode(key, text, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    padded = pad(text)
    ct = cipher.encrypt(padded)
    pt = unpad(AES.new(key, AES.MODE_CFB, iv, segment_size=128).decrypt(ct))
    print("\n--- CFB MODE ---")
    print("Ciphertext:", ct.hex())
    print("Decrypted :", pt)

# --- Main Program ---
key = get_random_bytes(16)
iv = get_random_bytes(16)
plaintext = "simats engineering"
print("Original Plaintext:", plaintext)

ecb_mode(key, plaintext)
cbc_mode(key, plaintext, iv)
cfb_mode(key, plaintext, iv)
