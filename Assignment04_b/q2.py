# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Split the string into words
words = user_input.split()

# Count the number of words
word_count = len(words)

# Print the number of words
print(f"\nTotal number of words: {word_count}")

# Print each word with its length in a tabular format
print("\nWord\tLength")
print("-" * 20)
for word in words:
    print(f"{word}\t{len(word)}")