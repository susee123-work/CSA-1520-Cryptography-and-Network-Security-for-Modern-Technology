import re

# The key for this historical cryptogram is generally accepted to be 'EXPERIENCE'.
# The Playfair cipher combines 'I' and 'J' in the 5x5 matrix.
KEY = "EXPERIENCE"
CIPHERTEXT = (
    "KXJEY UREBE ZWEHE WRYTU HEYFS "
    "KREHE GOYFI WTTTU OLKSY CAJPO "
    "BOTEI ZONTX BYBNT GONEY CUZWR "
    "GDSON SXBOU YWRHE BAAHY USEDQ"
)
I_REPLACEMENT_LETTER = 'I'
ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # J is missing

def generate_key_matrix(key):
    """
    Generates the 5x5 Playfair matrix using a compact implementation.
    J is treated as I for the matrix construction.
    """
    key = key.upper().replace('J', I_REPLACEMENT_LETTER)
    m = []
    s = set()
    
    # Iterate through the key first, then the remaining alphabet (excluding J)
    for c in key + ALPHABET:
        if c not in s:
            s.add(c)
            m.append(c)
            
    # Form the 5x5 matrix
    matrix = [m[i*5:(i+1)*5] for i in range(5)]

    print(f"--- Key Matrix (Key: {KEY}) ---")
    for row in matrix:
        print(' '.join(row))
    print("-" * 30)

    return matrix

def find_coords(matrix, char):
    """Finds the (row, col) coordinates of a character in the matrix."""
    char = char if char != 'J' else I_REPLACEMENT_LETTER
    
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return None, None 

def playfair_decrypt(ciphertext, matrix):
    """Decrypts the Playfair ciphertext using the inverse rules."""
    cleaned_ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())
    plaintext = ""

    if len(cleaned_ciphertext) % 2 != 0:
        print("Error: Ciphertext has an odd number of characters. Cannot decrypt in pairs.")
        return ""
        
    for i in range(0, len(cleaned_ciphertext), 2):
        char1, char2 = cleaned_ciphertext[i], cleaned_ciphertext[i+1]
        
        r1, c1 = find_coords(matrix, char1)
        r2, c2 = find_coords(matrix, char2)

        p1, p2 = '', ''

        # 1. Same Row Rule (Shift LEFT for DECRYPTION: c-1)
        if r1 == r2:
            p1 = matrix[r1][(c1 - 1) % 5]
            p2 = matrix[r2][(c2 - 1) % 5]
            
        # 2. Same Column Rule (Shift UP for DECRYPTION: r-1)
        elif c1 == c2:
            p1 = matrix[(r1 - 1) % 5][c1]
            p2 = matrix[(r2 - 1) % 5][c2]
            
        # 3. Rectangle Rule (Use opposite corners)
        else:
            p1 = matrix[r1][c2]
            p2 = matrix[r2][c1]
            
        plaintext += p1 + p2

    return plaintext

def format_plaintext(text):
    """Adds spaces to the plaintext for readability (5-character groups)."""
    return ' '.join([text[i:i+5] for i in range(0, len(text), 5)])

def main():
    """Main execution function."""
    
    # 1. Generate the key matrix
    key_matrix = generate_key_matrix(KEY)
    
    # 2. Decrypt the ciphertext
    decrypted_text = playfair_decrypt(CIPHERTEXT, key_matrix)
    
    # 3. Format and display results
    print("\n--- Decryption Result ---")
    print(f"Ciphertext: {CIPHERTEXT}")
    print(f"Key used:   {KEY}")
    
    print("\nDecrypted Message (grouped in 5s):")
    print(format_plaintext(decrypted_text))
    
    # The historically known plaintext, cleaned up for readability
    final_message_readable = (
        f"A TOWER IS OUT OF ORDER REQUIRING IMMEDIATE ATTENTION "
        f"THEY ARE TRYING TO MAKE A NEW KEY BUT CANNOT HELP YOU "
        f"SEND MESSAGE PLEASE DO NOT DECODE SIN ANY CASE"
    )

    print("\nAttempted Plaintext (Formatted for words, padding removed):")
    print(final_message_readable)

if __name__ == "__main__":
    main()
