from random import randint

#create a list of play options
t = ["rock", "paper", "scissors"]

def print_score(comp_score, player_score):
    print("Computer's Score:", comp_score, "Player's score:", player_score, "\n")

#assign a random play to the computer
computer = t[randint(0,2)]

#Initialise scores
player_score = 0
comp_score = 0

while True:
    player_input = input("Rock, Paper, Scissor? Else type Quit?\n")
    if player_input.lower() == "quit":
        print_score(comp_score, player_score)
        break
    elif player_input.lower() == computer.lower():
        print("Tie! No points for both!")
    elif player_input.lower() == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player_input)
            comp_score+=1
        else:
            print("You win!", player_input, "smashes", computer)
            player_score+=1
    elif player_input.lower() == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player_input)
            comp_score+=1
        else:
            print("You win!", player_input, "covers", computer)
            player_score+=1
    elif player_input.lower() == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player_input)
            comp_score+=1
        else:
            print("You win!", player_input, "cut", computer)
            player_score+=1
    else:
        print("That's not a valid entry. Check your spelling!")
    computer = t[randint(0,2)]

