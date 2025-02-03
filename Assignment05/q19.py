palindromic_numbers = [x for x in range(100, 1000) if str(x) == str(x)[::-1]]
print("Palindromic numbers between 100 and 1000:", palindromic_numbers)