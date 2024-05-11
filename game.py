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
player = GameSprite(0,200,'racket.png',75,150)
ai = GameSprite(625,200,'racket.png',75,150)

window = display.set_mode((700,500))

player_score = 0
ai_score = 0

font.init()
font = font.Font(None,50)


speed_x = 3
speed_y = 3

game = True
while game:

    window.fill((200,255,255))

    score1 = font.render('Очки: ' + str(player_score),1,(0,0,0))
    score2 = font.render('Очки: ' + str(ai_score),1,(0,0,0))

    window.blit(score1,(30,30))
    window.blit(score2,(500,30))

    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(ball,player) or sprite.collide_rect(ball,ai):
        speed_x *= -1

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    keys = key.get_pressed()
    if keys[K_UP] and player.rect.y > 0:
        player.rect.y -= 3
    if keys[K_DOWN] and player.rect.y < 400:
        player.rect.y += 3

    if ai.rect.y != ball.rect.y:
        if ai.rect.centery < ball.rect.centery:
            ai.rect.y += 1
        else:
            ai.rect.y -= 1

    if ball.rect.x < 0:
        ai_score += 1
        ball.rect.x = 300
        ball.rect.y = 200
        time.delay(1000)

    if ball.rect.x > 650:
        player_score += 1
        speed_x *= -1
        ball.rect.x = 300
        ball.rect.y = 200
        time.delay(1000)
    
    ball.view()
    player.view()
    ai.view()

    display.update()
    time.delay(10)
