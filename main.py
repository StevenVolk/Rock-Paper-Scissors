import random

def rockPaperScissors():
	moves = {"R": "Rock", "P": "Paper", "S": "Scissors"}
	option = ["R", "P", "S"]
	CPU = random.choice(option)

	while True:
		player = input("'R' for 'rock', 'P' for 'paper' & 'S' \
for 'scissors'\nPick an option between 'R', 'P' or 'S': ")
		if player == "R" or player == "P" or player == "S":
			break
		print("Error: Selected a wrong option; try again")

	print("Player({0}) : CPU({1})".format(moves[player], moves[CPU]))

	if CPU == player:
		print("It is a tie")
		rockPaperScissors()

	elif (player == "R" and CPU == "S") or (player == "P" and CPU == "R")\
 or (player == "S" and CPU == "P"):
		print("Player wins")

	else:
		print("CPU wins")

rockPaperScissors()