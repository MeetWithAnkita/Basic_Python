def pronic_numbers_within(limit):
    pronic_numbers = []
    n = 0
    while True:
        pronic = n * (n + 1)  
        if pronic > limit:
            break
        pronic_numbers.append(pronic)
        n += 1
    return pronic_numbers

pronic_numbers = pronic_numbers_within(200)
print("Pronic Numbers within 200:")
print(pronic_numbers)
