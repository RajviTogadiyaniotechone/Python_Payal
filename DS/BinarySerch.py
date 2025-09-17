# List to store the elements
a = []

# Element Input
n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))  
    a.append(element)

print("List:", a)

# Key to Search
Key = int(input("Enter a Search Element: ")) 

def Binary_Serch(a, n):
    low = 0
    high = len(a) - 1
    mid = 0

    while(low <= high):
        mid = (high + low)//2

        if(a[mid] == Key):
            return mid
        
        elif(a[mid] < n):
            low = mid + 1
            
        else:
            high = mid - 1
    return -1

Result = Binary_Serch(a, n)

if Result == -1:
    print("Element not found.")
else:
    print(f"Element found at index {Result}.")