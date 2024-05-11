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
player = GameSprite('player.png',0,250,100,250)
ai = GameSprite('ai.png',600,250,100,250)

font.init()

window = display.set_mode((700,500))

speed_x = 1
speed_y = 1

game = True
while game:

    window.fill((200,250,250))
    ball.show()
    player.show()
    ai.show()
    
    for e in event.get():
        if e.type == QUIT:
            game = False

   
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.x > 650 or ball.rect.x < 0:
        speed_x *= -1
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    mouse_x, mouse_y = mouse.get_pos()
    player.rect.centery = mouse_y

    if ai.rect.centery != ball.rect.centery:
        if ai.rect.centery < ball.rect.centery:
            ai.rect.y += 2
        else:
            ai.rect.y -= 2

    if sprite.collide_rect(ball,player) or sprite.collide_rect(ball,ai):
        speed_x *= -1

    
    display.update()
