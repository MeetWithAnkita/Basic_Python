scores = {}

# Input game scores
while True:
    entry = input("Enter game score (format: 'team1 score1-team2 score2', or 'stop' to finish): ").strip()
    if entry.lower() == "stop":
        break
    try:
        team1_score, team2_score = entry.split("-")
        team1, score1 = team1_score.rsplit(" ", 1)
        team2, score2 = team2_score.split(" ", 1)
        score1, score2 = int(score1), int(score2)
        
        scores[team1] = scores.get(team1, [0, 0])  # [wins, losses]
        scores[team2] = scores.get(team2, [0, 0])

        if score1 > score2:
            scores[team1][0] += 1
            scores[team2][1] += 1
        else:
            scores[team2][0] += 1
            scores[team1][1] += 1
    except ValueError:
        print("Invalid input format. Please use the format: 'team1 score1-team2 score2'.")

print("Game records:", scores)
