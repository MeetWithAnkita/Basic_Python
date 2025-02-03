# Create product-price dictionary
products = {}
while True:
    product = input("Enter product name (or 'stop' to finish): ").strip()
    if product.lower() == "stop":
        break
    price = float(input(f"Enter price for {product}: "))
    products[product] = price

# Query dictionary
while True:
    product_query = input("Enter product name to query (or 'stop' to exit): ").strip()
    if product_query.lower() == "stop":
        break
    print("Price:", products.get(product_query, "Product not found."))