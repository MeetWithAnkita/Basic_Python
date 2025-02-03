# Solution to Question 1
# Prompt user for list input
user_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

print("a) Total number of items:", len(user_list))
print("b) Last item in the list:", user_list[-1] if user_list else "List is empty")
print("c) Reversed list:", user_list[::-1])
print("d) Contains 5:", "Yes" if 5 in user_list else "No")
print("e) Count of 5s:", user_list.count(5))

# f) Remove first and last, sort, and print
modified_list = sorted(user_list[1:-1]) if len(user_list) > 2 else []
print("f) Sorted remaining items:", modified_list)

# g) Count numbers less than 5
print("g) Numbers less than 5:", sum(1 for i in user_list if i < 5))