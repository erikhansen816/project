#Erik Hansen
#11/1/2017
#calculator.py - program to make calculator applet

from ggame import *

black = black = Color(0x000000,1)
blackoutline = LineStyle(1,black)
white = Color(0xFFFFFF,0)
red = Color(0xFF0000,.5)
n = 1
text1 = TextAsset(1,fill=black, style = 'bold 35pt Times')
text2 = TextAsset(2,fill=black, style = 'bold 35pt Times')
text3 = TextAsset(3,fill=black, style = 'bold 35pt Times')
text4 = TextAsset(4,fill=black, style = 'bold 35pt Times')
text5 = TextAsset(5,fill=black, style = 'bold 35pt Times')
text6 = TextAsset(6,fill=black, style = 'bold 35pt Times')
text7 = TextAsset(7,fill=black, style = 'bold 35pt Times')
text8 = TextAsset(8,fill=black, style = 'bold 35pt Times')
text9 = TextAsset(9,fill=black, style = 'bold 35pt Times')
text10 = TextAsset('+/-',fill=black, style = 'bold 30pt Times')
text11 = TextAsset(0,fill=black, style = 'bold 35pt Times')
text12 = TextAsset('.',fill=black, style = 'bold 35pt Times')
text13 = TextAsset('/',fill=black, style = 'bold 35pt Times')
text14 = TextAsset('x',fill=black, style = 'bold 35pt Times')
text15 = TextAsset('+',fill=black, style = 'bold 35pt Times')
text16 = TextAsset('=',fill=black, style = 'bold 35pt Times')

calcoutline = RectangleAsset(300,350,blackoutline,white)
answerbar = RectangleAsset(275,50,blackoutline,white)
keys = RectangleAsset(55,55,blackoutline,white)
equalkey = RectangleAsset(55,55,blackoutline,red)

Sprite(calcoutline)
Sprite(answerbar, (12.5,12.5))
Sprite(text1,(28,85))
Sprite(text2,(28+72.5,85))
Sprite(text3,(28+72.5*2,85))
Sprite(text4,(28,85+68))
Sprite(text5,(28+72.5,85+68))
Sprite(text6,(28+72.5*2,85+68))
Sprite(text7,(28,85+68*2))
Sprite(text8,(28+72.5,85+68*2))
Sprite(text9,(28+72.5*2,85+68*2))
Sprite(text10,(15,85+68*3))
Sprite(text11,(28+72.5,85+68*3))
Sprite(text12,(28+72.5*2,85+68*3))
Sprite(text13,(28+72.5*3,85))
Sprite(text14,(28+72.5*3,85+68))
Sprite(text15,(28+72.5*3,85+68*2))
Sprite(text16,(28+72.5*3,85+68*3))

for j in range(4):
    for i in range(4):
        Sprite(keys,(12.5 + 72.5*i, 80 + 68*j))
        if i == 3 and j == 3:
            Sprite(equalkey, (230,284))

def mouseClick(event):
    timesclicked=0
    n=0
    timesclicked+=1
    if timesclicked == 2:
        n+=1
    if event.x>28 and event.x<(28+55) and event.y>85 and event.y<(85+55):
        Sprite(text1, ((260-30*n), 13))
    if event.x>28+72.5 and event.x<(28+72.5+55) and event.y>85 and event.y<(85+55):
        Sprite(text2, (260, 13))
    if event.x>28+72.5*2 and event.x<(28+72.5*2+55) and event.y>85 and event.y<(85+55):
        Sprite(text3, (260, 13))
App().listenMouseEvent('click',mouseClick)

App().run()
