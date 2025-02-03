def robot_steps(n, memo=None):
    if memo is None: # Initialize the memo dictionary
        memo = {}
    if n < 0: # No way to walk negative distances
        return 0
    if n == 0: # Base case: 1 way to walk 0 meters
        return 1
    # Check if the result is already calculated
    if n in memo:
        return memo[n]
    # Recursive step: Sum ways for (n-1), (n-2), and (n-3)
    memo[n] = robot_steps (n-1, memo) + robot_steps (n-2, memo) + robot_steps (n-3, memo)
    return memo [n]
# Example usage
if __name__== "_main_":
    n = 5
    print(f"Number of ways the robot can cross {n} meters: {robot_steps(n)}")