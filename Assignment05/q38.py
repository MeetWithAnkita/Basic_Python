def check_winner(board, m, n, k):
    # Check rows, columns, and diagonals for a winner
    def is_winner(player):
        # Check rows
        for row in board:
            for i in range(n - k + 1):
                if all(cell == player for cell in row[i:i + k]):
                    return True

        # Check columns
        for col in range(n):
            for i in range(m - k + 1):
                if all(board[row][col] == player for row in range(i, i + k)):
                    return True

        # Check diagonals
        for row in range(m - k + 1):
            for col in range(n - k + 1):
                if all(board[row + d][col + d] == player for d in range(k)):
                    return True
                if all(board[row + d][col + k - d - 1] == player for d in range(k)):
                    return True
        return False

    for player in ("X", "O"):
        if is_winner(player):
            return player
    return None

# Sample game (3×3×3 game with winner X)
board = [
    ["X", "O", "O"],
    ["O", "X", "O"],
    ["X", "X", "X"],
]
winner = check_winner(board, 3, 3, 3)
if winner:
    print("Winner:", winner)
else:
    print("No winner.")