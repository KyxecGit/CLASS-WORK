from pygame import *

class GameSprite():
    def __init__(self,x,y,w,h,img):
        self.image = transform.scale(image.load(img),(w,h))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
    
    def show(self):
        window.blit(self.image,(self.hitbox.x, self.hitbox.y))

#Создаем экран
window = display.set_mode( (700,500) )
background =  transform.scale(image.load('back.jpg'),(700,500))

hero = GameSprite(300,400,150,100,'hero.png')

game = True
while game:

    window.blit(background,(0,0))
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    hero.show()

    display.update()
