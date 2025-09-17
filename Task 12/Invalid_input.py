# Write a program that handles invalid input by using try and except blocks. 

def get_num():
    while True:
        try:
            user_input = input("Enter a number>>")
            number = float(user_input)
            return number;

        except ValueError:
            print("Invalid Input! Please Enter a valid Number")

number = get_num()
print("Your entered Number is>>",number)
