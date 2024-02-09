import random

usrScore = 0
cpuScore = 0
options = ["rock", "paper", "scissors"]

while True:
    usrInput = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if usrInput == 'q':
        break
    if usrInput not in options:
        print("Pick a valid resonse.")
        continue
    r = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    cpuPick = options[r]
    print("Computer Picked", cpuPick + ".")

    if usrInput == 'rock' and cpuPick == "scissors":
        print("You Won!")
        usrScore += 1
        continue
    
    elif usrInput == 'paper' and cpuPick == "rock":
        print("You Won!")
        usrScore += 1
        continue
    
    elif usrInput == 'scissors' and cpuPick == "paper":
        print("You Won!")
        usrScore += 1
        continue
    else:
        print("You Lost!")
        cpuScore += 1

print("You won", usrScore, "times.")
print("You lost", cpuScore, "times.")
print("Goodbye!")

