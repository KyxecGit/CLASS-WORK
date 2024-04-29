from pygame import *
#Создаем экран
window = display.set_mode((700,500))
display.set_caption('Gitler VS Pica')
#Загружаем картинки
img = image.load('back.jpg')
img = transform.scale(img,(700,500))

gitler = transform.scale(image.load('gitler.png'),(150,150))
pica = transform.scale(image.load('pica.png'),(150,150))
#Игровой цикл
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(img,(0,0))
    window.blit(gitler,(200,200))
    window.blit(pica,(400,200))
    display.update()
