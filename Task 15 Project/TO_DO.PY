# TO DO LIST APPLICATION

import os

# Function to add a task to the list
def Add_task(Task):
    new_task = input("Enter Task: ")
    Task.append(new_task)
    print(f"{new_task} is added.\n")

# Function to display the tasks
def Display_task(Task):
    if len(Task) == 0:
        print("No task has been added to the list.")
    else:
        for idx, task_item in enumerate(Task, 1):
            print(f"{idx}. {task_item}")
    print()

# Function to edit a task
def Edit_task(Task):
    Display_task(Task)
    try:
        task_index = int(input("Enter a Task Number to Edit: ")) - 1
        if 0 <= task_index < len(Task):
            new_task = input(f"Update the task (currently '{Task[task_index]}'): ")
            Task[task_index] = new_task
            print(f"Updated Task: {new_task}\n")
        else:
            print("Invalid Task Number!\n")
    except ValueError:
        print("Invalid Value Input. Please Enter a valid Task Number.\n")

# Function to delete a task
def Delete_task(Task):
    Display_task(Task)
    try:
        task_index = int(input("Enter a Task Number to Delete: ")) - 1
        if 0 <= task_index < len(Task):
            removed_task = Task.pop(task_index)
            print(f"'{removed_task}' has been removed.\n")
        else:
            print("Invalid Task Number!\n")
    except ValueError:
        print("Invalid Value Input. Please Enter a valid Task Number.\n")

# Main function for the To-Do List application
def To_do_list_application():
    Task = []

    while True:
        print("------To-Do-List-Application--------")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Display Tasks")
        print("4. Delete Task")
        print("5. Exit")
        print("-----------------")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            Add_task(Task)
        elif choice == "2":
            Edit_task(Task)
        elif choice == "3":
            Display_task(Task)
        elif choice == "4":
            Delete_task(Task)
        elif choice == "5":
            print("Exiting the application. Thank You.")
            break
        else:
            print("Invalid Input. Please choose a number between 1 and 5.\n")

# Entry point of the program
if __name__ == "__main__":
    To_do_list_application()
