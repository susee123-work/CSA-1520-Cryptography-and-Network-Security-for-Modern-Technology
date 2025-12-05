matrix = [
 ['M','F','H','I','K'],
 ['U','N','O','P','Q'],
 ['Z','V','W','X','Y'],
 ['E','L','A','R','G'],
 ['D','S','T','B','C']
]

def find(ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def prepare(text):
    text = text.upper().replace(" ", "").replace(".", "")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2
    return result

def encrypt_pair(a, b):
    r1, c1 = find(a)
    r2, c2 = find(b)

    if r1 == r2:
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2:
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

msg = "Must see you over Cadogan West Coming at once"
text = prepare(msg)
cipher = ""

for i in range(0, len(text), 2):
    cipher += encrypt_pair(text[i], text[i+1])

print(cipher)
