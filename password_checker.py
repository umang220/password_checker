import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Password should be at least 8 characters long.")
    if len(password) > 128:
        issues.append("Password is too long (max 128 characters).")
    if not re.search("[A-Z]", password):
        issues.append("Add at least one uppercase letter.")
    if not re.search("[a-z]", password):
        issues.append("Add at least one lowercase letter.")
    if not re.search("[0-9]", password):
        issues.append("Add at least one number.")
    if not re.search("[@#$%^&*!?_+-]", password):
        issues.append("Add at least one special character.")
    if issues:
        return "Weak: " + " ".join(issues)
    return "Strong: Great password!"

def check_password():
    password = password_entry.get()
    if not password.strip():
        result_label.config(text="Error: Password cannot be empty.", fg="red")
        return
    result = check_password_strength(password)
    result_label.config(text=result, fg="green" if result.startswith("Strong") else "red")

def exit_app():
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        root.destroy()

# Set up the GUI
root = tk.Tk()
root.title("Password Checker")
root.geometry("400x250")  # Window size
root.resizable(False, False)  # Disable resizing

# Title label
title_label = tk.Label(root, text="PASSWORD CHECKER", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password entry
password_frame = tk.Frame(root)
password_frame.pack(pady=10)
tk.Label(password_frame, text="Enter Password:", font=("Arial", 12)).pack(side=tk.LEFT)
password_entry = tk.Entry(password_frame, show="*", font=("Arial", 12), width=20)
password_entry.pack(side=tk.LEFT, padx=5)

# Check button
check_button = tk.Button(root, text="Check Password", font=("Arial", 12), command=check_password)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Enter a password to check.", font=("Arial", 12), wraplength=350)
result_label.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=exit_app)
exit_button.pack(pady=10)

# Start the main loop
root.mainloop()
