from tkinter import *
from tkinter import font
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
    global InputLabel
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width=10, borderwidth=12, relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=40)

def InitInputLabelEnd():
    global InputLabel
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width=10, borderwidth=12, relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=400, y=40)

def InitStartSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='검색', command='SearchButtonAction')
    SearchButton.pack()
    SearchButton.place(x=150, y=50)

def StartSearchButtonAction():
    pass

def InitEndSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='검색', command='SearchButtonAction')
    SearchButton.pack()
    SearchButton.place(x=540, y=50)

def EndSearchButtonAction():
    pass

def SendTelegramButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='텔레그램으로 보내기', command='SearchButtonAction',
                          width=30, height=3)
    SearchButton.pack()
    SearchButton.place(x=200, y=710)

'''
def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
    TempFont = font.Font(window, size=10, family='Consolas')
    RenderText = Text(window, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')
'''

def InitMapCanvas():
    canvas = Canvas(window, bg='white', width=500, height=600)
    canvas.pack()
    canvas.place(x=50, y=100)

InitStartSearchButton()
StartSearchButtonAction()
InitEndSearchButton()
EndSearchButtonAction()
InitInputLabelStart()
InitInputLabelEnd()
InitStartText()
InitEndText()
InitMapCanvas()
SendTelegramButton()

window.mainloop()