#window pack
from tkinter import *
from tkinter import filedialog
from PIL import *
from PIL import Image, ImageTk

#picture pack
from base64 import b64encode as enc64
from base64 import b64decode as dec64
from io import BytesIO
from PIL import Image

#window
root = Tk()
root.geometry("1280x720")
 
root.title("Кодировка изображения")
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)


#picture create func
def binary_pict(pict):
    with open(pict, 'rb') as f:
        binary = enc64(f.read())
    return binary

def export(binary):
    image = BytesIO(dec64(binary))
    pillow = Image.open(image)
    
    pillow.save('new.png')
    pillow.show()


#window func
#pic -> text
def encode(filepath):
    binary = binary_pict(filepath)
    text.insert(1.0, binary)
    
def insert_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        label['text'] = ""
        encode(filepath)
    else:
        label['text'] = "Некорректный путь! Повторите попытку."
   
#text -> pic
def get_binary():
    getbinary = text.get(1.0, END)
    export(getbinary)

#clear fields
def delete_content():
    text.delete(1.0, END)

#encode/decode func
def replace():
    firstMass = text.get(1.0, END)
    middleMass = []
    finalMass = []
    n = 0
    out = ''

    for i in firstMass:
        n += 1
        
        if len(middleMass) < 2:
            middleMass.append(i)
            
            if (n == len(firstMass)) and (len(middleMass) == 1):
                finalMass.append(i)
                break
            
        if len(middleMass) == 2:
            middleMass.reverse()

            for j in middleMass:
                finalMass.append(j)
                
            middleMass = []

    for i in finalMass:
        out += i
    finalMass = []
    
    text.delete(1.0, END)
    text.insert(1.0, out)
    
#interface block
text = Text(width=80, height=1080)
text.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

frame = Frame()
frame.pack()
Button(frame, text="Вставить изображение",
       command=insert_file, height=5, width=30).pack(side=LEFT)
Button(frame, text="Отобразить фото",
       command=get_binary, height=5, width=30).pack(side=LEFT)
Button(frame, text="Удалить",
       command=delete_content, height=5, width=30).pack(side=LEFT)

secondframe = Frame()
secondframe.pack()
Button(secondframe, text="Зашифровать/Разшифровать",
       command=replace, height=5, width=30).pack()
 
label = Label(width=40, heigh=10)
label.pack()


root.mainloop()
