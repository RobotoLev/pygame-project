import random
import pygame
from source.system_functions import *

FPS = 30
WIDTH = 1072
HEIGHT = 603
MENUBTTNS = [None for _ in range(4)]
MODEBTTNS = [None for _ in range(4)]
STNGBTTNS = [None for _ in range(4)]
PLAYRSCOUNT = 0
LEVELS = 2


player_one = None
player_two = None
VELOCITY = 4
VOLUME = 50
WASDBTTNS = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_LSHIFT]
ARRWBTTNS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE]
PLAYRSKEYS = [WASDBTTNS, ARRWBTTNS]
ANGLES = {0: 0, 1: 2, 2: 3, 3: 1}

PLAYER_DAMAGE = [None, 400, 400, 500]
PLAYER_SHOT_DAMAGE = [None, 100, 100, 200]
ENEMY_DAMAGE = [None, 100, 200, 300]
ENEMY_SHOT_DAMAGE = [None, 100, 200, 300]
PLAYER_HP = [None, 100, 200, 400]
ENEMY_HP = [None, 100, 100, 300]
SHOT_VELOCITY = 5
MAXDIST = 300

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
tank_shot = pygame.mixer.Sound('data/Sounds/tank_shot.wav')
sounds = list()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
iteration = 0


def pause(chosed=None, moved=None):
    screen.fill(pygame.Color('black'))
    tile_group.draw(screen)
    player_group.draw(screen)
    enemy_group.draw(screen)
    player_damageable_group.draw(screen)
    enemy_damageable_group.draw(screen)
    temporary_group.draw(screen)
    solid_group.draw(screen)
    image = pygame.Surface([WIDTH // 3, HEIGHT])
    image.fill(pygame.Color("black"))
    screen.blit(image, (WIDTH // 3, 0))
    font = pygame.font.Font(None, 50)
    texts = ["Продолжить", "Настройки", "Выйти в меню", "Выход"]
    for i in range(4):
        width = 1
        cr = (100, 255, 100)
        if i == chosed:
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


def settings(chosed=None, moved=None):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    texts = ['1 игрок', '2 игрока', 'Громкость', 'НАЗАД']
    for i in range(4):
        cr = (100, 255, 100)
        width = 1
        if chosed == i == 3:
            cr = (100, 175, 100)
            width = 2
        elif moved == i == 3:
            cr = (170, 255, 170)

        text = font.render(texts[i], 1, cr)
        text_h = text.get_height()
        text_w = text.get_width()
        text_y = HEIGHT // 5 * (i + 1) - text_h // 2
        if i != 3:
            text_x = WIDTH // 8 - text_w // 2
        else:
            text_x = WIDTH // 2 - text_w // 2
        screen.blit(text, (text_x, text_y))
        if i != 3:
            text_x = WIDTH // 3 * 2
            text_w = WIDTH // 4
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10 - width // 2, text_y - 10 - width // 2,
                                               text_w + 20, text_h + 20), width)
        if i == 2:
            pygame.draw.rect(screen, (0, 255, 0), (text_x - 10 - width // 2,
                                                   text_y - 10 - width // 2,
                                                   (text_w + 20) * (VOLUME / 100), text_h + 20))
            vol = font.render(str(VOLUME), 1, cr)
            screen.blit(vol, (text_x + 10 - width // 2 + text_w, text_y - 10 - width // 2))
        elif i == 0:
            if PLAYRSKEYS[0] == WASDBTTNS:
                screen.blit(load_image('WASD_picture.png'), (text_x - 10 - width // 2,
                                                             text_y - 10 - width // 2))
            else:
                screen.blit(load_image('Arrs_picture.png'), (text_x - 10 - width // 2,
                                                             text_y - 10 - width // 2))
        elif i == 1:
            if PLAYRSKEYS[1] == WASDBTTNS:
                screen.blit(load_image('WASD_picture.png'), (text_x - 10 - width // 2,
                                                             text_y - 10 - width // 2))
            else:
                screen.blit(load_image('Arrs_picture.png'), (text_x - 10 - width // 2,
                                                             text_y - 10 - width // 2))
        STNGBTTNS[i] = (((text_x - 10 - width // 2, text_y - 10 - width // 2,
                          text_w + 20, text_h + 20)), cr)


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


def pause_screen():
    pause()
    in_menu = True
    flag = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
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
                pause(btn)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if flag is not None:
                    iter = what_is_pressed(MENUBTTNS, event.pos)
                    if iter == btn:
                        if iter == 0:
                            return
                        elif iter == 1:
                            settings_screen(True)
                        elif iter == 2:
                            return start_screen
                        elif iter == 3:
                            terminate()
                        break
                    else:
                        flag = None
                    pause()
            elif event.type == pygame.MOUSEMOTION:
                butn = what_is_pressed(MENUBTTNS, event.pos)
                if 1 in event.buttons:
                    pause(btn, butn)
                else:
                    pause(moved=butn)
        if not in_menu:
            break

        pygame.display.flip()
        clock.tick(FPS)


def settings_screen(on_pause=False):
    flag = None
    global VOLUME
    settings()
    in_menu = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                btn = what_is_pressed(STNGBTTNS, (x, y))
                if btn == 3:
                    flag = start_screen
                elif btn == 2:
                    flag = 2
                elif btn == 1:
                    flag = 1
                elif btn == 0:
                    flag = 0
                settings(btn)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if flag is not None:
                    iter = what_is_pressed(STNGBTTNS, event.pos)
                    if iter == btn:
                        if iter == 3:
                            if on_pause:
                                return
                            in_menu = False
                            break
                        elif iter == 0:
                            if PLAYRSKEYS[0] == WASDBTTNS:
                                PLAYRSKEYS[0] = ARRWBTTNS
                            else:
                                PLAYRSKEYS[0] = WASDBTTNS
                        elif iter == 1:
                            if PLAYRSKEYS[1] == WASDBTTNS:
                                PLAYRSKEYS[1] = ARRWBTTNS
                            else:
                                PLAYRSKEYS[1] = WASDBTTNS
                    else:
                        flag = None
                    settings()
            elif event.type == pygame.MOUSEMOTION:
                butn = what_is_pressed(STNGBTTNS, event.pos)
                if 1 in event.buttons:
                    x, y = event.pos
                    if flag == 2:
                        VOLUME = int(((x - STNGBTTNS[2][0][0]) * 100 / STNGBTTNS[2][0][2]))
                        if VOLUME > 100:
                            VOLUME = 100
                        elif VOLUME < 0:
                            VOLUME = 0
                        tank_shot.set_volume(VOLUME / 100)
                        for i in sounds:
                            i.set_volume(VOLUME / 100)
                    settings(btn, butn)
                else:
                    settings(moved=butn)
        if not in_menu:
            break

        pygame.display.flip()
        clock.tick(FPS)
    flag()


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
                if random.randint(1, 10) == 1:
                    Tree('default', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '#':
                Building('wall', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'G':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
                player_one = Player(1, (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'R':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
                if PLAYRSCOUNT == 2:
                    player_two = Player(2, (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'E':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
                enemies_spawnpoints.append(((x - 1) // 2, (y - 1) // 2))
            elif level[y][x] == 'V':
                Tile('ver_rail', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'H':
                Tile('hor_rail', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '2':
                Tile('ver_rail_be', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '8':
                Tile('ver_rail_te', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '4':
                Tile('hor_rail_le', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '6':
                Tile('hor_rail_re', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'W':
                Tile('ver_rail', (x - 1) // 2, (y - 1) // 2)
                Train('verti', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'A':
                Tile('hor_rail', (x - 1) // 2, (y - 1) // 2)
                Train('horiz', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'T':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
                Tree('default', (x - 1) // 2, (y - 1) // 2)
    for y in range(1, len(level), 2):
        for x in range(0, len(level[y]), 2):
            if level[y][x] == 'V':
                Boarding('verti', x // 2, (y - 1) // 2)
    for y in range(0, len(level), 2):
        for x in range(1, len(level[y]), 2):
            if level[y][x] == 'H':
                Boarding('horiz', (x - 1) // 2, y // 2)
    return green_spawnpoint, red_spawnpoint, enemies_spawnpoints


def level_play(level='level1.txt'):
    global ENEMIES_LEFT
    print('Game has been started')
    in_game = True

    all_sprites.empty()
    tile_group.empty()
    player_group.empty()
    object_group.empty()
    solid_group.empty()
    player_damageable_group.empty()
    enemy_damageable_group.empty()
    temporary_group.empty()

    level, ENEMIES_LEFT = load_level(level)
    enemies_to_spawn = ENEMIES_LEFT
    green, red, enemies = generate_level(level)
    enemies = list(map(lambda x: [*x, random.randint(0, 30)], enemies))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    res = pause_screen()
                    if res is not None:
                        in_game = False
                        break
                print("Pressed", key)
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
                    if 0 <= idx <= 3:
                        player.moving = True
                        player.angle = ANGLES[idx]
                    if idx == 4:
                        player.shoot()
            elif event.type == pygame.KEYUP:
                key = event.key
                if (key in PLAYRSKEYS[0] and
                        (PLAYRSKEYS[0].index(key), player_one.angle) in list(ANGLES.items())):
                    player_one.moving = False
                if (key in PLAYRSKEYS[1] and PLAYRSCOUNT == 2 and
                        (PLAYRSKEYS[1].index(key), player_two.angle) in list(ANGLES.items())):
                    player_two.moving = False
        if not in_game:
            break
        for i in enemies:
            if i[2] >= 120 and random.randint(1, 8) == 1 and enemies_to_spawn > 0:
                Enemy(i[0], i[1])
                i[2] = -1
                enemies_to_spawn -= 1
            i[2] += 1

        screen.fill(pygame.Color('black'))
        tile_group.draw(screen)
        player_group.draw(screen)
        enemy_group.draw(screen)
        player_damageable_group.draw(screen)
        enemy_damageable_group.draw(screen)
        temporary_group.draw(screen)
        solid_group.draw(screen)
        if ENEMIES_LEFT == 0:
            return

        pygame.display.flip()
        all_sprites.update()
        clock.tick(FPS)
    res()


def game(start_level=0):
    level = start_level
    while True:
        level += 1
        level_play(f'level{level}.txt')
        print(level)


tile_images = {'empty': load_image('grass.png'),
               'hor_rail': load_image('horizontal_rails.png'),
               'hor_rail_le': load_image('horizontal_rails_lef_end.png'),
               'hor_rail_re': load_image('horizontal_rails_rig_end.png'),
               'ver_rail': load_image('vertical_rails.png'),
               'ver_rail_te': load_image('vertical_rails_top_end.png'),
               'ver_rail_be': load_image('vertical_rails_bot_end.png')}
board_images = {'horiz': [load_image('board_horizontal.png'),
                          load_image('board_horizontal_damaged.png')],
                'verti': [load_image('board_vertical.png'),
                          load_image('board_vertical_damaged.png')]}
train_images = {'horiz': [load_image('horizontal_train.png'),
                          load_image('horizontal_train_damaged.png')],
                'verti': [load_image('vertical_train.png'),
                          load_image('vertical_train_damaged.png')]}
tree_images = {'default': [load_image('trees\\tree_default_0.png'),
                           load_image('trees\\tree_default_1.png'),
                           load_image('trees\\tree_default_2.png'),
                           load_image('trees\\tree_default_3.png')]}
player_one_images = [None] +\
                    [get_rotated_images('tanks\\source_tanks\\tank_green_mk{}.png'.format(i), 180)
                     for i in range(1, 4)]
player_two_images = [None] +\
                    [get_rotated_images('tanks\\source_tanks\\tank_red_mk{}.png'.format(i), 180)
                     for i in range(1, 4)]
enemy_images = [get_rotated_images('tanks\\source_tanks\\tank_enemy_mk{}.png'.format(i), 0)
                for i in range(1, 4)]
# building_images = {'rt': load_image('building_right-top.png'),
#                    'lt': load_image('building_left-top.png'),
#                    'rb': load_image('building_right-bot.png'),
#                    'lb': load_image('building_left-bot.png'),
#                    'mt': load_image('building_mid-top.png'),
#                    'mr': load_image('building_mid-right.png'),
#                    'mb': load_image('building_mid-bot.png'),
#                    'ml': load_image('building_mid-left.png'),
#                    'center': load_image('building_center.png'),
#                    'wall': load_image('box.png')}
building_images = {'wall': load_image('box.png')}
shot_start_images = [
    [rotate_image(load_image('shot_start_{}.png'.format(i + 1)), 270) for i in range(4)],
    [load_image('shot_start_{}.png'.format(i + 1)) for i in range(4)],
    [rotate_image(load_image('shot_start_{}.png'.format(i + 1)), 90) for i in range(4)],
    [rotate_image(load_image('shot_start_{}.png'.format(i + 1)), 180) for i in range(4)]]
shot_end_images = [
    [rotate_image(load_image('shot_end_{}.png'.format(i + 1)), 270) for i in range(4)],
    [load_image('shot_end_{}.png'.format(i + 1)) for i in range(4)],
    [rotate_image(load_image('shot_end_{}.png'.format(i + 1)), 90) for i in range(4)],
    [rotate_image(load_image('shot_end_{}.png'.format(i + 1)), 180) for i in range(4)]]
# группы спрайтов
tile_width, tile_height = 50, 50

all_sprites = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

object_group = pygame.sprite.Group()
player_damageable_group = pygame.sprite.Group()
enemy_damageable_group = pygame.sprite.Group()
solid_group = pygame.sprite.Group()
temporary_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tile_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Object(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(list(groups) + [object_group])
        self.strength = 1000
        self.image = None
        self.fireable = False
        self.is_fired = False
        self.images = []

        self.is_update_images = True

    def damage(self, damage_level, shot=False):
        self.strength -= damage_level
        if shot and self.fireable:
            self.is_fired = True
            self.fire_damage = 1

    def update(self):
        global ENEMIES_LEFT
        if self.strength <= 0:
            if type(self) == Enemy:
                ENEMIES_LEFT -= 1
            self.kill()

        if self.is_update_images:
            for image in self.images:
                if image[0] <= self.strength <= image[1]:
                    self.image = image[2]

        if self.is_fired:
            self.strength -= self.fire_damage
            if random.randint(1, 8) == 1 and self.fire_damage <= 5:
                self.fire_damage += 1


class Building(Object):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(solid_group, all_sprites)
        self.strength = float("inf")
        self.image = building_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Boarding(Object):
    def __init__(self, board_type, pos_x, pos_y):
        super().__init__(player_damageable_group, enemy_damageable_group, all_sprites)
        self.strength = 600
        self.images = [[1, 300, board_images[board_type][1]],
                       [301, 600, board_images[board_type][0]]]
        self.image = board_images[board_type][0]
        board_width = 4
        board_height = 4
        self.rect = self.image.get_rect().move(tile_width * pos_x - board_width,
                                               tile_height * pos_y - board_height)


class Train(Object):
    def __init__(self, train_type, pos_x, pos_y):
        super().__init__(player_damageable_group, enemy_damageable_group, all_sprites)
        self.strength = 800
        self.images = [[1, 400, train_images[train_type][1]],
                       [401, 800, train_images[train_type][0]]]
        self.image = train_images[train_type][0]

        board_width = 2
        board_height = 2
        self.rect = self.image.get_rect().move(tile_width * pos_x + board_width,
                                               tile_height * pos_y + board_height)


class Tree(Object):
    def __init__(self, tree_type, pos_x, pos_y):
        super().__init__(player_damageable_group, enemy_damageable_group, all_sprites)
        self.strength = 400
        self.fireable = True
        self.images = [[133, 200, tree_images[tree_type][1]],
                       [201, 400, tree_images[tree_type][0]],
                       [66, 132, tree_images[tree_type][2]],
                       [0, 65, tree_images[tree_type][3]]]
        self.image = tree_images[tree_type][0]
        board_width = random.randint(1, 35)
        board_height = random.randint(1, 35)
        self.rect = self.image.get_rect().move(tile_width * pos_x + board_width,
                                               tile_height * pos_y + board_height)


class Player(Object):
    def __init__(self, num, pos_x, pos_y, level=1):
        super().__init__(player_group, enemy_damageable_group, all_sprites)

        self.num = num
        self.level = level
        self.level = 1
        self.xp = 0
        self.angle = 0
        self.delay = 0
        self.strength = PLAYER_HP[self.level]
        self.moving = False
        self.is_update_images = False

        self.update_image()
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

    def update(self):
        super().update()
        self.update_level()
        self.update_image()

        self.delay -= 1
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

        res = pygame.sprite.spritecollide(self, player_damageable_group, False)
        for obj in res:
            if type(obj) != Enemy:
                obj.damage(PLAYER_DAMAGE[self.level])

        condition = (pygame.sprite.spritecollideany(self, solid_group, False) or
                     pygame.sprite.spritecollideany(self, player_damageable_group, False) or
                     len(pygame.sprite.spritecollide(self, player_group, False)) > 1)
        if condition:
            self.rect = self.rect.move(-delta_x, -delta_y)
            self.moving = False

    def update_level(self):
        if self.level == len(PLAYER_LEVELS_LIMIT) - 1:
            return
        if self.xp > PLAYER_LEVELS_LIMIT[self.level + 1]:
            self.xp = 0
            self.level += 1
            self.update_image()

    def update_image(self):
        if self.num == 1:
            images = player_one_images
        else:
            images = player_two_images
        self.image = images[self.level][self.angle]

    def shoot(self):
        if self.delay <= 0:
            tank_shot.play()
            Shot(self)
            self.delay = 30


class Enemy(Object):
    def __init__(self, pos_x, pos_y, level=1):
        super().__init__(enemy_group, player_damageable_group, all_sprites)

        self.level = level
        self.angle = 0
        self.moving = False
        self.is_update_images = False
        self.strength = ENEMY_HP[level]

        if PLAYRSCOUNT == 1:
            self.player = player_one
        else:
            self.player = random.choice([player_one, player_two])

        self.update_image()
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.delay = 10
        self.shoot_delay = 0

    def update(self):
        super().update()
        self.update_image()
        self.move()

        self.shoot()
        self.shoot_delay -= 1

        if self.delay > 0:
            self.delay -= 1
            return
        self.moving = False

        if random.randint(1, 5) == 1:
            self.delay = random.randint(10, 20)
            return

        dx, dy = self.get_dist()

        angles = [0, 1, 2, 3]
        if abs(dx) > MAXDIST:
            if dx > 0:
                angles.remove(1)
            else:
                angles.remove(3)

        if abs(dy) > MAXDIST:
            if dy > 0:
                angles.remove(2)
            else:
                angles.remove(0)

        self.delay = random.randint(10, 30)
        self.angle = random.choice(angles)
        self.moving = True

    def get_dist(self):
        dx = self.rect.x - self.player.rect.x
        dy = self.rect.y - self.player.rect.y
        return dx, dy

    def move(self):
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

        res = pygame.sprite.spritecollide(self, enemy_damageable_group, False)
        for obj in res:
            if type(obj) != Player:
                obj.damage(ENEMY_DAMAGE[self.level])

        condition = (pygame.sprite.spritecollideany(self, solid_group, False) or
                     pygame.sprite.spritecollideany(self, enemy_damageable_group, False) or
                     len(pygame.sprite.spritecollide(self, enemy_group, False)) > 1)
        if condition:
            self.rect = self.rect.move(-delta_x, -delta_y)

    def update_image(self):
        images = enemy_images
        self.image = images[self.level][self.angle]

    def shoot(self):
        if self.shoot_delay <= 0:
            tank_shot.play()
            Shot(self)
            self.shoot_delay = random.randint(30, 120)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(list(groups))

        self.images = []
        self.cur_image = -1
        self.cadres = 1
        self.delay = 0
        self.lifetime = float("inf")

        self.image = None
        self.rect = None

    def update(self):
        if self.delay > 0:
            self.delay -= 1
            return

        if self.lifetime == 0:
            self.kill()
            return

        self.cur_image = (self.cur_image + 1) % (len(self.images) * self.cadres)
        self.image = self.images[self.cur_image // self.cadres]

        if self not in temporary_group.sprites():
            temporary_group.add(self)

        if self.cur_image == len(self.images) * self.cadres - 1:
            self.lifetime -= 1


class ShotStart(AnimatedSprite):
    def __init__(self, pos_x, pos_y, angle):
        super().__init__(all_sprites)
        self.images = shot_start_images[angle]
        self.rect = pygame.Rect(pos_x, pos_y, 48, 48)

        self.cadres = 1
        self.lifetime = 1


class ShotEnd(AnimatedSprite):
    def __init__(self, pos_x, pos_y, angle, res, level, is_player, obj):
        super().__init__(all_sprites)
        self.images = shot_end_images[angle]
        self.rect = pygame.Rect(pos_x, pos_y, 48, 48)

        self.res = res
        self.level = level
        self.is_player = is_player
        self.obj = obj

        self.cadres = 1
        self.lifetime = 1
        self.delay = 4

    def kill(self):
        if self.is_player:
            damage = PLAYER_SHOT_DAMAGE[self.level]

            res_type = type(self.res)
            if res_type in PLAYER_SHOT_XP and self.res.strength <= damage:
                self.obj.xp += PLAYER_SHOT_XP[res_type]
        else:
            damage = ENEMY_SHOT_DAMAGE[self.level]
        if not self.is_player or type(self.res) != Player:
            self.res.damage(damage, True)
        super().kill()


class Shot(pygame.sprite.Sprite):
    def __init__(self, obj):
        super().__init__(all_sprites, temporary_group)
        angle = obj.angle
        pos_x = obj.rect.x
        pos_y = obj.rect.y
        level = obj.level
        is_player = type(obj) == Player

        if angle == 0:
            self.x = pos_x + 23
            self.y = pos_y
        elif angle == 1:
            self.x = pos_x + 48
            self.y = pos_y + 23
        elif angle == 2:
            self.x = pos_x + 23
            self.y = pos_y + 48
        else:
            self.x = pos_x
            self.y = pos_y + 23
        self.rect = pygame.Rect(self.x, self.y, 4, 4)

        start = True
        while pygame.sprite.spritecollideany(self, object_group) is None or start:
            start = False
            delta_x = 0
            delta_y = 0
            if angle == 0:
                delta_y -= SHOT_VELOCITY
            elif angle == 1:
                delta_x += SHOT_VELOCITY
            elif angle == 2:
                delta_y += SHOT_VELOCITY
            else:
                delta_x -= SHOT_VELOCITY

            self.rect = self.rect.move(delta_x, delta_y)

        res = pygame.sprite.spritecollideany(self, object_group)

        x = pos_x
        y = pos_y
        if angle == 0:
            y -= 48
        elif angle == 1:
            x += 48
        elif angle == 2:
            y += 48
        else:
            x -= 48
        ShotStart(x, y, angle)

        if angle == 0:
            x = self.rect.x - 22
            y = res.rect.y + res.rect.height
        elif angle == 1:
            x = res.rect.x - 48
            y = self.rect.y - 22
        elif angle == 2:
            x = self.rect.x - 22
            y = res.rect.y - 48
        else:
            x = res.rect.x + res.rect.width
            y = self.rect.y - 22

        ShotEnd(x, y, angle, res, level, is_player, obj)
        self.kill()


PLAYER_SHOT_XP = {Boarding: 100, Tree: 100, Train: 200, Enemy: 500}
PLAYER_LEVELS_LIMIT = [None, 0, 200, 300]

start_screen()
# PLAYRSCOUNT = 2
# level_play()
pygame.quit()
