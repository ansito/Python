# Exercise 5 - Love Calculator

print("Welcome to the Love Calculator!")

# receive the input name
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# use lower() function to lower case name1 and name2
name1 = name1.lower()
name2 = name2.lower()

# concat name1 and name2
concat_name = name1 + name2

# check each char TRUE on concat_name
value_t = concat_name.count("t")
value_r = concat_name.count("r")
value_u = concat_name.count("u")
value_e = concat_name.count("e")

# count the TRUE similar char
value_true = value_t + value_r + value_u + value_e

# check each char LOVE on concat_name
value_l = concat_name.count("l")
value_o = concat_name.count("o")
value_v = concat_name.count("v")
value_e = concat_name.count("e")

# count the LOVE similar char
value_love = value_l + value_o + value_v + value_e

# combine char_for_true and char_for_love
score = str(value_true) + str(value_love)
score = int(score)

# print out the percentage of love
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")
