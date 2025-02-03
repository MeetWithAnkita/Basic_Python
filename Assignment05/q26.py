# Translation from (row, col) to flat index
def to_flat(row, col, width):
    return row * width + col

# Translation from flat index to (row, col)
def to_row_col(flat, width):
    return divmod(flat, width)

# Test
row, col, width = 1, 2, 3
flat_index = to_flat(row, col, width)
row_col = to_row_col(flat_index, width)
print("Flat index:", flat_index)
print("Row, Column:", row_col)