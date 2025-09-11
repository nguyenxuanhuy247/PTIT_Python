def encrypt(c):
    if 'a' <= c <= 'z':
        return chr(ord('z') - (ord(c) - ord('a')))
    elif 'A' <= c <= 'Z':
        return chr(ord('Z') - (ord(c) - ord('A')))
    else:
        return c
    
def encrypt_string(s):
    return ''.join(encrypt(c) for c in s)

t = int(input())
for test in range(int(t)):
    line = input()
    print(encrypt_string(line))

