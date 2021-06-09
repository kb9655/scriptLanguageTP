from tkinter import *
from tkinter import font
from findAddress import *
from Tourspot import *
from Pharmacy import *
import tkinter.ttk
import random
import tkinter.messagebox

import threading
import sys
import folium
from cefpython3 import cefpython as cef

from io import BytesIO
from PIL import Image,ImageTk

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

def SendTelegramButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='텔레그램으로 보내기', command='SearchButtonAction',#커맨드 수정 필요
                          width=30, height=3)
    SearchButton.pack()
    SearchButton.place(x=50, y=800)

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

def InitSerachButton_folium():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='folium 지도', command=Pressed)
    SearchButton.place(x=10, y=680)

def InitSearchButton_15():
    #축제/공연/행사
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='축제/공연/행사', command=StartSearchButtonAction_15)
    SearchButton.place(x=10, y=400)
 #   SearchButton.place(x=50, y=800)

def InitSearchButton_14():
    #문화시설
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='문화시설', command=StartSearchButtonAction_14)
    SearchButton.place(x=10, y=440)

def InitSearchButton_12():
    #관광지
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='관광지', command=StartSearchButtonAction_12)
    SearchButton.place(x=10, y=480)

def InitSearchButton_Graph():
    #그래프
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='Graph', command=StartSearchButtonAction_Graph)
    SearchButton.place(x=10, y=520)

def InitSearchButton_Map():
    #노선도
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='노선도', command=StartSearchButtonAction_Map)
    SearchButton.place(x=10, y=560)

def InitSearchPharmacy():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='약국', command=StartSearchButtonAction_Pharmacy)
    SearchButton.place(x=10, y=600)

def InitShowInfo():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text='정보', command=StartSearchButtonActionShowInfo)
    SearchButton.place(x=10, y=640)

def StartSearchButtonActionShowInfo():
    global SearchListBox, Lst_Now, Xpos_Now, Ypos_Now, PopUp_Now, canvas
    iSearchIndex = SearchListBox.curselection()[0]

    Xpos_Now = Lst_Now[iSearchIndex]['xPos']
    Ypos_Now = Lst_Now[iSearchIndex]['yPos']
    PopUp_Now = Lst_Now[iSearchIndex]['Name']
    #print(Xpos_Now)
    #print(Ypos_Now)

    canvas.delete(ALL)
    #정보 삽입
    canvas.create_text(150,100,text = Lst_Now[iSearchIndex]['Name'])
    canvas.create_text(150, 120, text=Lst_Now[iSearchIndex]['address'])
    canvas.create_text(150, 140, text=Lst_Now[iSearchIndex]['image'])
    '''
    url = Lst_Now[iSearchIndex]['image']
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()

    im = Image.open(BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)

    Label(canvas, image=image, height=400, width=400).pack()
    '''

def StartSearchButtonAction_15():
    global SearchListBox, Lst_15, Lst_NumData, LstBoxNum,Lst_Now
    Lst_Now = Lst_15
    for i in range(LstBoxNum):
        SearchListBox.delete(0)

    LstBoxNum = 0
    for i in range(len(Lst_15)):
        SearchListBox.insert(i, Lst_15[i]['Name'])
        LstBoxNum += 1

def StartSearchButtonAction_14():
    global SearchListBox,Lst_14, Lst_NumData, LstBoxNum,Lst_Now
    Lst_Now = Lst_14
    for i in range(LstBoxNum):
        SearchListBox.delete(0)

    LstBoxNum = 0
    for i in range(len(Lst_14)):
        SearchListBox.insert(i, Lst_14[i]['Name'])
        LstBoxNum += 1

def StartSearchButtonAction_12():
    global SearchListBox,  Lst_12, Lst_NumData, LstBoxNum, Lst_Now
    Lst_Now = Lst_12
    for i in range(LstBoxNum):
        SearchListBox.delete(0)

    LstBoxNum = 0
    for i in range(len(Lst_12)):
        SearchListBox.insert(i, Lst_12[i]['Name'])
        LstBoxNum += 1

def StartSearchButtonAction_Pharmacy():
    global SearchListBox,Lst_Phar, LstBoxNum, Lst_Now
    Lst_Now = Lst_Phar
    for i in range(LstBoxNum):
        SearchListBox.delete(0)

    LstBoxNum = 0
    for i in range(len(Lst_Phar)):
        SearchListBox.insert(i, Lst_Phar[i]['Name'])
        LstBoxNum += 1

def StartSearchButtonAction():
    global Lst_15, Lst_14, Lst_12, Lst_NumData,Lst_Phar,InputLabelS
    #print(InputLabelS.get())
    address = findAddress(InputLabelS.get())
    y,x = getCoord(str(address))
    Lst_15 = searchTourSpot(str(x), str(y), 1000, '15')
    print(Lst_15)
    Lst_14 = searchTourSpot(str(x), str(y), 1000, '14')
    print(Lst_14)
    Lst_12 = searchTourSpot(str(x), str(y), 1000, '12')
    print(Lst_12)
    Lst_NumData = searchTourSpotNumbers(str(x), str(y), 1000)
    Lst_Phar = searchParmacy(str(x), str(y), 1000)
    print(Lst_Phar)


    InitSearchListBox()
    print(Lst_NumData)

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
    global frame1
    InitStartSearchButton()
    #리스트 박스 내용 변경 버튼
    InitSearchButton_15()
    InitSearchButton_14()
    InitSearchButton_12()
    InitShowInfo()

    #캔버스 변경
    InitSearchPharmacy()
    InitSearchButton_Map()
    InitSearchButton_Graph()
    InitSerachButton_folium()

# cef모듈로 브라우저 실행
def showMap(frame2):
    sys.excepthook = cef.ExceptHook
    window_info = cef.WindowInfo(frame2.winfo_id())
    window_info.SetAsChild(frame2.winfo_id(), [0,0,800,600])
    cef.Initialize()
    browser = cef.CreateBrowserSync(window_info, url='file:///map.html')
    cef.MessageLoop()

def Pressed():
    global Xpos_Now, Ypos_Now,PopUp_Now
    # 지도 저장
    # 위도 경도 지정
    m = folium.Map(location=[Ypos_Now, Xpos_Now], zoom_start=13)
    # 마커 지정
    folium.Marker([Ypos_Now, Xpos_Now], popup=PopUp_Now).add_to(m)
    # html 파일로 저장
    m.save('map.html')

    # 브라우저를 위한 쓰레드 생성
    thread = threading.Thread(target=showMap, args=(frame2,))
    thread.daemon = True
    thread.start()

window = Tk()
window.geometry("800x1600")
frame1 = Frame(window, width=800, height=800)
frame1.pack()
frame2 = Frame(window, width=800, height=600)
frame2.pack()
c_height = 400
c_width = 500

LstBoxNum = 0
Lst_15 = []
Lst_14 = []
Lst_12 = []
Lst_NumData = []
Lst_Phar=[]
Lst_Now=[]
Xpos_Now = 0
Ypos_Now = 0
PopUp_Now = ''

InitInputLabelStart()
InitStartText()
Buttons()
InitSearchListBox()

canvas = Canvas(frame1, bg='white', width=c_width, height=c_height)
canvas.pack(side="right")
#canvas.place(x=200, y=300)
img = PhotoImage(file="image/smap.png")
canvas.create_image(c_width/2, c_height/2, image=img)

window.mainloop()