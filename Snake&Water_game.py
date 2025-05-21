'''
1 for snake 
-1 for water 
0 for gun
'''
import random
computer = random.choice([-1,0,1])
youstr = input("enter your choice: ")
youdict = {"s":1, "w":-1, "g":0 }
reversedict = {1: 'snake', -1:"water", 0:"gun" }

if youstr not in youdict:
    print("invalid input! please enter 's', 'w', or 'g' .")
else:
    you = youdict[youstr]

print(f"you chose {reversedict[you]}\n computer chose {reversedict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer == -1 and you == 1 ):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 1 and you == -1):
        print("you lose!")
    elif(computer == 1 and you == 0):
        print("you win!")
    elif(computer == 0 and you == -1):
        print("you win!")
    elif(computer == 0 and you == 1):
        print("you lose!")
    else:
        print("SOMETHING WENT WRONG")
'''
we can also replace the if-else ladder by finding the patter 
of win and lose according to the number and it can be written as:
if((computer - you) == -1 or (computer - you) == 2):
    print("you lose")
else:
    print('you win')

'''