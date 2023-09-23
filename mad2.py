from tkinter import Tk, Text, Label, Entry, Radiobutton, Button, StringVar, Frame, BOTH, END

class ChatApplication(Tk):
    def __init__(self):
        super().__init__()
        self.title("Chats")
        self.geometry("570x770")

        self.create_widgets()

    def create_widgets(self):
        self.chatLog = Text(self, width=50, height=15, fg="white", bg="black")
        self.chatLog.pack(padx=10, pady=10)

        self.labelMessage = Label(self, text="Message:", fg="white", bg="black")
        self.labelMessage.pack(padx=5, pady=5)

        self.entryMessage = Entry(self, width=67, fg="white", bg="black")
        self.entryMessage.pack(padx=5, pady=5)

        self.currentSender = StringVar()
        self.currentSender.set("Ahmed")

        #######################################################################################################
        self.radioAhmed = Radiobutton(self, text="Ahmed", variable=self.currentSender, value="Ahmed", fg="white", bg="blue")
        self.radioAhmed.pack(anchor="n")
        self.radioAhmed.pack(padx=1, pady=10)

        self.radioSalah = Radiobutton(self, text="Salah", variable=self.currentSender, value="Salah", fg="white", bg="brown")
        self.radioSalah.pack(anchor="w")
        self.radioSalah.pack(padx=1, pady=10)

        self.radioMohamed = Radiobutton(self, text="Mohamed", variable=self.currentSender, value="Mohamed", fg="white", bg="brown")
        self.radioMohamed.pack(anchor="w")
        self.radioMohamed.pack(padx=1, pady=10)

        self.radioYara = Radiobutton(self, text="Yara", variable=self.currentSender, value="Yara", fg="white", bg="green")
        self.radioYara.pack(anchor="n")
        self.radioYara.pack(padx=1, pady=10)

        self.radioToka = Radiobutton(self, text="Toka", variable=self.currentSender, value="Toka", fg="white", bg="green")
        self.radioToka.pack(anchor="n")
        self.radioToka.pack(padx=1, pady=10)

        self.radioMarwa = Radiobutton(self, text="Marwa", variable=self.currentSender, value="Marwa", fg="white", bg="grey")
        self.radioMarwa.pack(anchor="e")
        self.radioMarwa.pack(padx=1, pady=10)

        self.radioMenna = Radiobutton(self, text="Menna", variable=self.currentSender, value="Menna", fg="white", bg="grey")
        self.radioMenna.pack(anchor="e")
        self.radioMenna.pack(padx=1, pady=10)

        ################################################################################################################
        self.buttonSend = Button(self, text="Send", command=self.send_message, fg="white", bg="black")
        self.buttonSend.pack(padx=10, pady=10)

        self.buttonClearChat = Button(self, text="Completely Delete Chat", command=self.clear_chat, fg="white", bg="black")
        self.buttonClearChat.pack(padx=10, pady=10)

        self.frame = Frame(self, bg="blue")
        self.frame.pack(fill=BOTH, expand=True)

    def send_message(self):
        message = self.entryMessage.get()
        sender = self.currentSender.get()

        self.chatLog.insert(END, sender + ": " + message + "\n")

    def clear_chat(self):
        self.chatLog.delete(1.0, END)

    def run(self):
        self.mainloop()



