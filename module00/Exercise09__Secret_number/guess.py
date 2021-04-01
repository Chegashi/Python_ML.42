import random

msg = "This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n"
print(msg)
number = random.randint(1,99)
rep = input("What's your guess between 1 and 99?\n>>")
steps = 1
while rep != 'exit':
	if not rep.isdigit():
		print("That's not a number.")
	elif number < int(rep):
		print("Too high!")
	elif  number > int(rep):
		print("Too low!")
	else:
		print("Congratulations, you've got it!\nYou won in", steps, " attempts!")
		break
	rep = input("What's your guess between 1 and 99?\n>>")
	steps += 1
