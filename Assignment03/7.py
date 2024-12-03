# 7. To print the value of a given amount of currency value in words.
from num2words import num2words

def print_currency_in_words(amount):
    # Convert the number to words with currency style
    amount_in_words = num2words(amount, lang='en', to='currency', currency='INR')  # Use 'INR' for Indian Rupees
    return amount_in_words.capitalize()

# Input the amount
amount = float(input("Enter the currency amount: "))
print("The amount in words is:", print_currency_in_words(amount))
