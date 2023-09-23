from tkinter import *

def sendMessage():
    message = entryMessage.get()
    sender = currentSender.get()

    chatLog.insert(END, sender + ": " + message + "\n")  # add the message to the chat

def clearChat():  # clear your entire chat history
   chatLog.delete(1.0, END)

# create chat
Root = Tk()
Root.title("Chats")

Root.geometry("570x770")



# add elements
chatLog = Text(Root, width=50, height=15,fg="white", bg="black")
chatLog.pack(padx=10,pady=10)

labelMessage = Label(Root, text="Message:",fg="white", bg="black")
labelMessage.pack(padx=5,pady=5)

entryMessage = Entry(Root, width=67,fg="white", bg="black")
entryMessage.pack(padx=5,pady=5)

currentSender = StringVar()
currentSender.set("Ahmed")
#######################################################################################################
radioAhmed = Radiobutton(Root, text="Ahmed", variable=currentSender, value="Ahmed", fg="white", bg="blue")
radioAhmed.pack(anchor=N)
radioAhmed.pack(padx=1,pady=10)

radioSalah = Radiobutton(Root, text="Salah", variable=currentSender, value="Salah", fg="white", bg="brown")
radioSalah.pack(anchor=W)
radioSalah.pack(padx=1,pady=10)

radioMohamed = Radiobutton(Root, text="Mohamed", variable=currentSender, value="Mohamed", fg="white", bg="brown")
radioMohamed.pack(anchor=W)
radioMohamed.pack(padx=1,pady=10)


radioYara = Radiobutton(Root, text="Yara", variable=currentSender, value="Yara", fg="white", bg="green")
radioYara.pack(anchor=N)
radioYara.pack(padx=1,pady=10)

radioToka = Radiobutton(Root, text="Toka", variable=currentSender, value="Toka", fg="white", bg="green")
radioToka.pack(anchor=N)
radioToka.pack(padx=1,pady=10)

radioMarwa = Radiobutton(Root, text="Marwa", variable=currentSender, value="Marwa", fg="white", bg="grey")
radioMarwa.pack(anchor=E)
radioMarwa.pack(padx=1,pady=10)

radioMenna = Radiobutton(Root, text="Menna", variable=currentSender, value="Menna", fg="white", bg="grey")
radioMenna.pack(anchor=E)
radioMenna.pack(padx=1,pady=10)

################################################################################################################
buttonSend = Button(Root, text="Send", command=sendMessage,fg="white", bg="black")
buttonSend.pack(padx=10,pady=10)

buttonClear_chat = Button(Root, text="Completely Delete Chat", command=clearChat,fg="white", bg="black")
buttonClear_chat.pack(padx=10,pady=10)

frame = Frame(Root, bg="blue")
frame.pack(fill=BOTH, expand=True)


# تشغيل واجهة المستخدم
Root.mainloop()