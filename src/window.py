from tkinter import *
from tkinter import filedialog
from PIL import *
from PIL import Image, ImageTk
 
root = Tk()
root.geometry("600x400")
 
root.title("Кодировка изображения")
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)

def img(filepath):
    img = ImageTk.PhotoImage(Image.open(filepath))
    label = root.Label(window, image = img)
    label.pack(side = "bottom", fill = "both", expand = "yes")

    
def insert_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        img(filepath)
    
 
def get_text():
    s = text.get(1.0, END)
    label['text'] = s
 
 
def delete_text():
    text.delete(1.0, END)

 
labelMain = Label(text="Вставьте код")
labelMain.pack()

text = Text(width=40, height=10)
text.pack()
frame = Frame()
frame.pack()

Button(frame, text="Вставить изображение",
       command=insert_file).pack(side=LEFT)
Button(frame, text="Отобразить фото",
       command=get_text).pack(side=LEFT)
Button(frame, text="Удалить",
       command=delete_text).pack(side=LEFT)
 
label = Label()
label.pack()




root.mainloop()
