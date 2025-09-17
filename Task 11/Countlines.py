# Write a program to count the number of lines in a file.

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read all lines into a list
            return len(lines) 
    except FileNotFoundError:
        return "The file was not found."
    except Exception as e:
        return str(e)


file_path = 'D:\Payal Ramani\Task 11\Demo.txt' 


line_count = count_lines_in_file(file_path)
print(f"Number of lines in the file: {line_count}")
