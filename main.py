# main.py
import pygame
from game.hero import Hedgehog, Firefly, Mob
from game.world import World
from game.menu import StartMenu, DeathMenu, WinMenu
from config import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Ёжик и светлячки')
        
        # Загрузка иконки
        try:
            icon = pygame.image.load('assets/image/icon.webp')
            pygame.display.set_icon(icon)
        except:
            pass
        
        # Игровые состояния
        self.state = "menu"  # menu, playing, death, win
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
        
        # Часы
        self.clock = pygame.time.Clock()
        
    def reset_game(self):
        """Сброс состояния игры"""
        self.world = World()
        self.hedgehog = Hedgehog()
        self.fireflies = [Firefly()]
        self.mobs = []
        self.collected_fireflies = 0
        self.current_level = 1
    
    def run(self):
        """Основной игровой цикл"""
        running = True
        
        while running:
            # Обработка событий
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            
            # Обработка состояний игры
            if self.state == "menu":
                action = self.handle_menu(events)
                if action == "начать игру":
                    self.state = "playing"
                elif action == "выход":
                    running = False
            
            elif self.state == "playing":
                self.handle_playing(events)
            
            elif self.state == "death":
                action = self.handle_menu(events)
                if action == "начать заново":
                    self.reset_game()
                    self.state = "playing"
                elif action == "выход":
                    running = False
            
            elif self.state == "win":
                action = self.handle_menu(events)
                if action == "играть заново":
                    self.reset_game()
                    self.state = "playing"
                elif action == "выход":
                    running = False
            
            # Отрисовка
            self.draw()
            
            # Обновление экрана
            pygame.display.update()
            self.clock.tick(60)
        
        pygame.quit()
    
    def handle_menu(self, events):
        """Обработка событий меню"""
        for event in events:
            result = self.menus[self.state].handle_event(event)
            if result:
                return result
        return None
    
    def handle_playing(self, events):
        """Обработка игровых событий"""
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                # Сбор светлячков
                for firefly in self.fireflies[:]:
                    if self.hedgehog.rect.colliderect(firefly.rect):
                        self.collected_fireflies += 1
                        self.fireflies.remove(firefly)
                        if self.collected_fireflies < LEVEL_GOALS[self.current_level]:
                            self.fireflies.append(Firefly())
        
        # Управление ёжиком
        keys = pygame.key.get_pressed()
        self.hedgehog.move(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # Логика уровней
        if self.collected_fireflies >= LEVEL_GOALS[self.current_level]:
            self.current_level += 1
            self.collected_fireflies = 0
            
            if self.current_level > len(LEVEL_GOALS):
                self.state = "win"  # Победа!
            else:
                self.fireflies = [Firefly()]
                if self.current_level in MOB_SPEEDS:
                    self.mobs = [Mob(MOB_SPEEDS[self.current_level]) for _ in range(self.current_level-1)]
        
        # Движение мобов
        for mob in self.mobs:
            mob.chase(self.hedgehog.rect)
            if self.hedgehog.rect.colliderect(mob.rect):
                self.state = "death"  # Смерть
        
        # Обновление светлячков
        for firefly in self.fireflies:
            firefly.update()
    
    def draw(self):
        """Отрисовка текущего состояния"""
        if self.state == "playing":
            self.draw_game()
        else:
            self.draw_menu()
    
    def draw_menu(self):
        """Отрисовка меню"""
        self.menus[self.state].draw(self.screen)
    
    def draw_game(self):
        """Отрисовка игрового процесса"""
        self.screen.fill(BLACK)
        
        # Отрисовка мира
        self.world.draw_grass(self.screen)
        self.world.draw_bushes(self.screen)
        
        # Персонажи
        self.hedgehog.draw(self.screen)
        
        # Мобы
        for mob in self.mobs:
            mob.draw(self.screen)
        
        # Светлячки
        for firefly in self.fireflies:
            firefly.draw(self.screen)
        
        # Туман (оригинальная версия)
        self.world.draw_fog(self.screen, self.hedgehog.rect.center)
        
        # Интерфейс
        text = self.font.render(
            f"Найдено: {self.collected_fireflies}/{LEVEL_GOALS[self.current_level]}", 
            True, RED
        )
        self.screen.blit(text, (10, 10))

if __name__ == "__main__":
    game = Game()
    game.run()