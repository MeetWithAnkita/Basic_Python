import random

# Generate list of random integers
random_list = [random.randint(1, 100) for _ in range(20)]
print("a) List of random numbers:", random_list)

# b) Average of elements
average = sum(random_list) / len(random_list)
print("b) Average of elements:", average)

# c) Largest and smallest values
print("c) Largest:", max(random_list), "| Smallest:", min(random_list))

# d) Second largest and second smallest values
sorted_list = sorted(random_list)
print("d) Second largest:", sorted_list[-2], "| Second smallest:", sorted_list[1])

# e) Count of even numbers
even_count = sum(1 for x in random_list if x % 2 == 0)
print("e) Count of even numbers:", even_count)