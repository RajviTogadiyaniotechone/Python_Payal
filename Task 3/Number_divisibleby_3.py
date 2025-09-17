# Write a program that checks if a number is divisible by 3.

num = int(input("Enter number: "))

def num_diviby_3(num):
    if num % 3 == 0:
        return True;
    else:
        return False;

if num_diviby_3(num):
    print(" Number is divisible by 3");
else:
    print("Number is not divisible by 3");

