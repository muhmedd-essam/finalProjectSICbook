from tkinter import *
import json
from tkinter import messagebox
import tkinter as tk
from LOGIN_USER import LoginApplication
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.resizable(False, False)
        self.window.geometry('1366x768')
        # self.window.state('zoomed')
        self.window.title('SICbook')
        self.window.iconbitmap('images/logo_transparent.ico')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "SICbook"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)
        image_path = "images/facebook_profile_image.png"
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
        label = Label(self.lgn_frame, bg="#040405")
        label.config(image=photo)
        label.image = photo
        label.place(x=640, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Email", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white' , command=self.login)
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)
        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405", command=self.open_register_window)
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')
    def login(self):
        email = self.username_entry.get()
        password = self.password_entry.get()
        check=""
        if email == check:
             return messagebox.showinfo("Email","Please Enter Your Email!")
        if password == check:
             return messagebox.showinfo("Password","Please Enter Your Password!")



        # Load user data from JSON file
        with open('users.json', 'r') as file:
            users = json.load(file)
        with open('logeIn.json', 'r') as file:
            user = json.load(file)

        found = False
        for i in range(len(users)):
            if users[i]["email"] == email and users[i]["password"] == password:
                name = users[i]["name"]
                messagebox.showinfo("Login Successful", f"Welcome {name}!")
                found = True
                users[i]["Connect"] = "Done"

                with open('users.json', 'w') as file:
                    json.dump(users, file)
                account = users[i]
                user.append(account)
                with open('logeIn.json', 'w') as file:
                    json.dump(user, file)

                self.window.destroy()
                LoginApplication(tk.Tk())
        if found == False:
            messagebox.showerror("Login Failed", "Invalid email or password.")
    def browse_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])



    def open_register_window(self):
        self.window.destroy()
        register_app = RegisterApplication(tk.Tk())


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()



class RegisterApplication:
    def __init__(self, window):
        self.window = window
        self.window.resizable(False, False)
        self.window.geometry('1366x768')
        # self.window.state('zoomed')
        self.window.title('SICbook')
        self.window.iconbitmap('images/logo_transparent.ico')
        # ============================background image============================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)
        # ========================================================================
        self.txt = "SICbook"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)
        # ============ Left Side Image ================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)
        # ============ Sign In Image =============================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=10)
        image_path = "images/facebook_profile_image.png"
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
        label = Label(self.lgn_frame, bg="#040405")
        label.config(image=photo)
        label.image = photo
        label.place(x=640, y=10)
        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign Up", bg="#040405", fg="white",
                                   font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=120)


        # ========================================================================
        # ============================Email====================================
        # ========================================================================
        self.Email_label = Label(self.lgn_frame, text="Email", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.Email_label.place(x=550, y=150)

        self.Email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.Email_entry.place(x=580, y=182, width=270)

        self.Email_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.Email_line.place(x=550, y=209)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=182)


        # ============================Register button================================

        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=490)
        self.login = Button(self.lgn_button_label, text='REGISTER', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.register)
        self.login.place(x=20, y=10)

        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='You have an accoumt?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=510, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=220)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=580, y=252, width=244)
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=279)
        # ========================================================================
        # ============================Username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="User Name", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=290)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=325, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=349)
        # ========================================================================
        # ============================Age====================================
        # ========================================================================
        self.Age_label = Label(self.lgn_frame, text="Age", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.Age_label.place(x=550, y=360)

        self.Age_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.Age_entry.place(x=580, y=395, width=270)

        self.Age_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.Age_line.place(x=550, y=419)
        # ========================================================================
        # ============================Age====================================
        # ========================================================================
        self.browse_button = tk.Button(self.lgn_frame, text="Browse", command=self.browse_image, bg="#040405",fg="white", height=1,width=20)
        self.browse_button.place(x=630, y=449)
        self.Age_label = Label(self.lgn_frame, text="Image", bg="#040405", fg="#4f4e4d",
                               font=("yu gothic ui", 13, "bold"))
        self.Age_label.place(x=550, y=425)

        self.Age_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.Age_line.place(x=550, y=479)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=390)
        # ===== Email icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=320)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=250)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')


        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=257)
    def browse_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    def register(self):
        email = self.Email_entry.get()
        name = self.username_entry.get()
        password = self.password_entry.get()
        age = self.Age_entry.get()
        Photo = self.image_path
        check = ""

        try:
            with open('users.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        if email == check:
             return messagebox.showinfo("Email","Please Enter Your Email!")
        if password == check:
             return messagebox.showinfo("Password","Please Enter Your Password!")
        if name == check:
             return messagebox.showinfo("User Name","Please Enter Your Name!")
        if age == check:
             return messagebox.showinfo("Age","Please Enter Your Age!")
        for i in range(len(users)):
            if email in users :
                return messagebox.showinfo("Email", "This Email are used, please try another email")
        for i in range(len(users)):
            if name in users:
                return messagebox.showinfo("User Name", "This user name is used, Please try another user name")

        # Add new user data
        newUsers = {"email":email,
            "name": name,
            "password": password,
            "age": age,
            "profile": Photo,
            "Connect": ""
        }
        users.append(newUsers)

        # Save updated user data to JSON file
        with open('users.json', 'w') as file:
            json.dump(users, file)

        messagebox.showinfo("Registration Successful", "Registration completed successfully.")

        self.window.destroy()
        login_app = LoginPage(tk.Tk())

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=257)
        self.password_entry.config(show='')
    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=257)
        self.password_entry.config(show='*')

if __name__ == '__main__':
    page()
