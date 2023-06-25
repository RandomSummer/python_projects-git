#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import finale
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_number(number, number1, turns): 
  # print(number1)
  if number == number1:
    print(f"You got it! The answer was {number}.")
  elif number > number1:
    print("Too high!")
    return turns-1
  else:
    print("Too low!")
    return turns-1

def set_difficulty():
  get_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if get_mode == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL
    
end_of_game = False

number = random.randint(1, 101)

def game():
  print(finale)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 to 100.")
  
  turn = set_difficulty()
  
  guess = 0 
  
  while guess != number:
    print(f"you've {turn} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turn = check_number(guess, number1=number, turns=turn)
  
    if turn == 0:
      print("You've run out of guesses, you lose!")
      return
    elif guess != number:
      print("Guess again.")

game()
