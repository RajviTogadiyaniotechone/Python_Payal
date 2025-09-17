# lists are the ordered sequence of the array in python we don't have array we have lists instand.
# lists are changeble, ordered and allow duplicates.

l1 = ["Winter","Summer","Monsoon"]

print("\n")

print("index starting from the lastof the lists>>",l1[-1])

print("\n")

print(l1[0:])
print(l1[:1])

print("\n")

print("List>>>",l1)
print("Length>>",len(l1))
print("type >>",type(l1))

print("\n")

print(l1[1])

print("\n")

for i in l1:
    print(i)

#swap Lists
print("\n")
l1[2] = l1[0]
print(l1[2])
print(l1)

#change list directly
l1[2] = "Monsoon"
print(l1)

l1.append("Red")
print("After append>>",l1)

l1.insert(0,"blue")
print("After insert>>",l1)

l1.extend(["white","purple"])
print("After Extend>>",l1)

l1.insert(0,"winter")
print(l1)

l1.remove("winter")   #removes first occurrence of the element
print(l1)

popped_element = l1.pop(4)
print("popped element>>",popped_element)
print("After element is popped>>",l1)

del l1[5]
print("After deletation>>>",l1)

#Swapping Lists

l1[0] , l1[1] = l1[1] , l1[0]
print(l1)

l1.insert(3, "Orenge")
print(l1)
#NEsted lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print("value position at the given index is>>",matrix[1][2])

print("\n")
#Python List Slicing Syntax
#list_name[start : end : step]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:4])

e = a[-8:-1:2]
print(e)