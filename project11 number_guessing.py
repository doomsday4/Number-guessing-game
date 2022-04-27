import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

diff = input("Choose difficulty. Type 'easy' or 'hard': ")
if diff == "easy":
  attempts = 10
elif diff == "hard":
  attempts = 5
else:
  print("Invalid Input.")

while attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  attempts -= 1
  if guess == number:
    print(f"You Won! And you have {attempts} attempts remaining.")
    break
  elif guess > number:
    print("Too High")
  elif guess < number:
    print("Too Low.")

  if attempts == 0:
    print(f"You loose. The number was {number}. Better Luck next time.")
