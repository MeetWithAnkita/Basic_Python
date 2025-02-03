def swap_three(x, y, z):
    # Perform the swap
    x, y, z = y, z, x
    return x, y, z

# Example usage
x, y, z = 1, 2, 3
print(f"Before swapping: x = {x}, y = {y}, z = {z}")
x, y, z = swap_three(x, y, z)
print(f"After swapping: x = {x}, y = {y}, z = {z}")
