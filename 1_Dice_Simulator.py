#dice simulator python project
import random
def roll():
	#returns a random number between 1 and 6 inclusive
	random_num = random.randint(1,6)
	return random_num
print(roll())
