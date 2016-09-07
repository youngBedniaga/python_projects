import pygame
import os
from pygame import *
WIN_WIDTH=900
WIN_HEIGTH=900
DISPLAY = ((WIN_WIDTH,WIN_HEIGTH))
done=False

class kartinki(object):
    def __init__(self):#конструктор - здесь задаем параметры объектов класса
        self.text = ''
        self.img = ''
        self.q=0
        self.e=0
        self.t=0
        self.i=0
        self.x_c=500
        self.y_c=300
    def move(self,x):
        if x[pygame.K_UP]: self.y_c=self.y_c-1 
        if x[pygame.K_DOWN]: self.y_c=self.y_c+1
        if x[pygame.K_LEFT]: self.x_c=self.x_c-1
        if x[pygame.K_RIGHT]: self.x_c=self.x_c+1
        p = pygame.image.load('enemy.bmp')
        screen.blit(p,(self.x_c,self.y_c))
    def pechat(self,x):
        self.text = x
        print self.text
    def izo(self,x):
        if x[pygame.K_d]:
            self.img='1.gif'
            self.a=00
            self.b=00
            self.q=1
        if x[pygame.K_s]:
            self.img='2.gif'
            self.a=380
            self.b=1
            self.e=1
        if x[pygame.K_a]:
            self.img='3.gif'
            self.a=0
            self.b=160
            self.t=1
        if x[pygame.K_w]:
            self.img='4.gif'
            self.a=379
            self.b=160
            self.i=1
       # if x[pygame.K_w] == False: self.img=''
    def draw(self):
        if self.img != '':
            if self.q==1:
                x = pygame.image.load('1.gif')
                screen.blit(x,(0,0))
            if self.e==1:
                x = pygame.image.load('2.gif')
                screen.blit(x,(380,1))
            if self.t==1:
                x = pygame.image.load('3.gif')
                screen.blit(x,(0,160))
            if self.i==1:
                x = pygame.image.load('4.gif')
                screen.blit(x,(379,160))
            x = pygame.image.load(self.img)
            screen.blit(x,(self.a,self.b))
a=kartinki() #создаем объект класса
pripizdok=kartinki()
pygame.init()

screen=pygame.display.set_mode(DISPLAY)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((111,18,31))
    pressed = pygame.key.get_pressed()
    a.izo(pressed)
    pripizdok.move(pressed)
    a.draw()
    pygame.display.update()
    
