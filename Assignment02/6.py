# 6. To print a currency conversion table from Pounds, Dollar, Euro to
# equivalent Indian Rupees.
GBP_to_INR = 102.0   # 1 Pound = 102 INR
USD_to_INR = 83.0    # 1 Dollar = 83 INR
EUR_to_INR = 90.0    # 1 Euro = 90 INR
n = int(input("Enter the data for how many data i needed :"))
print(f"{'Rupees':<10} {'Pound':<15} {'Dollar':<15} {'Euro':<10}")
print("-"*55)
print("-" * 55)
for i in range(1,n) :
    pound = i * GBP_to_INR
    dollar = i * USD_to_INR
    euro = i * EUR_to_INR
    print(f"{i:<10}{pound:<15}{dollar:<15}{euro:<15}")
