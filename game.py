from pygame import *

class GameSprite():
    def __init__(self,x,y,img,width,height) :
        self.image = transform.scale( image.load(img) ,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def view(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

ball = GameSprite(350,200,'ball.png',50,50)

window = display.set_mode((700,500))

speed_x = 1
speed_y = 1

game = True
while game:

    window.fill((200,255,255))

    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.x > 650 or ball.rect.x < 0:
        speed_x *= -1
        
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    
    ball.view()

    display.update()
