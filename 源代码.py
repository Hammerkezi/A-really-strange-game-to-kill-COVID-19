import pygame
import time
from pygame.locals import *
from sys import exit
class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((640, 400))
        self.bg=pygame.image.load('bg.jpg')
        self.bg = pygame.transform.smoothscale(self.bg, (640, 400))
        self.winbg = pygame.image.load('winbg.jpg')
        self.winbg = pygame.transform.smoothscale(self.winbg, (640, 400))
        self.ico=pygame.image.load('gameicon.png')
        self.left_sprite=pygame.image.load('sprite.png')
        self.left_sprite=pygame.transform.smoothscale(self.left_sprite, (50, 50))
        self.right_sprite=pygame.transform.flip(self.left_sprite,True,False)
        self.right_sprite = pygame.transform.smoothscale(self.right_sprite, (50, 50))
        self.virus_smile=pygame.image.load('virus_smile.png')
        self.virus_cry=pygame.image.load('virus_cry.png')
        self.virus_smile=pygame.transform.smoothscale(self.virus_smile,(50,50))
        self.virus_cry=pygame.transform.smoothscale(self.virus_cry,(100,100))
        self.win=pygame.image.load('撒花.png')
        self.win=pygame.transform.smoothscale(self.win,(200,200))
        self.platform1=pygame.image.load('platform1.gif')
        pygame.display.set_icon(self.ico)
        pygame.mixer.music.load('bg mp3.mp3')
        pygame.mixer.music.play(-1)
        self.sprite_x=590
        self.sprite_y=350
        self.direction=0
        self.time=0
        self.oldtime=0
        self.newtime=0
        self.jumpflag=0
        self.winflag=0
        self.stopflag=0
        self.downflag=0
        self.platform_x=[450,300,150,0,150,0]
        self.platform_y=[360,300,240,180,120,50]
        pygame.display.set_caption('新冠灭亡')
    def listen(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type==QUIT or keys[K_ESCAPE]:
                exit()
            if event.type==KEYDOWN:
                key=event.key
                if key==K_SPACE or key==K_UP:
                    self.jumpflag = 1
                    self.newtime = time.time()
                    self.jump(0)
                    self.jump(1)
                    self.jumpflag=0
                    time.sleep(0.1)
            if self.sprite_x<=50 and self.sprite_y==0:
                text=self.write('simhei',40,'胜利',(255,0,0))
                self.screen.blit(text,(300,150))
                pygame.mixer.music.stop()
                pygame.mixer.music.load('胜利音效.mp3')
                pygame.mixer.music.play(1)
                self.winflag=1
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.sprite_x>=1:
            self.sprite_x-=0.25
            self.direction=0
            self.oldtime=time.time()
        if keys[K_RIGHT] and self.sprite_x<=589:
            self.sprite_x+=0.25
            self.direction=1
            self.oldtime=time.time()
    def crash(self):
        for i in range(0,6):
            if self.platform_x[i]==self.sprite_x+50 and self.sprite_y+50>self.platform_y[i] and self.sprite_y<self.platform_y[i]+10:
                self.sprite_x-=0.5
            if self.platform_x[i]+100==self.sprite_x and self.sprite_y+50>self.platform_y[i] and self.sprite_y<self.platform_y[i]+10:
                self.sprite_x+=0.5
    def jump(self,upDown):
        if upDown==0:
            for i in range(1, 100):
                for j in range(0, 6):
                    if self.platform_y[j] + 10 == self.sprite_y and self.sprite_x+50>self.platform_x[j] and self.sprite_x<self.platform_x[j]+100:
                        self.stopflag = 1
                        break
                if (self.stopflag == 1):
                    self.stopflag = 0
                    break
                if self.sprite_y >= 0:
                    self.sprite_y -= 1
                else:
                    break
                self.blit(1)
        else:
            while(True):
                for i in range(1, 100):
                    for j in range(0, 6):
                        if self.platform_y[j] == self.sprite_y+50 and self.sprite_x+50>self.platform_x[j] and self.sprite_x<self.platform_x[j]+100:
                            self.stopflag = 1
                            break
                    if self.stopflag == 1:
                        break
                if self.stopflag==1:
                    self.stopflag=0
                    break
                if self.sprite_y <= 349:
                    self.sprite_y += 1
                else:
                    break
                self.blit(1)
    def blit(self,isJump):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.platform1, (450, 360))
        self.screen.blit(self.platform1, (300, 300))
        self.screen.blit(self.platform1, (150, 240))
        self.screen.blit(self.platform1, (0, 180))
        self.screen.blit(self.platform1, (150, 120))
        self.screen.blit(self.platform1, (0, 50))
        self.screen.blit(self.virus_smile, (0, 0))
        if isJump==0:
            if self.jumpflag == 0:
                if self.direction == 0:
                    self.screen.blit(self.left_sprite, (self.sprite_x, self.sprite_y))
                else:
                    self.screen.blit(self.right_sprite, (self.sprite_x, self.sprite_y))
        elif isJump==1:
            if self.direction == 0:
                if self.newtime - self.oldtime <= 0.1 and self.sprite_x >= 1:
                    self.sprite_x -= 0.5
                self.screen.blit(self.left_sprite, (self.sprite_x, self.sprite_y))
            else:
                if self.newtime - self.oldtime <= 0.1 and self.sprite_x <= 589:
                    self.sprite_x += 0.5
                self.screen.blit(self.right_sprite, (self.sprite_x, self.sprite_y))
        else:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.winbg, (0, 0))
            self.screen.blit(self.virus_cry, (0, 0))
            self.screen.blit(self.win,(110,100))
            text=self.write('simhei',40,'胜利',(255,0,0))
            self.screen.blit(text,(300,180))
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == QUIT or keys[K_ESCAPE]:
                    exit()
        pygame.display.update()
    def down(self):
        while True:
            for j in range(0, 6):
                if self.platform_y[j] == self.sprite_y+50 and self.sprite_x+50>self.platform_x[j] and self.sprite_x<self.platform_x[j]+100:
                    self.stopflag = 1
                    break
            if self.stopflag == 0 and self.sprite_y < 350:
                self.sprite_y+=1
            else:
                self.stopflag = 0
                break
            self.blit(0)
    def write(self,name,size,text,color,):
        font = pygame.font.SysFont(name,size)
        image = font.render(text,True,color)
        return image
    def run(self):
        while True:
            if self.winflag==0:
                self.listen()
                self.blit(0)
                self.move()
                self.crash()
                self.down()
            else:
                self.blit(2)
            pygame.display.update()

game=Game()
game.run()