# Encrypt the string
def encrypt(string):
    odd = string[::2]
    even = string[1::2]
    return odd + even

# Prompt the user to enter a string
string = input("Enter a string: ")
encrypted = encrypt(string)
print("Encrypted string:", encrypted)

# Decrypt the string
def decrypt(encrypted):
    half = len(encrypted) // 2
    odd = encrypted[:half]
    even = encrypted[half:]
    result = ''.join(o + e for o, e in zip(odd, even))
    if len(odd) > len(even):
        result += odd[-1]
    return result

# Decrypt the string
decrypted = decrypt(encrypted)
print("Decrypted string:", decrypted)