# Prompt the user to enter a word and a letter
word = input("Enter a word: ")
letter = input("Enter a letter: ")

# Split the word at the given letter
if letter in word:
    index = word.index(letter)
    print("Part 1:", word[:index + 1])
    print("Part 2:", word[index + 1:])
else:
    print(f"The letter '{letter}' is not in the word.")