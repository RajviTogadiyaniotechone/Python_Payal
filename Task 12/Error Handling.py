#Error handling in the python refers to the error can be handled by the user whether is the user defied or the 
#  by the code it is generate.
# error can be handled by the Try, Except and Finally block
# THE Try block will the test the error of the code and create exception
# Except block handles the error
# Fianally block let execute the code regardless of the result of the try- and except blocks.
# it may refer to the concept that user know that this block of code might give the error in the future 
# so to overcome that error in the future error handling is useful


a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")


