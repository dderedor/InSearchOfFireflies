import pygame
import math
import random
from config import *

class World:
    def __init__(self):
        # Загрузка фонового изображения
        try:
            self.background = pygame.image.load(LEVEL_BG).convert()
            self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            # Если изображение не загружено, создаем зеленый фон
            self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.background.fill((100, 200, 100))
        
        # Позиции кустов
        self.bush_positions = [
            (20,100), (150,300), (60,550),
            (770,400), (700,200), (650,600)
        ]
        
        # Настройки тумана
        self.fog_noise = FOG_NOISE
        self.fog_color = FOG_COLOR
        
    def draw_background(self, screen):
        """Отрисовка фона (ваше изображение)"""
        screen.blit(self.background, (0, 0))
    
    def draw_bushes(self, screen):
        """Отрисовка кустов/листьев"""
        for pos in self.bush_positions:
            # Если у вас есть изображение куста, замените pygame.Rect на его отрисовку
            pygame.draw.rect(screen, (34, 139, 34), pygame.Rect(pos[0], pos[1], 60, 60))
    
    def draw_fog(self, screen, hedgehog_pos):
        """Туман с шумом"""
        screen_width, screen_height = screen.get_size()
        fog_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        hedgehog_center_x, hedgehog_center_y = hedgehog_pos
        
        for x in range(0, screen_width, 4):
            for y in range(0, screen_height, 4):
                dist = math.sqrt((x - hedgehog_center_x)**2 + (y - hedgehog_center_y)**2)
                if dist < FOG_RADIUS:
                    alpha = 0
                elif dist < FOG_RADIUS + 40:
                    alpha = int(255 * ((dist - FOG_RADIUS) / 40))
                else:
                    alpha = 255
                
                noise = random.randint(-self.fog_noise, self.fog_noise)
                alpha = max(0, min(255, alpha + noise))
                
                fog_surface.fill((*self.fog_color, alpha), (x, y, 4, 4))
        
        screen.blit(fog_surface, (0, 0))