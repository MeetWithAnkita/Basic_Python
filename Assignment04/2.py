def generate_multiplication_table(n, limit=10):
    """Generate and print the multiplication table for the given number n."""
    for i in range(1, limit + 1):
        print(f"{n} x {i} = {n * i}")

# Input number n
n = int(input("Enter a number to generate its multiplication table: "))

# Optional: You can specify the limit up to which the table should be generated (default is 10)
limit = int(input("Enter the limit (default is 10): ") or 10)

# Generate and print the multiplication table
generate_multiplication_table(n, limit)
