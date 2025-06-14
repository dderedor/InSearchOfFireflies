# main.py
import pygame
from game.hero import Hedgehog, Firefly, Mob
from game.world import World
from game.menu import StartMenu, DeathMenu, WinMenu
from config import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Инициализация аудио системы
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Ёжик и светлячки')
        
        # Загрузка иконки
        try:
            icon = pygame.image.load('assets/image/icon.webp')
            pygame.display.set_icon(icon)
        except:
            pass
        
        # Инициализация музыки
        self.music_on = True  # Флаг состояния музыки
        try:
            # ЗАМЕНИТЕ MUSIC_FILE НА ПУТЬ К ВАШЕМУ МУЗЫКАЛЬНОМУ ФАЙЛУ
            pygame.mixer.music.load(MUSIC_FILE)
            pygame.mixer.music.set_volume(MUSIC_VOLUME)  # Установка громкости
            pygame.mixer.music.play(-1)  # -1 означает бесконечное повторение
        except Exception as e:
            print(f"Ошибка загрузки музыки: {e}")
            self.music_on = False
        
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
                elif self.state != "playing":
                    # Обработка кнопок в меню
                    clicked_button = self.menus[self.state].handle_event(event)
                    if clicked_button:
                        self.handle_menu_button(clicked_button)
            
            # Обработка игровых событий в состоянии playing
            if self.state == "playing":
                self.handle_playing(events)
            
            # Отрисовка
            self.draw()
            
            # Обновление экрана
            pygame.display.update()
            self.clock.tick(60)
        
        pygame.quit()
    
    def handle_menu_button(self, button):
        """Обработка нажатий на кнопки в меню"""
        # Если нажата кнопка переключения музыки
        if isinstance(button, ToggleButton):
            button.toggle()
            self.music_on = button.state
            if self.music_on:
                pygame.mixer.music.play(-1)  # Запуск музыки
                pygame.mixer.music.set_volume(MUSIC_VOLUME)
            else:
                pygame.mixer.music.stop()  # Остановка музыки
        
        # Если нажата кнопка игры/перезапуска
        elif "Играть" in button.text or "Заново" in button.text or "Ещё раз" in button.text:
            self.reset_game()
            self.state = "playing"
            if self.music_on:
                pygame.mixer.music.play(-1)  # Перезапуск музыки при начале игры
        
        # Если нажата кнопка выхода
        elif "Выход" in button.text:
            return False  # Сигнал для выхода из игры
        
        return True
    
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
        
        # Туман
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