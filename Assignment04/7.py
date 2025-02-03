def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

rows = int(input("Enter the number of rows for Pascal's Triangle: "))
pascals_triangle = generate_pascals_triangle(rows)
print("\nPascal's Triangle:")
print_pascals_triangle(pascals_triangle)
