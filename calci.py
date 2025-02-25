import tkinter as tk
from tkinter import messagebox

# Functions

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
    elif value == '⌫':
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
    elif value == '√':
        try:
            result = eval(entry.get()) ** 0.5
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == 'x²':
        try:
            result = eval(entry.get()) ** 2
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)

def on_button_press(button):
    """Change button color on press."""
    button.config(bg="#ffcc00")

def on_button_release(button):
    """Reset button color on release."""
    button.config(bg="#ff9900")

# Main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")
root.configure(bg="#1e1e2e")

# Entry widget for input
entry = tk.Entry(root, width=16, font=('Arial', 28), borderwidth=2, justify='right', bg="#f4f4f4", fg="#333333", relief="solid")
entry.pack(pady=20)

# Button frame
button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.pack()

# Buttons layout
buttons = [
    '7', '8', '9', '/', '√',
    '4', '5', '6', '*', 'x²',
    '1', '2', '3', '-', '⌫',
    '0', 'C', '=', '+'
]

# Create buttons dynamically
for i, button in enumerate(buttons):
    action = lambda x=button: button_click(x)
    btn = tk.Button(button_frame, text=button, command=action, width=5, height=2, font=('Arial', 18), 
                    bg="#ff9900", fg="white", activebackground="#ffcc00", borderwidth=0)
    
    # Bind visual effects
    btn.bind("<ButtonPress>", lambda e, b=btn: on_button_press(b))
    btn.bind("<ButtonRelease>", lambda e, b=btn: on_button_release(b))
    
    btn.grid(row=i // 5, column=i % 5, padx=10, pady=10)

# Flat style for buttons
for widget in button_frame.winfo_children():
    widget.config(relief="flat")

# Run main loop
root.mainloop()
