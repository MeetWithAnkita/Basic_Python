import random

# Simplified card dictionary
cards = {i: i for i in range(2, 15)}  # 11=Jack, 12=Queen, 13=King, 14=Ace

# Deal cards to 2 players
player1 = random.sample(list(cards.values()), 3)
player2 = random.sample(list(cards.values()), 3)

# Compare highest cards
player1.sort(reverse=True)
player2.sort(reverse=True)

winner = "Draw"
if player1 > player2:
    winner = "Player 1 wins!"
elif player2 > player1:
    winner = "Player 2 wins!"

print("Player 1 cards:", player1)
print("Player 2 cards:", player2)
print(winner)