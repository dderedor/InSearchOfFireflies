import pygame
import math
import random
from game.hero import Hedgehog, Firefly, Mob
from game.world import World
from game.menu import StartMenu, DeathMenu, WinMenu, ToggleButton
from game.particles import Particle
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
        
        # Загрузка звуков
        self.sounds = {}
        for key, path in SOUND_EFFECTS.items():
            try:
                self.sounds[key] = pygame.mixer.Sound(path)
                self.sounds[key].set_volume(SOUND_VOLUME)
            except Exception as e:
                print(f"Ошибка загрузки звука {key}: {e}")
                self.sounds[key] = None
        
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
        self.last_monster_sound_time = 0
        self.last_step_time = 0
        self.particles = []
        
        # Создаем фоновые частицы
        for _ in range(PARTICLE_COUNT):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            self.particles.append(Particle(x, y))
    
    def reset_game(self):
        self.world = World()
        self.hedgehog = Hedgehog()
        self.fireflies = [Firefly()]
        self.mobs = []
        self.collected_fireflies = 0
        self.current_level = 1
        self.last_monster_sound_time = pygame.time.get_ticks()
        self.last_step_time = pygame.time.get_ticks()
        
        # Очищаем частицы
        self.particles = []
        
        # Создаем новые фоновые частицы
        for _ in range(PARTICLE_COUNT):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            self.particles.append(Particle(x, y))
    
    def run(self):
        running = True
        
        while running:
            current_time = pygame.time.get_ticks()
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
                self.handle_playing(events, current_time)
            
            self.draw()
            pygame.display.update()
            self.clock.tick(60)
        
        pygame.quit()
    
    def handle_menu_button(self, button):
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
        elif button.text in ["Играть", "Заново", "Ещё раз"]:
            self.reset_game()
            self.state = "playing"
            if self.music_on:
                try:
                    pygame.mixer.music.play(-1)
                except:
                    pass
        elif button.text == "Выход":
            return False
        return True
    
    def handle_playing(self, events, current_time):
        # Обработка шагов ёжика
        keys = pygame.key.get_pressed()
        moved, old_pos = self.hedgehog.move(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # Воспроизведение звука шагов
        if moved and current_time - self.last_step_time > STEP_SOUND_INTERVAL:
            if self.sounds.get('step'):
                self.sounds['step'].play()
            self.last_step_time = current_time
        
        # Сбор светлячков
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                for firefly in self.fireflies[:]:
                    if self.hedgehog.rect.colliderect(firefly.rect):
                        self.collected_fireflies += 1
                        self.fireflies.remove(firefly)
                        # Воспроизводим звук сбора
                        if self.sounds.get('collect'):
                            self.sounds['collect'].play()
                        if self.collected_fireflies < LEVEL_GOALS[self.current_level]:
                            self.fireflies.append(Firefly())
        
        # Звук монстра
        if current_time - self.last_monster_sound_time > MONSTER_SOUND_INTERVAL:
            for mob in self.mobs:
                # Расстояние до ёжика
                dist = math.sqrt((self.hedgehog.rect.x - mob.rect.x)**2 + 
                                (self.hedgehog.rect.y - mob.rect.y)**2)
                if dist < MONSTER_SOUND_RADIUS and self.sounds.get('monster'):
                    self.sounds['monster'].play()
                    break
            self.last_monster_sound_time = current_time
        
        # Логика уровней
        if self.collected_fireflies >= LEVEL_GOALS[self.current_level]:
            self.current_level += 1
            self.collected_fireflies = 0
            
            if self.current_level > len(LEVEL_GOALS):
                self.state = "win"
                if self.sounds.get('win'):
                    self.sounds['win'].play()
            else:
                self.fireflies = [Firefly()]
                if self.current_level in MOB_SPEEDS:
                    # Создаем мобов с безопасным спавном
                    if self.current_level == 2:
                        # На 2 уровне - 1 моб типа 1
                        self.mobs = [
                            Mob(
                                MOB_SPEEDS[self.current_level], 
                                self.current_level,
                                safe_position=(self.hedgehog.rect.x, self.hedgehog.rect.y)
                            )
                        ]
                    elif self.current_level == 3:
                        # На 3 уровне - 2 моба разных типов
                        self.mobs = [
                            Mob(
                                MOB_SPEEDS[self.current_level], 
                                self.current_level, 
                                "type2",
                                safe_position=(self.hedgehog.rect.x, self.hedgehog.rect.y)
                            ),
                            Mob(
                                MOB_SPEEDS[self.current_level], 
                                self.current_level, 
                                "type3",
                                safe_position=(self.hedgehog.rect.x, self.hedgehog.rect.y)
                            )
                        ]
        
        # Движение мобов и проверка столкновений
        for mob in self.mobs:
            collided = mob.chase(self.hedgehog.rect)
            if collided:
                self.state = "death"
                if self.sounds.get('death'):
                    self.sounds['death'].play()
        
        # Обновление светлячков и создание частиц
        for firefly in self.fireflies:
            if firefly.update():  # Возвращает True, когда нужно создать частицу
                # Создаем частицу у светлячка
                self.particles.append(Particle(
                    firefly.rect.centerx,
                    firefly.rect.centery,
                    is_background=False
                ))
        
        # Добавление случайных фоновых частиц
        if random.random() < PARTICLE_SPAWN_CHANCE:
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            self.particles.append(Particle(x, y))
        
        # Обновление частиц
        self.particles = [p for p in self.particles if p.update()]
    
    def draw(self):
        if self.state == "playing":
            self.draw_game()
        else:
            self.menus[self.state].draw(self.screen)
    
    def draw_game(self):
        # Отрисовка фона
        self.world.draw_background(self.screen)

        # Отрисовка ёжика
        self.hedgehog.draw(self.screen)
        
        # Отрисовка кустов
        self.world.draw_bushes(self.screen)
        
        # Отрисовка светлячков
        for firefly in self.fireflies:
            firefly.draw(self.screen)
        

        
        # Отрисовка мобов
        for mob in self.mobs:
            mob.draw(self.screen)
        
        # Отрисовка частиц (над всеми объектами, но под туманом)
        for particle in self.particles:
            particle.draw(self.screen)
        
        # Туман
        self.world.draw_fog(self.screen, self.hedgehog.rect.center)
        
        # Счетчик
        text = self.font.render(
            f"Найдено: {self.collected_fireflies}/{LEVEL_GOALS[self.current_level]}", 
            True, RED
        )
        self.screen.blit(text, (10, 10))

if __name__ == "__main__":
    game = Game()
    game.run()