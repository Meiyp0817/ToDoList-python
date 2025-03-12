# To Do List
tasks = []

def printlogo():
    logo = r"""
 _____ ______   _______   ___  ___       ___  ________  _________   
|\   _ \  _   \|\  ___ \ |\  \|\  \     |\  \|\   ____\|\___   ___\ 
\ \  \\\__\ \  \ \   __/|\ \  \ \  \    \ \  \ \  \___|\|___ \  \_| 
 \ \  \\|__| \  \ \  \_|/_\ \  \ \  \    \ \  \ \_____  \   \ \  \  
  \ \  \    \ \  \ \  \_|\ \ \  \ \  \____\ \  \|____|\  \   \ \  \ 
   \ \__\    \ \__\ \_______\ \__\ \_______\ \__\____\_\  \   \ \__\
    \|__|     \|__|\|_______|\|__|\|_______|\|__|\_________\   \|__|
                                                \|_________|        
                                                                    
                                                                    
"""
    print(logo)

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("\nThere are no tasks currently.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, start=1): 
            print(f"     #{i}. {task}")

def deleteTask():
    listTasks()
    if not tasks:
        return  # No tasks to delete

    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if 1 <= taskToDelete <= len(tasks):
            removed_task = tasks.pop(taskToDelete - 1)  
            print(f"Task #{taskToDelete} ('{removed_task}') has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    printlogo()
    print("Welcome to Mei's To Do List APP:")
    while True:
        print("\nPlease select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            break
        else:
            print("Invalid input!")

print("Goodbye!")
