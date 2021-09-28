
from pygame import *

finish = False 
game = True #флаг игры (идет/ не идет)
FPS = 60 #фпс игры
win_width = 800
win_height = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width=65,  height=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.height = height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and (self.rect.y+ self.height) <win_height :
            self.rect.y += self.speed

    def move_l(self):
        keys = key.get_pressed()
        if keys[K_w]and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_s] and (self.rect.y+ self.height) <win_height :
            self.rect.y += self.speed

window = display.set_mode((win_width, win_height))
display.set_caption("Шутер")

font.init()
font1 = font.Font(None, 50)
font2 = font.Font(None, 300)
win = font1.render("Ты победил!!!", True, (0,255,0))
lose = font1.render("Ты проиграл!", True, (255,0,0))

background = transform.scale(Surface((win_width,win_height)), ((win_width,win_height)))

clock = time.Clock()

player1 = Player("player.png", 5, win_height/2, 5, width=65, height=120)
player2 = Player("player.png", win_width - 70, win_height/2, 5, width=65, height=120)
ball= GameSprite("ball.png",win_width/2, win_height/2, 5, width=65, height=65 )
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0)) 
        background.fill((255,255,255))  
        player1.reset()
        player2.reset()
        player1.move_l()
        player2.move_r()
        ball.reset()
          
    clock.tick(FPS)
    display.update()
