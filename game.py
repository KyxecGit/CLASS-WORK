from random import randint
from pygame import *

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 10
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += 10

    def fire(self):
        bullet = Bullet('laser.png', self.rect.centerx, self.rect.top, 15, 20)
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= 5

class Enemy(GameSprite):
    def update(self):
        self.speed = 0
        self.rect.y += randint(1,10)
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0,600)


window = display.set_mode((700, 500))
background = transform.scale(image.load('back.jpg'), (700, 500))

ship = Player('hero.png', 5, 400, 100, 100)

bullets = sprite.Group()
enemys = sprite.Group()
for _ in range(5):
    enemy = Enemy('ufo.png', randint(1,600), 0, 100, 100)
    enemys.add(enemy)

#шрифт
font.init()

score = 0

run = True 
reload = False

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()

    if not reload:

        window.blit(background,(0,0))

        score_text = font.Font(None,50).render('Счет: ' + str(score),1,(255,255,255))
        window.blit(score_text,(10,10))

        ship.reset()
        bullets.draw(window)
        enemys.draw(window)

        ship.update()
        bullets.update()
        enemys.update()

        if sprite.groupcollide(bullets, enemys, True,True):
            enemy = Enemy('ufo.png', randint(1,600), 0, 100, 100)
            enemys.add(enemy)
            score += 1

        if score == 10:
            win = font.Font(None,100).render('YOU WIN',1,(0,255,0))
            window.blit(win,(200,200))
            reload = True

        display.update()

    else:
        score = 0
        time.delay(3000)
        reload = False


    time.delay(30)
