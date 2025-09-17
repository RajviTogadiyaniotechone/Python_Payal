# Swap two variables using tuple unpacking. 

t1 = ("India", "USA", "Canada", "Singapore")

print(t1)

a, b, c, d = t1

print("before unpacking>>",a)
print("before unpacking>>",b)

a,b = b,a

print("after unpacking>>",a)
print("after unpacking>>",b)