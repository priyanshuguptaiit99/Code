import random

# This is a snake water gun game 

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youdict = {"s" : 1, "w" : -1, "g" : 0}
reversedict = {1 : "Snake", 0 : "Gun", -1 : "Water"}

you = youdict[youstr]

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(computer == you):
    print("Its Draw")

else:
    if(computer ==- 1 and you == 1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1  and you == -1):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you ==- 1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")