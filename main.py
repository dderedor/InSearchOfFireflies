import pygame
from game.hero import Hedgehog, Firefly, Mob
from game.world import World
from game.menu import StartMenu, DeathMenu, WinMenu, ToggleButton
from config import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Ёжик и светлячки')
        
        try:
            icon = pygame.image.load('assets/image/icon.webp')
            pygame.display.set_icon(icon)
        except:
            pass
        
        # Инициализация музыки
        self.music_on = True
        try:
            pygame.mixer.music.load(MUSIC_FILE)
            pygame.mixer.music.set_volume(MUSIC_VOLUME)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Ошибка загрузки музыки: {e}")
            self.music_on = False
        
        # Игровые состояния
        self.state = "menu"
        self.menus = {
            "menu": StartMenu(),
            "death": DeathMenu(),
            "win": WinMenu()
        }
        
        # Инициализация игры
        self.reset_game()
        
        # Шрифт
        try:
            self.font = pygame.font.Font('assets/fonts.ttf', 30)
        except:
            self.font = pygame.font.SysFont(None, 30)
        
        self.clock = pygame.time.Clock()
        
    def reset_game(self):
        self.world = World()
        self.hedgehog = Hedgehog()
        self.fireflies = [Firefly()]
        self.mobs = []
        self.collected_fireflies = 0
        self.current_level = 1
    
    def run(self):
        running = True
        
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif self.state != "playing":
                    clicked_button = self.menus[self.state].handle_event(event)
                    if clicked_button:
                        if not self.handle_menu_button(clicked_button):
                            running = False
            
            if self.state == "playing":
                self.handle_playing(events)
            
            self.draw()
            pygame.display.update()
            self.clock.tick(60)
        
        pygame.quit()
    
    def handle_menu_button(self, button):
        # Кнопка музыки
        if isinstance(button, ToggleButton):
            button.toggle()
            self.music_on = button.state
            if self.music_on:
                try:
                    pygame.mixer.music.play(-1)
                except:
                    pass
            else:
                pygame.mixer.music.stop()
        
        # Кнопка игры
        elif button.text in ["Играть", "Заново", "Ещё раз"]:
            self.reset_game()
            self.state = "playing"
            if self.music_on:
                try:
                    pygame.mixer.music.play(-1)
                except:
                    pass
        
        # Кнопка выхода
        elif button.text == "Выход":
            return False  # Выход из игры
        
        return True
    
    def handle_playing(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                for firefly in self.fireflies[:]:
                    if self.hedgehog.rect.colliderect(firefly.rect):
                        self.collected_fireflies += 1
                        self.fireflies.remove(firefly)
                        if self.collected_fireflies < LEVEL_GOALS[self.current_level]:
                            self.fireflies.append(Firefly())
        
        keys = pygame.key.get_pressed()
        self.hedgehog.move(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        if self.collected_fireflies >= LEVEL_GOALS[self.current_level]:
            self.current_level += 1
            self.collected_fireflies = 0
            
            if self.current_level > len(LEVEL_GOALS):
                self.state = "win"
            else:
                self.fireflies = [Firefly()]
                if self.current_level in MOB_SPEEDS:
                    self.mobs = [Mob(MOB_SPEEDS[self.current_level]) for _ in range(self.current_level-1)]
        
        for mob in self.mobs:
            mob.chase(self.hedgehog.rect)
            if self.hedgehog.rect.colliderect(mob.rect):
                self.state = "death"
        
        for firefly in self.fireflies:
            firefly.update()
    
    def draw(self):
        if self.state == "playing":
            self.draw_game()
        else:
            self.menus[self.state].draw(self.screen)
    
    def draw_game(self):
        self.screen.fill(BLACK)
        
        # Отрисовка мира
        self.world.draw_grass(self.screen)
        self.world.draw_bushes(self.screen)
        self.hedgehog.draw(self.screen)
        
        for mob in self.mobs:
            mob.draw(self.screen)
        
        for firefly in self.fireflies:
            firefly.draw(self.screen)
        
        # Туман
        self.world.draw_fog(self.screen, self.hedgehog.rect.center)
        
        # Счетчик (рисуем поверх тумана)
        text = self.font.render(
            f"Найдено: {self.collected_fireflies}/{LEVEL_GOALS[self.current_level]}", 
            True, RED  # Ваш красный цвет
        )
        self.screen.blit(text, (10, 10))

if __name__ == "__main__":
    game = Game()
    game.run()