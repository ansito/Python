# Exercise 3: Adding Even Numbers

# do loop to generate number from 1 to 101.
# If we want to take the number 100, so it should be end of the range is 101.

# assign variable for total_even_number
total_even_number = 0


for number in range(1, 101):
    # check if the number is even
    if number % 2 == 0:
        total_even_number += number

# print out the total even number in range 1 to 100
print(total_even_number)
