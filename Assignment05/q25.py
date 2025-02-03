# Input 4x4 matrix
matrix = [[16, 2, 3, 13],
          [5, 11, 10, 8],
          [9, 7, 6, 12],
          [4, 14, 15, 1]]

# Check magic square
magic_sum = sum(matrix[0])
is_magic_square = all(sum(row) == magic_sum for row in matrix) and \
                  all(sum(matrix[i][j] for i in range(4)) == magic_sum for j in range(4)) and \
                  sum(matrix[i][i] for i in range(4)) == magic_sum and \
                  sum(matrix[i][3 - i] for i in range(4)) == magic_sum

print("4x4 List:")
for row in matrix:
    print(row)
print("Is magic square:", is_magic_square)