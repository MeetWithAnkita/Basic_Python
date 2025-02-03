teams = {}

# Input team data
while True:
    team = input("Enter team name (or 'stop' to finish): ").strip()
    if team.lower() == "stop":
        break
    wins = int(input(f"Enter wins for {team}: "))
    losses = int(input(f"Enter losses for {team}: "))
    teams[team] = [wins, losses]

# Calculate winning percentage
team_query = input("Enter team name to get winning percentage: ").strip()
if team_query in teams:
    wins, losses = teams[team_query]
    win_percentage = wins / (wins + losses) * 100
    print(f"Winning percentage of {team_query}: {win_percentage:.2f}%")
else:
    print("Team not found.")