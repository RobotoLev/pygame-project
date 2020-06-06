import sys
import os
import pygame


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'Textures', name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print("Невозможно загрузить изображение из файла:", name)
        raise SystemExit(message)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image = image.convert()
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


def rotate_image(image, angle):
    angle = (360 - angle) % 360
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = image.get_rect().copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def get_rotated_images(filename, angle):
    image = load_image(filename)
    res = []
    for i in range(4):
        res.append(rotate_image(image, angle))
        angle = (angle + 90) % 360
    return res


def load_level(filename):
    filename = "data/levels/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    enemies = int(level_map[-1])
    biom = level_map[-2]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map[:-2])), enemies, biom
