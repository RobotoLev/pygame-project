# Основной файл проекта


import random
from source.init import *


# Создание экрана паузы
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
    for i in range(4):  # Создание кнопок
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


# Создание экрана настроек
def settings(chosed=None, moved=None):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    texts = ['Игрок 1', 'Игрок 2', 'Громкость', 'НАЗАД']
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


# Создание экрана выбора режима игры
def choose_mode(chosed=None, moved=None):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    texts = ['1 игрок', '2 игрока', 'СТАРТ', 'НАЗАД']
    for i in range(4):  # Создание кнопок
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


# Создание экрана главного меню
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


# Функция, указывающая, на какой из кнопок сейчас мышь
def what_is_pressed(buttons, pos):
    x, y = pos
    for it, i in enumerate(buttons):
        if i[0][2] + i[0][0] >= x >= i[0][0] and i[0][1] <= y <= i[0][1] + i[0][3]:
            return it


# Обработчик главного меню
def start_screen():
    main_menu()
    in_menu = True
    flag = None
    btn = None
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
                    it = what_is_pressed(MENUBTTNS, event.pos)
                    if it == btn:
                        in_menu = False
                        break
                    else:
                        flag = None
                    main_menu()
            elif event.type == pygame.MOUSEMOTION:
                btn2 = what_is_pressed(MENUBTTNS, event.pos)
                if 1 in event.buttons:
                    main_menu(btn, btn2)
                else:
                    main_menu(moved=btn2)

        if not in_menu:
            break

        pygame.display.flip()
        clock.tick(FPS)
    flag()


# Обработчик экрана паузы
def pause_screen():
    pause()
    in_menu = True
    flag = None
    btn = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                btn = what_is_pressed(MENUBTTNS, (x, y))
                flag = btn
                pause(btn)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if flag is not None:
                    it = what_is_pressed(MENUBTTNS, event.pos)
                    if it == btn:
                        if it == 0:
                            return
                        elif it == 1:
                            settings_screen(True)
                        elif it == 2:
                            return start_screen
                        elif it == 3:
                            terminate()
                        break
                    else:
                        flag = None
                    pause()
            elif event.type == pygame.MOUSEMOTION:
                btn2 = what_is_pressed(MENUBTTNS, event.pos)
                if 1 in event.buttons:
                    pause(btn, btn2)
                else:
                    pause(moved=btn2)
        if not in_menu:
            break

        pygame.display.flip()
        clock.tick(FPS)


# Обработчик экрана настроек
def settings_screen(on_pause=False):
    flag = None
    global VOLUME
    settings()
    in_menu = True
    btn = None
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
                    it = what_is_pressed(STNGBTTNS, event.pos)
                    if it == btn:
                        if it == 3:
                            if on_pause:
                                return
                            in_menu = False
                            break
                        elif it == 0:
                            if PLAYRSKEYS[0] == WASDBTTNS:
                                PLAYRSKEYS[0] = ARRWBTTNS
                            else:
                                PLAYRSKEYS[0] = WASDBTTNS
                        elif it == 1:
                            if PLAYRSKEYS[1] == WASDBTTNS:
                                PLAYRSKEYS[1] = ARRWBTTNS
                            else:
                                PLAYRSKEYS[1] = WASDBTTNS
                    else:
                        flag = None
                    settings()
            elif event.type == pygame.MOUSEMOTION:
                btn2 = what_is_pressed(STNGBTTNS, event.pos)
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
                    settings(btn, btn2)
                else:
                    settings(moved=btn2)
        if not in_menu:
            break

        pygame.display.flip()
        clock.tick(FPS)
    flag()


# Загрузка игры с файла (при нажатии "Продолжить" в главном меню)
def continue_screen():
    global PLAYRSCOUNT, SCORE
    try:
        with open('data/cont.txt', 'r') as f:
            level, players, score = map(int, f.read().split())
        if 0 > level > LEVELS or players not in (1, 2):
            raise ValueError
        PLAYRSCOUNT = players
        SCORE = score
        game(level, True)
    except ValueError:  # Если битый файл загрузки или какие-то ещё беды
        start_screen()


# Создание и обработка экрана перехода между уровнями
def new_level_screen(level):
    time = 60
    flags = []
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                flags.append(event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button in flags:
                    return
            elif event.type == pygame.KEYDOWN:
                flags.append(event.key)
            elif event.type == pygame.KEYUP:
                if event.key in flags:
                    return
        screen.fill((0, 0, 0))
        texts = [f'Уровень {level}', f'Счёт {SCORE}', 'нажмите любую кнопку, чтобы начать']
        cr = (100, 255, 100)
        if time < 0:
            for i in range(3):
                font = pygame.font.Font(None, 50)
                if i in (2, 1):
                    font = pygame.font.Font(None, 30)
                text = font.render(texts[i], 1, cr)
                text_h = text.get_height()
                text_w = text.get_width()
                text_x = WIDTH // 2 - text_w // 2
                text_y = (HEIGHT // 5) * 2 - text_h // 2
                if i == 1:
                    text_y = (HEIGHT // 5) * 3 - text_h // 2
                if i == 2:
                    text_y = (HEIGHT // 5) * 4 - text_h // 2
                screen.blit(text, (text_x, text_y))
        if time < 0:
            pygame.display.flip()
        time -= 1
        clock.tick(FPS)


# Создание и обработка финального экрана(после прохождения всех уровней)
def look_at_score():
    flags = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                flags.append(event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button in flags:
                    return
            elif event.type == pygame.KEYDOWN:
                flags.append(event.key)
            elif event.type == pygame.KEYUP:
                if event.key in flags:
                    return
        screen.fill((0, 0, 0))
        texts = [f'Ваш счёт {SCORE}', 'нажмите любую кнопку, чтобы выйти в меню']
        cr = (100, 255, 100)
        for i in range(2):
            font = pygame.font.Font(None, 50)
            if i == 1:
                font = pygame.font.Font(None, 30)
            text = font.render(texts[i], 1, cr)
            text_h = text.get_height()
            text_w = text.get_width()
            text_x = WIDTH // 2 - text_w // 2
            text_y = (HEIGHT // 5) * 2 - text_h // 2
            if i == 1:
                text_y = (HEIGHT // 5) * 4 - text_h // 2
            screen.blit(text, (text_x, text_y))
        pygame.display.flip()
        clock.tick(FPS)


# Обработка экрана выбора режима игры
def choose_mode_screen():
    choose_mode()
    flag = None
    btn = None
    global PLAYRSCOUNT
    choosing = True
    while True:  # Оно работает, это главное
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
                    it = what_is_pressed(MODEBTTNS, event.pos)
                    if it == btn:
                        if it == 0:
                            PLAYRSCOUNT = 1
                        elif it == 1:
                            PLAYRSCOUNT = 2
                        elif it == 2:
                            if PLAYRSCOUNT != 0:
                                choosing = False
                                break
                        elif it == 3:
                            choosing = False
                            PLAYRSCOUNT = 0
                            break
                    else:
                        flag = None
                    choose_mode()
            elif event.type == pygame.MOUSEMOTION:
                btn2 = what_is_pressed(MODEBTTNS, event.pos)
                if 1 in event.buttons:
                    choose_mode(btn, btn2)
                else:
                    choose_mode(moved=btn2)
        if not choosing:
            break
        pygame.display.flip()
        clock.tick(FPS)
    flag()


# Функция создания уровня на экране
def generate_level(level, biom):
    global player_one, player_two, green_spawnpoint, red_spawnpoint
    green_spawnpoint, red_spawnpoint = None, None  # Точки появления для игроков
    enemies_spawnpoints = []  # список с точками появления проивников
    empty_name = 'empty'
    biome_modif = ''
    if biom == 'snowy':  # Поддержка биомов, указываемых в файле с уровнем
        biome_modif = 'snowy_'
        empty_name = 'snowy'
    for y in range(1, len(level), 2):  # Создание всех объектов, что не заборчики
        for x in range(1, len(level[y]), 2):
            if level[y][x] == '.':
                Tile(empty_name, (x - 1) // 2, (y - 1) // 2)
                if random.randint(1, 10) == 1:
                    Tree('default', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '#':
                Building(biome_modif + 'wall', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'G':
                Tile(empty_name, (x - 1) // 2, (y - 1) // 2)
                green_spawnpoint = ((x - 1) // 2, (y - 1) // 2)
                player_one = Player(1, green_spawnpoint)
            elif level[y][x] == 'R':
                Tile(empty_name, (x - 1) // 2, (y - 1) // 2)
                red_spawnpoint = ((x - 1) // 2, (y - 1) // 2)
                if PLAYRSCOUNT == 2:
                    red_spawnpoint = ((x - 1) // 2, (y - 1) // 2)
                    player_two = Player(2, red_spawnpoint)
            elif level[y][x] == 'E':
                Tile(empty_name, (x - 1) // 2, (y - 1) // 2)
                enemies_spawnpoints.append(((x - 1) // 2, (y - 1) // 2))
            elif level[y][x] == 'V':
                Tile(biome_modif + 'ver_rail', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'H':
                Tile(biome_modif + 'hor_rail', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '2':
                Tile(biome_modif + 'ver_rail_be', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '8':
                Tile(biome_modif + 'ver_rail_te', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '4':
                Tile(biome_modif + 'hor_rail_le', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == '6':
                Tile(biome_modif + 'hor_rail_re', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'W':
                Tile(biome_modif + 'ver_rail', (x - 1) // 2, (y - 1) // 2)
                Train('verti', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'A':
                Tile(biome_modif + 'hor_rail', (x - 1) // 2, (y - 1) // 2)
                Train('horiz', (x - 1) // 2, (y - 1) // 2)
            elif level[y][x] == 'T':
                Tile(empty_name, (x - 1) // 2, (y - 1) // 2)
                Tree('default', (x - 1) // 2, (y - 1) // 2)
    for y in range(1, len(level), 2):  # Обработка вертикальных заборчиков
        for x in range(0, len(level[y]), 2):
            if level[y][x] == 'V':
                Boarding('verti', x // 2, (y - 1) // 2)
    for y in range(0, len(level), 2):  # Обработка горизонтальных заборчиков(жаль, что они только 1 типа)
        for x in range(1, len(level[y]), 2):
            if level[y][x] == 'H':
                Boarding('horiz', (x - 1) // 2, y // 2)
    return green_spawnpoint, red_spawnpoint, enemies_spawnpoints  # возвращаем точки появления всех танков


# Функция обработки игрового процесса с заданным уровнем
def level_play(level_name='level1.txt'):
    global ENEMIES_LEFT, LOCAL_SCORE
    print('Game has been started')
    in_game = True
    LOCAL_SCORE = 0
    all_sprites.empty()
    tile_group.empty()
    player_group.empty()
    object_group.empty()
    solid_group.empty()
    player_damageable_group.empty()
    enemy_damageable_group.empty()
    temporary_group.empty()

    level, ENEMIES_LEFT, biom = load_level(level_name)
    enemies_to_spawn = ENEMIES_LEFT
    green, red, enemies = generate_level(level, biom)
    enemies = list(map(lambda x: [*x, random.randint(0, 30)], enemies))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    res = pause_screen()
                    print(res)
                    if res == start_screen:
                        with open('data/cont.txt', 'w') as f:
                            f.write(f'{int(level_name.split(".")[0].split("evel")[1]) - 1} '
                                    f'{PLAYRSCOUNT} {SCORE}')
                    if res is not None:
                        in_game = False
                        break
                # print("Pressed", key)
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
                en_type = random.randint(1, 3)
                if PLAYRSCOUNT == 1:
                    player = player_one
                else:
                    player = random.choice([player_one, player_two])
                Enemy(i[0], i[1], player, level=en_type)
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
            return LOCAL_SCORE

        all_sprites.update()
        clock.tick(FPS)
        # Тут у нас счёт вырисовывается. Криво, но рисуется
        font = pygame.font.Font(None, 50)
        cr = (0, 200, 0)
        text = font.render(str(LOCAL_SCORE + SCORE), 1, cr)
        text_h = text.get_height()
        text_w = text.get_width()
        text_x = WIDTH // 2 - text_w // 2
        text_y = (HEIGHT // 20) * 1 - text_h // 2
        pygame.draw.rect(screen, (255, 255, 255), (text_x - 5, text_y - 5,
                                                   text_w + 10, text_h + 10))
        screen.blit(text, (text_x, text_y))

        pygame.display.flip()

    res()  # Оно нужно. Просто знайте это


# Функция запуска игры
def game(start_level=0, load=None):
    global SCORE
    level = start_level
    if load is None:
        SCORE = 0

    while True:
        level += 1
        print(LEVELS, level)
        if LEVELS == level:
            break
        new_level_screen(level)
        result = level_play(f'level{level}.txt')
        SCORE += result
        print(level)

    look_at_score()  # Просмотр счёта после игры
    start_screen()  # Поиграли и в меню


# Класс одной клетки игрового поля
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tile_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


# Базовый класс объекта игрового поля
class Object(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(list(groups) + [object_group])
        self.strength = 1000
        self.image = None
        self.fireable = False
        self.is_fired = False
        self.fire_damage = 0
        self.images = []

        self.is_update_images = True

    # Функция нанесения урона
    def damage(self, damage_level, shot=False):
        self.strength -= damage_level
        if shot and self.fireable:
            self.is_fired = True
            self.fire_damage = 1

    # Функция обновления
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


# Класс объекта с бесконечным запасом прочности (Building, т.к. изначально это были постройки)
class Building(Object):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(solid_group, all_sprites)
        self.strength = float("inf")
        self.image = building_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


# Класс ограждения
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


# Класс вагона
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


# Класс дерева
# Если выстрелить в дерево - оно загорится и будет гореть, пока не сгорит полностью
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


# Класс игрока
class Player(Object):
    def __init__(self, num, spawnpoint, level=1):
        global ENEMIES_LEFT
        super().__init__(player_group, enemy_damageable_group, all_sprites)

        self.num = num
        self.level = level
        self.spawnpoint = spawnpoint
        self.xp = 0
        self.angle = 0
        self.shoot_delay = 0
        self.game_delay = -1
        self.strength = PLAYER_HP[self.level]
        self.moving = False
        self.is_update_images = False

        self.update_image()
        self.rect = self.image.get_rect().move(tile_width * spawnpoint[0],
                                               tile_height * spawnpoint[1])

        if len(pygame.sprite.spritecollide(self, player_group, False)) > 1:
            if self.num == 1:
                player_two.kill()
            else:
                player_one.kill()
        ENEMIES_LEFT -= len(pygame.sprite.spritecollide(self, enemy_group, True))

    def update(self):
        super().update()

        if self.game_delay > 0:
            self.game_delay -= 1
            return
        if self.game_delay == 0:
            self.killall()

        self.update_level()
        self.update_image()

        self.shoot_delay -= 1
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
        if self.xp >= PLAYER_LEVELS_LIMIT[self.level + 1]:
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
        if self.shoot_delay <= 0:
            tank_shot.play()
            Shot(self)
            self.shoot_delay = 30

    def kill(self):
        if self.game_delay == -1:
            self.game_delay = 120
        self.image = null_image
        player_group.remove(self)
        enemy_damageable_group.remove(self)

    def killall(self):
        global player_one, player_two
        if self.num == 1:
            player_one = Player(1, self.spawnpoint)
            player = player_one
        else:
            player_two = Player(2, self.spawnpoint)
            player = player_two
        player_group.add(player)
        enemy_damageable_group.add(player)
        super().kill()


# Класс врага
class Enemy(Object):
    def __init__(self, pos_x, pos_y, player, level=1):
        super().__init__(enemy_group, player_damageable_group, all_sprites)

        self.level = level
        self.angle = 0
        self.moving = False
        self.is_update_images = False
        self.strength = ENEMY_HP[level]

        self.player = player

        self.update_image()
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.delay = 10
        self.shoot_delay = 0

        pygame.sprite.spritecollide(self, player_group, True)

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

        condition = None
        if len(pygame.sprite.spritecollide(self, enemy_group, False)) > 1:
            condition = False

        self.rect = self.rect.move(delta_x, delta_y)

        res = pygame.sprite.spritecollide(self, enemy_damageable_group, False)
        for obj in res:
            if type(obj) != Player:
                obj.damage(ENEMY_DAMAGE[self.level])

        if condition is None:
            condition = len(pygame.sprite.spritecollide(self, enemy_group, False)) > 1
        condition = (condition or pygame.sprite.spritecollideany(self, solid_group, False) or
                     pygame.sprite.spritecollideany(self, enemy_damageable_group, False))

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


# Анимированный спрайт
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


# Анимация начала выстрела (возле пушки танка)
class ShotStart(AnimatedSprite):
    def __init__(self, pos_x, pos_y, angle):
        super().__init__(all_sprites)
        self.images = shot_start_images[angle]
        self.rect = pygame.Rect(pos_x, pos_y, 48, 48)

        self.cadres = 1
        self.lifetime = 1


# Анимация конца выстрела (там, куда попал "снаряд")
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
        global SCORE, LOCAL_SCORE
        res_type = type(self.res)
        if self.is_player:
            damage = PLAYER_SHOT_DAMAGE[self.level]
            if res_type in PLAYER_SHOT_XP and self.res.strength <= damage:
                self.obj.xp += PLAYER_SHOT_XP[res_type]
            if res_type == Enemy and self.res.strength <= damage:
                print('536')
                LOCAL_SCORE += PLAYER_SCORE_ENEMIES[self.res.level]
        else:
            damage = ENEMY_SHOT_DAMAGE[self.level]
            if res_type == Player and self.res.strength <= damage:
                print(self.res.game_delay)
                if self.res.game_delay == -1:
                    LOCAL_SCORE -= 1000
        if not self.is_player or type(self.res) != Player:
            self.res.damage(damage, True)
        super().kill()


# Класс выстрела
#
# Выстрел - невидимый спрайт, который движется с какой-то скоростью
# Когда выстрел с кем-то (или с чем-то) сталкивается, у этого объекта уменьшается прочность
# В начале и в конце выстрела проигрываются анимации выстрела/попадания соответственно
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


# Сколько прочности снимает выстрел игрока по объекту
PLAYER_SHOT_XP = {Boarding: 100, Tree: 100, Train: 200, Enemy: 300}
# Сколько очков дается игроку за врага определенного уровня
PLAYER_SCORE_ENEMIES = {1: 500, 2: 1200, 3: 2500}

# Запуск игры
start_screen()

# Завершение работы
pygame.quit()
