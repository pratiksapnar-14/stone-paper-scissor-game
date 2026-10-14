#stone, paper and Scissor Game 
import random


'''
-1 for stone
0 for paper
1 for scissor
'''

computer = random.choice([-1,0,1])
reverseDict = {-1: "stone", 0: "paper", 1:"scissor"}

user = int(input("Enter your choice (-1 for stone, 0 for paper, 1 for scissor) : "))

print(f"you choose {reverseDict[user]}\ncomputer choose {reverseDict[computer]}")

if (computer==user):
    print("it's a draw")

else :
    if(computer == -1 and user == 0):
        print("you win")

    elif(computer == 0 and user == -1):
        print("you loose")

    elif(computer == 0 and user == 1):
        print("you win")

    elif(computer == 1 and user == 0):
        print("you loose")  

    elif(computer == -1 and user == 1):
        print("you loose") 

    elif(computer == 1 and user == -1):
        print("you win")        

    else:
        print("error")    


