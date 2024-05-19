from pygame import *

window = display.set_mode((700,500))

back = image.load('back.png')
back = transform.scale(back,(700,500))

pica = image.load('pica.png')
pica = transform.scale(pica,(100,100))

gitler = image.load('gitler.png')
gitler = transform.scale(gitler,(100,100))

gitler_x = 0
gitler_y = 0

game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys = key.get_pressed()
    if keys[K_UP]:
        gitler_y -= 5
    if keys[K_DOWN]:
        gitler_y += 5
    if keys[K_LEFT]:
        gitler_x -= 5
    if keys[K_RIGHT]:
        gitler_x += 5


    window.blit(back,(0,0))
    window.blit(pica,(200,200))
    window.blit(gitler,(gitler_x,gitler_y))
    display.update()

    
