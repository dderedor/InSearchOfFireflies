import pygame
from config import *

class Button:
    def __init__(self, x, y, image_path, text=None):
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except:
            self.image = pygame.Surface((200, 60))
            self.image.fill((50, 150, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.text = text
        try:
            self.font = pygame.font.Font('assets/fonts.ttf', 30)
        except:
            self.font = pygame.font.SysFont(None, 30)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.text:
            text_surface = self.font.render(self.text, True, WHITE)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)
        
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class ToggleButton(Button):
    def __init__(self, x, y, on_image, off_image, initial_state=True):
        try:
            self.on_image = pygame.image.load(on_image).convert_alpha()
            self.off_image = pygame.image.load(off_image).convert_alpha()
        except:
            self.on_image = pygame.Surface((60, 60))
            self.on_image.fill((0, 100, 200))
            self.off_image = pygame.Surface((60, 60))
            self.off_image.fill((200, 100, 0))
            
        self.state = initial_state
        image = self.on_image if initial_state else self.off_image
        super().__init__(x, y, "")
        self.image = image
    
    def toggle(self):
        self.state = not self.state
        self.image = self.on_image if self.state else self.off_image

class Menu:
    def __init__(self, background_path):
        self.buttons = []
        try:
            self.background = pygame.image.load(background_path)
        except:
            self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.background.fill((30, 30, 70))
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.is_clicked(mouse_pos):
                    return button
        return None
        
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        for button in self.buttons:
            button.draw(screen)

class StartMenu(Menu):
    def __init__(self):
        super().__init__(MENU_BG)
        self.buttons = [
            Button(*START_PLAY_BUTTON_POS, PLAY_BUTTON_IMG, "Играть"),
            ToggleButton(*START_MUSIC_BUTTON_POS, MUSIC_ON_BUTTON_IMG, MUSIC_OFF_BUTTON_IMG),
            Button(*START_QUIT_BUTTON_POS, QUIT_BUTTON_IMG, "Выход")
        ]

class DeathMenu(Menu):
    def __init__(self):
        super().__init__(DEATH_BG)
        self.buttons = [
            Button(*END_PLAY_BUTTON_POS, PLAY_BUTTON_IMG, "Заново"),
            ToggleButton(*END_MUSIC_BUTTON_POS, MUSIC_ON_BUTTON_IMG, MUSIC_OFF_BUTTON_IMG),
            Button(*END_QUIT_BUTTON_POS, QUIT_BUTTON_IMG, "Выход")
        ]

class WinMenu(Menu):
    def __init__(self):
        super().__init__(WIN_BG)
        self.buttons = [
            Button(*END_PLAY_BUTTON_POS, PLAY_BUTTON_IMG, "Ещё раз"),
            ToggleButton(*END_MUSIC_BUTTON_POS, MUSIC_ON_BUTTON_IMG, MUSIC_OFF_BUTTON_IMG),
            Button(*END_QUIT_BUTTON_POS, QUIT_BUTTON_IMG, "Выход")
        ]