# Write a function that returns the square of a number
number = input("Enter a Number:: ");

def sqnum(number):
    print("This function returns the the square of the number:")
    return number**2;

ob = sqnum(number);
print("The square of the {number} is",ob)