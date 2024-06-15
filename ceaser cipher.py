# A python program to illustrate Caesar Cipher Technique
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char == " ":
            result += " "
        elif char.isdigit():
            result += chr((ord(char) + s - 48) % 26 + 48)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char == " ":
            result += " "
        elif char.isdigit():
            result += chr((ord(char) - s - 48) % 26 + 48)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char
    return result

s = 5
print("Enter 1 for encryption\nEnter 2 for decryption")
x = input()
print("Enter string")
text = input()

if x == "1":
    encrypted = encrypt(text, s)
    print("Text: " + text)
    print("Encoded: " + encrypted)

elif x == "2":
    decrypted = decrypt(text, s)
    print("Text: " + text)
    print("Decoded: " + decrypted)

else:
    print("Enter correct values")
