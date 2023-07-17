# Project - Tip Calculator

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

num_person = int(input("How many people to split the bill? "))

# calculation
# calculate the tip
sum_tip = float(total_bill * percentage_tip/100)

# calculate the split bill for each people
new_total_bill = float(total_bill + sum_tip)

split_bill = float(new_total_bill / num_person)
bill = round(split_bill, 2)

# print out 2 decimal after comma
bill = "{:.2f}".format(bill)

# print out for each person should pay
print(f"Each person should pay: ${bill}")
