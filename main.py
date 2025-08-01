from pygame import* 
from random import randint
import pygame

win_width = 600 #ширина єкрану
win_height = 600 #висота єкрану
window = display.set_mode((win_width, win_height)) #вікно з заданими розмірами
display.set_caption("Snake") #назва єкрану
background = image.load("grass.jpg") #зображення фону
background = transform.scale(image.load("grass.jpg"), (win_width, win_height)) #фон до розмірів вікна

clock = pygame.time.Clock() #годинник для контролю FPS
FPS = 60 #кількість кадрів за секунду FPS
running = True  #змінна для керування циклом гри




while running:#основний цикл
    for e in event.get(): #обробка подій
        if e.type == QUIT: #закрити вікно у грі
            running = False #закрити цикл
    window.blit(background, (0, 0)) #фон на кординатах 0 0
    display.update() #оновлення єкрану

    clock.tick(FPS) #цикл до 60 кадрів за секунду
pygame.quit() #завершування роботи гри