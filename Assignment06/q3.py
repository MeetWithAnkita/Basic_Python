def first_diff(str1, str2):
    """
    Returns the first location where the strings differ.
    
    Parameters:
    - str1 (str): The first string.
    - str2 (str): The second string.

    Returns:
    - int: The index of the first differing character, or -1 if the strings are identical.
    """
    # Get the minimum length to avoid index out of range errors
    min_length = min(len(str1), len(str2))

    for i in range(min_length):
        if str1[i] != str2[i]:
            return i  # Return the index where the strings differ
    
    # If one string is longer than the other, return the index where they start differing
    if len(str1) != len(str2):
        return min_length
    
    # If the strings are identical
    return -1

# Example usage
if __name__ == "__main__":
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    print(f"The first difference is at index: {first_diff(str1, str2)}")
