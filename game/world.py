# game/world.py
import pygame
import math
import random
from config import *

class World:
    def __init__(self):
        # Загрузка всех изображений
        self.grass_img = pygame.image.load('assets/image/trava.png')
        self.leaf_img = pygame.image.load('assets/image/leaf.png')
        self.tile_size = self.grass_img.get_width()
        
        # Позиции кустов
        self.bush_positions = [
            (20,100), (150,300), (60,550),
            (770,400), (700,200), (650,600)
        ]
        
        # Настройки тумана (оригинальные)
        self.fog_noise = FOG_NOISE
        self.fog_color = FOG_COLOR
        
    def draw_grass(self, screen):
        """Отрисовка травы (фона)"""
        screen_width, screen_height = screen.get_size()
        for y in range(0, screen_height, self.tile_size):
            for x in range(0, screen_width, self.tile_size):
                screen.blit(self.grass_img, (x, y))
    
    def draw_bushes(self, screen):
        """Отрисовка кустов/листьев"""
        for pos in self.bush_positions:
            screen.blit(self.leaf_img, pos)
    
    def draw_fog(self, screen, hedgehog_pos):
        """Оригинальный туман с шумом"""
        screen_width, screen_height = screen.get_size()
        fog_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        hedgehog_center_x, hedgehog_center_y = hedgehog_pos
        
        for x in range(0, screen_width, 4):
            for y in range(0, screen_height, 4):
                dist = math.sqrt((x - hedgehog_center_x)**2 + (y - hedgehog_center_y)**2)
                if dist < FOG_RADIUS:
                    alpha = 0
                elif dist < FOG_RADIUS + 40:  # Зона плавного перехода
                    alpha = int(255 * ((dist - FOG_RADIUS) / 40))
                else:
                    alpha = 255
                
                # Добавляем шум для атмосферности
                noise = random.randint(-self.fog_noise, self.fog_noise)
                alpha = max(0, min(255, alpha + noise))
                
                fog_surface.fill((*self.fog_color, alpha), (x, y, 4, 4))
        
        screen.blit(fog_surface, (0, 0))