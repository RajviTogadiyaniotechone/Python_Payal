# OS for operating system and perform operations repalted to the file systems and processess

# get the current working directory
import os
print(os.getcwd())

#change the current working directory to a specified path
os.chdir("D:\Payal Ramani\Task 13\Os")

# to list all the files and current directory in the given path
print(os.listdir("D:\Payal Ramani\Task 13\Os"))

#os.mkdir("New_Directory")

#os.makedirs("parent/child")

# to remove a file in the directory
# os.remove("abc.txt")

# to remove the directory in the file
#os.rmdir("new_directory")
#os.rmdir("abc")

#os.removedirs("parent/child")

# check if the file is exist or not
print(os.path.exists("Os"))

# rename the file directory
#os.rename("old_name.txt", "new_name.txt")

print(os.path.join("folder", "subfolder","file.txt"))

print(os.path.basename("D:\Payal Ramani\Task 13\Os\file.txt"))

print("dirname>>",os.path.dirname("D:\Payal Ramani\Task 13\Os\file.txt"))  # Output: /home/user

print("Absolute path::",os.path.isabs("D:\Payal Ramani\Task 13\Os\file.txt"))

print("spite the text from the extention::", os.path.splitext("file.txt"))

print("Get the environment variable::",os.getenv("HOME"))

os.system("ls")  # This will list files in the current directory

os.exit(0)  # Exit with a success status
