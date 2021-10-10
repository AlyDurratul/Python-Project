import random

def guess(x):
  random_number = random.randint(1, x)
  guess = 10
  while guess != random_number:
   guess = int(input(f"Guess a number between 1  and  {x}: "))
   if guess < random_number:
    print("Sorry, guess again. Too slow ")
   elif guess > random_number:
    print("Sorry, guess again. Too high ")
    
  print(f"Yay, congrates. You have guessed the number{random_number} correctly" )

guess(10)