# -*- coding:utf-8 -*-

#导入pygame， sys ， locals模块
import pygame
from pygame.locals import *
import sys

#定义窗口大小
size = [640,480]
#定义窗口背景颜色白色
backgroundColor = [255,255,255]

# 初始化
pygame.init()

screen = pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())
background.fill(backgroundColor)
clock = pygame.time.Clock()

#定义一个Ball类
class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        if self.rect.left <= screen.get_rect().left or self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos

my_ball = Ball('beach_ball.png',[10,0],[20,20])
running = True
while running:
    for event in pygame.event.get():
        #扫描QUIT事件
        if event.type == QUIT:
            running = False
        clock.tick(30)
        screen.blit(background, (0,0))
        my_ball.move()
        screen.blit(my_ball.image, my_ball.rect)
        pygame.display.flip()
pygame.quit()