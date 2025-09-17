# Functions are the block of code that executed when they are called.
# Functions are the built-in or user defined.

def fun():
    print("Hello Python!");


fun();
# four types of arguments
#1. Default Arguments

def num(a,b=10):
    print("a is",a)
    print("b is",b)

num(5)

#2. Keyword Arguments 
def employee(firstname, lastname):
    print(firstname, lastname)

employee(lastname="last",firstname="")

#3. positional Arguments 

def name(city,country):
    print("city is::",city)
    print("country is::",country)

name("rajkot","India")
name("India","Rajkot")

#4. Arbitary Arguments

print("Arbitary Arguments>>>>>>")

def myFun(*arg):
    for ar in arg:
        print(ar)

myFun('Hello', 'hi', 'hey', 'hola')


def sum_all(*args):
	result = 0
	for num in args:
		result += num
	return result

print("Arbitary Keyword Arguments>>>>>>")


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun(first='one', mid='two', last='three')

print(sum_all(1, 2, 3, 4, 5))

#positional arguments and keyword arguments

def print_args_and_kwargs(*args, **kwargs):
	print("Positional arguments:")
	for arg in args:
		print(arg)
	
	print("Keyword arguments:")
	for key, value in kwargs.items():
		print(f"{key}: {value}")

print_args_and_kwargs(1, 2, 3, name="Joey", age=123)

