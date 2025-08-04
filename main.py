from pygame import* 
from random import randint
import sys

win_width = 600 #ширина єкрану
win_height = 600 #висота єкрану

window = display.set_mode((win_width, win_height)) #вікно з заданими розмірами
display.set_caption("Snake") #назва єкрану

background = image.load("gamefon.jpg") #зображення фону
background = transform.scale(image.load("gamefon.jpg"), (win_width, win_height)) #фон до розмірів вікна

button_image = image.load("button2.png")
button_image = transform.scale(button_image, (300, 80))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = Color('gray15')
LIGHT_BLUE = Color('lightskyblue3')

font = font.SysFont("Courier New", 40)
small_font = font.Font(None, 30)

menu_items = ["Play", "Quit"]
menu_functions = ["start_game", "quit"]
menu_positions = []

for index, item in enumerate(menu_items):
    text = font.render(item, True, WHITE)
    position = button_image.get_rect(center=(win_width// 2, 200 + index * 120))
    menu_positions.append((text, position))

nickname_input_active = False
nickname = ""
input_box = Rect(win_width // 2 - 150, 100, 300, 50)
input_color_active = LIGHT_BLUE
input_color_inactive = GRAY
input_color = input_color_inactive

def start_game(nickname):
    print(f"Игра началась для игрока: {nickname}")
    # Здесь можно вызывать game_loop()

def quit_game():
    quit()
    sys.exit()

menu_actions = {
    "start_game": lambda: start_game(nickname),
    "quit": quit_game
}


def main_menu():
    global nickname_input_active, nickname, input_color

    while True:
        window.blit(background, (0, 0))

        mouse_pos = mouse.get_pos()
        for event in event.get():
            if event.type == QUIT:
                quit_game()

            elif event.type == MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    nickname_input_active = True
                    input_color = input_color_active
                else:
                    nickname_input_active = False
                    input_color = input_color_inactive

                for i, (_, position) in enumerate(menu_positions):
                    if position.collidepoint(mouse_pos):
                        action = menu_functions[i]
                        if nickname.strip():  # Только если введён ник
                            menu_actions[action]()

            elif event.type == KEYDOWN and nickname_input_active:
                if event.key == K_RETURN:
                    nickname_input_active = False
                    input_color = input_color_inactive
                elif event.key == K_BACKSPACE:
                    nickname = nickname[:-1]
                elif len(nickname) < 20:
                    nickname += event.unicode

        # Отрисовка поля ввода ника
        draw.rect(window, input_color, input_box, 2)
        nickname_surface = font.render(nickname or "nickname", True, WHITE if nickname else (150, 150, 150))
        window.blit(nickname_surface, (input_box.x + 10, input_box.y + 10))

        # Отображение кнопок меню
        for i, (text, position) in enumerate(menu_positions):
            if position.collidepoint(mouse_pos):
                text = font.render(menu_items[i], True, BLACK)
            else:
                text = font.render(menu_items[i], True, WHITE)

            window.blit(button_image, position)
            text_rect = text.get_rect(center=position.center)
            window.blit(text, text_rect)

        window.display.flip()

# Запуск главного меню
main_menu()

       

# Запуск главного меню
main_menu()

