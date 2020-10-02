'''
# This list comprehension does the same as:
> [values.get('rock') for values in selections if 'rock' in values]
> # this for loop
> for v in selections:
> ...   if 'rock' in v:
> ...     new_val.append(v['rock'])
rock = 1
paper = 2
scissors = 3
com_choice = 'rock'
player_choice = 'rock'
com_choice - player_choice = 0
print("It's a tie!")

com_choice = 'rock'
player_choice = 'paper'
com_choice - player_choice = -1
print("You win!")

com_choice = 'rock'
player_choice = 'scissors'
com_choice - player_choice = -2
print("I won!")

com_choice = 'paper'
player_choice = 'rock'
com_choice - player_choice = 1
print("I won!")

com_choice = 'scissors'
player_choice = 'rock'
com_choice - player_choice = 2
print("You win!") 
'''
#rock paper scissors game against the computer
import random
import sys

#list comprehension = for loop in one line - brings back a list 
def rules(com_choice, player_choice):
    com_value = [value.get(com_choice) for value in selections if com_choice in value][0]
    player_value = [value.get(player_choice) for value in selections if player_choice in value][0]
    answer = com_value - player_value 
    if answer == 0: 
        print("It's a tie!")
    elif abs(answer) > 1:
        print("You Win!" if answer > 0 else "I won!")
    elif abs(answer) == 1:
        print("You Win!" if answer < 0 else "I won!")

def play_again():
    choice = input("Do you want to play again? ")
    if choice.lower() == 'yes':
        return True 
    else:
        return False

if __name__ == '__main__':
    selections = [{'rock': 1}, {'paper': 2}, {'scissors': 3}]
    selections_keys = ['rock', 'paper', 'scissors']
    is_playing = True
    while is_playing:
        com_choice = random.choice(selections_keys)

        player_choice = input("Play rock paper scissors against me! Type rock, paper, or scissors: \n")

        #quit
        if player_choice not in selections_keys:
            print("That's not a valid answer.")
            sys.exit()

        print("You chose", player_choice, "!")
        print("I chose", com_choice)
        rules(com_choice, player_choice)
        is_playing = play_again()