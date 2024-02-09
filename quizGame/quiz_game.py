print("Welcome to the quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print('Welcome')

score = 0

answer = input("Who makes the Mustang? ")

if answer.lower() == "ford": #make things less case-sensitive with .lower()
    print("Correct!")
    score = score + 1
    print(score)
else:
    print("Sorry, you got that wrong")

answer = input("What soda comes in a Blue can? ")

if answer.lower() == "pepsi":
    print("Correct!")
    score += 1 #this is a cleaner way to add one to a variable
else:
    print("Sorry, you got that wrong")

answer = input("Who makes the Camaro? ")

if answer.lower() == "chevrolet":
    print("Correct!")
    score += 1
else:
    print("Sorry, you got that wrong")

answer = input("What website has videos? ")

if answer.lower() == "youtube":
    print("Correct!")
    score += 1
else:
    print("Sorry, you got that wrong")

print("Your score is: " + str(score) + " questions right!")
