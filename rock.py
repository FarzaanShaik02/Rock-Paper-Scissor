import random
c=["Rock","Paper","Scissor"]
computer=random.choice(c)
print(c)
user=input("Enter you Choice=")
if computer==user:
    print("It's a tie")
elif user=="Rock":
    if computer=="Paper":
        print("you Lose,Paper covers Rock!")
    else:
        print("You won,Rock smashes scissor!")
elif user=="Paper":
    if computer=="Scissor":
        print("You lose,Scissor cuts paper!")
    else:
        print("You won,Paper covers Rock!")
elif user=="Scissor":
    if computer=="Rock":
        print("You lose,Rock smashes Scissor!")
    else:
        print("You won,Scissor cuts paper!")
else:
    print("Enter appropriate input!!!!")
print("computer choice is=",computer)
