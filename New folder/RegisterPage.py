import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import json

class RegisterPage(tk.Frame):
    def __init__(self, root, app):
        tk.Frame.__init__(self, root)
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        register_frame = tk.Frame(self)

        self.email_label = tk.Label(register_frame, text="Email:")
        self.email_entry = tk.Entry(register_frame)
        self.username_label = tk.Label(register_frame, text="Username:")
        self.username_entry = tk.Entry(register_frame)
        self.password_label = tk.Label(register_frame, text="Password:")
        self.password_entry = tk.Entry(register_frame, show="*")
        self.gender_label = tk.Label(register_frame, text="Gender:")
        self.gender_entry = tk.Entry(register_frame)
        self.age_label = tk.Label(register_frame, text="Age:")
        self.age_entry = tk.Entry(register_frame)
        self.photo_label = tk.Label(register_frame, text="No Photo Selected")
        self.upload_photo_button = tk.Button(register_frame, text="Upload Profile Photo", command=self.upload_photo)
        self.register_button = tk.Button(register_frame, text="Register", command=self.register)
        self.back_button = tk.Button(register_frame, text="Back", command=self.app.show_login_page, bg="red")

        self.email_label.grid(row=0, column=0, padx=10, pady=5)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)
        self.username_label.grid(row=1, column=0, padx=10, pady=5)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)
        self.password_label.grid(row=2, column=0, padx=10, pady=5)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)
        self.gender_label.grid(row=3, column=0, padx=10, pady=5)
        self.gender_entry.grid(row=3, column=1, padx=10, pady=5)
        self.age_label.grid(row=4, column=0, padx=10, pady=5)
        self.age_entry.grid(row=4, column=1, padx=10, pady=5)
        self.photo_label.grid(row=5, columnspan=2, padx=10, pady=5)
        self.upload_photo_button.grid(row=6, columnspan=2, padx=10, pady=5)
        self.register_button.grid(row=7, columnspan=2, padx=10, pady=5)
        self.back_button.grid(row=8, columnspan=2, padx=10, pady=5)

        register_frame.pack(padx=20, pady=20)

    def is_email_unique(self, email):
        for user in self.app.users:
            if user["email"] == email:
                return False
        return True

    def register(self):
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        gender = self.gender_entry.get()
        age = self.age_entry.get()

        if not email or not username or not password or not gender or not age:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            if self.is_email_unique(email):
                registration_data = {
                    "email": email,
                    "username": username,
                    "password": password,
                    "gender": gender,
                    "age": age,
                }

                self.app.users.append(registration_data)

                with open("users.json", "w") as user_file:
                    json.dump(self.app.users, user_file, indent=2)

                messagebox.showinfo("Success", "Registration successful.")
                self.app.show_login_page()
            else:
                messagebox.showerror("Error", "Email already exists. Please choose a different one.")

    def upload_photo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.photo_label.config(text="Photo Selected")
