import random
import os
import time
 
def clear():
    os.system("clear")

 
# Instructions/win conditions for the game
def rps_instructions():
 
    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()
 

def rps():
     
    global rps_table
    global game_map
    global name
 
    # This prints and runs the game loop for rock paper scissors
    while True:
 
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter \"Rock\",\"Paper\",\"Scissors\" to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
 
        print()
 
        # Runs the player input
        inp = input("Enter your move : ")
 
        if inp.lower() == "help":
            clear()
            rps_instructions()
            continue
        elif inp.lower() == "exit":
            clear()
            break  
        elif inp.lower() == "rock":
            player_move = 0
        elif inp.lower() == "paper":
            player_move = 1    
        elif inp.lower() == "scissors":
            player_move = 2
        else:
            clear()
            print("Wrong Input!!")
            rps_instructions()  
            continue
 
        print("Computers turn")
 
        print()
        time.sleep(2)
 
        # Randomize the computer movement
        comp_move = random.randint(0, 2)
 
        # Print the computer move
        print("Computer chooses ", game_map[comp_move].upper())
 
        # Checking for a winner
        winner = rps_table[player_move][comp_move]
 
        # Declare the winner of the match 
        if winner == player_move:
            print(name, "Is the ultimate champion of the world!!!")
        elif winner == comp_move:
            print("The Computer has achieved vicotry today!")
        else:
            print("The game is a draw!")
 
        print()
        time.sleep(2)
        clear()


if __name__ == '__main__':
 
    # The mapping between moves and numbers
    game_map = {0:"rock", 1:"paper", 2:"scissors"}
 
    # Win-lose matrix for traditional game
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
  
    name = input("Enter your name: ")
 
    # The GAME LOOP
    while True:
 
        # The Game Menu
        print()
        print("Let's Play!!!")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to quit")
        print()
 
        # Try block to handle the player choice 
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong Choice")   
            continue
 
        # Play the traditional version of the game
        if choice == 1:
            rps()
 
 
        # Quit the GAME LOOP    
        elif choice == 2:
            break
 
        # Other wrong input
        else:
            clear()
            print("Wrong choice. Read instructions carefully.")