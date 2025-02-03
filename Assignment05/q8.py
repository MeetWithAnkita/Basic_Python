# Prompt for two lists
L = list(map(int, input("Enter elements of list L separated by spaces: ").split()))
M = list(map(int, input("Enter elements of list M separated by spaces: ").split()))

# Add corresponding elements
if len(L) == len(M):
    N = [L[i] + M[i] for i in range(len(L))]
    print("List N (sum of L and M):", N)
else:
    print("Error: Lists are not of the same size.")