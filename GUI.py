from tkinter import *
from tkinter import font
from findAddress import *
from Map import *
from Tourspot import *
import tkinter.ttk
import random
import tkinter.messagebox
window = Tk()
window.geometry("800x1600")

def InitStartText():
    TempFont = font.Font(window, size = 15, weight = 'bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="역 검색")
    MainText.pack()
    MainText.place(x=30)

def InitInputLabelStart():
    global InputLabelS
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabelS = Entry(window, font = TempFont, width=10, borderwidth=12, relief='ridge')
    InputLabelS.pack()
    InputLabelS.place(x=10, y=40)

def InitStartSearchButton():

    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='검색', command=StartSearchButtonAction)
    #SearchButton.pack()
    SearchButton.place(x=150, y=50)

    #api를 읽어 리스트 3개 생성, 그래프 데이터 반환

def StartSearchButtonAction():
    global Lst_15, Lst_14, Lst_12, Lst_NumData
    #print(InputLabelS.get())
    address = findAddress(InputLabelS.get())
    y,x = getCoord(str(address))
    Lst_15 = searchTourSpot(str(x), str(y), 3000, '15')
    print(Lst_15)
    Lst_14 = searchTourSpot(str(x), str(y), 3000, '14')
    print(Lst_14)
    Lst_12 = searchTourSpot(str(x), str(y), 3000, '12')
    print(Lst_12)
    Lst_NumData = searchTourSpotNumbers(str(x), str(y), 3000)

    InitSearchListBox()
    print(Lst_NumData)


def SendTelegramButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='텔레그램으로 보내기', command='SearchButtonAction',#커맨드 수정 필요
                          width=30, height=3)
    SearchButton.pack()
    SearchButton.place(x=200, y=710)

def InitSearchButton_15():
    #축제/공연/행사
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='축제/공연/행사', command=StartSearchButtonAction_15)
    SearchButton.pack()
 #   SearchButton.place(x=50, y=800)


def InitSearchButton_14():
    #문화시설
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='문화시설', command=StartSearchButtonAction_14)
    SearchButton.pack()


def InitSearchButton_12():
    #관광지
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='관광지', command=StartSearchButtonAction_12)
    SearchButton.pack()

def InitSearchButton_Graph():
    #그래프
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='Graph', command=StartSearchButtonAction_Graph)
    SearchButton.pack()

def InitSearchButton_Map():
    #노선도
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='노선도', command=StartSearchButtonAction_Map)
    SearchButton.pack()

def InitSearchPharmacy():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='약국', command=StartSearchButtonAction_Pharmacy)
    SearchButton.pack()

def StartSearchButtonAction_15():
    global SearchListBox, Lst_15, Lst_14, Lst_12, Lst_NumData, LstBoxNum

    for i in range(LstBoxNum):
        SearchListBox.delete(0)

    LstBoxNum = 0
    for i in range(len(Lst_15)):
        SearchListBox.insert(i, Lst_15[i]['Name'])
        LstBoxNum += 1

def StartSearchButtonAction_14():
    global SearchListBox, Lst_15, Lst_14, Lst_12, Lst_NumData, LstBoxNum

    for i in range(LstBoxNum):
        SearchListBox.delete(0)

    LstBoxNum = 0
    for i in range(len(Lst_14)):
        SearchListBox.insert(i, Lst_14[i]['Name'])
        LstBoxNum += 1

def StartSearchButtonAction_12():
    global SearchListBox, Lst_15, Lst_14, Lst_12, Lst_NumData, LstBoxNum
    for i in range(LstBoxNum):
        SearchListBox.delete(0)

    LstBoxNum = 0
    for i in range(len(Lst_12)):
        SearchListBox.insert(i, Lst_12[i]['Name'])
        LstBoxNum += 1

def StartSearchButtonAction_Pharmacy():
    #약국
    pass

def InitSearchListBox():
    global SearchListBox, Lst_15, Lst_14, Lst_12, Lst_NumData, LstBoxNum
    LstBoxNum = 0
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=100)

    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none',
                            width=10, height=10, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    for i in range(len(Lst_15)):
        SearchListBox.insert(i, Lst_15[i]['Name'])
        LstBoxNum += 1

    SearchListBox.pack()
    SearchListBox.place(x=10, y=100)

    ListBoxScrollbar.config(command=SearchListBox.yview)


def StartSearchButtonAction_Map():
    global canvas
    canvas.delete(ALL)
    canvas.create_image(c_width / 2, c_height / 2, image=img)

def StartSearchButtonAction_Graph():
    global canvas
    canvas.delete(ALL)
    data2 = Lst_NumData
    start = 0
    s = sum(data2)

    for i in range(3):
        extent = data2[i] / s * 360
        color = random_color()
        canvas.create_arc((0, 0, 300, 300), fill=color, outline='white', start=start, extent=extent)
        start = start + extent
        canvas.create_rectangle(300, 20 + 20 * i, 300 + 30, 20 + 20 * (i + 1), fill=color)
        canvas.create_text(300 + 50, 10 + 20 * (i + 1), text=str(data2[i]))

    canvas.create_text(300 + 120, 10 + 20 * 1, text='개의 축제/공연/행사')
    canvas.create_text(300 + 120, 10 + 20 * 2, text='개의 문화시설')
    canvas.create_text(300 + 120, 10 + 20 * 3, text='개의 관광지')



def random_color():
    color = '#'
    colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(6):
        color += colors[random.randint(0, 15)]
    return color

def Buttons():
    InitStartSearchButton()
    #리스트 박스 내용 변경 버튼
    InitSearchButton_15()
    InitSearchButton_14()
    InitSearchButton_12()

    #캔버스 변경
    InitSearchPharmacy()
    InitSearchButton_Map()
    InitSearchButton_Graph()

    Button(window, text='folium 지도', command=Pressed).pack()

c_height = 400
c_width = 500

LstBoxNum = 0
Lst_15 = []
Lst_14 = []
Lst_12 = []
Lst_NumData = []

InitInputLabelStart()
InitStartText()
Buttons()
InitSearchListBox()

canvas = Canvas(window, bg='white', width=c_width, height=c_height)
canvas.pack()
canvas.place(x=200, y=300)
img = PhotoImage(file="image/smap.png")
canvas.create_image(c_width/2, c_height/2, image=img)

window.mainloop()