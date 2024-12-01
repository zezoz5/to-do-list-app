tasks = []


def addTask():
    task = input("Add your new task: ").strip()
    if task:
        tasks.append({"description": task, "done": False})
        print(f"Task '{task}' has been added.")
    else:
        print("Task cannot be empty.")



def deleteTask():
    if len(tasks) == 0:
        print("There are no tasks to delete.")
        return

    try:
        listTasks()
        taskToDelete = int(input("Which task do you want to delete? Enter the task number: "))

        if 1 <= taskToDelete <= len(tasks):
            removed_task = tasks.pop(taskToDelete - 1)
            print(f"Task '{removed_task['description']}' has been deleted.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    

def editTask():
    if not tasks:
        print("There are no tasks to edit.")
        return

    listTasks()

    try:
        taskToEdit = int(input("Enter the number of the task you want to edit: ")) - 1

        if 0 <= taskToEdit < len(tasks):
            newTask = input(f"The old task: {tasks[taskToEdit]['description']}, Enter the new task: ").strip()
            if newTask:
                tasks[taskToEdit]["description"] = newTask
                print("Task has been edited successfully.")
            else:
                print("Task cannot be empty. Edit canceled.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

    
def markTask():
    if not tasks:
        print("Please add some tasks first.")
        return

    try:
        listTasks()
        taskIndex = int(input("Enter the task number you want to mark as done: ")) - 1

        if 0 <= taskIndex < len(tasks):
            tasks[taskIndex]["done"] = True
            print(f"Task '{tasks[taskIndex]['description']}' marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{index + 1}. {task['description']} [{status}]")


if __name__ == "__main__":
    print("Welcome to the To-Do List App!")

    while True:
        print("\nCommands:")
        print("add  - Add a new task")
        print("edit - Edit a task")
        print("mark - Mark task as done")
        print("del  - Delete a task")
        print("list - List all tasks")
        print("exit - Exit the program\n")

        # User input for the command
        choice = input("Enter your command: ").strip().lower()

        if choice == "add":
            addTask()
            input("\nPress Enter to continue...")
        elif choice == "edit":
            editTask()
            input("\nPress Enter to continue...")
        elif choice == "mark":
            markTask()
            input("\nPress Enter to continue...")
        elif choice == "del":
            deleteTask()
            input("\nPress Enter to continue...")
        elif choice == "list":
            listTasks()
            input("\nPress Enter to continue...")
        elif choice == "exit":
            print("Goodbye 👋")
            break
        else:
            print("Invalid command. Please choose from 'add', 'edit', 'mark', 'del', 'list', or 'exit'.")
            input("\nPress Enter to continue...")