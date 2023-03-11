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


#new window create
def open_w():
    a = Toplevel()
    a.geometry("1024x640")
    a.iconphoto(False, icon)
    a.title("Матричная кодировка")

    #clear fields
    def delete_content():
        textw.delete(1.0, END)

    #matrix encode/decode
    def matrix_encode():
        message = textw.get(1.0, END)
            # !!!КЛЮЧИ!!!
        KEYH = {"М": 0, "У": 0, "Н1": 0, "И1": 0, "Ц": 0, "И2": 0, "П": 0, "А": 0, "Л": 0, "Ь": 0, "Н2": 0, "Ы": 0, "Й": 0}
        KEYV = {"Ц": 0, "Е": 0, "Н": 0, "Т": 0, "Р": 0}
        # !!!КЛЮЧИ ДЛЯ СОЗДАНИЯ МАТРИЦЫ!!!
        VerticalKey = ["Ц", "Е", "Н", "Т", "Р"]
        HorisontalKey = ["М", "У", "Н", "И", "Ц", "И", "П", "А", "Л", "Ь", "Н", "Ы", "Й"]
        # Матричный блок, инструменты
        uncount = False
        oncount = False
        outstr = ""
        MatrixBlock = []
        BlankMass = []
        j = 0
        ja = 0

        for i in message:
            j += 1
            ja += 1
            BlankMass.append(i)

            # Несоответствие количества символов
            # Нехватка
            if ja == len(message):
                if (j != len(HorisontalKey)) or (len(MatrixBlock) < len(VerticalKey)):
        
                    r = (len(VerticalKey) * len(HorisontalKey)) - ((len(MatrixBlock) * len(HorisontalKey)) + len(BlankMass))
                    if r != 0:
                        if r % len(HorisontalKey) != 0:
                            for bm in range(r % len(HorisontalKey)):
                                BlankMass.append('.')
                            MatrixBlock.append(BlankMass)
                            BlankMass = []
                        if len(MatrixBlock) < len(VerticalKey):
                            for mb in range(len(VerticalKey) - len(MatrixBlock)):
                                BlankMass = []
                                for bm in range(len(HorisontalKey)):
                                    BlankMass.append('.')
                                MatrixBlock.append(BlankMass)
                                BlankMass = []
                    uncount = True

            # Перебор
            if (ja < len(message)) and (len(MatrixBlock) == len(VerticalKey)):
                oncount = True

            # Соответствие
            if j == len(HorisontalKey):
                j = 0
                MatrixBlock.append(BlankMass)
                BlankMass = []
    
            # Условие на сходство длинны сообщения с количеством доступных символов в матричном блоке/недобором/перебором
            if (len(MatrixBlock) == len(VerticalKey) or uncount or oncount):
                uncount = False
                oncount = False

                # Горизонтальная сортировка
                k = 0
                for vk in KEYV:
                    KEYV[vk] = MatrixBlock[k]
                    k += 1
                SORTKEYV = sorted(KEYV.items())
                MatrixBlock = []
    
                # Вертикальная сортировка
                k = 0
                elem = []
                for hk in KEYH:
                    for strng in SORTKEYV:
                        elem.append(strng[1][k])
                        KEYH[hk] = elem
                    k += 1
                    elem = []
                SORTKEYH = sorted(KEYH.items())

                # Преобразование в строку
                for strng in SORTKEYH:
                    elem.append(strng[1])
                for s in elem:
                    for n in s:
                        outstr += n

            # Возврат значения
        textw.delete(1.0, END)
        textw.insert(END, outstr)

    def matrix_decode():
        message = textw.get(1.0, END)
            # !!!КЛЮЧИ!!!
        KEYH = {"М": 0, "У": 0, "Н1": 0, "И1": 0, "Ц": 0, "И2": 0, "П": 0, "А": 0, "Л": 0, "Ь": 0, "Н2": 0, "Ы": 0, "Й": 0}
        KEYV = {"Ц": 0, "Е": 0, "Н": 0, "Т": 0, "Р": 0}
        # !!!КЛЮЧИ ДЛЯ СОЗДАНИЯ МАТРИЦЫ!!!
        VerticalKey = ["Ц", "Е", "Н", "Т", "Р"]
        HorisontalKey = ["М", "У", "Н", "И", "Ц", "И", "П", "А", "Л", "Ь", "Н", "Ы", "Й"]
        # Матричный блок, инструменты
        DESORTV = {"Ц": 0, "Е": 0, "Н": 0, "Т": 0, "Р": 0}
        DESORTH = {"М": 0, "У": 0, "Н1": 0, "И1": 0, "Ц": 0, "И2": 0, "П": 0, "А": 0, "Л": 0, "Ь": 0, "Н2": 0, "Ы": 0,
                   "Й": 0}
        oncount = False
        outstr = ""
        MatrixBlock = []
        BlankMass = []
        j = 0
        ja = 0

        for i in message:
            j += 1
            ja += 1
            BlankMass.append(i)

            # Перебор
            if (ja < len(message)) and (len(MatrixBlock) == len(HorisontalKey)):
                oncount = True
                print(MatrixBlock)

            # Соответствие
            if j == len(VerticalKey):
                j = 0
                MatrixBlock.append(BlankMass)
                BlankMass = []

            if (len(MatrixBlock) == len(HorisontalKey)) or oncount:
                oncount = False

                # Вертикальная десортировка
                k = 0
                elem = []
                for got in sorted(KEYH):
                    DESORTH[got] = MatrixBlock[k]
                    k += 1
                MatrixBlock = []

                # Горизонтальная десортировка
                elements = list(DESORTH.items())

                k = 0
                elem = []
                elemout = []
                for elm in range(len(DESORTV)):
                    for el in elements:
                        if k < 5:
                            elem.append(el[1][k])
                        if len(elem) == len(DESORTH):
                            elemout.append(elem)
                            elem = []
                            k += 1

                k = 0
                for got in sorted(KEYV):
                    DESORTV[got] = elemout[k]
                    k += 1

                # Преобразование в строку
                elements = list(DESORTV.items())
                for el in elements:
                    for elms in el[1]:
                        outstr += elms
        #outstr = outstr.replace('.', '')
        textw.delete(1.0, END)
        textw.insert(END, outstr)
    
    #interface block
    textw = Text(a, width=50, height=1080)
    textw.pack(side=LEFT)
    scrollw = Scrollbar(a, command=textw.yview)
    scrollw.pack(side=LEFT, fill=Y)
    textw.config(yscrollcommand=scrollw.set)

    framew = Frame(a)
    framew.pack()
    Button(framew, text="Зашифровать",
           command=matrix_encode, height=5, width=30).pack(side=LEFT)
    Button(framew, text="Разшифровать",
           command=matrix_decode, height=5, width=30).pack(side=LEFT)
    Button(framew, text="Удалить",
           command=delete_content, height=5, width=30).pack(side=LEFT)




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


  
#pic -> text
def encode(filepath):
    binary = binary_pict(filepath)
    text.delete(1.0, END)
    text.insert(1.0, binary)
    
def insert_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        label['text'] = ""
        encode(filepath)
    else:
        label['text'] = "!!!_Некорректный путь! Повторите попытку._!!!"
   
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
text = Text(width=50, height=1080)
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

Button(frame, text="Зашифровать/Разшифровать",
       command=replace, height=5, width=30).pack()
label = Label(width=40, heigh=4)
label.pack()


matrixframe = Frame()
matrixframe.pack()
matrixtext = Label(matrixframe, text='Матричный шифровщик:', height=2, width=30)
matrixtext.pack(side=TOP)
Button(matrixframe, text="Открыть!",
       command=open_w, height=5, width=30).pack(side=LEFT)



root.mainloop()
