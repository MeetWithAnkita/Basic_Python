# Prompt the user to enter the text with hyphens
text = input("Enter the text with hyphens: ")

# Replace hyphens with user-provided words
while '-' in text:
    word = input(f"Enter a word to replace the first hyphen: ")
    text = text.replace('-', word, 1)

# Print the reconstructed text
print("Reconstructed text:", text)