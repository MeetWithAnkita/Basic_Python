# Rail fence cipher encryption
def rail_fence_encrypt(string, step=3):
    rails = [''] * step
    rail_index = 0
    direction = 1  # 1 = down, -1 = up
    for char in string:
        rails[rail_index] += char
        rail_index += direction
        if rail_index == 0 or rail_index == step - 1:
            direction *= -1
    return ''.join(rails)

# Prompt the user to enter a string
string = input("Enter a string to encrypt: ")
encrypted = rail_fence_encrypt(string)
print("Rail Fence Encrypted:", encrypted)

# Rail fence cipher decryption
def rail_fence_decrypt(encrypted, step=3):
    length = len(encrypted)
    rails = [''] * step
    rail_length = [0] * step
    rail_index = 0
    direction = 1
    for _ in range(length):
        rail_length[rail_index] += 1
        rail_index += direction
        if rail_index == 0 or rail_index == step - 1:
            direction *= -1
    index = 0
    for i in range(step):
        rails[i] = encrypted[index:index + rail_length[i]]
        index += rail_length[i]
    rail_index = 0
    result = ''
    direction = 1
    for _ in range(length):
        result += rails[rail_index][0]
        rails[rail_index] = rails[rail_index][1:]
        rail_index += direction
        if rail_index == 0 or rail_index == step - 1:
            direction *= -1
    return result

# Decrypt the string
decrypted = rail_fence_decrypt(encrypted)
print("Rail Fence Decrypted:", decrypted)