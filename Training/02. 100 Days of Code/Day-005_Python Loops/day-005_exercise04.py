# Exercise 4: The FizzBuzz Job Interview Question

# do loop for generate number 1 to 100
for number in range(1, 101):

    # if FizzBuzz
    if number % 15 == 0:
        print("FizzBuzz")

    # if Buzz
    elif number % 5 == 0:
        print("Buzz")

    # if Fizz
    elif number % 3 == 0:
        print("Fizz")

    # else print number
    else:
        print(number)
