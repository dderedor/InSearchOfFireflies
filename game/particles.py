import pygame
import random
import math
from config import *

class Particle:
    def __init__(self, x, y, is_background=True):
        self.x = x
        self.y = y
        self.size = random.uniform(2, 5)
        self.color = PARTICLE_COLOR
        
        # Для фоновых частиц - медленное случайное движение
        if is_background:
            self.speed = random.uniform(0.1, 0.3)
            angle = random.uniform(0, 2 * math.pi)
            self.vx = math.cos(angle) * self.speed
            self.vy = math.sin(angle) * self.speed
            self.lifetime = random.randint(200, 400)
        # Для частиц от светлячков - быстрое движение от центра
        else:
            self.speed = random.uniform(1.5, 3.0)
            angle = random.uniform(0, 2 * math.pi)
            self.vx = math.cos(angle) * self.speed
            self.vy = math.sin(angle) * self.speed
            self.lifetime = random.randint(30, 60)
        
        self.alpha = 255
        self.decay = random.uniform(2, 5)
        
        # Если есть изображение частицы
        self.image = None
        try:
            self.image = pygame.image.load(FLY_PARTICLE).convert_alpha()
            self.image = pygame.transform.scale(self.image, (int(self.size*3), int(self.size*3)))
        except:
            pass
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1
        self.alpha = max(0, self.alpha - self.decay)
        return self.lifetime > 0
    
    def draw(self, screen):
        if self.image:
            img = self.image.copy()
            img.set_alpha(int(self.alpha))
            screen.blit(img, (self.x - img.get_width()//2, self.y - img.get_height()//2))
        else:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))