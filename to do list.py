#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Simple To-Do List Application

# Initialize an empty list to store tasks
todo_list = []

def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks in your list.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print("Task added successfully!")

def update_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to update: "))
        if 1 <= task_number <= len(todo_list):
            new_task = input("Enter the updated task: ")
            todo_list[task_number - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 5.")


# In[ ]:




