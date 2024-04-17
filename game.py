from pygame import *
#Создаем окно
window = display.set_mode((700,500))
display.set_caption('Догонялки')
#Фон
img = image.load('back.jpg')
back = transform.scale(img,(700,500))

#Игровой цикл
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(back,(0,0))    
    display.update() 
