def pascal_triangle(rows):
    triangle = []  # Initialize an empty list to store rows of the triangle

    for i in range(rows):
        # Create a new row with all 1s
        row = [1] * (i + 1)
        
        # Compute the intermediate values for the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Append the completed row to the triangle
        triangle.append(row)
    
    return triangle


def print_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))  # Find the width of the last row

    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))


# Example Usage
rows = int(input("Enter the number of rows for Pascal's Triangle: "))
triangle = pascal_triangle(rows)
print_triangle(triangle)
