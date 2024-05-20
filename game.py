from pygame import *

class GameSprite():
    def __init__(self,x,y,w,h,img):
        self.image =  transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

window = display.set_mode((700,500))
#музыка
mixer.init()
mixer.music.load('back.mp3')
mixer.music.play()

game = True
while game:
    
    window.fill((200,255,255))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
