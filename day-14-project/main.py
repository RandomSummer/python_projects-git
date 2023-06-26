from art import logo,vs
from game_data import data
import random


def generate_data(): 
  """get randomly generated account"""
  return random.choice(data)


def format_data(account):
  
  name = account["name"]
  desc = account["description"]
  country = account["country"]
  return f"{name} a {desc} from {country}."


def check_follower(guess, follow_1, follow_2):
  if follow_1 > follow_2:
    return guess == "a"
  else:
    return guess == "b"


def game():
  
  print(logo)
  score = 0
  should_continue_game = True
  account_1 = generate_data()
  account_2 = generate_data()
  
  while should_continue_game:
    account_1 = account_2
    account_2 = generate_data()

  while account_1 == account_2:
    account_2 = generate_data()

  print(f"Compare A: {format_data(account_1)}.")
  print(vs)
  print(f"Compare A: {format_data(account_1)}.")

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  follower_count_1 = account_1["follower_count"]
  follower_count_2 = account_2["follower_count"]
  is_correct = check_follower(guess, follower_count_1, follower_count_2)

  print(logo)
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")

game()