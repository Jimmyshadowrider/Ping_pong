
from pygame import *



back = (200,255,255)
w_width = 600
w_height = 500
window = display.set_mode((w_width,w_height))
window.fill(back)

run = True
clock = time.Clock()
FPS = 60
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    



    display.update()
    clock.tick(FPS)