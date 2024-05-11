from pygame import *

window = display.set_mode((700,500))

game = True
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
