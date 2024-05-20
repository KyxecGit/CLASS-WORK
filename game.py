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
#шрифт
font.init()
font = font.Font(None,50)

speed_x = 1
speed_y = 1

score1 = 0
score2 = 0

game = True
while game:
    
    window.fill((200,255,255))

    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.show()
    gitler.show()
    pica.show()


    pica_score = font.render('Счет: '+ str(score1),1,(255,255,255))
    gitler_score = font.render('Счет :'+ str(score2),1,(255,255,255))

    
    window.blit(pica_score,(20,20))
    window.blit(pica_score,(550,20))


    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.x >= 650:
        score1 += 1
        ball.rect.x = 350
        ball.rect.y = 200
        time.delay(1000)
       
    if ball.rect.x <= 0:
        score2 += 1
        ball.rect.x = 350
        ball.rect.y = 200
        time.delay(1000)

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    x,y = mouse.get_pos()
    pica.rect.y = y

    if ball.rect.centery > gitler.rect.centery :
        gitler.rect.y += 1
    else:
        gitler.rect.y -= 1

    if gitler.rect.colliderect(ball) or pica.rect.colliderect(ball):
        speed_x *= -1

    time.delay(3)
    display.update()
