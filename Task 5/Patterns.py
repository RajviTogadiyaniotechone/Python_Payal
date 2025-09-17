
#1 Simple * Pattern Pyramid

rows = int(input("Enter the number of rows: "))  

for i in range(0, rows):
    for j in range(0, i+1):
        print("* ",end=" ")
    print(); 


#2 Simple Alphabet Pyramid

rows = int(input("Enter the number of rows: "))  

for i in range(rows+1):
    for j in range(i):
        print(i,end=" ")
    print(); 

#3 Simple Inverted * Pattern Pyramid

rows = int(input("Enter the number of rows: "))  
aasci_value = 65;
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(aasci_value);
        print(alphabet,end=" ")
    aasci_value += 1;
    print(); 


#4 Simple Inverted Number Pyramid

rows = int(input("Enter the number of rows: "));

for i in range(rows+1, 0 ,-1):
    for j in range(0, i-1):
        print("* ",end=" ")
    print(); 


#5 Simple Inverted Number Pyramid in Descending Order

rows = int(input("Enter the number of rows: "));

for i in range(rows+1, 0 ,-1):
    num = i;
    for j in range(0, i):
        print(num ,end=" ")
    print();


#6 Simple Inverted Pyramid of a Digit

rows = int(input("Enter the number of rows: "));
num = rows;
for i in range(rows, 0 ,-1):
    for j in range(0, i):
        print(num ,end=" ")
    print(); 

#7 Number Pattern Mirrored Semi-Pyramid


rows = int(input("Enter the number of rows: "));

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j ,end=" ")
    print(); 


#8 Number Pattern Mirrored Semi-Pyramid

rows = int(input("Enter the number of rows: "));

for i in range(1, rows+1):
    num = 1;
    for j in range(rows, 0, -1):
        if j>i:
            print(" ",end="")
        else:
            print(num, end=" ");
            num += 1;
    print()  


#9 Number Pattern Inverted Semi-Pyramid

rows = int(input("Enter the number of rows: "));

for i in range(rows, 0, -1):
    for j in range(0, i+1):
        print(j,end="")
        
    print() 

#10 Reverse Number Pyramid

rows = int(input("Enter the number of rows: "));

for i in range(1, rows+1):
    for j in range(i,0,-1):
        print(j,end="")
        
    print() 

#11 Natural Number Pyramid

num = 1;
stop = 2;

rows = int(input("Enter the number of rows: "));

for i in range(rows):
    for j in range(1, stop):
        print(num,end=" ")
        num += 1;
        
    print() 
    stop += 2;


#12 Palindrome Number Pyramid

num = 1;
rows = int(input("Enter the number of rows: "));

for i in range(1, rows+1):
    for j in range(1, i-1):
        print(j, end=" ")
        num += 1;
    for j in range(i-1,0,-1):
        print(j,end=" ")
        
    print();

#13 Alternate/Odd Number Pyramid

rows = int(input("Enter the number of rows: "))  
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print((i * 2-1), end=" ")
        j += 1
    i +=  1

    print()

#14 Even Number Pyramid in Descending Order

rows = int(input("Enter the number of rows: "))  
lastnum = 2 * rows
even = lastnum

#Outer for loop to handle number of rows  
for i in range(1, rows+1):  
  even = lastnum
  for j in range(i): 
    print(even, end=" ")     
    even -= 2  
  print()