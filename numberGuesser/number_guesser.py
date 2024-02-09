import random

usrGuess = int(1)
attempts = 0
topOfRange = input("Type a Number: ")

if topOfRange.isdigit():
    topOfRange = int(topOfRange)
    if topOfRange <= 0:
            print("Please type a number larger than 1")
            quit()
else:
    print("Please type a number next time")
    quit()


r = int(random.randint(0, topOfRange)) # use randit because random.randnumber does not include upper bound. Highest possiblity with that would be topOfRange - 1

#print(r, type(r))

print("I am thinking of a number between 0 and " + str(topOfRange) + " can you guess it?")



while True: #loops until it finds break. We wont be setting this to false ever.
    attempts += 1
#obtain the first guess from the player
    usrGuess = input("Take a guess: ")
    if usrGuess.isdigit():
        usrGuess = int(usrGuess)
    else:
        print("Please type a number next time")
        continue #sends back to the top of the while loop
#check if the player was right
    if usrGuess == r:
        print("Good guess!")
        break
    elif usrGuess > r:
        print("Guess a lower number")
    else:
        print("Guess a higher number")

print("You found the right number in", attempts, "guesses!")
