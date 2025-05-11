import pygame
import math
import random

class Hedgehog:
    def __init__(self):
        self.images = {
            'down': pygame.image.load('assets/image/hedgehog_down.png'), # Загрузка изображений
            'up': pygame.image.load('assets/image/hedgehog_up.png'),
            'left': pygame.image.load('assets/image/hedgehog_left.png'),
            'right': pygame.image.load('assets/image/hedgehog_right.png')
        }
        self.x = 430 #  начальные координаты и скорость
        self.y = 600
        self.speed = 10
        self.current_img = self.images['down']
        self.width = self.images['down'].get_width()
        self.height = self.images['down'].get_height()

    def move(self, keys, screen_width, screen_height):
        # Сохраняем старую позицию для коллизий
        old_x, old_y = self.x, self.y

        # Обработка управления
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.current_img = self.images['left']
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.current_img = self.images['right']
        if keys[pygame.K_UP]:
            self.y -= self.speed
            self.current_img = self.images['up']
        if keys[pygame.K_DOWN]:
            self.y += self.speed
            self.current_img = self.images['down']

        # Границы экрана
        self.x = max(0, min(self.x, screen_width - self.width))
        self.y = max(0, min(self.y, screen_height - self.height))

        return old_x, old_y  # Возвращаем для проверки коллизий

    def draw(self, screen):
        screen.blit(self.current_img, (self.x, self.y))








class Firefly:
    def __init__(self):
        self.img = pygame.image.load('assets/image/fly.png')
        self.x = random.randint(0, 960 - self.img.get_width())
        self.y = random.randint(0, 768 - self.img.get_height())
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def update(self):
        # Мерцание
        self.alpha = 128 + int(128 * math.sin(pygame.time.get_ticks() * 0.003))

    def draw(self, screen):
        img_copy = self.img.copy()
        img_copy.set_alpha(self.alpha)
        screen.blit(img_copy, (self.x, self.y))










class Mob:
    def __init__(self, speed):
        self.img = pygame.image.load('assets/image/okak.png')
        self.x = random.randint(0, 960 - self.img.get_width())
        self.y = random.randint(0, 768 - self.img.get_height())
        self.speed = speed
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def chase(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        dist = max(1, math.sqrt(dx*dx + dy*dy))
        self.x += dx / dist * self.speed
        self.y += dy / dist * self.speed

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
