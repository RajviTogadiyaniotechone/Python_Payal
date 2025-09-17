# File handling is for to handle the file operation like add, append, read, write, open, delete files.
# x for create the file
# w for write the file
# r for read the file
# o for the open the file
# a for append the file
# b for binary mode
# t for the text mode


# create a empty text file
# in current directory
#fp = open('sales.txt', 'x')
#fp.close()


#this can write a file in the directory
fp = open('sales_2.txt', 'w')
fp.write("First Line")
fp.close()

# to reach the current directory of the file
import os
print(os.listdir())
print(os.path.isdir("Sales.txt"))

# Append lethod for the add a new line in the file
fp = open("sales.txt", 'a')
fp.write("This is the added line by the append method \n")

# to read the file
fp = open("sales.txt", 'r')
print(fp.read())
fp.close()

fp = open("sales.txt", 'a')
fp.write("\n Hello After append")

# to read the file
fp = open("sales.txt", 'r')
print(fp.read())
fp.close()