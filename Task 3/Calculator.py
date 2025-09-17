# Write a simple calculator program

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    if b == 0:
        return "Error! Division by Zero"
    return a / b

def Calculator():
    print("Select Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

   # if choice not in ['1', '2', '3','4']:
   # print("Invalid choice!! please enter a chioce between (1/2/3/4)")
   #     continue;

    num1 = int(input("Enter First number: "))
    num2 = int(input("Enter Second number: "))

  
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multi(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divi(num1, num2)}")
    else:
        print("Invalid input!")

if __name__ == "__main__":
    Calculator()
