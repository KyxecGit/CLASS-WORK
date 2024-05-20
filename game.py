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
gitler = GameSprite(620,200,80,150,'gitler.png')
pica = GameSprite(0,200,80,150,'pica.png')

window = display.set_mode((700,500))

#музыка
#mixer.init()
#mixer.music.load('back.mp3')
#mixer.music.play()

speed_x = 1
speed_y = 1

game = True
while game:
    
    window.fill((200,255,255))

    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.show()
    gitler.show()
    pica.show()


    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.x > 650 or ball.rect.x < 0:
        speed_x *= -1

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    time.delay(10)
    display.update()
