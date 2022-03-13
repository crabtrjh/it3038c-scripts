# The mapping between moves and numbers
game_map = {0:"rock", 1:"paper", 2:"scissors"}
 
# Win-lose matrix for traditional game
rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
 

import random

# Player Input
inp = input("Enter your move : ")
 
if inp.lower() == "help":
    clear()
    rps_instructions()
    
elif inp.lower() == "exit":
    clear()
  
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
    


# Get the computer move randomly
comp_move = random.randint(0, 2)
 
# Print the computer move
print("Computer chooses ", game_map[comp_move].upper())
