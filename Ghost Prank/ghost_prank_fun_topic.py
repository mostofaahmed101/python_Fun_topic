import pygame
from time import sleep


pygame.init()
sceen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()
sleep(1)

sceen.blit(pygame.image.load('scr.jpg') , (0,0))
pygame.display.update()
sleep(2)

print("kaisa laga mera majak :) ")
