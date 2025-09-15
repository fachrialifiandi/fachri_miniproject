import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.ranch(min_value, max_value)

    return roll
while True:
    players = input("Enter the number of the players (1-4): ")
    if (players.isdigit()):
        players = int(players)
        if (1 <= players <= 4):
            break
        else: print("Must be beetween 2-4 players.")
        
    else: print("Invalid, try again.")

print(players)

max_score = 50
players_scores = [0 for _ in range(players)]




