from pygame import *

#Создаем экран
window = display.set_mode( (700,500) )
background =  transform.scale(image.load('back.jpg'),(700,500))


game = True
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))

    display.update()
