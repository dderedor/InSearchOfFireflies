# game/game_object.py
import pygame

class GameObject:
    def __init__(self, x, y, image_path):
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except:
            # Создаем заглушку, если изображение не найдено
            self.image = pygame.Surface((32, 32))
            self.image.fill((255, 0, 255))  # Фиолетовый цвет для заметности
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self):
        pass