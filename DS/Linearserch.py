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

def Linear_search(a, n, Key):
    for i in range(n):
        if a[i] == Key:
            return i  
    return -1  

Result = Linear_search(a, n, Key)

if Result == -1:
    print("Element not found.")
else:
    print(f"Element found at index {Result}.")
