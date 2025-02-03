# Create an 8×8 list with a checkerboard pattern
checkerboard = [[(i + j) % 2 + 1 for j in range(8)] for i in range(8)]
print("Checkerboard 8x8 pattern:")
for row in checkerboard:
    print(row)