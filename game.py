
from pygame import *
from random import randint

#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

propusk = 0
#класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
    def update(self):
        global propusk
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80,600)
            self.rect.y = 0
            propusk += 1


#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Space shooter")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))


#Персонажи игры:
ship = Player('rocket.png', 310, 380,80,120, 10)

enemys = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png',randint(80,600),0,100,60,randint(5,10))
    enemys.add(enemy)

game = True
finish = False
clock = time.Clock()
FPS = 60


font.init()
font = font.Font(None, 40)
point = font.render('Убито:', True, (255, 255, 255))


#музыка
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()

#fire = mixer.Sound('fire.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))
    window.blit(point,(20,20))
    window.blit(font.render('Пропущено:'+ str(propusk), True, (255, 255, 255)),(20,60))

    ship.reset()
    ship.update()

    enemys.draw(window)
    enemys.update()
    
    display.update()
    clock.tick(FPS)
