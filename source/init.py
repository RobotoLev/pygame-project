from source.system_functions import *

FPS = 30
WIDTH = 1072
HEIGHT = 603
tile_width, tile_height = 50, 50
MENUBTTNS = [None for _ in range(4)]
MODEBTTNS = [None for _ in range(4)]
STNGBTTNS = [None for _ in range(4)]
PLAYRSCOUNT = 0
LEVELS = 7
SCORE = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
tank_shot = pygame.mixer.Sound('data/Sounds/tank_shot.wav')
sounds = list()
clock = pygame.time.Clock()

running = True
iteration = 0


player_one = None
player_two = None
green_spawnpoint = None
red_spawnpoint = None
VELOCITY = 3
VOLUME = 50
WASDBTTNS = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_LSHIFT]
ARRWBTTNS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE]
PLAYRSKEYS = [WASDBTTNS, ARRWBTTNS]
ANGLES = {0: 0, 1: 2, 2: 3, 3: 1}

PLAYER_LEVELS_LIMIT = [None, 0, 1200, 2400]
PLAYER_DAMAGE = [None, 400, 400, 500]
PLAYER_SHOT_DAMAGE = [None, 100, 100, 200]
ENEMY_DAMAGE = [None, 100, 200, 300]
ENEMY_SHOT_DAMAGE = [None, 100, 200, 300]
PLAYER_HP = [None, 100, 200, 400]
ENEMY_HP = [None, 100, 100, 300]
SHOT_VELOCITY = 5
MAXDIST = 300
ENEMIES_LEFT = 0

# Все полноценные части уровня
tile_images = {'empty': load_image('grass.png'),
               'snowy': load_image('snow.png'),

               'hor_rail': load_image('horizontal_rails.png'),
               'hor_rail_le': load_image('horizontal_rails_lef_end.png'),
               'hor_rail_re': load_image('horizontal_rails_rig_end.png'),
               'ver_rail': load_image('vertical_rails.png'),
               'ver_rail_te': load_image('vertical_rails_top_end.png'),
               'ver_rail_be': load_image('vertical_rails_bot_end.png'),

               'snowy_hor_rail': load_image('snowy_horizontal_rails.png'),
               'snowy_hor_rail_le': load_image('snowy_horizontal_rails_lef_end.png'),
               'snowy_hor_rail_re': load_image('snowy_horizontal_rails_rig_end.png'),
               'snowy_ver_rail': load_image('snowy_vertical_rails.png'),
               'snowy_ver_rail_te': load_image('snowy_vertical_rails_top_end.png'),
               'snowy_ver_rail_be': load_image('snowy_vertical_rails_bot_end.png')
               }
# Заборчики
board_images = {'horiz': [load_image('board_horizontal.png'),
                          load_image('board_horizontal_damaged.png')],
                'verti': [load_image('board_vertical.png'),
                          load_image('board_vertical_damaged.png')]}
# Поезда, поезда
train_images = {'horiz': [load_image('horizontal_train.png'),
                          load_image('horizontal_train_damaged.png')],
                'verti': [load_image('vertical_train.png'),
                          load_image('vertical_train_damaged.png')]}
# Дерево, которое "красиво" горит
tree_images = {'default': [load_image('trees\\tree_default_0.png'),
                           load_image('trees\\tree_default_1.png'),
                           load_image('trees\\tree_default_2.png'),
                           load_image('trees\\tree_default_3.png')]}
# Танчики
player_one_images = [None] +\
                    [get_rotated_images('tanks\\source_tanks\\tank_green_mk{}.png'.format(i), 180)
                     for i in range(1, 4)]
player_two_images = [None] +\
                    [get_rotated_images('tanks\\source_tanks\\tank_red_mk{}.png'.format(i), 180)
                     for i in range(1, 4)]
enemy_images = [None] + \
               [get_rotated_images('tanks\\source_tanks\\tank_enemy_mk{}.png'.format(i), 0)
                for i in range(1, 4)]
# Коробки, которые камни, которые выполняют функцию стен
building_images = {'wall': load_image('box.png'),
                   'snowy_wall': load_image('snowy_box.png')}
# Части анимации начала выстрела
shot_start_images = [
    [rotate_image(load_image('shot_start_{}.png'.format(i + 1)), 270) for i in range(4)],
    [load_image('shot_start_{}.png'.format(i + 1)) for i in range(4)],
    [rotate_image(load_image('shot_start_{}.png'.format(i + 1)), 90) for i in range(4)],
    [rotate_image(load_image('shot_start_{}.png'.format(i + 1)), 180) for i in range(4)]]
# Части анимации конца выстрела
shot_end_images = [
    [rotate_image(load_image('shot_end_{}.png'.format(i + 1)), 270) for i in range(4)],
    [load_image('shot_end_{}.png'.format(i + 1)) for i in range(4)],
    [rotate_image(load_image('shot_end_{}.png'.format(i + 1)), 90) for i in range(4)],
    [rotate_image(load_image('shot_end_{}.png'.format(i + 1)), 180) for i in range(4)]]
# ...
null_image = load_image("null.png")

all_sprites = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

object_group = pygame.sprite.Group()
player_damageable_group = pygame.sprite.Group()
enemy_damageable_group = pygame.sprite.Group()
solid_group = pygame.sprite.Group()
temporary_group = pygame.sprite.Group()
