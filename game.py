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
wall_1 = Wall(50,50,600,20)
hero = GameSprite(100,400,'hero.png')
enemy = GameSprite(500,200,'cyborg.png')
gold = GameSprite(600,400,'treasure.png')
#Создание экрана
window = display.set_mode((700,500))
#Картинка для нашего экрана
background = transform.scale(image.load('background.jpg'),(700,500))

#Игровой цикл
game = True
while game:

    window.blit(background,(0,0))
    
    #Обработка выхода из игры
    for e in event.get():
        if e.type == QUIT:
            game = False

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
        enemy.rect.x += 1

    if enemy.rect.x > hero.rect.x:
        enemy.rect.x -= 1

    if enemy.rect.y < hero.rect.y:
        enemy.rect.y += 1

    if enemy.rect.y > hero.rect.y:
        enemy.rect.y -= 1

    


    #Отображение персонажей
    hero.view()
    enemy.view()
    gold.view()

    wall_1.view()
    #Команда отвечает за частоту отработки цикла
    time.delay(5)
    #Обновление нашего экрана
    display.update()
