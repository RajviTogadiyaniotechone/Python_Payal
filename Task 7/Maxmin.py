# Write a program to find the maximum and minimum values in a list.

a = [10, 55, 95, 7, 73, 23]

maximum = max(a)
print("Maximum in a list is >>",maximum)

minimum = min(a)
print("Minimum in a list is >>",minimum)

print("-------------------")

# largest in other way
largest = a[0]

for val in a:
    if val > largest:

        largest = val

print(largest)

print("-------------------")

from functools import reduce

# Find the largest number using reduce
largest = reduce(lambda x, y: x if x > y else y, a)

print(largest)

print("-------------------")
