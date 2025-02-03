# Prompt the user to enter an algebraic expression
expression = input("Enter an algebraic expression: ")

# Insert multiplication symbols
result = ""
for i in range(len(expression) - 1):
    result += expression[i]
    if (expression[i].isdigit() and expression[i + 1].isalpha()) or \
       (expression[i] == ')' and expression[i + 1] == '('):
        result += '*'
result += expression[-1]

# Print the resulting expression
print("Expression with multiplication symbols:", result)