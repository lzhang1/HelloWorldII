# -*- coding:utf-8 -*-

#导入pygame， sys ， locals模块
import pygame
from pygame.locals import *
import sys


#定义一个MyBallClass球类
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        global score, score_surf, score_font
        self.rect = self.rect.move(self.speed)
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            self.speed[0] = -self.speed[0]
            hit_wall.play()

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            score += 1
            score_surf = score_font.render(str(score),1,(255,255,255))
            get_point.play()



#定义一个MyPaddleClass球拍类（挡板）
class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, location =[0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20])
        image_surface.fill([127,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#定义窗口大小
size = [640,480]
#定义窗口背景图片
backgroundImageFile = 'timg.jpg'

# 初始化
pygame.init()

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
ball_speed = [10,5]
background = pygame.image.load(backgroundImageFile).convert()
myBall = MyBallClass('wackyball.png',ball_speed,[50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270,400])
lives = 1
score = 0
score_font = pygame.font.Font('IMPRISHA.TTF',50)
score_surf = score_font.render(str(score),1,(255,255,255))
score_pos = [10,10]
#载入声音
hit_wall = pygame.mixer.Sound("hit_wall.wav")
hit_wall.set_volume(0.4)
get_point = pygame.mixer.Sound("get_point.wav")
get_point.set_volume(0.2)
splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.6)
new_life = pygame.mixer.Sound("new_life.wav")
new_life.set_volume(0.5)
bye = pygame.mixer.Sound("game_over.wav")
bye.set_volume(0.6)

done = False
running = True
while running:
    clock.tick(30)
    #绘制背景图
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        #扫描QUIT事件
        if event.type == QUIT:
            running = False
        #移动挡板
        elif event.type == MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]
    #球碰撞挡板后弹回
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myBall.speed[1] = -myBall.speed[1]



    myBall.move()

    #绘制球，挡板，(生命)球数以及更新分数
    if not done:
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_surf,score_pos)
        for i in range(lives):
            width = screen.get_width()
            screen.blit(myBall.image, [width - 40*i, 20])
        pygame.display.flip()
        #pygame.time.delay(1000)

    #当球落到屏幕底部以下，生命数减1
    if myBall.rect.top >= screen.get_rect().bottom:
        lives -= 1
        splat.play()
        #如果没有生命数，游戏结束
        if lives == 0:
            bye.play()
            final_text1 = "Game Over"
            final_text2 = "Your final score is: "+str(score)
            ft1_font = pygame.font.Font("IMPRISHA.TTF",70)
            ft1_surf = ft1_font.render(final_text1, 1,(0,0,0))
            ft2_font = pygame.font.Font("IMPRISHA.TTF",50)
            ft2_surf = ft1_font.render(final_text2, 1,(0,0,0))
            #文字居中显示
            screen.blit(ft1_surf,[screen.get_width()/2 - ft1_surf.get_width()/2,100])
            screen.blit(ft2_surf,[screen.get_width()/2 - ft2_surf.get_width()/2,200])
            pygame.display.flip()
            done = True
        #重新开始
        else:
            pygame.time.delay(1000)
            new_life.play()
            myBall.rect.topleft = [50,50]

pygame.quit()
