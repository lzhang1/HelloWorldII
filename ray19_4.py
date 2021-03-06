# -*- coding: UTF-8 -*-

import pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    if not pygame.mixer.music.get_busy():
        splat.play(2)
        pygame.time.delay(1000)
        running = False
pygame.quit()
