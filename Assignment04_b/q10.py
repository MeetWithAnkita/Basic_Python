def decipher_code(code_string):
    result = ""
    i = 0

    while i < len(code_string):
        # If the character is a space, add a space to the result
        if code_string[i] == " ":
            result += " "
            i += 1
            continue

        # Extract three digits at a time
        number = code_string[i:i+3]

        if len(number) == 3 and number.isdigit():
            # Convert the number to an integer
            ascii_value = int(number)

            # Apply rule (b): Add 5
            new_value = ascii_value + 5

            # Apply rule (c): Subtract 10 if the new value exceeds the range of letters
            if new_value > 122:  # 122 is ASCII for 'z'
                new_value -= 10

            # Append the corresponding character to the result
            result += chr(new_value)
        else:
            result += "?"  # For invalid input
        i += 3

    return result


# Input from the user
code_string = input("Enter the code string: ").strip()

# Decipher the code
translated_code = decipher_code(code_string)

# Display the result
print("Translated code:", translated_code)
