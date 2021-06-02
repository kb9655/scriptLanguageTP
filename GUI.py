from tkinter import *
from tkinter import font
from findAddress import *
from Map import *
from Tourspot import searchTourSpot


import tkinter.messagebox
window = Tk()
window.geometry("600x1600")

def InitStartText():
    TempFont = font.Font(window, size = 15, weight = 'bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="출발역")
    MainText.pack()
    MainText.place(x=30)

def InitEndText():
    TempFont = font.Font(window, size = 15, weight = 'bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="도착역")
    MainText.pack()
    MainText.place(x=405)

def InitInputLabelStart():
    global InputLabelS
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabelS = Entry(window, font = TempFont, width=10, borderwidth=12, relief='ridge')
    InputLabelS.pack()
    InputLabelS.place(x=10, y=40)

def InitInputLabelEnd():
    global InputLabelE
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabelE = Entry(window, font = TempFont, width=10, borderwidth=12, relief='ridge')
    InputLabelE.pack()
    InputLabelE.place(x=400, y=40)

def InitStartSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='검색', command=StartSearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=150, y=50)

def InitEndSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='검색', command=EndSearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=540, y=50)


def StartSearchButtonAction():
    print(InputLabelS.get())
    address = findAddress(InputLabelS.get())
    y,x = getCoord(str(address))
    print(x)
    searchTourSpot(str(x), str(y), 3000)


def EndSearchButtonAction():
    print(InputLabelS.get())
    address = findAddress(InputLabelE.get())
    y,x = getCoord(str(address))
    print(x)
    searchTourSpot(str(x), str(y), 3000)

def SendTelegramButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='텔레그램으로 보내기', command='SearchButtonAction',#커맨드 수정 필요
                          width=30, height=3)
    SearchButton.pack()
    SearchButton.place(x=200, y=710)

def InitMapCanvas():
    canvas = Canvas(window, bg='white', width=500, height=600)
    canvas.pack()
    canvas.place(x=50, y=100)

InitStartSearchButton()
InitEndSearchButton()
InitInputLabelStart()
InitInputLabelEnd()
InitStartText()
InitEndText()
InitMapCanvas()
print("a")


window.mainloop()