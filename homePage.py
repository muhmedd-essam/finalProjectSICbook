import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
from friend_request import FriendRequest

class HomePage(tk.Frame):
    def __init__(self, root, app):
        tk.Frame.__init__(self, root)
        self.root = root
        self.app = app
        self.friend_request_manager = app.friend_request_manager
        self.logout_callback = app.logout
        self.create_widgets()

    def create_widgets(self):
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")

        if self.app.current_user:
            welcome_label = tk.Label(self, text=f"Welcome, {self.app.current_user['username']}!",
                                     font=("Helvetica", 20), bg="lightblue")
            welcome_label.grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky="w")

        top_left_frame = tk.Frame(self, bg="lightblue")
        top_left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        friend_request_button = tk.Button(top_left_frame, text="Friend Requests", command=self.show_friend_requests,
                                          font=("Helvetica", 16), bg="orange", fg="white")
        friend_request_button.pack(padx=5, pady=5, side="top")

        friends_list_button = tk.Button(top_left_frame, text="Friends List", command=self.show_friends_list,
                                        font=("Helvetica", 16), bg="blue", fg="white")
        friends_list_button.pack(padx=5, pady=5, side="top")

        top_frame = tk.Frame(self, bg="lightblue")
        top_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.message_entry = tk.Entry(top_frame, font=("Helvetica", 14))
        self.message_entry.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        post_button = tk.Button(top_frame, text="Post", command=self.post_message, font=("Helvetica", 16), bg="green",
                                fg="white")
        post_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.posts_frame = tk.Frame(self, bg="white")
        self.posts_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        search_frame = tk.Frame(top_frame, bg="lightblue")
        search_frame.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        self.search_entry = tk.Entry(search_frame, font=("Helvetica", 14))
        self.search_entry.pack(pady=10, side="left")

        search_button = tk.Button(search_frame, text="Search Users", command=self.search_users, font=("Helvetica", 16),
                                  bg="blue", fg="white")
        search_button.pack(pady=10, side="left")

        logout_button = tk.Button(self, text="Logout", command=self.logout, font=("Helvetica", 16), bg="red", fg="white")
        logout_button.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

        self.load_posts()

    def logout(self):
        if self.logout_callback:
            self.logout_callback()

    def post_message(self):
        message = self.message_entry.get()
        if message:
            post = {
                "username": self.app.current_user['username'],
                "message": message,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            self.app.posts.append(post)

            with open("posts.json", "w") as posts_file:
                json.dump(self.app.posts, posts_file, indent=2)

            self.display_post(post)

            self.message_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Post Error", "Please enter a message to post.")

    def load_posts(self):
        try:
            with open("posts.json", "r") as posts_file:
                self.app.posts = json.load(posts_file)
        except FileNotFoundError:
            self.app.posts = []

        for post in self.app.posts:
            self.display_post(post)

    def display_post(self, post):
        post_label = tk.Label(self.posts_frame, text=f"{post['username']} ({post['timestamp']}):\n{post['message']}",
                              font=("Helvetica", 14), bg="white", padx=10, pady=10, borderwidth=1, relief="solid")
        post_label.pack(fill="both", padx=10, pady=5, ipadx=5, ipady=5)

    def search_users(self):
        query = self.search_entry.get()
        matching_users = []

        for user in self.app.users:
            if query.lower() in user["email"].lower() or query.lower() in user["username"].lower():
                matching_users.append(user)

        self.clear_search_results()

        if matching_users:
            search_results_label = tk.Label(self.posts_frame, text="Search Results:", font=("Helvetica", 14),
                                            bg="white")
            search_results_label.pack()

            for user in matching_users:
                if user["username"] == self.app.current_user["username"]:
                    # Display posts for the current user
                    self.display_user_posts(user["username"])
                    continue

                result_label = tk.Label(self.posts_frame, text=user["username"], font=("Helvetica", 14), bg="white")
                result_label.pack()

                if user["username"] in self.app.current_user.get("friends", []):
                    add_friend_button = tk.Button(self.posts_frame, text="Already a Friend",
                                                  font=("Helvetica", 12), bg="gray", fg="white")
                else:
                    add_friend_button = tk.Button(self.posts_frame, text="Add Friend",
                                                  command=lambda u=user: self.add_friend(u),
                                                  font=("Helvetica", 12), bg="green", fg="white")
                add_friend_button.pack()

                # Display posts for the matched user
                self.display_user_posts(user["username"])

            # Add a "Back" button to return to the posts page
            back_button = tk.Button(self.posts_frame, text="Back to Posts", command=self.display_posts_page,
                                    font=("Helvetica", 12), bg="blue", fg="white")
            back_button.pack()

        else:
            no_results_label = tk.Label(self.posts_frame, text="No matching users found.", font=("Helvetica", 14),
                                        bg="white")
            no_results_label.pack()

    def display_user_posts(self, username):
        # Find and display posts by the specified username
        for post in self.app.posts:
            if post["username"] == username:
                post_label = tk.Label(self.posts_frame,
                                      text=f"{post['username']} ({post['timestamp']}):\n{post['message']}",
                                      font=("Helvetica", 14), bg="white", padx=10, pady=10, borderwidth=1,
                                      relief="solid")
                post_label.pack(fill="both", padx=10, pady=5, ipadx=5, ipady=5)

    def add_friend(self, user):
        if self.app.current_user:
            if user["username"] not in self.app.current_user.get("friends", []):
                if self.friend_request_manager.send_friend_request(self.app.current_user["username"], user["username"]):
                    messagebox.showinfo("Friend Request Sent", f"Friend request sent to {user['username']}.")
                else:
                    messagebox.showinfo("Request Already Sent",
                                        f"You have already sent a request to {user['username']}.")
            else:
                messagebox.showinfo("Already a Friend", f"{user['username']} is already in your friend list.")
        else:
            messagebox.showwarning("Not Logged In", "You need to log in to add friends.")

    def show_friend_requests(self):
        pending_requests = self.friend_request_manager.get_pending_requests(self.app.current_user["username"])
        accepted_requests = self.friend_request_manager.get_accepted_requests(self.app.current_user["username"])

        friend_request_dialog = tk.Toplevel(self.root)
        friend_request_dialog.title("Friend Requests")

        if not pending_requests and not accepted_requests:
            no_requests_label = tk.Label(friend_request_dialog, text="No friend requests.", font=("Helvetica", 14))
            no_requests_label.pack(padx=10, pady=10)
        else:
            if pending_requests:
                pending_label = tk.Label(friend_request_dialog, text="Pending Friend Requests:", font=("Helvetica", 14))
                pending_label.pack(padx=10, pady=10)

                for request in pending_requests:
                    request_frame = tk.Frame(friend_request_dialog)
                    request_frame.pack(padx=10, pady=5, fill="x")

                    request_label = tk.Label(request_frame, text=request, font=("Helvetica", 12))
                    request_label.pack(side="left")

                    accept_button = tk.Button(request_frame, text="Accept",
                                              command=lambda req=request: self.accept_request(req),
                                              font=("Helvetica", 12), bg="green", fg="white")
                    accept_button.pack(side="right")

            if accepted_requests:
                accepted_label = tk.Label(friend_request_dialog, text="Accepted Friends:", font=("Helvetica", 14))
                accepted_label.pack(padx=10, pady=10)
                for request in accepted_requests:
                    request_label = tk.Label(friend_request_dialog, text=request, font=("Helvetica", 12))
                    request_label.pack()

    def accept_request(self, request):
        if isinstance(request, dict):
            sender = request.get('sender')
            receiver = request.get('receiver')

            if sender and receiver:
                if self.friend_request_manager.accept_friend_request(sender, receiver):
                    messagebox.showinfo("Friend Request Accepted", f"You are now friends with {sender}.")
                    self.show_friend_requests()
                    self.app.current_user.setdefault("friends", []).append(sender)
                    return
        messagebox.showerror("Error", "Failed to accept the friend request.")

    def show_friends_list(self):
        friends = self.app.current_user.get("friends", [])

        friends_list_dialog = tk.Toplevel(self.root)
        friends_list_dialog.title("Friends List")

        if friends:
            for friend in friends:
                friend_label = tk.Label(friends_list_dialog, text=friend, font=("Helvetica", 12))
                friend_label.pack(padx=10, pady=5)
        else:
            no_friends_label = tk.Label(friends_list_dialog, text="You have no friends yet.", font=("Helvetica", 14))
            no_friends_label.pack(padx=10, pady=10)

    def clear_search_results(self):
        for widget in self.posts_frame.winfo_children():
            widget.destroy()

    def display_posts_page(self):
        # Clear the current search results
        self.clear_search_results()

        # Reload and display the posts
        self.load_posts()
