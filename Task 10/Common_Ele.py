# Write a program to find common elements in two lists using sets.

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

# Find common elements using set intersection
common = list(set(a) & set(b))

print(common)

