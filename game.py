from pygame import *
'''Необходимые классы'''

#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def move(self):
        
        if self.rect.x <= 300:
            self.direction = 'right'
        if self.rect.x >= 600:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,wall_x,wall_y,wall_width,wall_height):
        self.width = wall_width
        self.height = wall_height
        self.wall = Surface((self.width,self.height))
        self.wall.fill((0,255,0))
        self.rect = self.wall.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def reset(self):
        window.blit(self.wall, (self.rect.x, self.rect.y))
        
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Персонажи игры:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

wall_1 = Wall(50,50,400,20)


game = True
stop = False
clock = time.Clock()
FPS = 60

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

#надпись
font.init()
font = font.Font(None, 120)
win = font.render('YOU WIN',True,(0,255,0))
lose = font.render('YOU LOSE',True,(255,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if stop != True:
        window.blit(background,(0, 0))
        player.reset()
        player.move()
        monster.reset()
        monster.move()
        final.reset()
        wall_1.reset()
        
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, wall_1):
            window.blit(lose,(150,200))
            kick.play()
            stop = True


        if sprite.collide_rect(player, final):
            window.blit(win,(150,200))
            money.play()
            stop = True

    display.update()
    clock.tick(FPS)
