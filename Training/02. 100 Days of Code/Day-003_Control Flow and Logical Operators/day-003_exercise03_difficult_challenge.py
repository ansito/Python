# Exercise 3: Leap Year

# input year
year = int(input("Which year do you want to check? "))

# check the year is leap or not leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")