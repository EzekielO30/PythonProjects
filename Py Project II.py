def greet_user():
    print("Hello! I am your AI-powered personal assistant.")
    user_name = input("What is your name? ")
    print(f"Nice to meet you, {user_name}!")
    return user_name

def set_reminder():
    reminders = []
    while True:
        reminder = input("Enter a reminder (or type 'done' to finish): ")
        if reminder.lower() == 'done':
            break
        reminders.append(reminder)
    return reminders

def manage_todo_list():
    todo_list = []
    while True:
        action = input("Enter 'add' to add a task, 'remove' to remove a task, 'view' to view tasks, or 'done' to finish: ").lower()
        if action == 'add':
            task = input("Enter the task: ")
            todo_list.append(task)
        elif action == 'remove':
            task = input("Enter the task to remove: ")
            if task in todo_list:
                todo_list.remove(task)
            else:
                print("Task not found.")
        elif action == 'view':
            print("Your to-do list:")
            for task in todo_list:
                print(f"- {task}")
        elif action == 'done':
            break
        else:
            print("Invalid action. Please try again.")
    return todo_list

def main():
    user_name = greet_user()
    print("\nLet's set some reminders.")
    reminders = set_reminder()
    print("\nYour reminders:")
    for reminder in reminders:
        print(f"- {reminder}")
    print("\nLet's manage your to-do list.")
    todo_list = manage_todo_list()

if __name__ == "__main__":
    main()
