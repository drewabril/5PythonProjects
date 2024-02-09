import random

usrScore = 0

cpuScore = 0

while True:
    usrInput = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if usrInput == 'q':
        break
    if usrInput not in ["rock", "paper", "scissors"]
        print("Pick a valid resonse.")
        continue
    r = random.randomint(0, 2)
    #rock: 0, paper: 1, scissors: 2

print("Goodbye!")



