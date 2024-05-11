from pygame import *

class GameSprite():
    def __init__(self,x,y,img,width,height) :
        self.image = transform.scale( image.load(img) ,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

ball = GameSprite(300,250,'ball.png',50,50)

window = display.set_mode((700,500))

game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((200,255,255))
    display.update()
