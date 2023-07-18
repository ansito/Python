# Project: Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# question 1
choice_1 = input('You\'re at a cross road. '
                 'Where do you want to go? Type "left" or "right" \n').lower()

if choice_1 == "left":

    # question 2
    choice_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait"'
                     'for a boat. Type "swim" to swim across. \n').lower()

    if choice_2 == "wait":

        # question 3
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. "
                         "One read, one yellow, and one blue. "
                         "Which colour do you choose? \n").lower()

        if choice_3 == "blue":
            print("You enter a room which full of beasts. You are eaten by them."
                  "Game over!")

        elif choice_3 == "red":
            print("You enter a room which full of fire. You are burned by fire."
                  "Game over!")

        elif choice_3 == "yellow":
            print("You enter a room of Treasure. Congratulations, You WIN.!")

        else:
            print("Game over!")

    else:
        print("You are attacked by trout. Game over!")

else:
    print("Fall into a hole. Game over!")
