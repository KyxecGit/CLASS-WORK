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
            self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += 5

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20)
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= 5

window = display.set_mode((700, 500))
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

ship = Player('rocket.png', 5, 400, 80, 100)
bullets = sprite.Group()

run = True 
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()

    window.blit(background,(0,0))

    ship.update()
    bullets.update()

    ship.reset()
    bullets.draw(window)

    display.update()
