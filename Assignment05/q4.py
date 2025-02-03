# Prompt user input
nums = list(map(int, input("Enter numbers between 11 and 22 (space-separated): ").split()))
# Replace numbers greater than 19
nums = [min(num, 19) for num in nums]
print("Modified list:", nums)