from pygame import *

class GameSprite():
    def __init__(self,x,y,w,h,img):
        self.image =  transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

ball = GameSprite(350,200,50,50,'ball.png')

window = display.set_mode((700,500))
#музыка
#mixer.init()
#mixer.music.load('back.mp3')
#mixer.music.play()

speed_x = 1

game = True
while game:
    
    window.fill((200,255,255))

    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.show()
    ball.rect.x += speed_x

    if ball.rect.x > 650 or ball.rect.x < 0:
        speed_x *= -1

    time.delay(10)
    display.update()
