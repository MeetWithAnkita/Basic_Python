import random

# Generate 10×10 random list
matrix = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

# Largest in the third row
largest_in_row_3 = max(matrix[2])

# Smallest in the sixth column
smallest_in_col_6 = min(row[5] for row in matrix)

print("10x10 Random List:")
for row in matrix:
    print(row)
print("Largest value in the third row:", largest_in_row_3)
print("Smallest value in the sixth column:", smallest_in_col_6)