import os

# Get current working directory
print("Current Directory:", os.getcwd())

# Create a new directory
os.mkdir("new_folder")

# Change directory
os.chdir("new_folder")
print("New Directory:", os.getcwd())

# Create a file and remove it
with open("sample.txt", "w") as file:
    file.write("Hello, World!")

# Check if file exists
if os.path.exists("sample.txt"):
    print("File exists!")

# Remove the file
os.remove("sample.txt")
