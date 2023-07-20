# Exercise 2: High Score

# prompt user input student scores
student_scores = input("Input a list of student scores ").split()

# do loop to convert the input string to integer
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# variable to store the largest score
highest_score = 0

# do loop for checking each scores
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
