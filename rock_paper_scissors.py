import random

print("Let's play rock, paper, or scissors!")

player_wins = 0
computer_wins = 0
choices = ["rock", "paper", "scissors"]
wins_against = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

while player_wins < 2 and computer_wins < 2:
    player_choice = input("\nChoose rock, paper, or scissors: ").lower().strip()
    
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif wins_against[player_choice] == computer_choice:
        print("You won this round!")
        player_wins += 1
    else:
        print("Computer won this round!")
        computer_wins += 1
    
    print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")

if player_wins > computer_wins:
    print("Congratulations! You won the game.")
else:
    print("Computer won the game!")
