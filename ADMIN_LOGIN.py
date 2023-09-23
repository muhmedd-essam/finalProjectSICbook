import tkinter as tk
import json
from tkinter import messagebox
from tkinter import *


class adminLoginApp:
    def __init__(self, shop):
        self.shop = shop

        self.shop.title("Online Shopping")
        self.shop.geometry("800x600+280+50")
        self.shop.resizable(False, False)
        self.shop.iconbitmap('supermarkets.ico')
        self.shop.title_label = tk.Label(self.shop, text='Store Online', fg='gold', bg='black',
                                         font=('tajawal', 16, 'bold'))
        self.shop.title_label.pack(fill=tk.X)

        self.F1 = Frame(shop, width=800, height=400, bg='black')
        self.F1.place(x=0, y=367)

        self.button_books = tk.Button(self.F1, text='Books', width=26, fg='black', bg='#DBA901',
                                      font=('tajawal', 16, 'bold'), command=self.books)
        self.button_books.place(x=20, y=10)
        self.button_Electronics = tk.Button(self.F1, text='Electronics', width=26, fg='black', bg='#DBA901',
                                            font=('tajawal', 16, 'bold'), command=self.Electronics)
        self.button_Electronics.place(x=440, y=10)
        self.button_Fashion = tk.Button(self.F1, text='Fashion', width=26, fg='black', bg='#DBA901',
                                        font=('tajawal', 16, 'bold'), command=self.Fashion)
        self.button_Fashion.place(x=20, y=80)
        self.button_Sports = tk.Button(self.F1, text='Sports', width=26, fg='black', bg='#DBA901',
                                       font=('tajawal', 16, 'bold'), command=self.Sports)
        self.button_Sports.place(x=440, y=80)

        self.buttons = [
            ("Books"),
            ("Electronics"),
            ("Fashion"),
            ("Sports")
        ]
        self.change = tk.Button(text='Change sort, Ascending/descending', width=30, fg='black', bg='#DBA901',
                                font=('tajawal', 16, 'bold'), command=self.toggle_sort)
        self.change.place(x=220, y=550)
        self.sort_ascending = True

        self.create_buttons()

        self.Photo = PhotoImage(file="2.png")
        self.imo = tk.Label(image=self.Photo)
        self.imo.place(x=0, y=30)
        self.logout_button = tk.Button( text="Logout", width=10, fg='black', bg='#DBA901',
                                font=('tajawal', 16, 'bold') ,command=self.logout)
        self.logout_button.place(x=10, y=550)

    def logout(self):
        self.shop.destroy()


    def books(self):
        with open('books_data.json', 'r') as file:
            users = json.load(file)




        def search_book():
            global mid
            search_text = search_entry.get()
            with open('books_data.json', 'r') as file:
                users = json.load(file)
            sorted(users)

            low = 0
            high = len(users) -1
            found = False

            while low <= high:
                mid = (low + high) // 2
                book = users[mid]['text']

                if search_text == book:
                    found = True
                    break
                elif search_text < book:
                    high = mid - 1
                else:
                    low = mid + 1



            if found:
                book_label = Label(Fab, text=users[mid]['text'] + ' ✓', fg='gold', bg='darkblue',
                                   font=('tajawal', 16, 'bold'))
                book_label.place(x=users[mid]['x'], y=positions[mid][1])
            else:
                messagebox.showinfo("Not Found", "The book was not found.")






        newWindow = Toplevel(self.shop)
        newWindow.title("Online Shopping")
        newWindow.geometry("800x600+280+50")
        newWindow.iconbitmap('supermarkets.ico')
        Label(newWindow, text='Books', fg='gold', bg='black', font=('tajawal', 16, 'bold')).pack(fill=tk.X)
        Fab = tk.Frame(newWindow, height=800, bg='darkblue')
        Fab.pack(fill=tk.X)


        with open('books_data.json', 'r') as file:
            users = json.load(file)

        positions = [(20, 270), (180, 270), (340, 270), (500, 270), (660, 270)]

        varBooks = [IntVar() for _ in range(5)]

        entries = []

        for i in range(len(users)):
            self.book_label = Label(Fab, text=users[i]['text'], fg='gold', bg='darkblue', font=('tajawal', 16, 'bold'))
            self.book_label.place(x=users[i]['x'], y=positions[i][1])

            book_entry = Entry(Fab, textvariable=varBooks[i], width=18, justify='center')
            book_entry.place(x=users[i]['x'] + 5, y=positions[i][1] + 40)

            entries.append(book_entry)
        def edit_books():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            book_label = Label(newWindow, text="Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, width=30)
            book_entry.pack()

            delete_button = Button(newWindow, text="Delete Book",
                                   command=lambda: delete_book_from_list(book_entry.get()))
            delete_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)
        def delete_book_from_list(book_name):
            for i, book in enumerate(users):
                if book['text'] == book_name:
                    users.pop(i)
                    messagebox.showinfo("Success", "The book has been deleted.")
                    file_path = 'books_data.json'
                    json_data = json.dumps(users)
                    with open(file_path, 'w') as file:
                        file.write(json_data)
                    break

        delete_button = Button(Fab, text="Delete Books", command=edit_books, width=15, fg='black', bg='#DBA901',
                                font=('tajawal', 16, 'bold'))
        delete_button.place(x=60, y=200)
        def add_books():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            book_label = Label(newWindow, text="Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, width=30)
            book_entry.pack()

            add_button = Button(newWindow, text="add Book",
                                   command=lambda: save_book(book_entry.get()))
            add_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

        add_button = Button(Fab, text="Add Books", command=add_books, width=15, fg='black', bg='#DBA901',
                                font=('tajawal', 16, 'bold'))
        add_button.place(x=520, y=200)
        def save_book(book_name):
            with open('books_data.json', 'r') as file:
                users = json.load(file)
            newBook={"text":book_name}
            users.append(newBook)
            file_path = 'books_data.json'
            json_data = json.dumps(users)
            with open(file_path, 'w') as file:
                file.write(json_data)
            messagebox.showinfo("Success", "The book has been deleted.")
        def changebooks():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            varOldName = StringVar()
            varNewName = StringVar()

            book_label = Label(newWindow, text="Book Name you need to change it:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, textvariable=varOldName,width=30)
            book_entry.pack()

            book_label = Label(newWindow, text="New Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            newname = Entry(newWindow, textvariable=varNewName,width=30)
            newname.pack()

            add_button = Button(newWindow, text='Edit',
                                   command=lambda: change_book(varOldName.get(), varNewName.get()))
            add_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

            def change_book(old_name, new_name):
                with open('books_data.json', 'r') as file:
                    users = json.load(file)
                for user in users:
                    if user['text'] == old_name:
                        user['text'] = new_name
                        with open('books_data.json', 'w') as file:
                            json.dump(users, file)
                        messagebox.showinfo("Success", "The book has been changed.")
                        newWindow.destroy()
                        self.books()
                        return
                messagebox.showinfo("Error", "The book was not found.")


        add_button = Button(Fab, text="Edit Books", command=changebooks, width=15, fg='black', bg='#DBA901',
                                font=('tajawal', 16, 'bold'),)
        add_button.place(x=290, y=200)


        search_label = tk.Label(Fab, text="Search for Item:", bg='darkblue', fg='gold',
                                font=('tajawal', 16, 'bold'))
        search_label.place(x=230, y=460)

        search_entry = tk.Entry(Fab, width=18, justify='center')
        search_entry.place(x=400, y=466)
        back_button = tk.Button(Fab, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                command=self.back_to_home)
        back_button.place(x=20, y=20)

        search = Button(Fab,text='search', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                        command=search_book)
        search.place(x=320, y=490)

        varBook1 = IntVar()
        varBook2 = IntVar()
        varBook3 = IntVar()
        varBook4 = IntVar()
        varBook5 = IntVar()

        varPrice = StringVar()

        book1ent = Entry(Fab, textvariable=varBook1, width=18, justify='center')
        book1ent.place(x=25, y=310)

        book2ent = Entry(Fab, textvariable=varBook2, width=18, justify='center')
        book2ent.place(x=185, y=310)

        book3ent = Entry(Fab, textvariable=varBook3, width=18, justify='center')
        book3ent.place(x=345, y=310)

        book4ent = Entry(Fab, textvariable=varBook4, width=18, justify='center')
        book4ent.place(x=505, y=310)

        book5ent = Entry(Fab, textvariable=varBook5, width=18, justify='center')
        book5ent.place(x=665, y=310)


    def Electronics(self):
        with open('Elctronics_data.json', 'r') as file:
            users = json.load(file)

        def search_book():
            global mid
            search_text = search_entry.get()
            with open('Elctronics_data.json', 'r') as file:
                users = json.load(file)
            sorted(users)

            low = 0
            high = len(users) - 1
            found = False

            while low <= high:
                mid = (low + high) // 2
                book = users[mid]['text']

                if search_text == book:
                    found = True
                    break
                elif search_text < book:
                    high = mid - 1
                else:
                    low = mid + 1

            if found:
                book_label = Label(Fab, text=users[mid]['text'] + ' ✓', fg='gold', bg='darkblue',
                                   font=('tajawal', 16, 'bold'))
                book_label.place(x=users[mid]['x'], y=positions[mid][1])
            else:
                messagebox.showinfo("Not Found", "The book was not found.")

        newWindow = Toplevel(self.shop)
        newWindow.title("Online Shopping")
        newWindow.geometry("800x600+280+50")
        newWindow.iconbitmap('supermarkets.ico')
        Label(newWindow, text='Books', fg='gold', bg='black', font=('tajawal', 16, 'bold')).pack(fill=tk.X)
        Fab = tk.Frame(newWindow, height=800, bg='darkblue')
        Fab.pack(fill=tk.X)

        with open('Elctronics_data.json', 'r') as file:
            users = json.load(file)

        positions = [(20, 270), (180, 270), (340, 270), (500, 270), (660, 270)]

        varBooks = [IntVar() for _ in range(5)]

        entries = []

        for i in range(len(users)):
            self.book_label = Label(Fab, text=users[i]['text'], fg='gold', bg='darkblue', font=('tajawal', 16, 'bold'))
            self.book_label.place(x=users[i]['x'], y=positions[i][1])

            book_entry = Entry(Fab, textvariable=varBooks[i], width=18, justify='center')
            book_entry.place(x=users[i]['x'] + 5, y=positions[i][1] + 40)

            entries.append(book_entry)

        def edit_books():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            book_label = Label(newWindow, text="Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, width=30)
            book_entry.pack()

            delete_button = Button(newWindow, text="Delete Book",
                                   command=lambda: delete_book_from_list(book_entry.get()))
            delete_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

        def delete_book_from_list(book_name):
            for i, book in enumerate(users):
                if book['text'] == book_name:
                    users.pop(i)
                    messagebox.showinfo("Success", "The book has been deleted.")
                    file_path = 'Elctronics_data.json'
                    json_data = json.dumps(users)
                    with open(file_path, 'w') as file:
                        file.write(json_data)
                    break

        delete_button = Button(Fab, text="Delete Books", command=edit_books, width=15, fg='black', bg='#DBA901',
                               font=('tajawal', 16, 'bold'))
        delete_button.place(x=60, y=200)

        def add_books():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            book_label = Label(newWindow, text="Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, width=30)
            book_entry.pack()

            add_button = Button(newWindow, text="add Book",
                                command=lambda: save_book(book_entry.get()))
            add_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

        add_button = Button(Fab, text="Add Books", command=add_books, width=15, fg='black', bg='#DBA901',
                            font=('tajawal', 16, 'bold'))
        add_button.place(x=520, y=200)

        def save_book(book_name):
            with open('Elctronics_data.json', 'r') as file:
                users = json.load(file)
            newBook = {"text": book_name}
            users.append(newBook)
            file_path = 'Elctronics_data.json'
            json_data = json.dumps(users)
            with open(file_path, 'w') as file:
                file.write(json_data)
            messagebox.showinfo("Success", "The book has been deleted.")

        def changebooks():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            varOldName = StringVar()
            varNewName = StringVar()

            book_label = Label(newWindow, text="Book Name you need to change it:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, textvariable=varOldName, width=30)
            book_entry.pack()

            book_label = Label(newWindow, text="New Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            newname = Entry(newWindow, textvariable=varNewName, width=30)
            newname.pack()

            add_button = Button(newWindow, text='Edit',
                                command=lambda: change_book(varOldName.get(), varNewName.get()))
            add_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

            def change_book(old_name, new_name):
                with open('Elctronics_data.json', 'r') as file:
                    users = json.load(file)
                for user in users:
                    if user['text'] == old_name:
                        user['text'] = new_name
                        with open('Elctronics_data.jsonn', 'w') as file:
                            json.dump(users, file)
                        messagebox.showinfo("Success", "The book has been changed.")
                        newWindow.destroy()
                        self.books()
                        return
                messagebox.showinfo("Error", "The book was not found.")

        add_button = Button(Fab, text="Edit Books", command=changebooks, width=15, fg='black', bg='#DBA901',
                            font=('tajawal', 16, 'bold'), )
        add_button.place(x=290, y=200)

        search_label = tk.Label(Fab, text="Search for Item:", bg='darkblue', fg='gold',
                                font=('tajawal', 16, 'bold'))
        search_label.place(x=230, y=460)

        search_entry = tk.Entry(Fab, width=18, justify='center')
        search_entry.place(x=400, y=466)
        back_button = tk.Button(Fab, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                command=self.back_to_home)
        back_button.place(x=20, y=20)

        search = Button(Fab, text='search', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                        command=search_book)
        search.place(x=320, y=490)

        varBook1 = IntVar()
        varBook2 = IntVar()
        varBook3 = IntVar()
        varBook4 = IntVar()
        varBook5 = IntVar()

        varPrice = StringVar()

        book1ent = Entry(Fab, textvariable=varBook1, width=18, justify='center')
        book1ent.place(x=25, y=310)

        book2ent = Entry(Fab, textvariable=varBook2, width=18, justify='center')
        book2ent.place(x=185, y=310)

        book3ent = Entry(Fab, textvariable=varBook3, width=18, justify='center')
        book3ent.place(x=345, y=310)

        book4ent = Entry(Fab, textvariable=varBook4, width=18, justify='center')
        book4ent.place(x=505, y=310)

        book5ent = Entry(Fab, textvariable=varBook5, width=18, justify='center')
        book5ent.place(x=665, y=310)


    def Fashion(self):
        with open('Fashion.json', 'r') as file:
            users = json.load(file)

        def search_book():
            global mid
            search_text = search_entry.get()
            with open('Fashion.json', 'r') as file:
                users = json.load(file)
            sorted(users)

            low = 0
            high = len(users) - 1
            found = False

            while low <= high:
                mid = (low + high) // 2
                book = users[mid]['text']

                if search_text == book:
                    found = True
                    break
                elif search_text < book:
                    high = mid - 1
                else:
                    low = mid + 1

            if found:
                book_label = Label(Fab, text=users[mid]['text'] + ' ✓', fg='gold', bg='darkblue',
                                   font=('tajawal', 16, 'bold'))
                book_label.place(x=users[mid]['x'], y=positions[mid][1])
            else:
                messagebox.showinfo("Not Found", "The book was not found.")

        newWindow = Toplevel(self.shop)
        newWindow.title("Online Shopping")
        newWindow.geometry("800x600+280+50")
        newWindow.iconbitmap('supermarkets.ico')
        Label(newWindow, text='Books', fg='gold', bg='black', font=('tajawal', 16, 'bold')).pack(fill=tk.X)
        Fab = tk.Frame(newWindow, height=800, bg='darkblue')
        Fab.pack(fill=tk.X)

        with open('Fashion.json', 'r') as file:
            users = json.load(file)

        positions = [(20, 270), (180, 270), (340, 270), (500, 270), (660, 270)]

        varBooks = [IntVar() for _ in range(5)]

        entries = []

        for i in range(len(users)):
            self.book_label = Label(Fab, text=users[i]['text'], fg='gold', bg='darkblue', font=('tajawal', 16, 'bold'))
            self.book_label.place(x=users[i]['x'], y=positions[i][1])

            book_entry = Entry(Fab, textvariable=varBooks[i], width=18, justify='center')
            book_entry.place(x=users[i]['x'] + 5, y=positions[i][1] + 40)

            entries.append(book_entry)

        def edit_books():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            book_label = Label(newWindow, text="Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, width=30)
            book_entry.pack()

            delete_button = Button(newWindow, text="Delete Book",
                                   command=lambda: delete_book_from_list(book_entry.get()))
            delete_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

        def delete_book_from_list(book_name):
            for i, book in enumerate(users):
                if book['text'] == book_name:
                    users.pop(i)
                    messagebox.showinfo("Success", "The book has been deleted.")
                    file_path = 'Fashion.json'
                    json_data = json.dumps(users)
                    with open(file_path, 'w') as file:
                        file.write(json_data)
                    break

        delete_button = Button(Fab, text="Delete Books", command=edit_books, width=15, fg='black', bg='#DBA901',
                               font=('tajawal', 16, 'bold'))
        delete_button.place(x=60, y=200)

        def add_books():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            book_label = Label(newWindow, text="Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, width=30)
            book_entry.pack()

            add_button = Button(newWindow, text="add Book",
                                command=lambda: save_book(book_entry.get()))
            add_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

        add_button = Button(Fab, text="Add Books", command=add_books, width=15, fg='black', bg='#DBA901',
                            font=('tajawal', 16, 'bold'))
        add_button.place(x=520, y=200)

        def save_book(book_name):
            with open('Fashion.json', 'r') as file:
                users = json.load(file)
            newBook = {"text": book_name}
            users.append(newBook)
            file_path = 'Fashion.json'
            json_data = json.dumps(users)
            with open(file_path, 'w') as file:
                file.write(json_data)
            messagebox.showinfo("Success", "The book has been deleted.")

        def changebooks():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            varOldName = StringVar()
            varNewName = StringVar()

            book_label = Label(newWindow, text="Book Name you need to change it:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, textvariable=varOldName, width=30)
            book_entry.pack()

            book_label = Label(newWindow, text="New Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            newname = Entry(newWindow, textvariable=varNewName, width=30)
            newname.pack()

            add_button = Button(newWindow, text='Edit',
                                command=lambda: change_book(varOldName.get(), varNewName.get()))
            add_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

            def change_book(old_name, new_name):
                with open('Fashion.json', 'r') as file:
                    users = json.load(file)
                for user in users:
                    if user['text'] == old_name:
                        user['text'] = new_name
                        with open('Fashion.json', 'w') as file:
                            json.dump(users, file)
                        messagebox.showinfo("Success", "The book has been changed.")
                        newWindow.destroy()
                        self.books()
                        return
                messagebox.showinfo("Error", "The book was not found.")

        add_button = Button(Fab, text="Edit Books", command=changebooks, width=15, fg='black', bg='#DBA901',
                            font=('tajawal', 16, 'bold'), )
        add_button.place(x=290, y=200)

        search_label = tk.Label(Fab, text="Search for Item:", bg='darkblue', fg='gold',
                                font=('tajawal', 16, 'bold'))
        search_label.place(x=230, y=460)

        search_entry = tk.Entry(Fab, width=18, justify='center')
        search_entry.place(x=400, y=466)
        back_button = tk.Button(Fab, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                command=self.back_to_home)
        back_button.place(x=20, y=20)

        search = Button(Fab, text='search', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                        command=search_book)
        search.place(x=320, y=490)

        varBook1 = IntVar()
        varBook2 = IntVar()
        varBook3 = IntVar()
        varBook4 = IntVar()
        varBook5 = IntVar()


        book1ent = Entry(Fab, textvariable=varBook1, width=18, justify='center')
        book1ent.place(x=25, y=310)

        book2ent = Entry(Fab, textvariable=varBook2, width=18, justify='center')
        book2ent.place(x=185, y=310)

        book3ent = Entry(Fab, textvariable=varBook3, width=18, justify='center')
        book3ent.place(x=345, y=310)

        book4ent = Entry(Fab, textvariable=varBook4, width=18, justify='center')
        book4ent.place(x=505, y=310)

        book5ent = Entry(Fab, textvariable=varBook5, width=18, justify='center')
        book5ent.place(x=665, y=310)


    def Sports(self):
        with open('Sport.json', 'r') as file:
            users = json.load(file)

        def search_book():
            global mid
            search_text = search_entry.get()
            with open('Sport.json', 'r') as file:
                users = json.load(file)
            sorted(users)

            low = 0
            high = len(users) - 1
            found = False

            while low <= high:
                mid = (low + high) // 2
                book = users[mid]['text']

                if search_text == book:
                    found = True
                    break
                elif search_text < book:
                    high = mid - 1
                else:
                    low = mid + 1

            if found:
                book_label = Label(Fab, text=users[mid]['text'] + ' ✓', fg='gold', bg='darkblue',
                                   font=('tajawal', 16, 'bold'))
                book_label.place(x=users[mid]['x'], y=positions[mid][1])
            else:
                messagebox.showinfo("Not Found", "The book was not found.")

        newWindow = Toplevel(self.shop)
        newWindow.title("Online Shopping")
        newWindow.geometry("800x600+280+50")
        newWindow.iconbitmap('supermarkets.ico')
        Label(newWindow, text='Books', fg='gold', bg='black', font=('tajawal', 16, 'bold')).pack(fill=tk.X)
        Fab = tk.Frame(newWindow, height=800, bg='darkblue')
        Fab.pack(fill=tk.X)

        with open('Sport.json', 'r') as file:
            users = json.load(file)

        positions = [(20, 270), (180, 270), (340, 270), (500, 270), (660, 270)]

        varBooks = [IntVar() for _ in range(5)]

        entries = []

        for i in range(len(users)):
            self.book_label = Label(Fab, text=users[i]['text'], fg='gold', bg='darkblue', font=('tajawal', 16, 'bold'))
            self.book_label.place(x=users[i]['x'], y=positions[i][1])

            book_entry = Entry(Fab, textvariable=varBooks[i], width=18, justify='center')
            book_entry.place(x=users[i]['x'] + 5, y=positions[i][1] + 40)

            entries.append(book_entry)

        def edit_books():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            book_label = Label(newWindow, text="Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, width=30)
            book_entry.pack()

            delete_button = Button(newWindow, text="Delete Book",
                                   command=lambda: delete_book_from_list(book_entry.get()))
            delete_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

        def delete_book_from_list(book_name):
            for i, book in enumerate(users):
                if book['text'] == book_name:
                    users.pop(i)
                    messagebox.showinfo("Success", "The book has been deleted.")
                    file_path = 'Sport.json'
                    json_data = json.dumps(users)
                    with open(file_path, 'w') as file:
                        file.write(json_data)
                    break

        delete_button = Button(Fab, text="Delete Books", command=edit_books, width=15, fg='black', bg='#DBA901',
                               font=('tajawal', 16, 'bold'))
        delete_button.place(x=60, y=200)

        def add_books():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            book_label = Label(newWindow, text="Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, width=30)
            book_entry.pack()

            add_button = Button(newWindow, text="add Book",
                                command=lambda: save_book(book_entry.get()))
            add_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

        add_button = Button(Fab, text="Add Books", command=add_books, width=15, fg='black', bg='#DBA901',
                            font=('tajawal', 16, 'bold'))
        add_button.place(x=520, y=200)

        def save_book(book_name):
            with open('Sport.json', 'r') as file:
                users = json.load(file)
            newBook = {"text": book_name}
            users.append(newBook)
            file_path = 'Sport.json'
            json_data = json.dumps(users)
            with open(file_path, 'w') as file:
                file.write(json_data)
            messagebox.showinfo("Success", "The book has been deleted.")

        def changebooks():
            newWindow = Toplevel(self.shop)
            newWindow.title("Edit Books")
            newWindow.geometry("400x300+400+200")
            newWindow.iconbitmap('supermarkets.ico')

            varOldName = StringVar()
            varNewName = StringVar()

            book_label = Label(newWindow, text="Book Name you need to change it:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            book_entry = Entry(newWindow, textvariable=varOldName, width=30)
            book_entry.pack()

            book_label = Label(newWindow, text="New Book Name:", font=('tajawal', 12, 'bold'))
            book_label.pack(pady=10)

            newname = Entry(newWindow, textvariable=varNewName, width=30)
            newname.pack()

            add_button = Button(newWindow, text='Edit',
                                command=lambda: change_book(varOldName.get(), varNewName.get()))
            add_button.pack(pady=10)

            back_button = Button(newWindow, text="Back", command=newWindow.destroy)
            back_button.pack(pady=10)

            def change_book(old_name, new_name):
                with open('Sport.json', 'r') as file:
                    users = json.load(file)
                for user in users:
                    if user['text'] == old_name:
                        user['text'] = new_name
                        with open('Sport.json', 'w') as file:
                            json.dump(users, file)
                        messagebox.showinfo("Success", "The book has been changed.")
                        newWindow.destroy()
                        self.books()
                        return
                messagebox.showinfo("Error", "The book was not found.")

        add_button = Button(Fab, text="Edit Books", command=changebooks, width=15, fg='black', bg='#DBA901',
                            font=('tajawal', 16, 'bold'), )
        add_button.place(x=290, y=200)

        search_label = tk.Label(Fab, text="Search for Item:", bg='darkblue', fg='gold',
                                font=('tajawal', 16, 'bold'))
        search_label.place(x=230, y=460)

        search_entry = tk.Entry(Fab, width=18, justify='center')
        search_entry.place(x=400, y=466)
        back_button = tk.Button(Fab, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                command=self.back_to_home)
        back_button.place(x=20, y=20)

        search = Button(Fab, text='search', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                        command=search_book)
        search.place(x=320, y=490)

        varBook1 = IntVar()
        varBook2 = IntVar()
        varBook3 = IntVar()
        varBook4 = IntVar()
        varBook5 = IntVar()

        varPrice = StringVar()

        book1ent = Entry(Fab, textvariable=varBook1, width=18, justify='center')
        book1ent.place(x=25, y=310)

        book2ent = Entry(Fab, textvariable=varBook2, width=18, justify='center')
        book2ent.place(x=185, y=310)

        book3ent = Entry(Fab, textvariable=varBook3, width=18, justify='center')
        book3ent.place(x=345, y=310)

        book4ent = Entry(Fab, textvariable=varBook4, width=18, justify='center')
        book4ent.place(x=505, y=310)

        book5ent = Entry(Fab, textvariable=varBook5, width=18, justify='center')
        book5ent.place(x=665, y=310)


    def create_buttons(self):
        # حذف Buttons الحالية
        for button in self.F1.winfo_children():
            button.destroy()

        # ترتيب buttons بناء على الترتيب المحدد
        if self.sort_ascending:
            sorted_buttons = self.sort_ascending_custom(self.buttons, key=lambda x: x[0])  # ترتيب تصاعدي
        else:
            sorted_buttons = self.sort_descending_custom(self.buttons, key=lambda x: x[0])  # ترتيب تنازلي

        button_list = [(20, 10), (440, 10), (20, 80), (440, 80)]

        for i in range(len(button_list)):
            x, y = button_list[i]
            button_text = sorted_buttons[i]
            button = tk.Button(self.F1, text=button_text, width=26, fg='black', bg='#DBA901',
                               font=('tajawal', 16, 'bold'))
            button.place(x=x, y=y)
            if button_text == "Books":
                button.configure(command=self.books)
            elif button_text == "Electronics":
                button.configure(command=self.Electronics)
            elif button_text == "Fashion":
                button.configure(command=self.Fashion)
            elif button_text == "Sports":
                button.configure(command=self.Sports)
    def sort_ascending_custom(self, arr, key=lambda x: x):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if key(arr[j]) > key(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def sort_descending_custom(self, arr, key=lambda x: x):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if key(arr[j]) < key(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def toggle_sort(self):
        self.sort_ascending = not self.sort_ascending
        self.create_buttons()

    def back_to_home(self):
        self.shop.deiconify()



