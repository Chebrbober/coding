from pygame import *
from ui import Button
from fade import fade_out
from assets import *  # для картинок кнопок и фона
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

mixer.init()
mixer.music.load(menu_music)
mixer.music.play(-1)

class Menu:
    def __init__(self):
        self.next_scene = self
        self.font = font.SysFont(None, 60)
        self.play_button = Button(300, 510, [play_button_none, play_button_hovered, play_button_pressed])
        self.exit_button = Button(45, 45, [exit_button_none, exit_button_hovered, exit_button_pressed])
        self.bg_y = 0

    def handle_event(self, event):
        pass

    def update(self):
        self.bg_y -= 3
        if self.bg_y <= -900:
            self.bg_y = 0

        mouse_pos = mouse.get_pos()
        mouse_buttons = mouse.get_pressed()

        self.play_button.update(mouse_pos, mouse_buttons)
        self.exit_button.update(mouse_pos, mouse_buttons)

        if self.play_button.was_clicked():
            fade_out(display.get_surface())
            self.next_scene = Levels()  # спокойно работает

        if self.exit_button.was_clicked():
            quit()

    def draw(self, surface):
        surface.blit(bg, (0, self.bg_y))
        surface.blit(bg, (0, self.bg_y + 900))
        surface.blit(board_name, (75, 95))
        surface.blit(game_name, (150, 160))
        self.play_button.draw(surface)
        self.exit_button.draw(surface)

class Levels:
    def __init__(self):
        self.next_scene = self
        self.font = font.SysFont(None, 60)

        self.levelone_button = Button(225, 460, [levelone_button_none, levelone_button_hovered, levelone_button_pressed])
        self.leveltwo_button = Button(375, 460, [leveltwo_button_none, leveltwo_button_hovered, leveltwo_button_pressed])
        self.back_button = Button(45, 45, [back_none, back_hovered, back_pressed])
        self.bg_y = 0

    def handle_event(self, event):
        pass

    def update(self):
        self.bg_y -= 3
        if self.bg_y <= -900:
            self.bg_y = 0

        mouse_pos = mouse.get_pos()
        mouse_buttons = mouse.get_pressed()

        self.levelone_button.update(mouse_pos, mouse_buttons)
        self.leveltwo_button.update(mouse_pos, mouse_buttons)
        self.back_button.update(mouse_pos, mouse_buttons)

        if self.levelone_button.was_clicked():
            fade_out(display.get_surface())
            # self.next_scene = Level_one()
        if self.leveltwo_button.was_clicked():
            fade_out(display.get_surface())
            # self.next_scene = Level_two()
        if self.back_button.was_clicked():
            fade_out(display.get_surface())
            self.next_scene = Menu()  # теперь это работает без цикла

    def draw(self, surface):
        surface.blit(bg, (0, self.bg_y))
        surface.blit(bg, (0, self.bg_y + 900))
        surface.blit(board_lvl, (115, 155))
        surface.blit(lvl_name, (154, 205))
        self.levelone_button.draw(surface)
        self.leveltwo_button.draw(surface)
        self.back_button.draw(surface)