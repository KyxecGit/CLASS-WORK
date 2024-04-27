#Создай собственный Шутер!
from random import randint
from typing import Any
from pygame import *

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed

# класс врагов
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > window_height:
            self.rect.y = 0
            self.rect.x = randint(0,700)

#Создаем персонажей
ship  = Player('rocket.png',300,380,70,120,10)
enemy  = Enemy('ufo.png',300,0,100,50,5)

#Создаем окно
window_width = 700
window_height = 500
window = display.set_mode((window_width,window_height))
background = transform.scale(image.load('galaxy.jpg'),(window_width,window_height))

#Игровой цикл
game = True
while game:
   
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))

    ship.reset()
    ship.update()

    enemy.reset()
    enemy.update()

    display.update()
    time.delay(20)
