#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill? "))
cal_percent = (percent/100)*bill
total_bill = bill + cal_percent
per_head = round(total_bill/person,2)
# per_head = ':.2f'.format(total_bill/person)

print(f"Each person should pay: ${per_head}")