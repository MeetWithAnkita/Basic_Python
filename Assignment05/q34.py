import random

# Create 3 cards
cards = random.sample(range(2, 15), 3)

flush = all(card % 13 == cards[0] % 13 for card in cards)
three_of_a_kind = len(set(cards)) == 1
pair = len(set(cards)) == 2
straight = sorted(cards)[2] - sorted(cards)[0] == 2 and len(set(cards)) == 3

print("Cards:", cards)
print("Flush:", flush)
print("Three of a kind:", three_of_a_kind)
print("Pair:", pair)
print("Straight:", straight)