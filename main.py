import random
import pygame
from source.system_functions import load_image, terminate, load_level

FPS = 30
WIDTH = 1072
HEIGHT = 603
MENUBTTNS = [None for _ in range(4)]
MODEBTTNS = [None for _ in range(4)]
STNGBTTNS = [None for _ in range(4)]
PLAYRSCOUNT = 0


player_one = None
player_two = None
VELOCITY = 5
VOLUME = 50
WASDBTTNS = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_LSHIFT]
ARRWBTTNS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE]
PLAYRSKEYS = [WASDBTTNS, ARRWBTTNS]
ANGLES = {0: 0, 1: 2, 2: 3, 3: 1}

TANK_DAMAGE = [None, 100, 200, 500]


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
iteration = 0


def pause(chosed=None, moved=None):
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
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
            elif level[y][x] == '#':
                Building('wall', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'G':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
                player_one = Player(1, (x - 1) // 2, (y - 1) // 2)
                # green_spawn = ((x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'R':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
                if PLAYRSCOUNT == 2:
                    player_two = Player(2, (x - 1) // 2, (y - 1) // 2)
                    # red_spawn = ((x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'E':
                Tile('empty', (x - 1) // 2, (y - 1) // 2)
                enemies_spawnpoints.append(((x - 1) // 2, (y - 1) // 2))
            elif level[y][x] == 'V':
                Tile('rail_vert', (x - 1) // 2, (y - 1) // 2)

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
    in_game = True

    all_sprites.empty()
    tile_group.empty()
    player_group.empty()
    solid_group.empty()
    damageable_group.empty()

    level = load_level('level1.txt')
    generate_level(level)
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
        if not in_game:
            break

        screen.fill(pygame.Color('black'))
        all_sprites.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()

        all_sprites.update()
        clock.tick(FPS)
    res()


tile_images = {'empty': load_image('grass.png')}
board_images = {'horiz': load_image('board_horizontal.png'),
                'verti': load_image('board_vertical.png')}
player_one_images = [load_image('tanks\\tank_green_mk1_{}.png'.format(i)) for i in range(4)]
player_two_images = [load_image('tanks\\tank_red_mk1_{}.png'.format(i)) for i in range(4)]
building_images = {'rt': load_image('building_right-top.png'),
                   'lt': load_image('building_left-top.png'),
                   'rb': load_image('building_right-bot.png'),
                   'lb': load_image('building_left-bot.png'),
                   'mt': load_image('building_mid-top.png'),
                   'mr': load_image('building_mid-right.png'),
                   'mb': load_image('building_mid-bot.png'),
                   'ml': load_image('building_mid-left.png'),
                   'center': load_image('building_center.png'),
                   'wall': load_image('box.png')}
# группы спрайтов
tile_width, tile_height = 50, 50
all_sprites = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
damageable_group = pygame.sprite.Group()
solid_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tile_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Object(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(groups)
        self.strength = 1000

    def damage(self, damage_level):
        self.strength -= damage_level

    def update(self):
        if self.strength <= 0:
            self.kill()

        # Сюда можно подцепить подмену изображений с уменьшением прочности
        # (забор трескается)


class Building(Object):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(solid_group, all_sprites)
        self.strength = float("inf")
        self.image = building_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Boarding(Object):
    def __init__(self, board_type, pos_x, pos_y):
        super().__init__(damageable_group, all_sprites)
        # self.strength = 300
        self.image = board_images[board_type]
        board_width = board_height = 0
        board_width = 4
        board_height = 4
        self.rect = self.image.get_rect().move(tile_width * pos_x - board_width,
                                               tile_height * pos_y - board_height)


class Player(Object):
    def __init__(self, num, pos_x, pos_y):
        super().__init__(player_group, all_sprites)

        self.num = num
        self.level = 1
        self.angle = 0
        self.moving = False

        self.update_image()
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

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

        res = pygame.sprite.spritecollide(self, damageable_group, False)
        for obj in res:
            obj.damage(TANK_DAMAGE[self.level])

        condition = (pygame.sprite.spritecollideany(self, solid_group, False) or
                     pygame.sprite.spritecollideany(self, damageable_group, False))
        if self.num == 1 and PLAYRSCOUNT == 2:
            condition = condition or pygame.sprite.collide_rect(self, player_two)
        elif self.num == 2:
            condition = condition or pygame.sprite.collide_rect(self, player_one)
        if condition:
            self.rect = self.rect.move(-delta_x, -delta_y)
            self.moving = False
        self.update_image()

    def update_image(self):
        if self.num == 1:
            images = player_one_images
        else:
            images = player_two_images
        self.image = images[self.angle]


start_screen()
pygame.quit()
