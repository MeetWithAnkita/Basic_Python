import random
from collections import Counter

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]
frequency = Counter(num for row in matrix for num in row)
top_three = frequency.most_common(3)

print("5x5 Matrix:")
for row in matrix:
    print(row)
print("Top 3 most common numbers:", top_three)