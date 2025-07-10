import tkinter as tk
from tkinter import messagebox

def button_click(value):
    """Handles button clicks for numbers and operations."""
    if value == 'C':
        entry.delete(0, tk.END)
    elif value == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)

def on_button_press(button):
    """Change button color on press."""
    button.config(bg="#45a049")

def on_button_release(button):
    """Reset button color on release."""
    button.config(bg="#4CAF50")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#2E2E2E")

# Create an entry widget for user input with a border
entry = tk.Entry(root, width=16, font=('Arial', 28), borderwidth=2, justify='right', bg="#FFFFFF", relief="solid")
entry.pack(pady=20)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#2E2E2E")
button_frame.pack()

# Define button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create buttons dynamically with a modern look
for i, button in enumerate(buttons):
    action = lambda x=button: button_click(x)
    btn = tk.Button(button_frame, text=button, command=action, width=5, height=2, font=('Arial', 18), 
                    bg="#4CAF50", fg="white", activebackground="#45a049", borderwidth=0)
    
    # Bind button press and release events for visual effect
    btn.bind("<ButtonPress>", lambda e, b=btn: on_button_press(b))
    btn.bind("<ButtonRelease>", lambda e, b=btn: on_button_release(b))
    
    btn.grid(row=i // 4, column=i % 4, padx=10, pady=10)

# Style the buttons with rounded corners
for widget in button_frame.winfo_children():
    widget.config(relief="flat")  # Remove the default button relief

# Start the GUI event loop
root.mainloop()