#Erik Hansen
#11/1/2017
#calculator.py - program to make calculator applet

from ggame import *

def plusminus():
    if data['operation'] == '':
        data['num1'] = float(data['num1'])*-1
        data['buttonpressed1'] = data['buttonpressed1']*-1
        data['display'].destroy()
        data['display'] = Sprite(TextAsset(data['num1'],fill=black, style = 'bold 35pt Times'),(15,13))
    if data['operation'] != '':
        data['num2'] = float(data['num2'])*-1
        data['buttonpressed2'] = data['buttonpressed2']*-1 
        data['display'].destroy()
        data['display'] = Sprite(TextAsset(data['num2'],fill=black, style = 'bold 35pt Times'),(15,13))

def processNumber(n):
    if data['operation'] == '':
        data['buttonpressed1'] = data['buttonpressed1']+str(n)
        data['num1'] = data['buttonpressed1']
        data['display'].destroy()
        data['display'] = Sprite(TextAsset(data['num1'],fill=black, style = 'bold 35pt Times'),(15,13))
        return(data['num1'])
    if data['operation']!= '':
        data['buttonpressed2'] = data['buttonpressed2']+str(n)
        data['num2'] = data['buttonpressed2']
        data['display'].destroy()
        data['display'] = Sprite(TextAsset(data['num2'],fill=black, style = 'bold 35pt Times'),(15,13))
        return(data['num2'])

def clear():
    data['buttonpressed1'] = ''
    data['num1'] = ''
    data['num2'] = ''
    data['buttonpressed2'] = ''
    data['operation'] = ''
    data['display'].destroy()
    data['display'] = Sprite(TextAsset('',fill=black, style = 'bold 35pt Times'),(15,13))
    
def math():
    if data['operation'] == '':
        ans = data['num1']
    if data['operation'] == 'x':
        ans = float(data['num1']) * float(data['num2'])
    if data['operation'] == '÷':
        ans = float(data['num1']) / float(data['num2'])
    if data['operation'] == '+':
        ans = float(data['num1']) + float(data['num2'])
    if data['operation'] == '-':
        ans = float(data['num1']) - float(data['num2'])
    data['num1'] = ans
    data['buttonpressed1'] = ''
    data['buttonpressed2'] = ''
    data['num2'] = ''
    data['operation'] = ''
    data['display'].destroy()
    data['display'] = Sprite(TextAsset(data['num1'],fill=black, style = 'bold 35pt Times'),(15,13))



def operation(n):
    data['operation'] = n
    data['display'].destroy()
    data['display'] = Sprite(TextAsset(data['operation'],fill=black, style = 'bold 35pt Times'),(15,13))
    

def mouseClick(event):
    if event.x>28 and event.x<(28+55) and event.y>85+68 and event.y<(85+68+55):
        processNumber(1)
    if event.x>28+72.5 and event.x<(28+72.5+55) and event.y>85+68 and event.y<(85+68+55):
        processNumber(2)
    if event.x>28+72.5*2 and event.x<(28+72.5*2+55) and event.y>85+68 and event.y<(85+68+55):
        processNumber(3)
    if event.x>28 and event.x<(28+55) and event.y>85+68*2 and event.y<(85+68*2+55):
        processNumber(4)
    if event.x>28+72.5 and event.x<(28+72.5+55) and event.y>85+68*2 and event.y<(85+68*2+55):
        processNumber(5)
    if event.x>28+72.5*2 and event.x<(28+72.5*2+55) and event.y>85+68*2 and event.y<(85+68*2+55):
        processNumber(6)
    if event.x>28 and event.x<(28+55) and event.y>85+68*3 and event.y<(85+68*3+55):
        processNumber(7)
    if event.x>28+72.5 and event.x<(28+72.5+55) and event.y>85+68*3 and event.y<(85+68*3+55):
        processNumber(8)
    if event.x>28+72.5*2 and event.x<(28+72.5*2+55) and event.y>85+68*3 and event.y<(85+68*3+55):
        processNumber(9)
    if event.x>28+72.5 and event.x<(28+72.5+55) and event.y>85+68*4 and event.y<(85+68*4+55):
        processNumber(0)
    if event.x>28 and event.x<28+55 and event.y>85 and event.y<85+55:
        clear()
    if event.x>28+72.5*3 and event.x<28+72.5*3+55 and event.y>85 and event.y<85+55:
        operation('÷')
    if event.x>28+72.5*3 and event.x<28+72.5*3+55 and event.y>85+68 and event.y<85+68+55:
        operation('x')
    if event.x>28+72.5*3 and event.x<28+72.5*3+55 and event.y>85+68*2 and event.y<85+68*2+55:
        operation('+')
    if event.x>28+72.5*3 and event.x<28+72.5*3+55 and event.y>85+68*3 and event.y<85+68*3+55:
        operation('-')
    if event.x>28+72.5*3 and event.x<28+72.5*3+55 and event.y>85+68*4 and event.y<85+68*4+55:
        math()
    if event.x>28 and event.x<28+55 and event.y>85+68*4 and event.y<85+68*4+55:
        plusminus()
    if event.x>28+72.5*2 and event.x<(28+72.5*2+55) and event.y>85+68*4 and event.y<(85+68*4+55):
        processNumber('.')

if __name__ == '__main__':
    data = {}
    data['num1'] = ''
    data['buttonpressed1'] = ''
    data['operation'] = ''
    data['buttonpressed2'] = ''
    data['num2'] = ''
    data['display'] = Sprite(TextAsset(''),(15,13))
    
    black = black = Color(0x000000,1)
    blackoutline = LineStyle(1,black)
    white = Color(0xFFFFFF,0)
    red = Color(0xFF0000,.5)

    text1 = TextAsset('C',fill=black, style = 'bold 35pt Times')
    text2 = TextAsset('',fill=black, style = 'bold 35pt Times')
    text3 = TextAsset('',fill=black, style = 'bold 35pt Times')
    text4 = TextAsset(1,fill=black, style = 'bold 35pt Times')
    text5 = TextAsset(2,fill=black, style = 'bold 35pt Times')
    text6 = TextAsset(3,fill=black, style = 'bold 35pt Times')
    text7 = TextAsset(4,fill=black, style = 'bold 35pt Times')
    text8 = TextAsset(5,fill=black, style = 'bold 35pt Times')
    text9 = TextAsset(6,fill=black, style = 'bold 35pt Times')
    text10 = TextAsset(7,fill=black, style = 'bold 35pt Times')
    text11 = TextAsset(8,fill=black, style = 'bold 35pt Times')
    text12 = TextAsset(9,fill=black, style = 'bold 35pt Times')
    text13 = TextAsset('÷',fill=black, style = 'bold 35pt Times')
    text14 = TextAsset('x',fill=black, style = 'bold 35pt Times')
    text15 = TextAsset('+',fill=black, style = 'bold 35pt Times')
    text16 = TextAsset('-',fill=black, style = 'bold 35pt Times')
    text17 = TextAsset('+/-',fill=black, style = 'bold 30pt Times')
    text18 = TextAsset(0,fill=black, style = 'bold 35pt Times')
    text19 = TextAsset('.',fill=black, style = 'bold 35pt Times')
    text20 = TextAsset('=',fill=black, style = 'bold 35pt Times')

    calcoutline = RectangleAsset(300,420,blackoutline,white)
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
    Sprite(text10,(28,85+68*3))
    Sprite(text11,(28+72.5,85+68*3))
    Sprite(text12,(28+72.5*2,85+68*3))
    Sprite(text13,(28+72.5*3,85))
    Sprite(text14,(28+72.5*3,85+68))
    Sprite(text15,(28+72.5*3,85+68*2))
    Sprite(text16,(28+72.5*3,85+68*3))
    Sprite(text17,(15,85+68*4))
    Sprite(text18,(28+72.5,85+68*4))
    Sprite(text19,(28+72.5*2,85+68*4))
    Sprite(text20,(28+72.5*3,85+68*4))

    for j in range(5):
        for i in range(4):
            Sprite(keys,(12.5 + 72.5*i, 80 + 68*j))
            if i == 3 and j == 4:
                Sprite(equalkey, (230,284+68))


    App().listenMouseEvent('click',mouseClick)


    

    App().run()
