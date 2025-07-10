import tkinter as tk
from tkinter import messagebox
import json

# File to store tasks
TASK_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks():
    """Save tasks to JSON file."""
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

def open_task_page():
    welcome_frame.pack_forget()
    task_frame.pack()

def add_task():
    """Add a new task to the list."""
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks()
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    """Remove selected task."""
    try:
        selected = task_listbox.curselection()[0]
        del tasks[selected]
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove!")

def mark_done():
    """Mark selected task as done."""
    try:
        selected = task_listbox.curselection()[0]
        tasks[selected]["done"] = True
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as done!")

def update_listbox():
    """Update task listbox."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

def track_tasks():
    """Display a summary of tasks."""
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["done"])
    pending_tasks = total_tasks - completed_tasks
    messagebox.showinfo("Task Summary", f"Total Tasks: {total_tasks}\nCompleted: {completed_tasks}\nPending: {pending_tasks}")

# Load existing tasks
tasks = load_tasks()

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

# Welcome Screen
welcome_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
welcome_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(welcome_frame, text="Hello, Welcome!", font=("Arial", 18, "bold"), bg="#ffffff")
welcome_label.pack(pady=10)

start_button = tk.Button(welcome_frame, text="Go to To-Do List", command=open_task_page, font=("Arial", 12), bg="#4caf50", fg="white", padx=10, pady=5)
start_button.pack()

# Task Page
task_frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)

title_label = tk.Label(task_frame, text="My To-Do List", font=("Arial", 16, "bold"), bg="#ffffff")
title_label.pack()

task_entry = tk.Entry(task_frame, width=40, font=("Arial", 12))
task_entry.pack(pady=5)

task_listbox = tk.Listbox(task_frame, width=50, height=10, font=("Arial", 12), bg="#f9f9f9", selectbackground="#ddd")
task_listbox.pack(pady=5)

update_listbox()

button_frame = tk.Frame(task_frame, bg="#ffffff")
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Arial", 12), bg="#4caf50", fg="white", padx=10, pady=5)
add_button.grid(row=0, column=0, padx=5, pady=5)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, font=("Arial", 12), bg="#f44336", fg="white", padx=10, pady=5)
remove_button.grid(row=0, column=1, padx=5, pady=5)

mark_done_button = tk.Button(button_frame, text="Mark Done", command=mark_done, font=("Arial", 12), bg="#2196f3", fg="white", padx=10, pady=5)
mark_done_button.grid(row=0, column=2, padx=5, pady=5)

track_button = tk.Button(task_frame, text="Track Tasks", command=track_tasks, font=("Arial", 12), bg="#ff9800", fg="white", padx=10, pady=5)
track_button.pack(pady=10)

root.mainloop()
