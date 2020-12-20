from random import randint

#create a list of play options
t = ["rock", "paper", "scissors"]

# Class Player
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = "" # Init choice to null

def print_score(player_1, player_2):
    print(player_1.name, ":", player_1.score, player_2.name, ":", player_2.score, "\n")

def update_score(player_1, player_2):
    if player_1.choice.lower() == player_2.choice.lower():
        print("Tie! No points for both!")
    elif player_1.choice.lower() == "rock":
        if player_2.choice == "paper":
            print(player_2.name, "wins!", player_1.choice, "covers", player_2.choice)
            player_2.score+=1
        else:
            print(player_1.name, "wins!", player_1.choice, "smashes", player_2.choice)
            player_1.score+=1
    elif player_1.choice.lower() == "paper":
        if player_2.choice == "scissors":
            print(player_2.name, "wins!", player_2.choice, "cut", player_1.choice)
            player_2.score+=1
        else:
            print(player_1.name, "wins!", player_1.choice, "covers", player_2.choice)
            player_1.score+=1
    elif player_1.choice.lower() == "scissors":
        if player_2.choice == "rock":
            print(player_2.name, "wins!", player_2.choice, "smashes", player_1.choice)
            player_2.score+=1
        else:
            print(player_1.name, "wins!", player_1.choice, "cut", player_2.choice)
            player_1.score+=1
    else:
        print("That's not a valid entry. Check your spelling!")

def play_computer(player):
    comp = Player ("Computer") 
    while True:
        p_1 = input("Rock, Paper, Scissor? Else type Quit?\n")
        if p_1.lower() == "quit":
            print_score(player, comp)
            break
        else:
            choice = t[randint(0,2)]
            comp.choice = choice
            player.choice = p_1
            update_score(player, comp)


def main():
    #Check for refactor
    name = input("Enter your name:")
    p1 = Player(name)

    play_computer(p1)

    #Code for multiplayer


if __name__ == "__main__":
    main()
