import tkinter as tk
from tkinter import messagebox

# List to store tasks
tasks = []

# Function to update the listbox
def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        entry.delete(0, tk.END)
        update_list()
    else:
        messagebox.showwarning("Empty Entry", "Please enter a task.")

# Function to delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_list()
    else:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Title label
tk.Label(root, text="My To-Do List", font=("Arial", 14, "bold")).pack(pady=10)

# Entry box
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Add task button
tk.Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=35, height=10)
listbox.pack(pady=10)

# Delete task button
tk.Button(root, text="Delete Task", width=20, command=delete_task).pack(pady=5)

# Start the app
root.mainloop()
