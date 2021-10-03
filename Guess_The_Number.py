#  progame to guess a number within a 
#  range in limited number of attempts
import random
def guess(x):
 random_num = random.randint(1,x)
 i = 0
 #  player gets n/2 +1 chances if range 
 #  was 6 player gets 4 chances
 while i != int(x/2)+1:
  if int(input()) == random_num:
   print("Congratulations!! You guessed right.")
   break
  else:
   if i==int(x/2):
    print("Sorry!! You are OUT OF CHANCES")
   else:
    print("Wrong guess!\n"+str(int(x/2)-i)+" chances left.")
  i += 1
#Enter range of numbers
num=int(input("Enter number range from 1 to "))
#Guess the number
print("Guess a number...")
guess(num)
