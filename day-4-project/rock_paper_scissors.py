import random as rm

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
option = [rock, paper, scissors]

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

if user_choose >= 3 or user_choose < 0:
    print("You typed an invalid number, You Lose!")
else:
    print("You choose :")
    print(option[user_choose])

    computer_choice = rm.randint(0, 2)

    print("Computer choose :")
    print(option[computer_choice])
    if user_choose == 0 and computer_choice == 2:
        print("You Win!")
    elif user_choose == 2 and computer_choice == 0:
        print("You Lose!")
    elif computer_choice > user_choose:
        print("You Lose!")
    elif user_choose > computer_choice:
        print("You Win!")
    elif user_choose == computer_choice:
        print("It's a draw")

