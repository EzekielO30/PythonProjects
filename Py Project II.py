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

def get_weather_update():
    # Placeholder function for getting weather updates
    weather = "It's sunny and 75 degrees Fahrenheit."
    print("Weather update: " + weather)
    return weather

def get_news_briefing():
    # Placeholder function for getting news briefings
    news = [
        "AI technology is rapidly evolving.",
        "New Python version released with exciting features.",
        "Global efforts to combat climate change are increasing."
    ]
    print("Today's news briefing:")
    for headline in news:
        print(f"- {headline}")
    return news

def command_parser():
    print("You can ask me to do the following tasks:")
    print("1. Set a reminder")
    print("2. Manage your to-do list")
    print("3. Get a weather update")
    print("4. Get a news briefing")
    print("5. Exit")

    while True:
        command = input("What would you like me to do? ").lower()
        if "reminder" in command:
            reminders = set_reminder()
            print("Your reminders:")
            for reminder in reminders:
                print(f"- {reminder}")
        elif "to-do" in command or "todo" in command:
            todo_list = manage_todo_list()
        elif "weather" in command:
            get_weather_update()
        elif "news" in command:
            get_news_briefing()
        elif "exit" in command:
            print("Goodbye!")
            break
        else:
            print("Sorry, I didn't understand that command. Please try again.")

def main():
    user_name = greet_user()
    command_parser()

if __name__ == "__main__":
    main()
