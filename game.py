
from pygame import *

#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (80, 80))
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


#класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
    def update(self):
        pass

#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Space shooter")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))


#Персонажи игры:
ship = Player('rocket.png', 310, 410, 10)

game = True
finish = False
clock = time.Clock()
FPS = 60


font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))


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

    ship.reset()
    ship.update()

    display.update()
    clock.tick(FPS)
