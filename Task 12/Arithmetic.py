# Arithmetic Error

'''try:
    ans = "100" / 50

except ArithmeticError:
    print("Arithmetic Error")

except:
    print("Something Went Wrong!!")
'''

number = 7;
if number > 5:
    raise Exception("Number should be greater than 5")
print(number)