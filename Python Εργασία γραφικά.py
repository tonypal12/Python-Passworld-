import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from getpass import getpass
import string
import random
import hashlib
import json
from tkinter import simpledialog, messagebox, StringVar
import os

def hash_password(password):
    salt = 'random_salt_here'
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password
def check_password_criteria(password):
    if len(password) < 12:
        return "Weak: Password should be at least 12 characters long."
    elif not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    elif not any(char.isalpha() for char in password):
        return "Weak: Password should contain at least one letter."
    elif not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    elif not any(char in string.punctuation for char in password):
        return "Weak: Password should contain at least one special character."
    else:
        return "Strong: Password meets the criteria."

def generate_password(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password
def on_button_click(choice):
    if choice.startswith("1"):
        def create_account():
            password = password_entry.get()
            result = check_password_criteria(password)
            if "Weak" in result:
                message_label.config(text=result)
            else:
                message_label.config(text="Account created successfully")

        root = tk.Tk()
        root.title("Create Account")

        choice_btn = tk.Button(root, text="Choice 1")  # Add functionality for Choice 1 button

        create_account_btn = tk.Button(root, text="1. Create an account", command=create_account)
        create_account_btn.pack()

        username_label = tk.Label(root, text="Username:")
        username_label.pack()

        username_entry = tk.Entry(root)
        username_entry.pack()

        password_label = tk.Label(root, text="Password:")
        password_label.pack()

        password_entry = tk.Entry(root, show="*")
        password_entry.pack()

        message_label = tk.Label(root, text="")
        message_label.pack()

        root.mainloop()


    elif choice.startswith("2"):
        def add_password():
            website = website_entry.get()
            username = username_entry.get()
            password = password_entry.get()

            password_criteria_result = check_password_criteria(password)
            if "Strong" in password_criteria_result:
                messagebox.showinfo("Password Added", "Password added successfully!")
                hashed_password = hash_password(password)

                try:
                    with open('data.json', 'r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    data = {}

                data[website] = {"username": username, "password": password}

                with open('data.json', 'w') as file:
                    json.dump(data, file)
            else:
                messagebox.showerror("Invalid Password", "Password does not meet the criteria. Please try again.")

        root = tk.Tk()
        root.title("Password Manager")

        website_label = tk.Label(root, text="Enter the website or app name:")
        website_label.pack()
        website_entry = tk.Entry(root)
        website_entry.pack()

        username_label = tk.Label(root, text="Enter your username:")
        username_label.pack()
        username_entry = tk.Entry(root)
        username_entry.pack()

        password_label = tk.Label(root, text="Enter your password:")
        password_label.pack()
        password_entry = tk.Entry(root, show="*")
        password_entry.pack()

        add_password_button = tk.Button(root, text="2. Add Password", command=add_password)
        add_password_button.pack()

        root.mainloop()

    elif choice.startswith("3"):




        def retrieve_password():
            website = website_entry.get()


            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
                    if website in data:



                        messagebox.showinfo("Password Retrieved", f"Password for {website}: {data[website]}")
                    else:
                        messagebox.showerror("Website Not Found", "Password for this website is not stored.")
            except FileNotFoundError:
                messagebox.showerror("File Not Found", "No passwords saved yet.")

        root = tk.Tk()
        root.title("Password Manager")

        website_label = tk.Label(root, text="Enter the website or app name:")
        website_label.pack()
        website_entry = tk.Entry(root)
        website_entry.pack()

        retrieve_password_button = tk.Button(root, text="Retrieve Password", command=retrieve_password)
        retrieve_password_button.pack()

        root.mainloop()



    elif choice.startswith("4"):
        def generate_strong_password():
            password = phrase_entry.get()
            first_letters = ''.join(word[:2] for word in password.split())
            strong_password = generate_password(len(password) + 5)

            final_password = first_letters + strong_password
            result_label.config(text="Your strong password is: " + final_password)

        root = tk.Tk()
        root.title("4 Generate Password")

        phrase_label = tk.Label(root, text="Enter a phrase you like:")
        phrase_label.pack()

        phrase_entry = tk.Entry(root)
        phrase_entry.pack()

        generate_button = tk.Button(root, text="4. Generate Password", command=generate_strong_password)
        generate_button.pack()

        result_label = tk.Label(root, text="")
        result_label.pack()

        root.mainloop()

    elif choice.startswith("5"):
        def check_password_strength():
            password = password_entry.get()
            result = check_password_criteria(password)
            messagebox.showinfo("Password Strength", result)

        root = tk.Tk()
        root.title("Password Strength Checker")

        password_label = tk.Label(root, text="Enter a password:")
        password_label.pack()

        password_entry = tk.Entry(root, show="*")
        password_entry.pack()

        check_strength_button = tk.Button(root, text="5. Check Password Strength", command=check_password_strength)
        check_strength_button.pack()

        root.mainloop()


    elif choice.startswith("6"):
        def open_change_password_window():
            change_password_window = tk.Toplevel()
            change_password_window.title("Change Password")
            change_password_button = tk.Button(change_password_window, text="Change Password",
                                               command=change_password_function)
            change_password_button.pack()

        def change_password_function():
            website = simpledialog.askstring("Website or App Name", "Enter the website or app name:")
            old_password = simpledialog.askstring("Old Password", "Enter the old password:")
            validate_password(old_password, website)

        def validate_password(old_password, website):
            new_password = simpledialog.askstring("New Password", "Enter your new password:")
            while True:
                if len(new_password) < 12 or not any(char.isdigit() for char in new_password) or not any(
                        char.isalpha() for char in new_password) or not any(
                        char.isupper() for char in new_password) or not any(
                        char in string.punctuation for char in new_password):
                    new_password = simpledialog.askstring("New Password", "Weak password. Enter another password:")
                else:
                    hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
                    passwords[website] = {'password': new_password, 'hashed_password': hashed_new_password}
                    messagebox.showinfo("Success", "Password changed successfully!")
                    save_passwords()
                    break

        root = tk.Tk()
        root.title("Password Manager")

        passwords = {}

        def load_passwords():
            if os.path.exists("passwords.json"):
                with open("passwords.json", "r") as file:
                    passwords.update(json.load(file))

        def save_passwords():
            with open("passwords.json", "w") as file:
                json.dump(passwords, file)

        load_passwords()

        def choice_6():
            open_change_password_window()

        choice_6_button = tk.Button(root, text="6. Change Password", command=choice_6)
        choice_6_button.pack()

        root.mainloop()
    elif choice.startswith("Q"):
        def save_to_file(data):
            def save_passwords():
                with open("passwords.json", "w") as file:
                    json.dump(passwords, file)
            pass

        def exit_program():
            save_to_file(passwords)
            print("~~Password manager data saved. Exiting~~.")
            root.quit()

        def on_choice_q():
            print("Choice Q button pressed")

        def on_q_or_exit(event):
            if event.char.lower() == 'q':
                exit_program()

        passwords = []  # Assuming passwords is a list containing password data

        root = tk.Tk()

        choice_q_button = tk.Button(root, text="Q. QUIT", command=on_choice_q)
        choice_q_button.pack()

        exit_button = tk.Button(root, text="EXIT", command=exit_program)
        exit_button.pack()

        root.bind('<Key>', on_q_or_exit)

        root.mainloop()
        root.quit()
    else:
        print("Invalid choice")

root = tk.Tk()
root.title("Menu")

choices = ["1. Create an account", "2. Add Password", "3. Retrieve Password", "4. Generate Password", "5.Check Password Strength", "6. Change Password", "Q. QUIT"]

for i, choice in enumerate(choices):
    button = tk.Button(root, text=choice, command=lambda c=choice: on_button_click(c))
    button.pack()

root.mainloop()

