# User defined Module

import Modules_and_Libraries

print("Multiply>>",Modules_and_Libraries.multi(10,5))

print("Sum>>",Modules_and_Libraries.add(102567,145879))

# import function from the module to direct use
from Modules_and_Libraries import greet

print(greet("Hello"))

# Rename Module
import Modules_and_Libraries as ML

print(ML.greet("Payal"))

print("\n")
print("-----------------------------------------------")
# Math Module  ==>
from math import *

print("Square root>> ",sqrt(10))
print("Factorial>> ",factorial(5))
print("Power of the number: ",pow(2,3))
print("Absolute vale of x: ",fabs(-7))
print("Smallest integer greater than or equal to x: ",ceil(7.7))
print("Largest integer amaller than or equal to x: ",floor(4.5))
print("sin of x: ",sin(pi/2))
print("value of pi:",pi)
print("Euler's number:",e)
print("Tangent of x (x is in radians)",tan(pi / 4))  # Output: 1.0
print("Convert degrees in to radians: ",radians(180))  # Output: 3.141592653589793
print("Convert radiants into degrees: ",degrees(pi))  # Output: 180.0
print("Logaritham of x with a given base: ",log(100, 10))  # Output: 2.0 (log base 10 of 100)
print("Logarithm of x with base 10",log10(100))  # Output: 2.0
print("Logaritham of x base 2: ",log2(16))  # Output: 4.0
print("Greatstest common divisor of a and b: ",gcd(56, 98))  # Output: 14
print("Hypotenuse of a right triangle, sqrt(x^2 + y^2)",hypot(3, 4))  # Output: 5.0
print("Gamma Function: ",gamma(5))  # Output: 24.0 (Gamma(5) = 4! = 24)
print("Error Function: ",erf(1))  # Output: 0.8427007929497149


d = dir(ML)
print(d)

print("\n")
print("------------------------------")

# Calculation of the Area of the circle using math module
import math
radius = 5;
area = math.pi * math.pow(radius, 2)
print(f"ARea of the circle {area}")


