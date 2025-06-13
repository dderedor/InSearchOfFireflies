# game/menu.py
import pygame
from config import *

class Button:
    def __init__(self, x, y, image_path, text):
        try:
            self.image = pygame.image.load(image_path)
        except:
            # Создаем заглушку, если изображение не найдено
            self.image = pygame.Surface((200, 60))
            self.image.fill((50, 150, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.text = text
        try:
            self.font = pygame.font.Font('assets/fonts.ttf', 30)
        except:
            self.font = pygame.font.SysFont(None, 30)
        
    def draw(self, screen):
        """Отрисовка кнопки с текстом"""
        screen.blit(self.image, self.rect)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def is_clicked(self, pos):
        """Проверка клика по кнопке"""
        return self.rect.collidepoint(pos)

class Menu:
    def __init__(self, background_path):
        self.buttons = []
        try:
            self.background = pygame.image.load(background_path)
        except:
            # Создаем заглушку для фона
            self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.background.fill((30, 30, 70))
        
    def handle_event(self, event):
        """Обработка событий меню"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.is_clicked(mouse_pos):
                    return button.text.lower()
        return None
        
    def draw(self, screen):
        """Отрисовка меню"""
        screen.blit(self.background, (0, 0))
        for button in self.buttons:
            button.draw(screen)

class StartMenu(Menu):
    def __init__(self):
        super().__init__(MENU_BG)
        self.buttons = [
            Button(*START_BUTTON_POS, BUTTON_IMG, "Начать игру"),
            Button(*QUIT_BUTTON_POS, BUTTON_IMG, "Выход")
        ]

class DeathMenu(Menu):
    def __init__(self):
        super().__init__(DEATH_BG)
        self.buttons = [
            Button(*RESTART_BUTTON_POS, BUTTON_IMG, "Начать заново"),
            Button(*QUIT_BUTTON_POS, BUTTON_IMG, "Выход")
        ]

class WinMenu(Menu):
    def __init__(self):
        super().__init__(WIN_BG)
        self.buttons = [
            Button(*RESTART_BUTTON_POS, BUTTON_IMG, "Играть заново"),
            Button(*QUIT_BUTTON_POS, BUTTON_IMG, "Выход")
        ]