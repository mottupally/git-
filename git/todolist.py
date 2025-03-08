# Simple To-Do List Application in Python

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found.')

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks have been cleared.")

# Main menu to interact with the to-do list
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Clear All Tasks")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            todo_list.clear_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
