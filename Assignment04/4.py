import math
def find_pythagorean_triplets(limit):
    """Find all Pythagorean triplets (x, y, z) within the given limit."""
    triplets = []
    for x in range(1, limit + 1):
        for y in range(x, limit + 1): 
            z = math.sqrt(x**2 + y**2)
            if z.is_integer() and z <= limit: 
                triplets.append((x, y, int(z)))
    return triplets
limit = 100
pythagorean_triplets = find_pythagorean_triplets(limit)
print(f"Pythagorean triplets within {limit}:")
for triplet in pythagorean_triplets:
    print(triplet)
