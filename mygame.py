#venv\Scripts\activate.bat
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((960, 768))
pygame.display.set_caption('Ёжик и светлячки')
icon = pygame.image.load('image/icon.webp')
pygame.display.set_icon(icon)

# Загрузка изображений
hedgehog_down_img = pygame.image.load('image/hedgehog_down.png')
hedgehog_up_img = pygame.image.load('image/hedgehog_up.png')
hedgehog_left_img = pygame.image.load('image/hedgehog_left.png')
hedgehog_right_img = pygame.image.load('image/hedgehog_right.png')
grass_img = pygame.image.load('image/trava.png')
firefly_img = pygame.image.load('image/fly.png')

# Размеры экрана
screen_width = screen.get_width()
screen_height = screen.get_height()

# Размеры тайла
tile_size = grass_img.get_width()

# Ёжик
hedgehog_x = 430 #  начальные координаты и скорость
hedgehog_y = 600  #
hedgehog_speed = 5
current_hedgehog_img = hedgehog_down_img



font = pygame.font.Font('fonts.ttf', 16) # Выбираем шрифт и размер (Arial, размер 36)




# --- НОВЫЕ СТРОКИ: СВЕТЛЯЧКИ ---
fireflies = [] # Список для хранения светлячков
# --- УБРАЛИ: РАДИУС СБОРА СВЕТЛЯЧКОВ ---
# --- НОВАЯ ПЕРЕМЕННАЯ: СЧЕТЧИК СВЕТЛЯЧКОВ ---
collected_fireflies = 0 # Сколько светлячков собрано
# --- НОВАЯ ПЕРЕМЕННАЯ: ТЕКУЩИЙ УРОВЕНЬ ---
current_level = 1 # Текущий уровень
# --- НОВЫЙ СЛОВАРЬ: ЦЕЛИ ПО УРОВНЯМ ---
level_goals = {
    1: 3,
    2: 5,
    3: 7
}

# --- НОВАЯ ФУНКЦИЯ: СОЗДАНИЕ СВЕТЛЯЧКА ---
def create_firefly():
    x = random.randint(0, screen_width - firefly_img.get_width())
    y = random.randint(0, screen_height - firefly_img.get_height())
    fireflies.append([x, y])

# --- НОВАЯ ФУНКЦИЯ: НАЧАЛО НОВОГО УРОВНЯ ---
def start_new_level():
    global fireflies, collected_fireflies
    fireflies = [] # Очищаем список светлячков
    collected_fireflies = 0 # Сбрасываем счетчик светлячков
    # --- СОЗДАЕМ ПЕРВЫЙ СВЕТЛЯЧОК ---
    create_firefly()

# --- НОВАЯ СТРОКА: СОЗДАЕМ ПЕРВЫЙ СВЕТЛЯЧОК ---
start_new_level()

# --- ИЗМЕНЕНО: ИНИЦИАЛИЗАЦИЯ ШРИФТА ---
font = pygame.font.Font('fonts.ttf', 16) # Выбираем шрифт и размер (Arial, размер 36)

run = True
while run:
    # Отрисовка травы
    for y in range(0, screen_height, tile_size):
        for x in range(0, screen_width, tile_size):
            screen.blit(grass_img, (x, y))

    # Отрисовка ёжика
    screen.blit(current_hedgehog_img, (hedgehog_x, hedgehog_y))

    # Отрисовка светлячков
    for firefly in fireflies:
        screen.blit(firefly_img, (firefly[0], firefly[1]))

    # --- ИЗМЕНЕНО: ОТОБРАЖЕНИЕ СЧЕТЧИКА СВЕТЛЯЧКОВ ---
    # --- ИЗМЕНЕНО: БЕЛЫЙ ЦВЕТ ТЕКСТА ---
    text = font.render(f"Found: {collected_fireflies} / {level_goals[current_level]}", True, (255, 255, 255)) # Создаем текст
    screen.blit(text, (10, 10)) # Отображаем текст на экране

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # --- ИЗМЕНЕННЫЙ БЛОК: СБОР СВЕТЛЯЧКОВ ---
        if event.type == pygame.KEYDOWN:
            # --- ИЗМЕНЕНО: КЛАВИША СБОРА - "E" ---
            if event.key == pygame.K_e: # Клавиша "E" для сбора светлячков
                # --- НОВЫЙ ЦИКЛ: ПЕРЕБИРАЕМ ВСЕ СВЕТЛЯЧКИ ---
                for i, firefly in enumerate(fireflies):
                    # --- ИЗМЕНЕНО: ПРОВЕРЯЕМ, НАХОДИТСЯ ЛИ ЁЖИК НА ТОМ ЖЕ ТАЙЛЕ, ЧТО И СВЕТЛЯЧОК ---
                    if hedgehog_x // tile_size == firefly[0] // tile_size and hedgehog_y // tile_size == firefly[1] // tile_size:
                        # --- УВЕЛИЧИВАЕМ СЧЕТЧИК СВЕТЛЯЧКОВ ---
                        collected_fireflies += 1
                        # --- УДАЛЯЕМ СОБРАННЫЙ СВЕТЛЯЧОК ---
                        del fireflies[i]
                        # --- СОЗДАЕМ НОВЫЙ СВЕТЛЯЧОК ---
                        create_firefly()
                        # --- ВЫХОДИМ ИЗ ЦИКЛА (СОБРАЛИ ТОЛЬКО ОДНОГО СВЕТЛЯЧКА) ---
                        break

    # --- НОВЫЙ БЛОК: ДВИЖЕНИЕ ЁЖИКА ПРИ ЗАЖАТОЙ КЛАВИШЕ ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hedgehog_x -= hedgehog_speed
        current_hedgehog_img = hedgehog_left_img
    if keys[pygame.K_RIGHT]:
        hedgehog_x += hedgehog_speed
        current_hedgehog_img = hedgehog_right_img
    if keys[pygame.K_UP]:
        if hedgehog_y > 0:
            hedgehog_y -= hedgehog_speed
        current_hedgehog_img = hedgehog_up_img
    if keys[pygame.K_DOWN]:
        if hedgehog_y < screen_height - current_hedgehog_img.get_height():
            hedgehog_y += hedgehog_speed
        current_hedgehog_img = hedgehog_down_img

    # Ограничение движения ёжика
    hedgehog_x = max(0, min(hedgehog_x, screen_width - current_hedgehog_img.get_width()))
    hedgehog_y = max(0, min(hedgehog_y, screen_height - current_hedgehog_img.get_height()))

    # --- НОВЫЙ БЛОК: ПРОВЕРКА НА СМЕНУ УРОВНЯ ---
    if collected_fireflies >= level_goals[current_level]:
        # --- ПЕРЕХОДИМ НА СЛЕДУЮЩИЙ УРОВЕНЬ ---
        current_level += 1
        # --- ПРОВЕРЯЕМ, НЕ ЗАКОНЧИЛАСЬ ЛИ ИГРА ---
        if current_level > len(level_goals):
            print("Игра пройдена! Ты нашел маму!") # TODO: Заменить на отрисовку мамы
        #    run = False # Заканчиваем игру
        else:
            # --- НАЧИНАЕМ НОВЫЙ УРОВЕНЬ ---
            start_new_level()

    pygame.display.update()

pygame.quit()