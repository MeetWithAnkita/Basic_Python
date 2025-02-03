# Prompt the user to enter a formula
formula = input("Enter a formula: ")

# Check for balanced parentheses
if formula.count('(') == formula.count(')'):
    print("The formula has balanced parentheses.")
else:
    print("The formula does not have balanced parentheses.")