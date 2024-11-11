# 4. To determine the stock value of a store of certain item on the basis
# stock value = number of item * amount per item 
y = 0
choice = 'y'  # Initialize choice to enter the loop
total = 0

# Using a do-while-like structure in Python (Python doesn’t have a native do-while loop)
while True:
    item = int(input("Number of items: "))
    amount = float(input("Amount per item: "))
    value = item * amount
    print(f"Value of this item: {value}")
    total = value + total 

    choice = input("If there is another item, press 'y'; otherwise, press 'n': ").lower()
    if choice != 'y':
        break
print(f"Toltal stock value is :{total}")
