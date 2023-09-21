#Number Guessing Game Objectives:

# Include an ASCII art logo.
import random
from art import logo



def difficulty_level(choice):
  if choice == 'easy':
    choice = 10
    return choice
  elif choice == 'hard':
    choice = 5
    return choice


def main():
  number_guessing = random.randint(1,101)
  
  game_over = False
  print(logo)
  print("welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  print(f"Psssttt, the answer is {number_guessing}")
  difficulty = input("Choose the difficulty. Type 'easy' or 'hard': ")
  attempts = difficulty_level(difficulty)
  
# Allow the player to submit a guess for a number between 1 and 100.
  while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number")
    player_guess = int(input("Make a guess: "))
    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
    if player_guess != number_guessing and player_guess > number_guessing:
      print("Too high")
      # Track the number of turns remaining.
      attempts -= 1
    elif player_guess != number_guessing and player_guess <  number_guessing:
      print("Too low")
      # Track the number of turns remaining.
      attempts -= 1
      if attempts == 0:
        game_over = True
        # If they run out of turns, provide feedback to the player. 
        print("You've run out of guesses, you lost")
    else:
      # If they got the answer correct, show the actual answer to the player.
      game_over = True
      print(f"You won! The correct answer is {number_guessing}.")
  




# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

if __name__ == "__main__":
  main()