# game/hero.py
import pygame
import math
import random
from .game_object import GameObject
from config import HEDGEHOG_START_POS

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

    def move(self, keys, screen_width, screen_height):
        old_pos = self.rect.copy()
        
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.current_img = self.images['left']
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.current_img = self.images['right']
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.current_img = self.images['up']
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.current_img = self.images['down']

        # Границы экрана
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))

        return old_pos

    def draw(self, screen):
        screen.blit(self.current_img, self.rect)

class Firefly(GameObject):
    def __init__(self):
        super().__init__(
            random.randint(0, 960 - 32), 
            random.randint(0, 768 - 32),
            'assets/image/fly.png'
        )
        self.alpha = 255

    def update(self):
        self.alpha = 128 + int(128 * math.sin(pygame.time.get_ticks() * 0.003))
        # Создаем копию изображения для установки альфа-канала
        self.image = pygame.image.load('assets/image/fly.png').convert_alpha()
        self.image.set_alpha(self.alpha)

class Mob(GameObject):
    def __init__(self, speed):
        super().__init__(
            random.randint(0, 960 - 64), 
            random.randint(0, 768 - 64),
            'assets/image/okak.png'
        )
        self.speed = speed

    def chase(self, target_rect):
        dx = target_rect.x - self.rect.x
        dy = target_rect.y - self.rect.y
        dist = max(1, math.sqrt(dx*dx + dy*dy))
        self.rect.x += dx / dist * self.speed
        self.rect.y += dy / dist * self.speed