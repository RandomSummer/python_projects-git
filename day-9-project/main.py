# from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid}")


new_dic = {}
bidding_finished = False

while not bidding_finished:
  bidder = input("What's your name?: ")
  bid = int(input("What's your bid?: $"))
  new_dic[bidder] = bid
  should_continue = input("Are there any other bidder? Type 'yes' or 'no'.\n").lower()
  if should_continue == "no":
    highest_bidder(bidding_record = new_dic)
    bidding_finished = True
  elif should_continue == "yes":
    # clear()
    pass
    
