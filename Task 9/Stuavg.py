# # Write a program to find the average grade of all students.

students = {
    "student1" : [90, 85, 99],
    "student2" : [99, 79, 88],
    "student3" : [89, 98, 99],
    "student4" : [87, 89, 99]
}

total_grades = 0
total_count = 0

for grades in students.values():
    total_grades += sum(grades)  
    total_count += len(grades)  

# Calculate average grade
average_grade = total_grades / total_count

print(f"The average grade of all students is: {average_grade:.2f}")
