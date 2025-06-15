# Основные настройки
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 768
LEVEL_GOALS = {1: 1, 2: 1, 3: 1}  # Изменено количество светлячков
MOB_SPEEDS = {2: 1.5, 3: 1.5}
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
PLAY_BUTTON_IMG = 'assets/image/play_button.png'
QUIT_BUTTON_IMG = 'assets/image/quit_button.png'
MUSIC_ON_BUTTON_IMG = 'assets/image/music_on.png'
MUSIC_OFF_BUTTON_IMG = 'assets/image/music_off.png'

# Пути к изображениям мобов (разные для каждого типа)
MOB_IMAGES = {
    "type1": 'assets/image/mob1.png',  # Моб для 2 уровня
    "type2": 'assets/image/mob2.png',  # Первый моб для 3 уровня
    "type3": 'assets/image/mob3.png'   # Второй моб для 3 уровня
}

# Путь к музыкальному файлу
MUSIC_FILE = 'assets/sound/game_music.mp3'

# Звуковые эффекты
SOUND_EFFECTS = {
    'collect': 'assets/sound/collect.wav',  # Сбор светлячка
    'monster': 'assets/sound/monster.wav'   # Звук монстра
}

# Громкость
MUSIC_VOLUME = 0.5
SOUND_VOLUME = 0.7

# Интервал звука монстра (в миллисекундах)
MONSTER_SOUND_INTERVAL = 3000  # 3 секунды

# Радиус активации звука монстра
MONSTER_SOUND_RADIUS = 300  # Пикселей

# Позиции кнопок для КАЖДОГО МЕНЮ ОТДЕЛЬНО

# Стартовое меню
START_MENU_BUTTONS = {
    "play": (700, 350),   # Кнопка "Играть"
    "music": (500, 350),  # Кнопка музыки
    "quit": (600, 350)    # Кнопка "Выход"
}

# Меню смерти
DEATH_MENU_BUTTONS = {
    "play": (550, 400),   # Кнопка "Заново"
    "music": (350, 400),  # Кнопка музыки
    "quit": (450, 400)    # Кнопка "Выход"
}

# Меню победы
WIN_MENU_BUTTONS = {
    "play": (550, 380),   # Кнопка "Играть заново"
    "music": (350, 380),  # Кнопка музыки
    "quit": (450, 380)    # Кнопка "Выход"
}