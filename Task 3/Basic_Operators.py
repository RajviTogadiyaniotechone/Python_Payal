#OPerators are the special symbol used to perform specific operation on one or more operands.

a = 10;
b = 5;

#1. Arithmatic Operators
print("sum: ",a+b);
print("substaction: ",a-b);
print("multiplication: ",a*b);
print("division: ",a/b);
print("floor division: ",a//b);
print("power: ",a**b);
print("modulo: ",a%b);

print("\n")

#2. Assignment operator
a += b;
print("Addition Assignment: ",a);
a -= b;
print("substraction Assignment: ",a);
a *= b;
print("multiplication Assignment: ",a);
a /= b;
print("division Assignment: ",a);
a %= b;
print("renainder Assignment: ",a);
a **= b;
print("exponent Assignment: ",a);

print("\n");

#3. comparision operator
a=10;
print("equality operator: ", a==b);
print("inquality operator: ",a!=b);
print("greater operator: ",a>b);
print("lesser operator: ",a<b);
print("greater than equal to: ",a>=b);
print("less than equal to: ",a<=b);

print("\n")

#4. logical operator
print("Logical AND:",(a > b) and (b >= 2))
print("Logical OR:",(a > b) or (b >= 7))
print("Logical NOT:",not(a > b) and (b >= 2))   #Reverse the result, returns False if the result is true

print("\n")

#5. Identity operator
x = ['one', 'two']
y = ['one', 'three']
z = x;

print(x is z)
print(x is y)
print(x is not y)

print("one" in y)
print("three" is not x)



