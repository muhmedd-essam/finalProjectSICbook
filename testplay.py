from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()

image_path = "C:/Users/E S S A M/Desktop/315859822_1668378490224336_7890039000407411832_n.jpg"
desired_width = 200
desired_height = 200

# تحميل الصورة وتغيير حجمها
image = Image.open(image_path)
image = image.resize((desired_width, desired_height), Image.ANTIALIAS)

# إنشاء كائن PhotoImage وعرضه في Label
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.pack()

root.mainloop()