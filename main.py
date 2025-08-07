import pygame
from pygame import *
from random import randint
import sys


pygame.init()

win_width = 720
win_height = 480
window = display.set_mode((win_width, win_height))
display.set_caption("Snake")

background = transform.scale(image.load("gamefon.jpg"), (win_width, win_height))
button_image = transform.scale(image.load("button2.png"), (300, 80))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = Color('gray15')
LIGHT_BLUE = Color('white')


font = pygame.font.SysFont("Arial", 40)
small_font = pygame.font.Font(None, 30)
font_gameover = pygame.font.SysFont("Arial", 45)

menu_items = ["Play", "Quit"]
menu_functions = ["start_game", "quit"]
menu_positions = []

for index, item in enumerate(menu_items):
    text = font.render(item, True, WHITE)
    position = button_image.get_rect(center=(win_width // 2, 200 + index * 120))
    menu_positions.append((text, position))

nickname_input_active = False
nickname = ""
input_box = Rect(win_width // 2 - 150, 100, 300, 50)
input_color_active = LIGHT_BLUE
input_color_inactive = GRAY
input_color = input_color_inactive

def quit_game():
    pygame.quit()
    sys.exit()

def start_game(nickname):
    WSize = (720, 480)
    win_game = display.set_mode(WSize)

    TSide = 30
    MSize = WSize[0] // TSide, WSize[1] // TSide

    start_pos = MSize[0] // 2, MSize[1] // 2
    snake = [start_game]
    avile = True

    direction = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    apple = randint(0, MSize[0] - 1), randint(0, MSize[1] - 1)

    FPS = 4
    clock = time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        win_game.fill("black")

    for e in event.get():
        if e.type == QUIT:
            run = False
            quit_game()
        if e.type == KEYDOWN:
            if alive:
                if e.key == K_d and direction != 2:
                    direction = 0
                if e.key == K_s and direction != 3:
                    direction = 1
                if e.key == K_a and direction != 0:
                    direction = 2
                if e.key == K_w and direction != 1:
                    direction = 3
            else:
                if e.key == K_SPACE:
                    return
    [pygame.draw.rect(win_game, "green", (x *TSide, y * TSide, TSide - 1, TSide - 1)) for x, y in snake]            
    pygame.draw.rect(win_game,"red",(apple[0] * TSide, apple[1] * TSide, TSide - 1, TSide - 1))

    if alive:
        new_pos = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]
        if not (0 <= new_pos[0] < MSize[0] and 0 <= new_pos[1] < MSize[1]) or new_pos in snake:
           alive = False
        else:
            snake.insert(0, new_pos)
            if new_pos == apple:
                FPS += 1
                apple = randint(0, MSize[0] - 1), randint(0, MSize[1] - 1)
            else:
                snake.pop(-1)
    else: 
        text = font_gameover.render("Game Over", True, "while")
        win_game.blit(text, (WSize[0] // 2 - text.get_width() // 2 - 40))
        text2 = small_font.render("Press SPACE to return to menu", True, "white")
        win_game(text2, (WSize[0] // 2 - text2.get_width() // 2, WSize[1] // 2 + 10))
    display.flip()

menu_actions = {
    "start_game": lambda: start_game(nickname),
    "quit": quit_game
}


def main_menu():
    global nickname_input_active, nickname, input_color

    while True:
        window.blit(background, (0, 0))
        mouse_pos = mouse.get_pos()

        for e in event.get():
            if e.type == QUIT:
                quit_game()

            elif e.type == MOUSEBUTTONDOWN:
                if input_box.collidepoint(e.pos):
                    nickname_input_active = True
                    input_color = input_color_active
                else:
                    nickname_input_active = False
                    input_color = input_color_inactive

                for i, (_, position) in enumerate(menu_positions):
                    if position.collidepoint(mouse_pos):
                        action = menu_functions[i]
                        if nickname.strip():  
                            menu_actions[action]()

            elif e.type == KEYDOWN and nickname_input_active:
                if e.key == K_RETURN:
                    nickname_input_active = False
                    input_color = input_color_inactive
                elif e.key == K_BACKSPACE:
                    nickname = nickname[:-1]
                elif len(nickname) < 20:
                    nickname += e.unicode

    
        draw.rect(window, input_color, input_box, 2)
        nickname_surface = font.render(nickname or "nickname", True, WHITE if nickname else (225, 225, 225))
        window.blit(nickname_surface, (input_box.x + 10, input_box.y + 10))

        for i, (text, position) in enumerate(menu_positions):
            if position.collidepoint(mouse_pos):
                text = font.render(menu_items[i], True, BLACK)
            else:
                text = font.render(menu_items[i], True, WHITE)

            window.blit(button_image, position)
            text_rect = text.get_rect(center=position.center)
            window.blit(text, text_rect)

        display.flip()


main_menu()
