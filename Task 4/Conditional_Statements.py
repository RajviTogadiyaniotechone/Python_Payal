# COnditional statements are the statements in python which is not executed untill specific condition is satisfied.
# the flow of the python programe is decided on the basis of the condition of the program.

#IF statement

if 10 > 7:
    print("10 is greater.")

print("\n");

a = 33;
b = 77;

if a>b:
    print("a is greater than b");
else:
    print("a is not greater than b");

print("\n");

x = 10;
y = 20;

print("x is greater") if x > y else print("y is greater");

print("\n");

#AND
a = 33;
b = 77;
c = 100;

if b>a and c>a:
    print("both condition is true")

print("\n");

#OR

if a>b or c>a:
    print("one of the condition is true");

print("\n");

#NOT

if not a>b:
    print("a is not greater than b");

print("\n");

# greater number program
n1 = 10;
n2 = 20;
n3 = -30;

if n1>n2:
    if n1>n3:
        print("n1 is greater>",n1);
elif n2 > n1:
    if n2 > n3:
        print("n2 is greater>",n2);
    else:
        print("n3 is greater>",n3);

