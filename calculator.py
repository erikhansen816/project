#Erik Hansen
#11/1/2017
#calculator.py - program to make calculator applet

from ggame import *

black = black = Color(0x000000,1)
blackoutline = LineStyle(1,black)
white = Color(0xFFFFFF,1)

calcoutline = RectangleAsset(300,350,blackoutline,white)
answerbar = RectangleAsset(275,50,blackoutline,white)
keys = RectangleAsset(50,50,blackoutline,white)
Sprite(calcoutline)
Sprite(answerbar, (12.5,12.5))
Sprite(keys, (12.5,75))

App().run()
