# Write a program to perform union and intersection operations on sets.

m1 = set(("January", "February", "March", "April"))
m2 = set(("February", "May", "June", "January"))

u = m1.union(m2)
print("Union>>>",u)

i = m1.intersection(m2)
print("intersecion>>",i)