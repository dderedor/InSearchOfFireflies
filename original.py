#venv\Scripts\activate.bat
import pygame
import math
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
leaf_img = pygame.image.load('image/leaf.png')





# Настройки мобов
MOB_SPEEDS = {2: 1.5, 3: 2.5}  # Скорости для уровней 2 и 3
mobs = []  # Список мобов: [x, y, speed]
okak_img = pygame.image.load('image/okak.png')  # Спрайт моба


# Размеры экрана
screen_width = screen.get_width()
screen_height = screen.get_height()

# Размеры тайла
tile_size = grass_img.get_width()

# Ёжик
hedgehog_x = 430 #  начальные координаты и скорость
hedgehog_y = 600  
hedgehog_speed = 10
current_hedgehog_img = hedgehog_down_img

HEDGEHOG_WIDTH = hedgehog_down_img.get_width()  # Получаем ширину спрайта
HEDGEHOG_HEIGHT = hedgehog_down_img.get_height()  # Получаем высоту спрайта


font = pygame.font.Font('fonts.ttf', 30) # Выбираем шрифт и размер (Arial, размер 36)


korleaf = [
    (20,100),
    (150,300),
    (60,550),
    
    (770,400),
    (700,200),
    (650,600),

]

fireflies = [] # Список для хранения светлячков
collected_fireflies = 0 # Сколько светлячков собрано
current_level = 1 # Текущий уровень
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



def spawn_mobs(level):
    mobs.clear()
    if level in MOB_SPEEDS:  # Если для уровня есть мобы
        x = random.randint(0, screen_width - okak_img.get_width())
        y = random.randint(0, screen_height - okak_img.get_height())
        mobs.append([x, y, MOB_SPEEDS[level]])
























run = True
while run:
    
    # Отрисовка травы
    for y in range(0, screen_height, tile_size):
        for x in range(0, screen_width, tile_size):
            screen.blit(grass_img, (x, y))


    # Отрисовка светлячков с мерцанием
    for firefly in fireflies:
        firefly_copy = firefly_img.copy()  # Создаём копию изображения
        alpha = 128+ int(128 * math.sin(pygame.time.get_ticks() * 0.003))  # Пульсация
        firefly_copy.set_alpha(alpha)  # Применяем прозрачность
        screen.blit(firefly_copy, (firefly[0], firefly[1]))  # Рисуем копию

    # Отрисовка ёжика
    screen.blit(current_hedgehog_img, (hedgehog_x, hedgehog_y))
    #отрисовка кустов
    for i in korleaf:
        screen.blit(leaf_img, i)





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
            spawn_mobs(current_level)  # Создаем мобов для нового уровня




# Движение мобов туман
    for mob in mobs:
        # Расчет направления
        dx = hedgehog_x - mob[0]
        dy = hedgehog_y - mob[1]
        dist = max(1, math.sqrt(dx*dx + dy*dy))
    
        # Обновление позиции
        mob[0] += dx / dist * mob[2]
        mob[1] += dy / dist * mob[2]
    
    # Отрисовка
        screen.blit(okak_img, (mob[0], mob[1]))
    
    # Проверка столкновения
        if (abs(hedgehog_x - mob[0]) < HEDGEHOG_WIDTH and 
            abs(hedgehog_y - mob[1]) < HEDGEHOG_HEIGHT):
            run = False  # Завершаем игру
            print("Game Over! Моб догнал ёжика!")





    # ====== ДИНАМИЧЕСКИЙ ТУМАН ======
    fog_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    fog_color = (192, 192, 192)  # Серо-синий цвет
    fog_density = 1
    clear_radius = 200
    inner_soft = 60

    hedgehog_center_x = hedgehog_x + HEDGEHOG_WIDTH // 2
    hedgehog_center_y = hedgehog_y + HEDGEHOG_HEIGHT // 2
    
    for x in range(0, screen_width, 4):
        for y in range(0, screen_height, 4):
            dist = math.sqrt((x - hedgehog_center_x)**2 + (y - hedgehog_center_y)**2)
            
            if dist < clear_radius - inner_soft:
                alpha = 0
            elif dist < clear_radius:
                progress = (dist - (clear_radius - inner_soft)) / inner_soft
                alpha = int(fog_density * 255 * progress)
            else:
                alpha = int(fog_density * 255)
            
            noise = random.randint(-20, 20)
            alpha = max(0, min(255, alpha + noise))
            fog_surface.fill((*fog_color, alpha), (x, y, 4, 4))
    
    screen.blit(fog_surface, (0, 0))
    # ====== КОНЕЦ ТУМАНА ======

        # --- ИЗМЕНЕНО: ОТОБРАЖЕНИЕ СЧЕТЧИКА СВЕТЛЯЧКОВ ---
    text = font.render(f"Found: {collected_fireflies} / {level_goals[current_level]}", True, (139, 0, 0)) # Создаем текст
    screen.blit(text, (10, 10)) # Отображаем текст на экране



    pygame.display.update()
    
pygame.quit()
