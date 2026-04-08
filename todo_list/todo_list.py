import json
def main():
    """Todo list with CRUD functionality"""
    todos = load_tasks()

    while True:
        print("\n--- TODO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark As Done")
        print("5. Exit")

        choice = input("What is your choice? ")

        if choice == "1":
            show_tasks(todos)
        elif choice == "2":
            task = input("What is the task? ")
            add_task(todos, task)
        elif choice == "3":
            delete_task(todos)
        elif choice == "4":
            complete_task(todos)
        elif choice == "5":
            print("Todo list exited!")
        else:
            print("Invalid choice ❌")
def show_tasks(todos):
    """Show lists of todos with indices"""
    if not todos:
        print("No task yet")
    else:
        for i, task in enumerate(todos):
            print(f"{i + 1} {task['name']} {'✅' if task['done'] is True else '(Not Done)'}")      
def add_task(todos, task):
    """Add new task to todo list"""
    if task:
        todos.append({"name": task, "done": False})
        save_tasks(todos)
def delete_task(todos):
    """Delete a task from the list"""
    show_tasks(todos)
    try:
        index = int(input("What index of task you want to delete?")) - 1
        removed = todos.pop(index)
        save_tasks(todos)
        print(f"Deleted: {removed["name"]}")
    except:
        print("Invalid Input!")
def complete_task(todos):
    """Marking a task as completed"""
    show_tasks(todos)
    try:
        index = int(input("Which task do you want to mark as complete")) - 1
        if todos[index]["done"] is False:
            todos[index]["done"] = True
        save_tasks(todos)
    except:
        print("Invalid Index chosen!")
def load_tasks():
    """Load task file and if no task file return an empty list"""
    try:
        with open("todos.json", "r") as f:
            return json.load(f)
    except:
        return  []
def save_tasks(todos):
    """Write to task file"""
    with open("todos.json", "w") as f:
        json.dump(todos, f)
if __name__ == "__main__":
    main()