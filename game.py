from pygame import *

#Создаем класс для наших спрайтов
class GameSprite():
    def __init__(self,x,y,img):
        self.image = transform.scale(image.load(img),(70,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    #Способность отображение для персонажей
    def view(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Wall():
    def __init__(self,x,y,width,height):
        self.image = Surface((width,height))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def view(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


#Создаем обьекты для нашей игры
wall_1 = Wall(200,100,10,600)
hero = GameSprite(100,400,'hero.png')
enemy = GameSprite(500,200,'cyborg.png')
gold = GameSprite(600,400,'treasure.png')
#Создание экрана
window = display.set_mode((700,500))
#Картинка для нашего экрана
background = transform.scale(image.load('background.jpg'),(700,500))
#шрифт
font.init()
#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
#Игровой цикл
game = True
finish = False
while game:

    window.blit(background,(0,0))
    
    #Обработка выхода из игры
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        #Движение главного героя
        keys = key.get_pressed()
        if keys[K_UP]:
            hero.rect.y -= 10
        if keys[K_DOWN]:
            hero.rect.y += 10
        if keys[K_LEFT]:
            hero.rect.x -= 10
        if keys[K_RIGHT]:
            hero.rect.x += 10

        #Движение врага
        if enemy.rect.x < hero.rect.x:
            enemy.rect.x += 0.1

        if enemy.rect.x > hero.rect.x:
            enemy.rect.x -= 0.1

        if enemy.rect.y < hero.rect.y:
            enemy.rect.y += 0.1

        if enemy.rect.y > hero.rect.y:
            enemy.rect.y -= 0.1

    #условие поражения
    if sprite.collide_rect(hero, enemy):
        lose = font.Font(None,100).render('YOU LOSE',1,(255,0,0))
        window.blit(lose,(200,200))
        finish = True

    #условие победы
    if sprite.collide_rect(hero, gold):
        win = font.Font(None,100).render('YOU WIN',1,(0,255,0))
        window.blit(win,(200,200))
        finish = True

    if sprite.collide_rect(hero,wall_1):
        if hero.rect.x >= wall_1.rect.x:
            hero.rect.x += 10
        else:
            hero.rect.x -= 10



    #Отображение персонажей
    hero.view()
    enemy.view()
    gold.view()

    wall_1.view()
    #Команда отвечает за частоту отработки цикла
    time.delay(5)
    #Обновление нашего экрана
    display.update()
