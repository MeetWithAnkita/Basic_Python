# Use the same product-price dictionary from Question 27
products = {'Apple': 50, 'Banana': 30, 'Mango': 20}

# a) Query by price range
max_price = float(input("Enter maximum price to filter: "))
affordable_products = [product for product, price in products.items() if price < max_price]
print("Affordable products under", max_price, ":", affordable_products)

# b) Days in months dictionary
months = {
    "January": 31, "February": 28, "March": 31, "April": 30, "May": 31,
    "June": 30, "July": 31, "August": 31, "September": 30, "October": 31,
    "November": 30, "December": 31,
}
month_name = input("Enter month name: ").capitalize()
print(f"Days in {month_name}:", months.get(month_name, "Invalid month"))