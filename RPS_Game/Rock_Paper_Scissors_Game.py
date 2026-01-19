# Game : Paper, Rock and Scissors
''' 

Paper 1
Rock -1
Scissors 0

''' 
import random
Computer = random.choice([1, -1 , 0])
user=input("Enter Your Choice : ")
dict={"P" : 1, "R" : -1, "S" : 0}
reverse_dict={1 : "Paper", -1 : "Rock", 0 : "Scissors"}
you=dict[user]
print(f" You chose {reverse_dict[you]} \n Computer chose {reverse_dict[Computer]}\n")
if (Computer == you ):
    print("\tIts Tie")
# else:
#     if (Computer - you == 1) or (Computer - you == -2):
#         print("You Win ")
#     elif(Computer - you == -1) or (Computer - you == 2):
#         print("You Lose")
else:
    if (Computer == 1 and you == -1):   # 2 
        print("\tYou Lose")
    elif (Computer == 1 and you == 0):  # 1  
        print("\tYou Win")
    elif (Computer == -1 and you == 1): # -2 
        print("\tYou Win")
    elif (Computer == -1 and you == 0): # -1 
        print("\tYou Lose")
    elif (Computer == 0 and you == -1): # 1 
        print("\tYou Win")
    elif (Computer == 0 and you == 1):  # -1 
        print("\tYou Lose")
    else :
        print("Something Went Wrong")


    