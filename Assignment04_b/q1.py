# Import required libraries
from itertools import permutations
import re

# Prompt the user to enter a string
user_input = input("Enter a string: ")

# a) Total number of characters in the string
print("\n(a) Total number of characters:", len(user_input))

# b) String repeated 5 times
print("(b) String repeated 5 times:", user_input * 5)

# c) First character of the string
print("(c) First character:", user_input[0])

# d) First four characters of the string
print("(d) First four characters:", user_input[:4])

# e) Last two characters of the string
print("(e) Last two characters:", user_input[-2:])

# f) String in reversed form
print("(f) Reversed string:", user_input[::-1])

# g) Ninth character of the string (if long enough)
if len(user_input) >= 9:
    print("(g) Ninth character:", user_input[8])
else:
    print("(g) The string is too short for a ninth character.")

# h) String with first and last characters removed
print("(h) String without first and last characters:", user_input[1:-1])

# i) String in uppercase
print("(i) String in uppercase:", user_input.upper())

# j) String with every 'i' replaced with 'I'
print("(j) String with 'i' replaced with 'I':", user_input.replace('i', 'I'))

# k) String with every letter replaced by a space
print("(k) String with all characters replaced by spaces:", " " * len(user_input))

# l) Frequency of each character in the string
frequency = {}
for char in user_input:
    frequency[char] = frequency.get(char, 0) + 1
print("(l) Frequency of each character:", frequency)

# m) Least frequent character
least_frequent = min(frequency, key=frequency.get)
print("(m) Least frequent character:", least_frequent)

# n) Execute a Python code in a string
exec_code = input("\n(n) Enter a Python code to execute (use caution): ")
try:
    exec(exec_code)
except Exception as e:
    print("Error in executing the code:", e)

# o) Show uncommon words from two given strings
string1 = input("\n(o) Enter the first string: ")
string2 = input("Enter the second string: ")
set1, set2 = set(string1.split()), set(string2.split())
uncommon_words = set1.symmetric_difference(set2)
print("Uncommon words:", uncommon_words)

# p) Print URLs from a string
url_string = input("\n(p) Enter a string with URLs: ")
urls = re.findall(r'https?://\S+', url_string)
print("URLs found:", urls)

# q) Find all permutations of a given string
perm_string = input("\n(q) Enter a string to find permutations: ")
all_permutations = [''.join(p) for p in permutations(perm_string)]
print("All permutations:", all_permutations)

# r) Count total letters, digits, and special characters in a string
total_letters = sum(char.isalpha() for char in user_input)
total_digits = sum(char.isdigit() for char in user_input)
total_specials = len(user_input) - total_letters - total_digits
print("\n(r) Letters:", total_letters, "Digits:", total_digits, "Special characters:", total_specials)