# Given list
L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Calculate gaps
gaps = [L[i + 1] - L[i] for i in range(len(L) - 1)]

# Maximum gap
max_gap = max(gaps)

# Percentage of gaps of size 2
percentage_gaps_2 = (gaps.count(2) / len(gaps)) * 100

print("Gaps between consecutive entries:", gaps)
print("Maximum gap size:", max_gap)
print(f"Percentage of gaps of size 2: {percentage_gaps_2:.2f}%")