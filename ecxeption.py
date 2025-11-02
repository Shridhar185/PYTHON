import tkinter as tk #tkinker is a std gui library for python
from tkinter import messagebox #messagebox is a module within tkinter that provides methods for displaying various types of message boxes.

def register_event(event_name, name, age, roll_no):
    if not (name and age and roll_no):
        messagebox.showerror("Error", "Please fill in all registration fields.")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Invalid age. Please enter a valid number.")
        return

    if age < 16:
        messagebox.showerror("Error", "Minimum age requirement is 16.")
        return

    filename = f"{event_name}_registrations.txt"
    with open(filename, "a") as file:
        file.write(f"Name: {name}, Age: {age}, Roll No: {roll_no}\n")
    
    messagebox.showinfo("Success", f"Registered for {event_name}!")

# Create the main window
root = tk.Tk()
root.title("Event Registration")
root.geometry("500x300")

# Event selection
event_label = tk.Label(root, text="Select Event:")
event_label.pack()

event_var = tk.StringVar()
event_var.set("Hackathon")  # Default selection
event_options = ["Hackathon", "Table Tennis","Music"]
event_menu = tk.OptionMenu(root, event_var, *event_options)
event_menu.pack()

# Name entry
name_label = tk.Label(root, text="Your Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

# Age entry
age_label = tk.Label(root, text="Your Age:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

# Roll No entry
roll_no_label = tk.Label(root, text="Your Roll No:")
roll_no_label.pack()

roll_no_entry = tk.Entry(root)
roll_no_entry.pack()

# Register button
def on_register():
    event_name = event_var.get()
    name = name_entry.get()
    age = age_entry.get()
    roll_no = roll_no_entry.get()
    register_event(event_name, name, age, roll_no)

register_button = tk.Button(root, text="Register", command=on_register)
register_button.pack()

# Start the GUI event loop
root.mainloop()