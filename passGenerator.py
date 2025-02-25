import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length, use_digits, use_special, use_uppercase, use_lowercase, strength_level):
    characters = ""
    
    # Adjust password requirements based on the strength level
    if strength_level >= 8:
        length = max(length, 12)  # Strong password should be at least 12 characters
        if use_digits: 
            characters += string.digits
        if use_special:
            characters += string.punctuation
    elif strength_level >= 4:
        length = max(length, 8)  # Medium password should be at least 8 characters
    else:
        length = max(length, 6)  # Weak password should be at least 6 characters
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    
    if not characters:
        return "Invalid input"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    length = len(password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    
    score = sum([has_digit, has_special, has_upper, has_lower])
    if length >= 12 and score >= 3:
        return "Strong"
    elif length >= 8 and score >= 2:
        return "Medium"
    else:
        return "Weak"

def on_generate():
    try:
        length = int(length_entry.get())
        use_digits = digits_var.get()
        use_special = special_var.get()
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        strength_level = strength_slider.get()
        
        password = generate_password(length, use_digits, use_special, use_uppercase, use_lowercase, strength_level)
        strength = password_strength(password)
        
        password_display.config(text=password, fg='#FFD700', font=('Arial', 14, 'bold'))
        strength_display.config(text=f"Strength: {strength} (Strength Level: {strength_level})", fg='#00FFFF', font=('Arial', 12))
        pyperclip.copy(password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x600")
root.configure(bg='#1E1E1E')

# Title Label
title_label = tk.Label(root, text="🔐 Password Generator 🔐", font=('Arial', 26, 'bold'), bg='#1E1E1E', fg='#00FFFF')
title_label.pack(pady=20)

# Heading
description_label = tk.Label(root, text="Create secure, customizable, and strong passwords!", font=('Arial', 14), bg='#1E1E1E', fg='#FFFFFF')
description_label.pack(pady=5)

# Length Input
length_label = tk.Label(root, text="Enter Password Length:", font=('Arial', 12), bg='#1E1E1E', fg='#FFFFFF')
length_label.pack(pady=5)
length_entry = tk.Entry(root, font=('Arial', 12), bg='#333333', fg='#FFFFFF', insertbackground='white')
length_entry.pack(pady=5)

# Options for Digits, Special Characters, Uppercase, and Lowercase
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()

digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var, font=('Arial', 12), bg='#1E1E1E', fg='#00FFFF', selectcolor='#333333')
digits_check.pack(pady=5)

special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=('Arial', 12), bg='#1E1E1E', fg='#00FFFF', selectcolor='#333333')
special_check.pack(pady=5)

uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, font=('Arial', 12), bg='#1E1E1E', fg='#00FFFF', selectcolor='#333333')
uppercase_check.pack(pady=5)

lowercase_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var, font=('Arial', 12), bg='#1E1E1E', fg='#00FFFF', selectcolor='#333333')
lowercase_check.pack(pady=5)

# Password Strength Slider
strength_slider_label = tk.Label(root, text="Select Password Strength (1-10):", font=('Arial', 12), bg='#1E1E1E', fg='#FFFFFF')
strength_slider_label.pack(pady=5)
strength_slider = tk.Scale(root, from_=1, to=10, orient='horizontal', font=('Arial', 12), bg='#333333', fg='#FFFFFF', sliderlength=30)
strength_slider.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=on_generate, font=('Arial', 14, 'bold'), bg='#00FFFF', fg='#1E1E1E')
generate_button.pack(pady=20)

# Password Display
password_display = tk.Label(root, text="", font=('Arial', 14), bg='#1E1E1E', fg='#FFD700')
password_display.pack(pady=5)

# Password Strength Display
strength_display = tk.Label(root, text="", font=('Arial', 12), bg='#1E1E1E', fg='#00FFFF')
strength_display.pack(pady=5)

# Run the Application
root.mainloop()
