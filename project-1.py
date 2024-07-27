import random

def number_guessing_game():
  """Number guessing game."""
  number = random.randint(1, 10)
  guess = None
  attempts = 0

  while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess < number:
      print("Too low!")
    elif guess > number:
      print("Too high!")

  print(f"Congratulations! You guessed the number in {attempts} attempts.")

if __name__ == "__main__":
  number_guessing_game()
