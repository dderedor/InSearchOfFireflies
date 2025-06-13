# config.py
# Основные настройки
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 768
LEVEL_GOALS = {1: 3, 2: 5, 3: 7}
MOB_SPEEDS = {2: 1.5, 3: 2.5}
HEDGEHOG_START_POS = (430, 600)

# Настройки тумана (возвращаем оригинальные)
FOG_RADIUS = 160
FOG_NOISE = 20
FOG_COLOR = (192, 192, 192)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (139, 0, 0)

# Пути к изображениям меню
MENU_BG = 'assets/image/menu_bg.png'
DEATH_BG = 'assets/image/death_bg.png'
WIN_BG = 'assets/image/win_bg.png'
BUTTON_IMG = 'assets/image/button.png'

# Позиции кнопок
START_BUTTON_POS = (380, 500)
RESTART_BUTTON_POS = (380, 500)
QUIT_BUTTON_POS = (380, 580)