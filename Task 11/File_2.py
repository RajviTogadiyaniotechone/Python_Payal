# create a file at a specific location

'''import os

file_path = 'D:\Payal Ramani\Task 11'
file_name = "computer.txt"

with open(os.path.join('D:\Payal Ramani\Task 11','computer.txt'), 'w') as fp:
    fp.write("Hello!")
'''


#Create a file with a Datetime

from datetime import datetime

x = datetime.now()

# Writing to 'Date.txt'
date_time = x.strftime('%d-%m-%y.txt')
with open('Date.txt', 'w') as fp:
    fp.write('created ' + date_time)  # Concatenating the string
    print('created ' + date_time)


# Writing to 'Date2.txt'
date_time_2 = x.strftime('%d-%m-%y-%H-%M-%S.txt')
with open('Date2.txt', 'w') as fp:
    fp.write('created ' + date_time_2)  # Concatenating the string
    print('created ' + date_time_2)


# Writing to 'Date3.txt' with correct file path
date_time_3 = "D:\\Payal Ramani\\Task 11\\" + x.strftime('%d-%m-%y-%H-%M-%S.txt')
with open('Date3.txt', 'w') as fp:
    fp.write('created ' + date_time_3)  # Concatenating the string
    print('created ' + date_time_3)

