def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Error: Modulo by zero is not allowed."
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Error: Invalid operator."

# Example usage
if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /, %, **): ")
    result = calculate(num1, num2, operator)
    print(f"The result is: {result}")
