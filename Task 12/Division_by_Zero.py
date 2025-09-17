# Create a program that divides two numbers and handles division by zero.

try:
    a = 0;
    b = 10;
    c = a/b;
    ans = 100/c

except ZeroDivisionError:
    print("You Can't divide by Zero!")

else:
    print("Result is>>>",ans)

finally:
    print("Execution Completed.")
