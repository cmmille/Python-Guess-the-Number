from art import logo
import random

print(logo)

difficulty = input("'Easy' or 'Hard' mode?\t").lower()
if difficulty == "easy":
  num_guesses = 10
else:
  num_guesses = 5

random_num = random.randint(2, 101)
print("I'm thinking of a number between 1 and 100...")

game_over = False
while not game_over:
  user_guess = int(input("\nWhat number am I thinking of?\t"))

  if random_num == user_guess:
    print("You Win!")
    game_over = True
  elif random_num > user_guess:
    num_guesses-=1
    print(f"{num_guesses} guesses remaining...")
    print("Higher...")
  else:
    num_guesses-=1
    print(f"{num_guesses} guesses remaining...")
    print("Lower...")

  if num_guesses <= 0:
    print("Sorry, you lose.")
    print(f"I was thinking of {random_num}...")
    game_over = True