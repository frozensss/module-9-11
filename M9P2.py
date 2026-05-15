# M9P2.py
# Enter a player's last name, hits, and at bats.
# Use a function to compute and return batting average.


def compute_batting_average(hits, at_bats):
    if at_bats == 0:
        average = 0.0
    else:
        average = hits / at_bats

    return average


player_count = 0
response = input("Do you want to enter a player? Enter Yes or No: ")

print()
print(f"{'Last Name':<15}{'Batting Average':>18}")
print("-" * 33)

while response.lower() == "yes":
    last_name = input("Enter player's last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))

    batting_average = compute_batting_average(hits, at_bats)
    player_count = player_count + 1

    print(f"{last_name:<15}{batting_average:>18.3f}")

    response = input("Do you want to enter another player? Enter Yes or No: ")

print("-" * 33)
print(f"Number of players entered: {player_count}")
