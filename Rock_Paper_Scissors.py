"Implementation of rock,paper,Scissors game"


import random
def rockpaperscissors(player,opponent):
    

    if player== opponent:
        print('It\'s a tie')
        
    elif (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        print('You won')
        
    else:
        print('You lost')
        

player = input("What's your choice? Type\n'r' for rock \n'p' for paper \n's' for scissors\n")
opponent = random.choice(['r', 'p', 's'])
print("Opponents's choice is ",opponent)
rockpaperscissors(player,opponent)
