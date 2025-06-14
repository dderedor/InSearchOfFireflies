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
RED = (139, 0, 0)  # Ваш красный цвет

# Пути к изображениям меню
MENU_BG = 'assets/image/menu_bg.png'
DEATH_BG = 'assets/image/death_bg.png'
WIN_BG = 'assets/image/win_bg.png'

# Пути к изображениям кнопок
PLAY_BUTTON_IMG = 'assets/image/play_button.png'
QUIT_BUTTON_IMG = 'assets/image/quit_button.png'
MUSIC_ON_BUTTON_IMG = 'assets/image/music_on.png'
MUSIC_OFF_BUTTON_IMG = 'assets/image/music_off.png'

# Путь к музыкальному файлу
MUSIC_FILE = 'assets/sound/game_music.mp3'  # Поддерживает .mp3 и .ogg

# Громкость музыки (от 0.0 до 1.0)
MUSIC_VOLUME = 0.5

# Позиции кнопок (ЗДЕСЬ МОЖНО МЕНЯТЬ РАСПОЛОЖЕНИЕ КНОПОК!)
# Для стартового меню
START_PLAY_BUTTON_POS = (700, 350)    # (x, y) - координаты кнопки "Играть"
START_MUSIC_BUTTON_POS = (500, 350)   # (x, y) - координаты кнопки музыки
START_QUIT_BUTTON_POS = (600, 350)    # (x, y) - координаты кнопки "Выход"

# Для меню смерти и победы
END_PLAY_BUTTON_POS = (550, 550)     # (x, y) - координаты кнопки "Играть заново"
END_MUSIC_BUTTON_POS = (350, 550)    # (x, y) - координаты кнопки музыки
END_QUIT_BUTTON_POS = (450, 550)    # (x, y) - координаты кнопки "Выход"