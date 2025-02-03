# Prompt the user to enter a string
user_input = input("Enter a multiline string (end with an empty line):\n")

# Split the input into lines
lines = user_input.strip().split('\n')

# Count the number of lines
line_count = len(lines)

# Count the number of sentences
sentence_count = sum(line.count('.') + line.count('?') + line.count('!') for line in lines)

# Print the counts
print(f"\nNumber of lines: {line_count}")
print(f"Number of sentences: {sentence_count}")