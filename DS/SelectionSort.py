# Selection Sort

Array =[]

num =int(input("ENter the number of elements:"))

print(f"Enter {num} values:")

for k in range(num):
    Array.append(int(input()))

#Array = [15, 6, 10, 7, 25]
print("Unsorted List is:", Array)

for i in range(len(Array)):

    min_index = i

    for j in range(i+1, len(Array)):

        if Array[min_index] > Array[j]:
            
            min_index = j
    
    Array[i], Array[min_index] = Array[min_index], Array[i]

    print(Array)
