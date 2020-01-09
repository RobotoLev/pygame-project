import random
import pygame
from source.system_functions import load_image, terminate, load_level


FPS = 50
tile_width, tile_height = 50, 50
WIDTH = 1072
HEIGHT = 603
MENUBTTNS = [None for _ in range(4)]
MODEBTTNS = [None for _ in range(3)]
PLAYRSCOUNT = 0


# Включить, когда будет объект игрока с координатами
#
# def move_player(player, delta_x, delta_y):
#     player.x += delta_x
#     player.y += delta_y


# Объект игрока (пока непонятно с классом, поэтому None) и временная константа его скорости
player_one = None
VELOCITY = 10

# Подобным образом можно легко задать обработку любого события
# Но есть небольшой минус - все события по разу вызываются сразу после создания словаря
KEYBTTNS = {# "w": move_player(player_one, 0, VELOCITY),
            # "a": move_player(player_one, -VELOCITY, 0),
            # "s": move_player(player_one, 0, -VELOCITY),
            # "d": move_player(player_one, VELOCITY, 0),
            "q": print("Привет!")}

# Пример использования
#
# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         terminate()
#     elif event.type == pygame.KEYDOWN:
#         key = event.unicode.lower()
#         if key in KEYBTTNS:
#             KEYBTTNS[key]


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
iteration = 0


def choose_mode(chosed=None):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    texts = ['1 игрок', '2 игрока', 'СТАРТ']
    for i in range(3):
        cr = (100, 255, 100)
        if chosed == i:
            cr = (100, 175, 100)
        elif PLAYRSCOUNT - 1 == i:
            cr = (150, 255, 150)
        text = font.render(texts[i], 1, cr)
        text_h = text.get_height()
        text_w = text.get_width()
        text_y = HEIGHT // 4 - text_h // 2
        text_x = WIDTH // 3 * i + WIDTH // 4
        if i == 2:
            text_y = HEIGHT // 4 * 3 - text_h // 2
            text_x = WIDTH // 2 - text_w // 2
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        MODEBTTNS[i] = ((text_x, text_y, text_w, text_h), cr)


def main_menu(chosed=None):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    texts = ["Новая игра", "Продолжить", "Настройки", "Выход"]
    for i in range(4):
        cr = (100, 255, 100)
        if i == chosed:
            cr = (100, 175, 100)
        text = font.render(texts[i], 1, cr)
        text_h = text.get_height()
        text_w = text.get_width()
        text_x = WIDTH // 2 - text.get_width() // 2
        text_y = (HEIGHT // 5) * i + text_h // 2 + HEIGHT // 10
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        MENUBTTNS[i] = ((text_x, text_y, text_w, text_h), cr)


def what_is_pressed(buttons, pos):
    x, y = pos
    for iteration, i in enumerate(buttons):
        if i[0][2] + i[0][0] >= x >= i[0][0] and i[0][1] <= y <= i[0][1] + i[0][3]:
            return iteration
        print(i[0][2] + i[0][0], x, i[0][0], '\n',
              i[0][1] + i[0][3], y, i[0][1])


def start_screen():
    main_menu()
    in_menu = True
    flag = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                iteration = what_is_pressed(MENUBTTNS, (x, y))
                if iteration == 3:
                    flag = terminate
                elif iteration == 2:
                    flag = settings_screen
                elif iteration == 1:
                    flag = continue_screen
                else:
                    flag = choose_mode_screen
                main_menu(iteration)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if flag is not None:
                    iter = what_is_pressed(MENUBTTNS, event.pos)
                    if iter == iteration:
                        in_menu = False
                        break
                    else:
                        flag = None
                    main_menu()

        if not in_menu:
            break

        pygame.display.flip()
        clock.tick(FPS)
    flag()


def settings_screen():
    pass


def continue_screen():
    pass


def choose_mode_screen():
    choose_mode()
    flag = None
    global PLAYRSCOUNT
    choosing = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                btn = what_is_pressed(MODEBTTNS, (x, y))
                if btn == 0:
                    flag = 1
                elif btn == 1:
                    flag = 2
                else:
                    flag = game
                choose_mode(btn)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if flag is not None:
                    iter = what_is_pressed(MODEBTTNS, event.pos)
                    if iter == btn:
                        if iter == 0:
                            PLAYRSCOUNT = 1
                        elif iter == 1:
                            PLAYRSCOUNT = 2
                        else:
                            if PLAYRSCOUNT != 0:
                                choosing = False
                                break
                    else:
                        flag = None
                    choose_mode()
        if not choosing:
            break
        pygame.display.flip()
        clock.tick(FPS)
    flag()


def generate_level(level):
    green_spawnpoint, red_spawnpoint = None, None  # Точки появления для игроков
    enemies_spawnpoints = []  # список с точками появления проивников

    for y in range(1, len(level), 2):
        for x in range(1, len(level[y]), 2):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == 'G':
                green_spawn = (x, y)
            elif level[y][x] == 'R':
                red_spawn = (x, y)
            elif level[y][x] == 'E':
                enemies_spawnpoints.append((x, y))
    return green_spawnpoint, red_spawnpoint, enemies_spawnpoints


def game():
    pass


tile_images = {'empty': load_image('grass.png'), 'wall': load_image('box.png')}
player_image = load_image('tank_green_mk1.png')

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


start_screen()

pygame.quit()
