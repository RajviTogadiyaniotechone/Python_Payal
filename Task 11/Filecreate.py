# Write a program to create a text file and write some content to it. 

import os

filepath = "D:\Payal Ramani\Task 11"
filename = "Demo.txt"

with open(os.path.join("D:\Payal Ramani\Task 11", "Demo.txt"),'w') as fp:
    fp.write(" This is the Some content in the file")
    print("created")

# Read the content of a file and print it. 

fp = open("D:\Payal Ramani\Task 11\Demo.txt", 'r')
print("this is the content from demo.txt by r method>> \n",fp.read())
   