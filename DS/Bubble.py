# Bubble Sort

li=[]

num =int(input("ENter the number of elements:"))

print(f"Enter {num} values:")

for k in range(num):
    li.append(int(input()))

#li = [10, 50, 77, 40, 55, 96, 7]

print("Unsorted List is:",li)

for j in range(len(li)-1,0,-1):

    for i in range(j):

        if li[i] > li[i+1]:

            li[i], li[i+1] = li[i+1], li[i]

        else:

            print(li)

    print(li)

print()

print("Sorted List is:",li)
