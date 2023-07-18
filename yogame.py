# Number guesising game 

import random

attempts_list = []

def show_score():

    if not attempts_list:
        print("There is cuurently no high score, it's yours for the taking!")

    else:
        print(f'The current high score is' f'{min(attempts_list)} attempts')


def start_game():

    attempts = 0

    random_number = random.randint(1, 10)

    print("Helllo Traveller, welcome to the game of guesses!")

    player_name = input('What is the your name?')

    wanna_play = input(f'Hi, {player_name}, would you like to play the game? (Enter yes/no): ')


    if wanna_play.lower() != 'yes':
        print('That is too bad, have a nice day!')

        exit()

    else: show_score()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 10: '))

            if guess < 1 or guess > 10:
                raise ValueError(' Please guess a number within the given range ')
            
            attempts += 1

            attempts_list.append(attempts)

            if guess == random_number:


                print('Nice! You got it!')

                print(f'It to you {attempts} attempts')
                wanna_play = input('Would you like to play again? (Enter yes/no): ')
                if wanna_play.lower() == 'yes':

                    print('Awesome!, have a good one!')
                    break 

                else:
                    attempts = 0
                    random_number = random.randint(1, 10)
                    show_score()
                    continue

            else:
                if guess > random_number:
                    print('It is lower')

                elif guess < random_number:
                    print('It is higher')

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again....')
    

if __name__ == '__main__':
    start_game()