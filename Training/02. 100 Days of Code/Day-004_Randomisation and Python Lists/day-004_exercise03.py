# Exercise 3 - Treasure Map

# Initiation
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map_list = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# split the string input to be a list
position = list(position)

# store the value of the position[1] into y as a row
# then convert it to int
y = int(position[1])

# store the value of the position[0] into x as a column
# then convert it to int
x = int(position[0])

# change the coordinate input x,y into "X"
map_list[y - 1][x - 1] = "X"

# update the map current condition
print(f"{row1}\n{row2}\n{row3}")
