from pygame import *

class GameSprite():
    def __init__(self,x,y,w,h,img):
        self.image = transform.scale(image.load(img),(w,h))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
    
    def show(self):
        window.blit(self.image,(self.hitbox.x, self.hitbox.y))

class Player(GameSprite):

    def move(self):
        keys =  key.get_pressed()
        if keys[K_LEFT] and self.hitbox.x > 0:
            self.hitbox.x -= 5
        if keys[K_RIGHT] and self.hitbox.x < 600:
            self.hitbox.x += 5

        #движение с помощью мыши
        #x,y = mouse.get_pos()
        #self.hitbox.x = x

#Создаем экран
window = display.set_mode( (700,500) )
background =  transform.scale(image.load('back.jpg'),(700,500))

hero = Player(300,400,100,100,'hero.png')

game = True
while game:

    window.blit(background,(0,0))
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    hero.show()
    hero.move()

    display.update()
