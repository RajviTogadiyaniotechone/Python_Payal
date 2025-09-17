# Write a for loop that prints a multiplication table for a given number.


number = int(input("Enter a Number to print multiplication table: "));

for i in range(1,11):
    ans = number * i
    print(f"{number} x {i} = {ans}")



