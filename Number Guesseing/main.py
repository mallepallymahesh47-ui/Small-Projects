#Goal: Computer generates a random number between 1–100.
# User guesses until correct, and you give hints — “Too High” / “Too Low”.

from random import randint
computer=randint(1,100)

u=-1
gusses=1
while (u!=computer):
    try:
        u=int(input("Enter a Number : "))
    except ValueError as V:
        print(V)

    if (u>computer):
        print("Too High... Enter Smaller Number")
        gusses+=1
    elif(u<computer):
        print("Too Low.. Enter Higher Number")
        gusses+=1
print(f"You gussesed Number {u} in {gusses} gusses")




