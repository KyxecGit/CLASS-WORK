from pygame import *

class GameSprite():
    def __init__(self,img,x ,y ,w ,h ):
        self.image = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

ball = GameSprite('ball.png',350,250,50,50)

window = display.set_mode((700,500))

game = True
while game:

    window.fill((200,250,250))
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.show()

    
    display.update()
