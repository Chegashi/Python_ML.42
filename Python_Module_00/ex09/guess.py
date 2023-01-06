import random

print("This is an interactive guessing game!\n", end='')
print("You have to enter a number between 1 and 99 to find out the ", end='')
print("secret number.\nType 'exit' to end the game.\nGood luck!\n")
number = random.randint(1, 99)
rep = input("What's your guess between 1 and 99?\n>>")
steps = 1
while rep != 'exit':
    if not rep.isdigit():
        print("That's not a number.")
    elif number < int(rep):
        print("Too high!")
    elif number > int(rep):
        print("Too low!")
    else:
        if (number == int(rep)):
            print("The answer to the ultimate question of life,", end='')
            print("the universe and everything is 42.")
        if (steps == 1):
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!", end='')
            print("You won in {} attempts!steps, ".format(steps))
        break
    rep = input("What's your guess between 1 and 99?\n>>")
    steps += 1
