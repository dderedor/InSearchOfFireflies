#venv\Scripts\activate.bat
import pygame
from game.hero import Hedgehog, Firefly, Mob
from game.world import World

def main():
    # Инициализация pygame
    pygame.init()
    screen = pygame.display.set_mode((960, 768))
    pygame.display.set_caption('Ёжик и светлячки')
    
    # Загрузка иконки
    icon = pygame.image.load('assets/image/icon.webp')
    pygame.display.set_icon(icon)

    # Инициализация мира
    world = World()
    
    # Настройки игры
    font = pygame.font.Font('assets/fonts.ttf', 30)
    level_goals = {1: 3, 2: 5, 3: 7}
    MOB_SPEEDS = {2: 1.5, 3: 2.5}

    # Игровые объекты
    hedgehog = Hedgehog()
    fireflies = [Firefly()]  # Начинаем с одного светлячка
    mobs = []
    collected_fireflies = 0
    current_level = 1

    # Основной цикл
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                for firefly in fireflies[:]:
                    if (abs(hedgehog.x - firefly.x) < hedgehog.width and 
                        abs(hedgehog.y - firefly.y) < hedgehog.height):
                        collected_fireflies += 1
                        fireflies.remove(firefly)
                        if collected_fireflies < level_goals[current_level]:
                            fireflies.append(Firefly())

        # Обновление игрового состояния
        keys = pygame.key.get_pressed()
        hedgehog.move(keys, screen.get_width(), screen.get_height())

        # Логика уровней
        if collected_fireflies >= level_goals[current_level]:
            current_level += 1
            collected_fireflies = 0
            if current_level > len(level_goals):
                print("Игра пройдена! Ты нашел маму!")
                running = False
            else:
                fireflies = [Firefly()]
                if current_level in MOB_SPEEDS:
                    mobs = [Mob(MOB_SPEEDS[current_level]) for _ in range(current_level-1)]

        # Проверка столкновений с мобами
        for mob in mobs:
            mob.chase(hedgehog.x, hedgehog.y)
            if (abs(hedgehog.x - mob.x) < hedgehog.width and 
                abs(hedgehog.y - mob.y) < hedgehog.height):
                print("Game Over! Моб догнал ёжика!")
                running = False

        # Отрисовка
        screen.fill((0, 0, 0))  # Очистка экрана
        
        # Отрисовка мира (порядок важен!)
        world.draw_grass(screen)      # 1. Трава (фон)
        hedgehog.draw(screen)         # 2. Ёжик
        world.draw_bushes(screen)     # 3. Кусты

        
        for mob in mobs:              # 4. Мобы
            mob.draw(screen)
            
        for firefly in fireflies:     # 5. Светлячки
            firefly.update()
            firefly.draw(screen)
        
        world.draw_fog(screen, (      # 6. Туман (поверх всего)
            hedgehog.x + hedgehog.width // 2,
            hedgehog.y + hedgehog.height // 2
        ))

        # Интерфейс
        text = font.render(
            f"Found: {collected_fireflies}/{level_goals[current_level]}", 
            True, (139, 0, 0)
        )
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()