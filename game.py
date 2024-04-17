from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,x,y,img):
        self.img = transform.scale(image.load(img),(70,70))
        self.hit_box = self.img.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y

    def view(self):
        window.blit(self.img,(self.hit_box.x,self.hit_box.y))

#Персонажи
hero = GameSprite(300,200,'gitler.png')
#Создаем окно
window = display.set_mode((700,500))
display.set_caption('Догонялки')
#Фон
img = image.load('back.jpg')
back = transform.scale(img,(700,500))
#Музыка
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()

#Игровой цикл
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(back,(0,0))    
    hero.view()
    display.update() 
