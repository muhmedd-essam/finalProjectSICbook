import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class LoginPage(tk.Frame):
    def __init__(self, root, app):
        tk.Frame.__init__(self, root)
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        login_frame = tk.Frame(self)

        self.email_label = tk.Label(login_frame, text="Email or Username:")
        self.email_entry = tk.Entry(login_frame)
        self.password_label = tk.Label(login_frame, text="Password:")
        self.password_entry = tk.Entry(login_frame, show="*")
        self.login_button = tk.Button(login_frame, text="Login", command=self.login)
        self.register_button = tk.Button(login_frame, text="Register", command=self.app.show_register_page)
        self.forgot_password_link = tk.Label(login_frame, text="Forgot Password?", fg="blue", cursor="hand2")
        self.forgot_password_link.bind("<Button-1>", self.forgot_password)

        self.email_label.grid(row=0, column=0, padx=10, pady=5)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        self.register_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        self.forgot_password_link.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        login_frame.pack(padx=20, pady=20)

    def login(self):
        email_or_username = self.email_entry.get()
        password = self.password_entry.get()
        user = self.app.get_user(email_or_username, password)

        if user:
            self.app.set_current_user(user)  # Set the current_user
            messagebox.showinfo("Login Successful", "Welcome, {}!".format(user.get("username")))
            self.app.show_home_page()
        else:
            messagebox.showerror("Login Failed", "Invalid email/username or password.")
    def forgot_password(self, event):
        email_or_username = simpledialog.askstring("Forgot Password", "Enter your email or username:")

        if email_or_username:
            if self.app.user_exists(email_or_username):
                messagebox.showinfo("Password Recovery", "Password recovery instructions have been sent to your email.")
            else:
                messagebox.showerror("User Not Found", "The provided email/username does not exist.")
