import random
from turtle import goto
 
def play():
    Player = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n")
    Player = Player.lower()
    CPU = random.choice(['r', 'p', 's'])
    if Player == "r" or Player == "p" or Player == "s" :          
       
        
        if CPU == Player:
            print("Player and CPU have same choice " + Player.upper() +  ". It's a tie")
            play()
        
        # r > s, s > p, p > r   
        elif is_win(CPU, Player):
            print("Player has chosen " + Player.upper() + " and the CPU have chosen " + CPU.upper() + " Player won")
        else:   
            print("Player has chosen " + Player.upper()  + " and the CPU have chosen " + CPU.upper() + " Player lost")
    else:
        print("not amongst our options")
        play()
    
                  
def  is_win(CPU, Player):                 
     # return true is the Player beat the CPU
     # winning conditions:r > s, s > p, p > r  
     if (CPU == 'r' and Player == 's') or (CPU == 's' and Player == 'p') or (CPU == 'p' and  Player == 'r'):
        return False   
     return True
     
play();
 
    


     
                 