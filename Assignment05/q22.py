# 4×4 list
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

# Flatten the matrix and find average
average = sum(sum(row) for row in matrix) / (len(matrix) * len(matrix[0]))
print("4x4 List:", matrix)
print("Average of all elements:", average)