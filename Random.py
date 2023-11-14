#https://replit.com/@MariaMartin8/Random-game?s=app 
import random
number=random.randint(1,10)
attempt=0
while attempt<3:
  attempt+=1
  guess=int(input("guess a number between 1 and 10 "))
  if guess == number:
    print(f"You win! you did it in {attempt} attempts!")
    break
print("I'm sorry, you lost because you ran out of attempts, try again!")
