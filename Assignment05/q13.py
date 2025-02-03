# Input list with duplicates
user_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
# Remove duplicates
unique_list = list(dict.fromkeys(user_list))
print("List after removing duplicates:", unique_list)