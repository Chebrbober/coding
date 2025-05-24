import pygame
from ui import Button
import random
from fade import draw_fade_overlay
from assets import *  # для картинок кнопок и фона
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from entities import Player, Enemy, Boss, Projectile, Explosion

class BaseScene:
    def __init__(self):
        self.next_scene = self # Указывает на текущую сцену по умолчанию
        self.background_y = 0 # Для прокрутки фона
        self.is_fading = False # Флаг для управления затемнением/проявлением
        self.fade_alpha = 0    # Текущая прозрачность затемнения (0-255)
        self.fade_speed = 10    # Скорость изменения прозрачности
        self.fade_direction = 1 # 1 для затемнения, -1 для проявления
        self.target_scene_class = None # Класс сцены, на которую нужно перейти после затемнения
        self.next_music_path = None

    def handle_event(self, event):
        # Базовая обработка событий, может быть переопределена в дочерних классах
        pass

    def update(self):
        # Общая логика прокрутки фона
        self.background_y += 3
        if self.background_y >= 900:
            self.background_y = 0

        # Логика затемнения/проявления
        if self.is_fading:
            self.fade_alpha += self.fade_direction * self.fade_speed
            if self.fade_direction == 1: # Затемнение
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    # Когда затемнение завершено, переключаем сцену
                    if self.target_scene_class:
                        self.next_scene = self.target_scene_class()
                        self.next_scene.start_fade_in()
                    self.is_fading = False
                    self.fade_alpha = 0 # Сброс для следующего затемнения
                    self.fade_direction = 1 # Сброс на затемнение
            elif self.fade_direction == -1: # Проявление
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.is_fading = False
                    self.fade_direction = 1 # Сброс на затемнение

    def draw(self, surface):
        # Отрисовка прокручивающегося фона
        surface.blit(bg, (0, self.background_y))
        surface.blit(bg, (0, self.background_y - 900))

    def start_fade_out(self, target_scene_class, next_music_path=None): # Добавили next_music_path
        self.is_fading = True
        self.fade_direction = 1 # Затемнение
        self.target_scene_class = target_scene_class
        self.next_music_path = next_music_path # Сохраняем путь к музыке для следующей сцены.mixer.music.fadeout(500) для плавного затухания


    def start_fade_in(self):
        self.is_fading = True
        self.fade_direction = -1 # Проявление
        self.fade_alpha = 255 # Начинаем с полного затемнения
        # Музыка будет запущена в main.py после создания новой сцены

class Menu(BaseScene):
    def __init__(self):
        super().__init__() # Вызываем конструктор родительского класса
        self.font = pygame.font.SysFont(None, 60)
        self.play_button = Button(300, 510, [play_button_none, play_button_hovered, play_button_pressed])
        self.exit_button = Button(45, 45, [exit_button_none, exit_button_hovered, exit_button_pressed])

    def handle_event(self, event):
        pass

    def update(self):
        super().update() # Важно вызвать update родительского класса для фона и затемнения

        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        self.play_button.update(mouse_pos, mouse_buttons)
        self.exit_button.update(mouse_pos, mouse_buttons)

        # Переходы с затемнением
        if not self.is_fading: # Не обрабатываем клики, если идет затемнение
            if self.play_button.was_clicked():
                self.start_fade_out(Levels, menu_music) # Используем метод из BaseScene
            if self.exit_button.was_clicked():
                pygame.quit()

    def draw(self, surface):
        super().draw(surface) # Важно вызвать draw родительского класса для фона и затемнения
        surface.blit(board_name, (75, 95))
        surface.blit(game_name, (150, 160))
        self.play_button.draw(surface)
        self.exit_button.draw(surface)


class Levels(BaseScene):
    def __init__(self):
        super().__init__() # Вызываем конструктор родительского класса
        self.font = pygame.font.SysFont(None, 60)

        self.levelone_button = Button(225, 460, [levelone_button_none, levelone_button_hovered, levelone_button_pressed])
        self.leveltwo_button = Button(375, 460, [leveltwo_button_none, leveltwo_button_hovered, leveltwo_button_pressed])
        self.back_button = Button(45, 45, [back_none, back_hovered, back_pressed])

    def handle_event(self, event):
        pass

    def update(self):
        super().update() # Важно вызвать update родительского класса

        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        self.levelone_button.update(mouse_pos, mouse_buttons)
        self.leveltwo_button.update(mouse_pos, mouse_buttons)
        self.back_button.update(mouse_pos, mouse_buttons)

        if not self.is_fading: # Не обрабатываем клики, если идет затемнение
            if self.levelone_button.was_clicked():
                self.start_fade_out(LevelOne, levelone_music) # Будет создан позже
            if self.leveltwo_button.was_clicked():
                self.start_fade_out(LevelTwo, leveltwo_music) # Будет создан позже
            if self.back_button.was_clicked():
                self.start_fade_out(Menu, menu_music)

    def draw(self, surface):
        super().draw(surface) # Важно вызвать draw родительского класса
        surface.blit(board_lvl, (115, 155))
        surface.blit(lvl_name, (154, 205))
        self.levelone_button.draw(surface)
        self.leveltwo_button.draw(surface)
        self.back_button.draw(surface)

class BaseLevel(BaseScene):
    def __init__(self):
        super().__init__()
        print("BaseLevel initialized!")

        self.laser_sound = pygame.mixer.Sound(laser_blast)
        self.laser_sound.set_volume(0.3)

        self.all_sprites = pygame.sprite.Group()
        self.player_projectiles = pygame.sprite.Group()
        self.enemy_projectiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

        self.player = Player(player_default, player_projectile, player_explosion)
        self.all_sprites.add(self.player)

        self.score = 0 # Очки остаются для потенциального использования в будущем, но не влияют на спавн босса
        self.game_over = False

        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 180
        self.boss_spawned = False
        self.level_completed = False # Новый флаг для завершения уровня

    def spawn_enemy(self, enemy_type="scout"):
        if enemy_type == "scout":
            enemy = Enemy(random.randint(0, SCREEN_WIDTH - enemy_scout_default.get_width()),
                          random.randint(-100, -50),
                          enemy_scout_default, enemy_projectile, enemy_scout_explosion)
        elif enemy_type == "bomber":
            enemy = Enemy(random.randint(0, SCREEN_WIDTH - enemy_bomber_default.get_width()),
                          random.randint(-100, -50),
                          enemy_bomber_default, enemy_projectile, enemy_bomber_explosion)
        else:
            return

        self.enemies.add(enemy)
        self.all_sprites.add(enemy)

    def spawn_boss(self):
        if not self.boss_spawned:
            boss = Boss(SCREEN_WIDTH // 2 - boss_default.get_width() // 2,
                        -boss_default.get_height(),
                        boss_default, boss_projectile, boss_explosion)
            self.enemies.add(boss)
            self.all_sprites.add(boss)
            self.boss_spawned = True
            print("Босс появился!")

    def handle_event(self, event):
        super().handle_event(event)

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not self.player.is_dead:
                    self.player.shoot()
                    self.laser_sound.play()
                    for p in self.player.projectiles_group:
                        if p not in self.player_projectiles:
                            self.player_projectiles.add(p)
                            self.all_sprites.add(p)

    def update(self):
        super().update()

        if self.game_over or self.level_completed: # Если игра окончена или уровень завершен
            if not self.is_fading:
                if self.game_over:
                    self.start_fade_out(GameOverScene, gameover_music)
                elif self.level_completed:
                    # Здесь может быть переход на следующий уровень или экран победы
                    print("Уровень завершен! Переход к следующему уровню или экрану победы.")
                    # Пока ничего не делаем, дочерний класс LevelOne, LevelTwo будут обрабатывать
            return

        keys = pygame.key.get_pressed()
        if not self.player.is_dead:
            self.player.handle_keys(keys)
            self.player.update()
        else:
            if not self.player.explosion_started:
                explosion = Explosion(self.player.rect.centerx, self.player.rect.centery,
                                       self.player.explosion_frames)
                self.explosions.add(explosion)
                self.all_sprites.add(explosion)
                self.player.explosion_started = True


        # Добавляем новые снаряды игрока в общие группы
        for p in self.player.projectiles_group:
            if p not in self.player_projectiles:
                self.player_projectiles.add(p)
                self.all_sprites.add(p)

        # Обновляем всех врагов и добавляем их снаряды в общие группы
        for enemy in self.enemies:
            enemy.update()
            for p in enemy.projectiles_group:
                if p not in self.enemy_projectiles:
                    self.enemy_projectiles.add(p)
                    self.all_sprites.add(p)

        # Теперь обновляем снаряды игрока и врагов ОТДЕЛЬНО
        self.player_projectiles.update()
        self.enemy_projectiles.update()

        # Удаляем снаряды игрока, которые вышли за экран
        for p in self.player_projectiles.copy(): # Используем .copy(), чтобы можно было удалять элементы во время итерации
            if p.rect.bottom < 0: # Если снаряд ушел вверх
                self.player_projectiles.remove(p)
                self.all_sprites.remove(p)

        # Удаляем снаряды врагов, которые вышли за экран
        for p in self.enemy_projectiles.copy(): # Используем .copy()
            if p.rect.top > SCREEN_HEIGHT: # Если снаряд ушел вниз
                self.enemy_projectiles.remove(p)
                self.all_sprites.remove(p)

        self.explosions.update()
        for exp in self.explosions.copy():
            if not exp.alive():
                self.explosions.remove(exp)
                self.all_sprites.remove(exp)

        self.handle_collisions()

        if self.player.is_dead and not self.explosions:
            self.game_over = True


    def handle_collisions(self):
        # Коллизии: пули игрока vs враги
        hits = sprite.groupcollide(self.player_projectiles, self.enemies, True, False)
        for projectile, enemies_hit in hits.items():
            for enemy in enemies_hit:
                if enemy.take_damage(20):
                    # Очки начисляем только если это нужно для уровня
                    if not isinstance(enemy, Boss): # Не начисляем очки за босса здесь, если его нет в LevelOne
                         self.score += 10 # Очки за уничтоженного обычного врага
                    explosion = Explosion(enemy.rect.centerx, enemy.rect.centery, enemy.explosion_frames)
                    self.explosions.add(explosion)
                    self.all_sprites.add(explosion)
                    enemy.kill()

        # Коллизии: пули врагов vs игрок
        player_hits = sprite.spritecollide(self.player, self.enemy_projectiles, True)
        for projectile in player_hits:
            if not self.player.is_dead:
                self.player.take_damage(10)
                # print(f"Игрок получил урон. HP: {self.player.hp}")

        # Коллизии: враги vs игрок (таран)
        player_enemy_collisions = sprite.spritecollide(self.player, self.enemies, False)
        for enemy in player_enemy_collisions:
            if not self.player.is_dead:
                self.player.take_damage(25)
                # print(f"Игрок столкнулся с врагом. HP: {self.player.hp}")
                if not isinstance(enemy, Boss):
                    if enemy.take_damage(enemy.hp):
                        # self.score += 5 # Не начисляем очки за таран, если они не нужны в LevelOne
                        explosion = Explosion(enemy.rect.centerx, enemy.rect.centery, enemy.explosion_frames)
                        self.explosions.add(explosion)
                        self.all_sprites.add(explosion)
                        enemy.kill()

    def draw(self, surface):
        super().draw(surface)

        self.all_sprites.draw(surface)

        # Отрисовка HP
        font_for_hp = pygame.font.SysFont(None, 30)
        hp_text = f"HP: {self.player.hp}"
        text_surface = font_for_hp.render(hp_text, True, (255, 255, 255))
        surface.blit(text_surface, (10, 10))

        # Очки отображаются только в LevelTwo (или по необходимости)
        # score_text = f"Score: {self.score}"
        # text_surface = font.render(score_text, True, (255, 255, 255))
        # surface.blit(text_surface, (SCREEN_WIDTH - text_surface.get_width() - 10, 10))

class LevelOne(BaseLevel):
    def __init__(self):
        super().__init__()
        print("LevelOne created!")
        
        self.enemy_spawn_interval = 120 # Чуть чаще появляются (2 секунды)
        self.wave_count = 0
        self.max_waves = 3 # Например, 3 волны врагов
        self.enemies_per_wave = 5 # Количество врагов в каждой волне

        # Для того, чтобы сразу начался отсчет для первой волны
        self.initial_enemies_on_screen = 7 # Количество врагов, которые появляются сразу
        self.enemies_to_spawn_in_first_wave = 0

        # Общее количество врагов, которые должны быть уничтожены в первой волне, чтобы она завершилась
        self.current_wave_total_enemies = self.initial_enemies_on_screen + self.enemies_to_spawn_in_first_wave

        # Начальное количество врагов
        for _ in range(self.initial_enemies_on_screen): # Увеличил количество начальных врагов
            self.spawn_enemy(random.choice(["scout", "bomber"]))

        self.enemy_spawn_timer = 0 # Таймер для спавна новых врагов в рамках волн
        self.is_first_wave_completed = False # Флаг для отслеживания завершения первой волны

    def update(self):
        super().update()

        if self.game_over: # Если игрок умер, выходим из update уровня
            return

        # Увеличиваем таймер спавна врагов
        self.enemy_spawn_timer += 1

        # Логика появления волн врагов для Уровня 1
        # Логика для первой волны (которая имеет фиксированное начальное количество врагов)
        if self.wave_count == 0:
            # Проверяем, уничтожены ли все начальные враги и враги первой "воронки"
            # Если в current_wave_total_enemies нет врагов, которые еще будут спавниться,
            # и группа self.enemies пуста, значит, первая волна завершена.
            if not self.is_first_wave_completed:
                if not self.enemies: # Если нет врагов на экране (все 7 начальных уничтожены)
                    print("Первая волна Уровня 1 завершена!")
                    self.is_first_wave_completed = True
                    self.wave_count = 1 # Переходим к следующей волне
                    self.enemies_remaining_in_wave = self.enemies_per_wave # Инициализируем для второй волны
                    self.enemy_spawn_timer = 0 # Сбрасываем таймер для новой волны
        
        # Логика для последующих волн (начиная со второй)
        elif self.wave_count > 0 and self.wave_count <= self.max_waves:
            # Спавним врага, если пришло время и есть еще враги в текущей волне
            if self.enemy_spawn_timer >= self.enemy_spawn_interval and self.enemies_remaining_in_wave > 0:
                self.spawn_enemy(random.choice(["scout", "bomber"]))
                self.enemies_remaining_in_wave -= 1
                self.enemy_spawn_timer = 0 # Сброс таймера для следующего спавна

            # Проверяем, завершилась ли текущая волна (все враги появились И все на экране уничтожены)
            if self.enemies_remaining_in_wave == 0 and not self.enemies:
                self.wave_count += 1
                if self.wave_count <= self.max_waves:
                    print(f"Начало волны {self.wave_count} в Уровне 1")
                    self.enemies_remaining_in_wave = self.enemies_per_wave
                    self.enemy_spawn_timer = 0 # Сброс таймера для новой волны
                else: # Все волны завершены
                    print("Все волны Уровня 1 завершены!")
                    # Уровень считается пройденным только когда все враги (и на экране, и в очереди на спавн) исчезли
                    # Условие self.enemies_remaining_in_wave == 0 уже гарантирует, что все запланированные враги появились.
                    # Остается только проверить, что на экране никого нет.
                    if not self.enemies: # Важно убедиться, что на экране нет ни одного врага
                        self.level_completed = True

        # Если уровень завершен и затемнение не идет, переходим на экран победы
        if self.level_completed and not self.is_fading:
            self.start_fade_out(WinScene, win_music) # Переход на WinScene после прохождения LevelOne

class LevelTwo(BaseLevel):
    def __init__(self):
        super().__init__()
        print("LevelTwo created!")
        self.spawn_boss()
        self.player.hp = 100 # Можешь дать игроку полное HP перед боссом

    def update(self):
        super().update()

        if self.game_over: # Если игрок умер
            return

        # Проверяем, уничтожен ли босс
        # 'any(isinstance(e, Boss) for e in self.enemies)' проверит, есть ли еще объекты типа Boss в группе enemies
        if self.boss_spawned and not any(isinstance(e, Boss) for e in self.enemies) and not self.is_fading:
            print("Босс Уровня 2 уничтожен! Уровень 2 завершен.")
            self.level_completed = True # Уровень считается пройденным

        if self.level_completed and not self.is_fading:
            self.start_fade_out(WinScene, win_music) # Переход на экран победы (создадим ниже)

    def draw(self, surface):
        super().draw(surface)

class GameOverScene(BaseScene):
    def __init__(self):
        super().__init__()
        print("Game Over Screen!")

        self.restart_button = Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 100,
                                   [restart_button_none, restart_button_hovered, restart_button_pressed])
        self.menu_button = Button(SCREEN_WIDTH // 2 + 120, SCREEN_HEIGHT // 2 + 100,
                                  [menu_button_none, menu_button_hovered, menu_button_pressed])

    def handle_event(self, event):
        pass

    def update(self):
        super().update()
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        self.restart_button.update(mouse_pos, mouse_buttons)
        self.menu_button.update(mouse_pos, mouse_buttons)

        if not self.is_fading:
            if self.restart_button.was_clicked():
                self.start_fade_out(LevelOne, levelone_music) # Начать заново Уровень 1
            if self.menu_button.was_clicked():
                self.start_fade_out(Menu, menu_music) # Вернуться в главное меню

    def draw(self, surface):
        super().draw(surface)

        self.restart_button.draw(surface)
        self.menu_button.draw(surface)


# --- Класс для экрана Победы (Win Screen) ---
class WinScene(BaseScene):
    def __init__(self):
        super().__init__()
        print("Win Screen!")

        self.menu_button = Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50,
                                  [menu_button_none, menu_button_hovered, menu_button_pressed])
        self.restart_button = Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50,
                                     [restart_button_none, restart_button_hovered, restart_button_pressed])

    def handle_event(self, event):
        pass

    def update(self):
        super().update()
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        self.menu_button.update(mouse_pos, mouse_buttons)
        self.restart_button.update(mouse_pos, mouse_buttons)

        if not self.is_fading:
            if self.restart_button.was_clicked():
                self.start_fade_out(LevelOne, levelone_music) # Начать игру сначала
            if self.menu_button.was_clicked():
                self.start_fade_out(Menu, menu_music) # Вернуться в главное меню

    def draw(self, surface):
        super().draw(surface)

        self.restart_button.draw(surface)
        self.menu_button.draw(surface)