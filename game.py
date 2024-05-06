from pygame import *

class GameSprite():
    def __init__(self,x,y,img):
        self.image = transform.scale(image.load(img),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def view(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

hero = GameSprite(100,400,'hero.png')

window = display.set_mode((700,500))
background = transform.scale(image.load('background.jpg'),(700,500))

game = True
while game:

    window.blit(background,(0,0))
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    hero.view()
    
    display.update()
