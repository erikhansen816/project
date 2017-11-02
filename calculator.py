#Erik Hansen
#11/1/2017
#calculator.py - program to make calculator applet

from ggame import *

black = black = Color(0x000000,1)
blackoutline = LineStyle(1,black)
white = Color(0xFFFFFF,0)
red = Color(0xFF0000,.5)

calcoutline = RectangleAsset(300,350,blackoutline,white)
answerbar = RectangleAsset(275,50,blackoutline,white)
keys = RectangleAsset(55,55,blackoutline,white)
equalkey = RectangleAsset(55,55,blackoutline,red)
Sprite(calcoutline)
Sprite(answerbar, (12.5,12.5))
for j in range(4):
    for i in range(4):
        Sprite(keys,(12.5 + 72.5*i, 80 + 68*j))
        if i == 3 and j == 3:
            Sprite(equalkey, (230,284))


App().run()
