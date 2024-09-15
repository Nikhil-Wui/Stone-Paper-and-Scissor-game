import random


computer = random.choice([0, -1, 1])

you= input("Enter Your Choice: ")
youdict={"s":1,"p":-1,"z":0}

reversedict={1:"Stone",-1:"Paper",0:"Scissor"}

youstr=youdict[you]
print(f"Computer choose {reversedict[computer]} and you choosed {reversedict[youstr]}")

if(computer==youstr):
    print("It's a DRAW")
else:
    if(computer==1 and youstr==-1):
        print("You win")
    elif(computer==1 and youstr==0):
        print("You Lost")
    elif(computer==-1 and youstr==0):
        print("You win")
    elif(computer==-1 and youstr==1):
        print("You Lost")
    elif(computer==0 and youstr==-1):
        print("You Lost")
    elif(computer==0 and youstr==1):
        print("You win")
    else:
        print("Something went wrong")


        
    



