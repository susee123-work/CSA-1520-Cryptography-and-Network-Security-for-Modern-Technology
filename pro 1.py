def caesar_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char
    return result

# Example
plaintext = input("Enter plaintext: ")
k = int(input("Enter shift value (1-25): "))

ciphertext = caesar_cipher(plaintext, k)
print("Encrypted (Caesar Cipher):", ciphertext)
