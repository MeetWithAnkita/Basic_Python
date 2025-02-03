tableData = [['Jasmine', 'Rose', 'Tulip', 'Chrysanthemum'],
             ['Julia', 'Jahanara', 'Manasi', 'Tapasi'],
             ['is akin to', 'resembles', 'reminds me of', 'is another name for']]

# Function to print the table
def printTable(data):
    col_widths = [max(len(item) for item in col) for col in zip(*data)]
    for row in zip(*data):
        print(' '.join(item.ljust(width) for item, width in zip(row, col_widths)))

# Print the table
printTable(tableData)

# Generate sentences
for i in range(len(tableData[0])):
    print(f"{tableData[1][i]} {tableData[2][i]} {tableData[0][i]}.")