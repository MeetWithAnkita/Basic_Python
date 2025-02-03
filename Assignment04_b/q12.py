# Prompt the user to enter a word
word = input("Enter a word: ")

# Capitalize every alternate letter
result = ''.join(char.upper() if i % 2 != 0 else char.lower() for i, char in enumerate(word))
print("Resulting word:", result)