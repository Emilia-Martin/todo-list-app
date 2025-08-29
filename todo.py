# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []
finished = []

# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks
def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Step 4: Delete a task
def delete_task(list):
    kill = input("What task would you like to remove: ")
    spot = 0
    if list[spot] == kill:
        list.pop(spot)
    else:
        spot = spot + 1

# Step 5: Mark task complete
def mark_complete(list):
    completed = input("What is completed: ")
    spot = 0
    if list[spot] == completed:
        finished.append(list[spot])
        list.pop(spot)
    else:
        spot = spot + 1


# Step 6: Save/load tasks (extra stretch for today)


# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    view_tasks(tasks)
    mark_complete(0)
    view_tasks()
    save_tasks()