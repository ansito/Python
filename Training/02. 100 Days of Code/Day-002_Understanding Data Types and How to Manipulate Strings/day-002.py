# Data Types

# String

print("Hello"[0])
print("Hello"[4])
print("Hello"[-1])
print("Hello"[::2])

# Integer
# 123
num = 123

# Float
# 3.14159
mystery = 734_529.678
print(type(mystery))

# Boolean
# True or False
has_eaten = True

# Type Error, Type Checking, and Type Conversion
num_char = len(input("What is your name?"))
print(type(num_char))
# Type Conversion, int to string
new_num_char = str(num_char)
print(type(new_num_char))
# Type Conversion, int to float
a = float(123)
print(type(a))
# Type Conversion, string to float
print(70 + float("100.5"))
# Type Conversion, int to string
print(str(70) + str(100))
print("\n")

# Exercise 1 - Data Types
two_digit_number = input("Type a two digit number: ")

print(int(two_digit_number[0]) + int(two_digit_number[1]))
print("\n")

# Exercise 2 - BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

print(int(int(weight) / float(height) ** 2))
print("\n")

# Exercise 3 - Life in Weeks
age = input("What is your current age? ")
years_remaining = 90 - int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
print("\n")
