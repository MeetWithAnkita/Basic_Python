# Prompt for list input
lst = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
# Rotate list
rotated_list = lst[1:] + lst[:1] if lst else lst
print("Rotated list:", rotated_list)