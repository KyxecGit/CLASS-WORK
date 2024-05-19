from pygame import *

window = display.set_mode((700,500))

back = image.load('back.png')
back = transform.scale(back,(700,500))

pica = image.load('pica.png')
pica = transform.scale(pica,(100,100))

gitler = image.load('gitler.png')
gitler = transform.scale(gitler,(100,100))


game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(back,(0,0))
    window.blit(pica,(200,200))
    window.blit(gitler,(400,200))
    display.update()

    
