def compute_derivative(term):
    # Check if the input matches the pattern x^n
    if "^" in term:
        base, exponent = term.split("^")
        if base.strip() == "x" and exponent.isdigit():
            n = int(exponent)
            coefficient = n
            new_exponent = n - 1
            
            # Build the derivative string
            if new_exponent == 1:
                return f"{coefficient}x"
            elif new_exponent == 0:
                return f"{coefficient}"
            else:
                return f"{coefficient}x^{new_exponent}"
    elif term.strip() == "x":
        return "1"  # Derivative of x is 1
    elif term.isdigit():
        return "0"  # Derivative of a constant is 0
    
    return "Invalid input. Use format like x^3 or x^25."

# Prompt the user for input
user_input = input("Enter a term like x^3 or x^25: ").strip()
result = compute_derivative(user_input)
print("The derivative is:", result)
