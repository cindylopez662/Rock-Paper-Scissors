#rock paper scissors game against the computer
import random
import sys
selections = ['rock', 'paper', 'scissors']
com_choice = random.choice(selections)
player_choice = input("Play rock paper scissors against me! Type rock, paper, or scissors: \n")

#quit
if player_choice not in selections:
    print("That's not a valid answer.")
    sys.exit()

print("You chose", player_choice, "!")
print("I chose", com_choice)

if com_choice == player_choice:
     print("It's a tie!")
     sys.exit()

if com_choice == 'rock' and player_choice == 'paper':
     print("You win!")
     sys.exit()
if com_choice == 'rock'and player_choice == 'scissors':
     print("I win!")
     sys.exit()
if com_choice == 'paper' and player_choice == 'scissors':
     print("You win!")
     sys.exit()
if com_choice == 'paper' and player_choice == 'rock':
     print("I win!")
     sys.exit()
if com_choice == 'scissors'and player_choice == 'paper':
     print("I win!")
     sys.exit()
if com_choice == 'scissors'and player_choice == 'rock':
     print("You win!")
     sys.exit()