# Exercise 1: Average Height

# prompt user input
student_heights = input("Input a list of student heights ").split()

# do loop for convert the input string into integer in the list

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


# do loop for calculate the sum of input number list, and get the total member of list
total_height = 0
number_of_students = 0

for height in student_heights:
    total_height += height

for student in student_heights:
    number_of_students += 1

# count the average number
average_heights = round(total_height / number_of_students)
print(average_heights)
