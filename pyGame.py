import random

OPTIONS = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(OPTIONS)

def get_player_choice():
    while True:

        choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if choice in OPTIONS:
            return choice
        
def check_winner (player, computer):
    if player == computer:
        return "Tiel!"
    
    elif beats(player, computer):
        return "You won!"
    
    return "Computer won!"


def beats(one, two):

    wins = [('rock', 'scissors'), 
          ('paper', 'rock'),
          ('scissors', 'paper')]
    
    return (one, two) in wins

def play_game():
    while True:
        player = get_player_choice()
        computer = get_computer_choice()
        print("Computer played:", computer)
        winner = check_winner(player, computer)
        print(winner)


        play_again = input("Play again? (yes/no) ").lower()

        if play_again != "yes":
            break

if __name__ == '__main__':
    play_game()

