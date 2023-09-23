import tkinter as tk
from loginPage import LoginPage
from RegisterPage import RegisterPage
from homePage import HomePage
from friend_request import FriendRequest
import json


class App(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        # Initialize the FriendRequest object before using it
        self.friend_request_manager = FriendRequest()

        self.current_user = None  # Initialize current_user only once

        self.root.title("Social App")
        self.root.geometry("500x500")
        self.pages = []
        self.page_stack = []

        self.load_user_data()
        self.load_posts()  # Load posts data
        self.initialize_pages()
        self.show_page("LoginPage")

    def load_user_data(self):
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = []

    def load_posts(self):
        try:
            with open("posts.json", "r") as posts_file:
                self.posts = json.load(posts_file)
        except FileNotFoundError:
            self.posts = []

    def add_page(self, page_class, page_instance):
        self.pages.append((page_class, page_instance))

    def initialize_pages(self):
        self.login_page = LoginPage(self.root, self)
        self.register_page = RegisterPage(self.root, self)
        self.page_home = HomePage(self.root, self)  # Pass the FriendRequest object and logout callback
        self.add_page(LoginPage, self.login_page)
        self.add_page(RegisterPage, self.register_page)
        self.add_page(HomePage, self.page_home)

    def show_page(self, page_name, category_items=None):
        for page_class, page_instance in self.pages:
            if page_class.__name__ == page_name:
                if self.page_stack:
                    previous_page = self.page_stack[-1]
                    previous_page.pack_forget()
                page_instance.pack()
                self.page_stack.append(page_instance)
                break

    # Define the 'logout' method
    def logout(self):
        # Clear the current user and show the login page
        self.current_user = None
        self.show_login_page()

    def show_login_page(self):
        self.show_page("LoginPage")

    def show_register_page(self):
        self.show_page("RegisterPage")

    def show_home_page(self):
        self.show_page("HomePage")

    def get_user(self, email_or_username, password):
        for user in self.users:
            if (user.get("email") == email_or_username or user.get("username") == email_or_username) and user.get(
                    "password") == password:
                return user
        return None

    def user_exists(self, email_or_username):
        for user in self.users:
            if user.get("email") == email_or_username or user.get("username") == email_or_username:
                return True
        return False

    def set_current_user(self, user):
        self.current_user = user


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
