import tkinter as tk
import json
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from mad2 import ChatApplication






class LoginApplication():
    def __init__(self, shop):
        self.shop = shop

        self.shop.title("SICbook")
        self.shop.geometry("1366x768")
        self.shop.resizable(False, False)
        self.shop.iconbitmap('images/logo_transparent.ico')

        # ========================================================================
        # ============================Frames============================
        # ========================================================================
        self.frameLeft = Frame(shop, width=455, height=768, bg='#040405')
        self.frameLeft.place(x=0, y=0)

        scroll_frame = Frame(width=555, height=768, bg='white', relief='sunken', borderwidth=4)
        scroll_frame.place(x=455, y=0)

        my_canvas = tk.Canvas(scroll_frame, bg='white')
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


        my_scrollbar = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))
        new_width = 530
        new_height = 768
        my_canvas.configure(width=new_width, height=new_height)

        self.feed = tk.Frame(my_canvas, width=620, height=2000, bg="black")
        my_canvas.create_window(500, 0, window=self.feed)

        self.frameRight = Frame(width=355, height=768,  bg='#040405')
        self.frameRight.place(x=1010, y=0)
        # ========================================================================
        # ============================frameLeft============================
        # ========================================================================

        # ================================Name account + Photo Profile==================================
        try:
            with open('logeIn.json', 'r') as file:
                connect = json.load(file)
        except FileNotFoundError:
            connect = {}
        for i in range(len(connect)):
            if connect[i]["Connect"] == "Done":
                self.nameAccount = Label(self.frameLeft, text=connect[i]["name"], font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
                self.nameAccount.place(x=45, y=170)
                image_path = connect[i]["profile"]
                image = Image.open(image_path)
                new_width = 150
                new_height = 150
                image2 = image.resize((new_width, new_height))
                mask = Image.new("L", (new_width, new_height), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, new_width, new_height), fill=255)
                masked_image = Image.new("RGBA", (new_width, new_height))
                masked_image.paste(image2, (0, 0), mask=mask)
                photo = ImageTk.PhotoImage(masked_image)
                label = Label(self.frameLeft,bg="#040405" )
                label.config(image=photo)
                label.image = photo
                label.place(x=20, y=20)
        self.username_line = Canvas(self.frameLeft, width=455, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=0, y=240)


        self.logOut = Button(self.frameLeft, text='Log out', fg='black', bg='#656B89', width=11, font=('tajawal', 16, 'bold'),
                                  command=self.logOut)
        self.logOut.place(x=300, y=100)
        # =================================Games=======================================
        image_path = "images/gamepad.png"
        image = Image.open(image_path)
        new_width = 100
        new_height = 100
        image2 = image.resize((new_width, new_height))
        mask = Image.new("L", (new_width, new_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_width, new_height), fill=255)
        masked_image = Image.new("RGBA", (new_width, new_height))
        masked_image.paste(image2, (0, 0), mask=mask)
        photo = ImageTk.PhotoImage(masked_image)
        label = Label(self.frameLeft, bg="#040405")
        label.config(image=photo)
        label.image = photo
        label.place(x=170, y=250)
        self.snack = Button(self.frameLeft, text="Snack", fg='white', width=10,bg="#750787" ,font=('yu gothic ui', 15, "bold"))
        self.snack.place(x=40, y=370)
        self.roud = Button(self.frameLeft, text="Roud",fg='white',width=10, bg="#750787",font=('yu gothic ui', 15, "bold"))
        self.roud.place(x=300, y=370)

        # ========================================================================
        # ============================frameCenter============================
        # ========================================================================


        entry_font = ("Arial", 26)
        entry_border_width = 2

        self.postEnter = tk.Entry(self.feed, bg='lightgray', fg="#6b6a69", width=24, relief='sunken', borderwidth=4, font=entry_font, bd=entry_border_width)
        self.postEnter.place(x=35, y=50)
        default_text = "What's on your mind?"
        self.postEnter.insert(0, default_text)




        self.post_button = tk.Button(self.feed, text="Post",font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.share)
        self.post_button.place(x=140, y=110)


        try:
            with open('posts.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}
        # try:
        #     with open('logeIn.json', 'r') as file:
        #         user = json.load(file)
        # except FileNotFoundError:
        #     user = {}
        # try:
        #     with open('users.json', 'r') as file:
        #         usersAcc = json.load(file)
        # except FileNotFoundError:
        #     usersAcc = {}

        for i in range(len(users)):
            self.book_label = Label(self.feed, text=users[i]['Post'], fg='#2A2D3A', relief="sunken", borderwidth=2 ,bg='white', width=30 , height= 4 , font=('Arial', 16, 'bold'))
            self.book_label.place(x=users[i]['x'] + 70, y=users[i]['y']+50)
            self.book_Button = Button(self.feed, text='Like', fg='gold', bg='white', width=11, font=('tajawal', 16, 'bold'),
                                      command=lambda index=i: self.afterLike(index))
            self.book_Button.place(x=users[i]['x'] + 300, y=users[i]['y'] + 180)
            self.username_line = Canvas(self.feed, width=455, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.username_line.place(x=users[i]['x'] + 40, y=users[i]['y'] + 170)
            self.username_line2 = Canvas(self.feed, width=455, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.username_line2.place(x=users[i]['x'] + 40, y=users[i]['y'] + 230)
            if users[i]['Like'] >= 1 :
                self.book_label2 = Button(self.feed, text='Like', fg='black', bg='darkblue', width=11, font=('tajawal', 16, 'bold'),
                                          command=lambda index=i: self.deleteLike(index))
                self.book_label2.place(x=users[i]['x'] + 300, y=users[i]['y'] + 180)
            totalComments = users[i]['Comment']
            label_text = f"Comments: {totalComments}"
            self.book_Button2 = Button(self.feed, text=label_text, fg='black', bg='green',  font=('tajawal', 16, 'bold'),
                                      command=lambda index=i: self.comments(index))
            self.book_Button2.place(x=users[i]['x'] + 80, y=users[i]['y'] + 180)
            image_path = users[i]["profile"]
            image = Image.open(image_path)
            new_width = 40
            new_height = 40
            image2 = image.resize((new_width, new_height))
            mask = Image.new("L", (new_width, new_height), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, new_width, new_height), fill=255)
            masked_image = Image.new("RGBA", (new_width, new_height))
            masked_image.paste(image2, (0, 0), mask=mask)
            photo = ImageTk.PhotoImage(masked_image)
            label = Label(self.feed, bg="white")
            label.config(image=photo)
            label.image = photo
            label.place(x=users[i]['x'] + 72, y=users[i]['y'] + 53)
            self.nameUserLogin = Label(self.feed,anchor="w" ,text=users[i]['name'], fg='black', bg='white', width= 20, height=1,
                                       font=('tajawal', 12, 'bold'))
            self.nameUserLogin.place(x=users[i]['x'] + 118, y=users[i]['y'] + 60)



        # ========================================================================
        # ============================frameRight============================
        # ========================================================================
        self.username_line = Canvas(self.frameRight, width=455, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=0, y=400)
        self.book_Button2 = Button(self.frameRight, text="Chats", fg='black', bg='green', font=('tajawal', 16, 'bold'),
                                   command=ChatApplication)
        self.book_Button2.place(x=130 , y= 290)
        image_path ="images/chat_724715.png"
        image = Image.open(image_path)
        new_width = 150
        new_height = 150
        image2 = image.resize((new_width, new_height))
        mask = Image.new("L", (new_width, new_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_width, new_height), fill=255)
        masked_image = Image.new("RGBA", (new_width, new_height))
        masked_image.paste(image2, (0, 0), mask=mask)
        photo = ImageTk.PhotoImage(masked_image)
        label = Label(self.frameRight, bg="white")
        label.config(image=photo)
        label.image = photo
        label.place(x=95, y=120)
        self.book_Button3 = Button(self.frameRight, text="Search", fg='black', bg='green', font=('tajawal', 16, 'bold'))
        self.book_Button3.place(x=130, y=690)




    def logOut(self):
        try:
            with open('logeIn.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        users = []
        with open('logeIn.json', 'w') as file:
            json.dump(users, file)

        try:
            with open('users.json', 'r') as file:
                connect = json.load(file)
        except FileNotFoundError:
            connect = {}
        for i in range(len(connect)):
            if connect[i]["Connect"] == "Done":
                connect[i]["Connect"] = ""
                with open('users.json', 'w') as file:
                    json.dump(connect, file)
        self.shop.destroy()






    def addComment(self, index, comment):
        try:
            with open('posts.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}
        try:
            with open('Comments.json', 'r') as file:
                users2 = json.load(file)
        except FileNotFoundError:
            users2 = {}

        # users[index]["Comment"] = comment

        # with open('posts.json', 'w') as file:
        #     json.dump(users, file)
        Post = {"Post": users[index]["Post"],
                "Comment": comment,
                }
        users2.append(Post)
        with open('Comments.json', 'w') as file:
            json.dump(users2, file)
        users[index]["Comment"] += 1
        with open('posts.json', 'w') as file:
            json.dump(users, file)
        self.comment_window.destroy()
        self.comments(index)

    def comments(self, index):
        try:
            with open('Comments.json', 'r') as file:
                users2 = json.load(file)
        except FileNotFoundError:
            users2 = {}

        try:
            with open('posts.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}
        self.comment_window = tk.Toplevel(self.shop)
        self.comment_window.title("Comments")
        self.comment_window.geometry("400x200")


        label_text = "Post: " + users[index]["Post"]
        post_label = tk.Label(self.comment_window, text=label_text)
        post_label.pack()


        comment_entry = tk.Entry(self.comment_window)
        comment_entry.pack()


        confirm_button = tk.Button(self.comment_window, text="Confirm",
                                   command=lambda: self.addComment(index, comment_entry.get()))
        confirm_button.pack()
        for i in range(len(users2)):
            if users2[index]["Post"] == users[index]["Post"]:
                self.comment = Label(self.comment_window, text=users2[i]['Comment'], fg='gold', bg='white', font=('tajawal', 16, 'bold'))
                self.comment.place(x=0, y= 10)

    def share(self):
        post = self.postEnter.get()
        try:
            with open('posts.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}
        if users == [] :
            y = 180
            x = 0
            try:
                with open('logeIn.json', 'r') as file:
                    accountLog = json.load(file)
            except FileNotFoundError:
                accountLog = {}

            # Add new post
            Post = {"emailShare": accountLog[0]["email"],
                    "name": accountLog[0]["name"],
                    "Post": post,
                    "Like": 0,
                    "Comment": 0,
                    "x": x,
                    "y": y,
                    "profile": accountLog[0]["profile"]
                    }
            users.append(Post)

            # Save updated user data to JSON file
            with open('posts.json', 'w') as file:
                json.dump(users, file)
            messagebox.showinfo("Post", "done share post")
            self.afterShare()
        else:
            try:
                with open('posts.json', 'r') as file:
                    posts_data = json.load(file)
            except FileNotFoundError:
                posts_data = {}
            y = posts_data[-1]["y"] + 220
            x = 0
            try:
                with open('logeIn.json', 'r') as file:
                    accountLog = json.load(file)
            except FileNotFoundError:
                accountLog = {}

            # Add new post
            Post = {"emailShare": accountLog[0]["email"],
                    "name": accountLog[0]["name"],
                    "Post": post,
                    "Like": 0,
                    "Comment": 0,
                    "x": x,
                    "y": y,
                    "profile": accountLog[0]["profile"]
                    }
            posts_data.append(Post)

            # Save updated user data to JSON file
            with open('posts.json', 'w') as file:
                json.dump(posts_data, file)
            messagebox.showinfo("Post", "done share post")
            self.afterShare()


    def afterShare(self):
        self.shop.destroy()
        LoginApplication(tk.Tk())

    def afterLike(self,indexLike):
        try:
            with open('posts.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        users[indexLike]["Like"] += 1
        with open('posts.json', 'w') as file:
            json.dump(users, file)

        try:
            with open('logeIn.json', 'r') as file:
                accountLog = json.load(file)
        except FileNotFoundError:
            accountLog = {}
        try:
            with open('posts.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}
        try:
            with open('like_history.json', 'r') as file:
                like = json.load(file)
        except FileNotFoundError:
            like = {}
        for i in range(len(like)):
            if like[i]["from"] != accountLog[0]["email"] or like[i]["to"] != users[indexLike]["emailShare"]:
                history = {"from": accountLog[0]["email"],
                           "like": 0,
                           "to": users[indexLike]["emailShare"]
                           }
                like.append(history)
                like[i]["like"] += 1
                with open('like_history.json', 'w') as file:
                    json.dump(like, file)

            elif like[i]["from"] == accountLog[0]["email"] and like[i]["to"] == users[indexLike]["emailShare"]:
                like[i]["like"] += 1
                with open('like_history.json', 'w') as file:
                    json.dump(like, file)
        try:
            with open('posts.json', 'r') as file:
                posts_data = json.load(file)
        except FileNotFoundError:
            posts_data = {}


        try:
            with open('posts.json', 'r') as file:
                posts_data = json.load(file)
        except FileNotFoundError:
            posts_data = {}
        posts_data = sorted(posts_data, key=lambda post: sum(history["like"] for history in like if history["to"] == post["emailShare"]), reverse=True)
        if len(posts_data) > 0:
            start_y = 180
            end_y = posts_data[-1]["y"] + 220
            step = (end_y - start_y) / (len(posts_data) - 1)
            for i, post in enumerate(posts_data):
                post["y"] = int(start_y + (i * step))
        else:
            posts_data = []
        with open('posts.json', 'w') as file:
            json.dump(posts_data, file)









        self.shop.destroy()
        LoginApplication(tk.Tk())

    def deleteLike(self, indexLike):

        try:
            with open('posts.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        users[indexLike]["Like"] -= 1
        with open('posts.json', 'w') as file:
            json.dump(users, file)

        self.shop.destroy()
        LoginApplication(tk.Tk())

