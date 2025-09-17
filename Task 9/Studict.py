# Create a dictionary with student names as keys and grades as values, 
# then print the grade of a specific student

student = {
    "student1" : [90,85,99],
    "student2" : [99,79,88],
    "student3" : [89,98,99],
    "student4" : [87,89,99]
}

print(type(student))

print(student)

a = student["student1"]
print("Grade of the student 1 is>>",a)

d = student["student4"]
print("Grade of the student 4 is>>",d)

# Add a new student and grade to the dictionary

student["student5"] = 100

print(student)


