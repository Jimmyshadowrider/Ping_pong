
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.x < w_width-80:
            self.rect.y += self.speed
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.x < w_width-80:
            self.rect.y += self.speed


racket_l = Player('racket.png',30,200,100,150,4)
racket_r = Player('racket.png',470,200,100,150,4)

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
    window.fill(back)
    racket_l.update_l()
    racket_r.update_r()
    racket_l.reset()
    racket_r.reset()


    display.update()
    clock.tick(FPS)
