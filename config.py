# Основные настройки
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 768
LEVEL_GOALS = {1: 3, 2: 3, 3: 3}  # Количество светлячков по уровням
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
PARTICLE_COLOR = (255, 255, 200)  # Цвет частиц светлячков

# Пути к изображениям
LEVEL_BG = 'assets/image/level_bg.jpg'  # ФОНОВОЕ ИЗОБРАЖЕНИЕ ВМЕСТО ТРАВЫ (960x768)
MENU_BG = 'assets/image/menu_bg.png'
DEATH_BG = 'assets/image/death_bg.png'
WIN_BG = 'assets/image/win_bg.png'
PLAY_BUTTON_IMG = 'assets/image/play_button.png'
QUIT_BUTTON_IMG = 'assets/image/quit_button.png'
MUSIC_ON_BUTTON_IMG = 'assets/image/music_on.png'
MUSIC_OFF_BUTTON_IMG = 'assets/image/music_off.png'
FLY_PARTICLE = 'assets/image/fly_particle.png'  # ИЗОБРАЖЕНИЕ ЧАСТИЦЫ (16x16)

# Пути к изображениям мобов (разные для каждого типа)
MOB_IMAGES = {
    "type1": 'assets/image/mob1.png',  # Моб для 2 уровня (рекомендуемый размер 64x64)
    "type2": 'assets/image/mob2.png',  # Первый моб для 3 уровня
    "type3": 'assets/image/mob3.png'   # Второй моб для 3 уровня
}

# Путь к музыкальному файлу
MUSIC_FILE = 'assets/sound/game_music.mp3'

# Звуковые эффекты
SOUND_EFFECTS = {
    'collect': 'assets/sound/collect.wav',  # Сбор светлячка
    'monster': 'assets/sound/monster.wav',  # Звук монстра
    'death': 'assets/sound/death.wav',      # Звук смерти
    'win': 'assets/sound/win.wav',          # Звук победы
    'step': 'assets/sound/step.wav'         # Звук шагов ёжика
}

# Громкость
MUSIC_VOLUME = 0.5
SOUND_VOLUME = 0.7

# Настройки частиц
PARTICLE_COUNT = 30    # Количество фоновых частиц
PARTICLE_SPEED = 0.7  # Скорость движения частиц
PARTICLE_SPAWN_CHANCE = 0.04  # Шанс появления новой частицы каждый кадр

# Интервалы
MONSTER_SOUND_INTERVAL = 3000  # Интервал звука монстра (3 секунды)
STEP_SOUND_INTERVAL = 300      # Интервал звука шагов (0.3 секунды)

# Радиус активации звука монстра
MONSTER_SOUND_RADIUS = 300  # Пикселей

# расстояние для спавна мобов от ёжика
SAFE_SPAWN_DISTANCE = 300  # Пикселей

# КНОПКИ
# Старт
START_MENU_BUTTONS = {
    "play": (700, 350),
    "music": (500, 350),
    "quit": (600, 350)
}

# смерт
DEATH_MENU_BUTTONS = {
    "play": (520, 530),
    "music": (320, 530),
    "quit": (420, 530)
}

# победа
WIN_MENU_BUTTONS = {
    "play": (400, 480),
    "music": (200, 480),
    "quit": (300, 480)
}