# config.py
# Основные настройки
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 768
LEVEL_GOALS = {1: 3, 2: 5, 3: 7}
MOB_SPEEDS = {2: 1.5, 3: 2.5}
HEDGEHOG_START_POS = (430, 600)

# Настройки тумана
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

# Пути к изображениям кнопок
PLAY_BUTTON_IMG = 'assets/image/play_button.png'       # Кнопка "Играть"
QUIT_BUTTON_IMG = 'assets/image/quit_button.png'       # Кнопка "Выход"
MUSIC_ON_BUTTON_IMG = 'assets/image/music_on.png'      # Кнопка "Музыка вкл"
MUSIC_OFF_BUTTON_IMG = 'assets/image/music_off.png'    # Кнопка "Музыка выкл"

# Путь к музыкальному файлу (должен быть в формате .ogg или .wav)
MUSIC_FILE = 'assets/sound/game_music.ogg'

# Громкость музыки (от 0.0 до 1.0)
MUSIC_VOLUME = 0.5

# Позиции кнопок
# Для стартового меню
START_PLAY_BUTTON_POS = (380, 400)
START_MUSIC_BUTTON_POS = (380, 500)
START_QUIT_BUTTON_POS = (380, 600)

# Для меню смерти и победы (одинаковые позиции)
END_PLAY_BUTTON_POS = (380, 400)
END_MUSIC_BUTTON_POS = (380, 500)
END_QUIT_BUTTON_POS = (380, 600)