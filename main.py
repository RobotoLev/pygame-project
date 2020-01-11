import random
import pygame
from source.system_functions import load_image, terminate, load_level


FPS = 30
WIDTH = 1072
HEIGHT = 603
MENUBTTNS = [None for _ in range(4)]
MODEBTTNS = [None for _ in range(4)]
PLAYRSCOUNT = 0


# Включить, когда будет объект игрока с координатами
# UPD. Включение откладывается, т.к. есть новая версия
#
# def move_player(player, delta_x, delta_y):
#     print("Привет")
#     if player is not None:
#         print("Привет еще раз")
#         player.rect = player.image.get_rect().move(delta_x, delta_y)

# Вторая версия функции
# Закоментированно по ненадобности
#
# def move_player(key):
#     global PLAYRSKEYS, KEYBTTNS, player_one, player_two
#
#     if key in PLAYRSKEYS["player_one"]:
#         player = player_one
#     else:
#         if PLAYRSCOUNT == 2:
#             player = player_two
#         else:
#             return
#
#     delta_x = 0
#     delta_y = 0
#     if key in {119, 273}:
#         delta_y -= VELOCITY
#     elif key in {97, 276}:
#         delta_x -= VELOCITY
#     elif key in {115, 274}:
#         delta_y += VELOCITY
#     else:
#         delta_x += VELOCITY
#
#     player.rect = player.rect.move(delta_x, delta_y)


# Объект игрока и константа его скорости
player_one = None
player_two = None
VELOCITY = 2

WASDBTTNS = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_LSHIFT]
ARRWBTTNS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE]
PLAYRSKEYS = [WASDBTTNS, ARRWBTTNS]
ANGLES = {0: 0, 1: 2, 2: 3, 3: 1}
# KEYBTTNS = {119: move_player,
#             97: move_player,
#             115: move_player,
#             100: move_player,
#             273: move_player,
#             276: move_player,
#             274: move_player,
#             275: move_player}


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
iteration = 0


def choose_mode(chosed=None, moved=None):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    texts = ['1 игрок', '2 игрока', 'СТАРТ', 'НАЗАД']
    for i in range(4):
        cr = (100, 255, 100)
        width = 1
        if chosed == i:
            cr = (100, 175, 100)
            width = 2
        elif moved == i:
            cr = (170, 255, 170)
        if PLAYRSCOUNT - 1 == i:
            cr = (50, 205, 50)
            width = 4

        text = font.render(texts[i], 1, cr)
        text_h = text.get_height()
        text_w = text.get_width()
        text_y = HEIGHT // 4 - text_h // 2
        text_x = WIDTH // 3 * i + WIDTH // 4
        if i == 2:
            text_y = HEIGHT // 4 * 2.5 - text_h // 2
            text_x = WIDTH // 2 - text_w // 2
        elif i == 3:
            text_y = HEIGHT // 4 * 3.5 - text_h // 2
            text_x = WIDTH // 2 - text_w // 2
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10 - width // 2, text_y - 10 - width // 2,
                                               text_w + 20, text_h + 20), width)
        MODEBTTNS[i] = ((text_x - 10 - width // 2, text_y - 10,
                         text_w + 20 - width // 2, text_h + 20), cr)


def main_menu(pressed=None, moved=None):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    texts = ["Новая игра", "Продолжить", "Настройки", "Выход"]
    for i in range(4):
        width = 1
        cr = (100, 255, 100)
        if i == pressed:
            cr = (50, 175, 100)
            width = 2
        elif i == moved:
            cr = (180, 255, 180)
        text = font.render(texts[i], 1, cr)
        text_h = text.get_height()
        text_w = text.get_width()
        text_x = WIDTH // 2 - text.get_width() // 2
        text_y = (HEIGHT // 5) * i + text_h // 2 + HEIGHT // 10
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10 - width // 2, text_y - 10,
                                               text_w + 20 - width // 2, text_h + 20), width)
        MENUBTTNS[i] = ((text_x - 10 - width // 2, text_y - 10,
                         text_w + 20 - width // 2, text_h + 20), cr)


def what_is_pressed(buttons, pos):
    x, y = pos
    for iteration, i in enumerate(buttons):
        if i[0][2] + i[0][0] >= x >= i[0][0] and i[0][1] <= y <= i[0][1] + i[0][3]:
            return iteration


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
                btn = what_is_pressed(MENUBTTNS, (x, y))
                if btn == 3:
                    flag = terminate
                elif btn == 2:
                    flag = settings_screen
                elif btn == 1:
                    flag = continue_screen
                elif btn == 0:
                    flag = choose_mode_screen
                main_menu(btn)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if flag is not None:
                    iter = what_is_pressed(MENUBTTNS, event.pos)
                    if iter == btn:
                        in_menu = False
                        break
                    else:
                        flag = None
                    main_menu()
            elif event.type == pygame.MOUSEMOTION:
                butn = what_is_pressed(MENUBTTNS, event.pos)
                if 1 in event.buttons:
                    main_menu(btn, butn)
                else:
                    main_menu(moved=butn)

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
                elif btn == 2:
                    flag = game
                else:
                    flag = start_screen
                choose_mode(btn)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if flag is not None:
                    iter = what_is_pressed(MODEBTTNS, event.pos)
                    if iter == btn:
                        if iter == 0:
                            PLAYRSCOUNT = 1
                        elif iter == 1:
                            PLAYRSCOUNT = 2
                        elif iter == 2:
                            if PLAYRSCOUNT != 0:
                                choosing = False
                                break
                        elif iter == 3:
                            choosing = False
                            PLAYRSCOUNT = 0
                            break
                    else:
                        flag = None
                    choose_mode()
            elif event.type == pygame.MOUSEMOTION:
                butn = what_is_pressed(MODEBTTNS, event.pos)
                if 1 in event.buttons:
                    choose_mode(btn, butn)
                else:
                    choose_mode(moved=butn)
        if not choosing:
            break
        pygame.display.flip()
        clock.tick(FPS)
    flag()


def generate_level(level):
    global player_one, player_two
    green_spawnpoint, red_spawnpoint = None, None  # Точки появления для игроков
    enemies_spawnpoints = []  # список с точками появления проивников

    for y in range(1, len(level), 2):
        for x in range(1, len(level[y]), 2):
            if level[y][x] == '.':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '#':
                Tile('wall', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'G':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
                player_one = Player((x - 1) // 2, (y - 1) // 2)
                # green_spawn = ((x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'R':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
                if PLAYRSCOUNT == 2:
                    player_two = Player((x - 1) // 2, (y - 1) // 2)
                    # red_spawn = ((x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'E':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
                enemies_spawnpoints.append(((x - 1) // 2, (y - 1) // 2))
            elif level[y][x] == '9':
                Building('rt', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '7':
                Building('lt', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '1':
                Building('lb', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '3':
                Building('rb', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '8':
                Building('mt', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '6':
                Building('mr', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '2':
                Building('mb', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '4':
                Building('ml', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '5':
                Building('center', (x - 1) // 2, (y - 1) // 2)
    for y in range(1, len(level), 2):
        for x in range(0, len(level[y]), 2):
            if level[y][x] == 'V':
                Boarding('verti', x // 2, (y - 1) // 2)
    for y in range(0, len(level), 2):
        for x in range(1, len(level[y]), 2):
            if level[y][x] == 'H':
                Boarding('horiz', (x - 1) // 2, y // 2)
    return green_spawnpoint, red_spawnpoint, enemies_spawnpoints


def game():
    print('Game has been started')
    level = load_level('level1.txt')
    generate_level(level)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                key = event.key
                print("Pressed", key)
                # if key in KEYBTTNS:
                #     KEYBTTNS[key](key)
                for num, keys in enumerate(PLAYRSKEYS):
                    if key not in keys:
                        continue
                    if num == 0:
                        player = player_one
                    else:
                        if PLAYRSCOUNT == 2:
                            player = player_two
                        else:
                            continue

                    idx = keys.index(key)
                    if idx != 4:
                        player.moving = True
                        player.angle = ANGLES[idx]
            elif event.type == pygame.KEYUP:
                key = event.key
                if (key in PLAYRSKEYS[0] and
                        (PLAYRSKEYS[0].index(key), player_one.angle) in list(ANGLES.items())):
                    player_one.moving = False
                if (key in PLAYRSKEYS[1] and PLAYRSCOUNT == 2 and
                        (PLAYRSKEYS[1].index(key), player_two.angle) in list(ANGLES.items())):
                    player_two.moving = False

        screen.fill(pygame.Color('black'))
        all_sprites.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()

        player_group.update()
        clock.tick(FPS)
    pass


tile_images = {'empty': load_image('grass.png'), 'wall': load_image('box.png')}
board_images = {'horiz': load_image('board_horizontal.png'), 'verti': load_image('board_vertical.png')}
player_image = load_image('tank_green_mk1.png')
building_images = {'rt': load_image('building_right-top.png'),
                   'lt': load_image('building_left-top.png'),
                   'rb': load_image('building_right-bot.png'),
                   'lb': load_image('building_left-bot.png'),
                   'mt': load_image('building_mid-top.png'),
                   'mr': load_image('building_mid-right.png'),
                   'mb': load_image('building_mid-bot.png'),
                   'ml': load_image('building_mid-left.png'),
                   'center': load_image('building_center.png')}
# группы спрайтов
tile_width, tile_height = 50, 50
all_sprites = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
board_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
building_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tile_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Building(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(building_group, all_sprites)
        self.image = building_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Boarding(pygame.sprite.Sprite):
    def __init__(self, board_type, pos_x, pos_y):
        super().__init__(board_group, all_sprites)
        self.image = board_images[board_type]
        board_width = board_height = 0
        board_width = 4
        board_height = 4
        self.rect = self.image.get_rect().move(tile_width * pos_x - board_width, tile_height * pos_y - board_height)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

        self.angle = 0
        self.moving = False

    def update(self):
        if not self.moving:
            return

        delta_x = 0
        delta_y = 0
        if self.angle == 0:
            delta_y -= VELOCITY
        elif self.angle == 1:
            delta_x += VELOCITY
        elif self.angle == 2:
            delta_y += VELOCITY
        else:
            delta_x -= VELOCITY

        self.rect = self.rect.move(delta_x, delta_y)


start_screen()
pygame.quit()
