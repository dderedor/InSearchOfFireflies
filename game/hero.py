import pygame
import math
import random
from .game_object import GameObject
from config import HEDGEHOG_START_POS, SCREEN_WIDTH, SCREEN_HEIGHT, MOB_IMAGES, SAFE_SPAWN_DISTANCE

class Hedgehog(GameObject):
    def __init__(self):
        super().__init__(HEDGEHOG_START_POS[0], HEDGEHOG_START_POS[1], 'assets/image/hedgehog_down.png')
        self.images = {
            'down': pygame.image.load('assets/image/hedgehog_down.png'),
            'up': pygame.image.load('assets/image/hedgehog_up.png'),
            'left': pygame.image.load('assets/image/hedgehog_left.png'),
            'right': pygame.image.load('assets/image/hedgehog_right.png')
        }
        self.speed = 10
        self.current_img = self.images['down']
        self.rect = self.current_img.get_rect(topleft=(self.rect.x, self.rect.y))
        self.last_move_x = 0
        self.last_move_y = 0

    def move(self, keys, screen_width, screen_height):
        moved = False
        old_x, old_y = self.rect.x, self.rect.y
        
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.current_img = self.images['left']
            moved = True
            self.last_move_x = -1
            self.last_move_y = 0
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.current_img = self.images['right']
            moved = True
            self.last_move_x = 1
            self.last_move_y = 0
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.current_img = self.images['up']
            moved = True
            self.last_move_x = 0
            self.last_move_y = -1
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.current_img = self.images['down']
            moved = True
            self.last_move_x = 0
            self.last_move_y = 1

        # Границы экрана
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))

        return moved, (old_x, old_y)

    def draw(self, screen):
        screen.blit(self.current_img, self.rect)

class Firefly(GameObject):
    def __init__(self):
        # Убедимся, что светлячок не появляется за границами экрана
        super().__init__(
            random.randint(50, SCREEN_WIDTH - 82),
            random.randint(50, SCREEN_HEIGHT - 82),
            'assets/image/fly.png'
        )
        self.alpha = 255
        self.particle_timer = random.randint(10, 30)

    def update(self):
        self.alpha = 128 + int(128 * math.sin(pygame.time.get_ticks() * 0.003))
        self.image = pygame.image.load('assets/image/fly.png').convert_alpha()
        self.image.set_alpha(self.alpha)
        
        # Таймер для создания частиц
        self.particle_timer -= 1
        if self.particle_timer <= 0:
            self.particle_timer = random.randint(10, 30)
            return True  # Сигнал для создания частицы
        
        return False

class Mob(GameObject):
    def __init__(self, speed, level, mob_type=None, safe_position=None):
        """
        :param safe_position: Позиция ёжика, от которой нужно держаться на расстоянии
        """
        # Определяем изображение в зависимости от уровня и типа
        if level == 2:
            image_path = MOB_IMAGES["type1"]
        elif level == 3:
            image_path = MOB_IMAGES["type2"] if mob_type == "type2" else MOB_IMAGES["type3"]
        else:
            image_path = 'assets/image/okak.png'
        
        # Пытаемся найти безопасную позицию
        for _ in range(20):  # Максимум 20 попыток
            x = random.randint(0, SCREEN_WIDTH - 64)
            y = random.randint(0, SCREEN_HEIGHT - 64)
            
            # Проверяем расстояние до ёжика
            if safe_position:
                dist = math.sqrt((x - safe_position[0])**2 + (y - safe_position[1])**2)
                if dist > SAFE_SPAWN_DISTANCE:
                    break
        else:
            # Если не нашли безопасную позицию, используем последнюю
            x = random.randint(0, SCREEN_WIDTH - 64)
            y = random.randint(0, SCREEN_HEIGHT - 64)
        
        super().__init__(x, y, image_path)
        self.speed = speed
        self.level = level
        self.mob_type = mob_type

    def chase(self, target_rect):
        dx = target_rect.x - self.rect.x
        dy = target_rect.y - self.rect.y
        dist = max(1, math.sqrt(dx*dx + dy*dy))
        self.rect.x += dx / dist * self.speed
        self.rect.y += dy / dist * self.speed
        
        # Проверка столкновения с ёжиком
        if dist < max(self.rect.width, self.rect.height) / 2:
            return True
        return False