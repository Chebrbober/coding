from pygame import *
from ui import Button
from fade import draw_fade_overlay
from assets import *  # для картинок кнопок и фона
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

mixer.init()
mixer.music.load(menu_music)
mixer.music.play(-1)

class BaseScene:
    def __init__(self):
        self.next_scene = self # Указывает на текущую сцену по умолчанию
        self.background_y = 0 # Для прокрутки фона
        self.is_fading = False # Флаг для управления затемнением/проявлением
        self.fade_alpha = 0    # Текущая прозрачность затемнения (0-255)
        self.fade_speed = 10    # Скорость изменения прозрачности
        self.fade_direction = 1 # 1 для затемнения, -1 для проявления
        self.target_scene_class = None # Класс сцены, на которую нужно перейти после затемнения

    def handle_event(self, event):
        # Базовая обработка событий, может быть переопределена в дочерних классах
        pass

    def update(self):
        # Общая логика прокрутки фона
        self.background_y -= 3
        if self.background_y <= -900:
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
        surface.blit(bg, (0, self.background_y + 900))

    def start_fade_out(self, target_scene_class):
        self.is_fading = True
        self.fade_direction = 1 # Затемнение
        self.target_scene_class = target_scene_class

    def start_fade_in(self):
        self.is_fading = True
        self.fade_direction = -1 # Проявление
        self.fade_alpha = 255 # Начинаем с полного затемнения

class Menu(BaseScene):
    def __init__(self):
        super().__init__() # Вызываем конструктор родительского класса
        self.font = font.SysFont(None, 60)
        self.play_button = Button(300, 510, [play_button_none, play_button_hovered, play_button_pressed])
        self.exit_button = Button(45, 45, [exit_button_none, exit_button_hovered, exit_button_pressed])

    def handle_event(self, event):
        pass

    def update(self):
        super().update() # Важно вызвать update родительского класса для фона и затемнения

        mouse_pos = mouse.get_pos()
        mouse_buttons = mouse.get_pressed()

        self.play_button.update(mouse_pos, mouse_buttons)
        self.exit_button.update(mouse_pos, mouse_buttons)

        # Переходы с затемнением
        if not self.is_fading: # Не обрабатываем клики, если идет затемнение
            if self.play_button.was_clicked():
                self.start_fade_out(Levels) # Используем метод из BaseScene
            if self.exit_button.was_clicked():
                quit()

    def draw(self, surface):
        super().draw(surface) # Важно вызвать draw родительского класса для фона и затемнения
        surface.blit(board_name, (75, 95))
        surface.blit(game_name, (150, 160))
        self.play_button.draw(surface)
        self.exit_button.draw(surface)

        if self.is_fading or self.fade_alpha > 0:
            draw_fade_overlay(surface, self.fade_alpha)


class Levels(BaseScene):
    def __init__(self):
        super().__init__() # Вызываем конструктор родительского класса
        self.font = font.SysFont(None, 60)

        self.levelone_button = Button(225, 460, [levelone_button_none, levelone_button_hovered, levelone_button_pressed])
        self.leveltwo_button = Button(375, 460, [leveltwo_button_none, leveltwo_button_hovered, leveltwo_button_pressed])
        self.back_button = Button(45, 45, [back_none, back_hovered, back_pressed])

    def handle_event(self, event):
        pass

    def update(self):
        super().update() # Важно вызвать update родительского класса

        mouse_pos = mouse.get_pos()
        mouse_buttons = mouse.get_pressed()

        self.levelone_button.update(mouse_pos, mouse_buttons)
        self.leveltwo_button.update(mouse_pos, mouse_buttons)
        self.back_button.update(mouse_pos, mouse_buttons)

        if not self.is_fading: # Не обрабатываем клики, если идет затемнение
            if self.levelone_button.was_clicked():
                #self.start_fade_out(LevelOne) # Будет создан позже
                print("Начать уровень 1")
            if self.leveltwo_button.was_clicked():
                #self.start_fade_out(LevelTwo) # Будет создан позже
                print("Начать уровень 2")
            if self.back_button.was_clicked():
                self.start_fade_out(Menu)

    def draw(self, surface):
        super().draw(surface) # Важно вызвать draw родительского класса
        surface.blit(board_lvl, (115, 155))
        surface.blit(lvl_name, (154, 205))
        self.levelone_button.draw(surface)
        self.leveltwo_button.draw(surface)
        self.back_button.draw(surface)

        if self.is_fading or self.fade_alpha > 0:
            draw_fade_overlay(surface, self.fade_alpha)
