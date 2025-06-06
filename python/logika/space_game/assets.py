# У цьому модулі зберігаються всі картинки, такі як: кораблі, кнопки, вибухи, фони.
# Програма завантажує їх і змінює розміри, щоб вони підходили для гри.
from pygame import *

def load_image(path, scale=None):
    img = image.load(path)
    if scale:
        img = transform.scale(img, scale)
    return img

# Меню
play_button_none = load_image("images/menu/play_0.png", (217, 105))
play_button_hovered = load_image("images/menu/play_1.png", (217, 105))
play_button_pressed = load_image("images/menu/play_2.png", (217, 105))

exit_button_none = load_image("images/menu/exit_0.png", (72, 72))
exit_button_hovered = load_image("images/menu/exit_1.png", (72, 72))
exit_button_pressed = load_image("images/menu/exit_2.png", (72, 72))

levelone_button_none = load_image("images/menu/lvlone_0.png", (75, 75))
levelone_button_hovered = load_image("images/menu/lvlone_1.png", (75, 75))
levelone_button_pressed = load_image("images/menu/lvlone_2.png", (75, 75))

leveltwo_button_none = load_image("images/menu/lvltwo_0.png", (75, 75))
leveltwo_button_hovered = load_image("images/menu/lvltwo_1.png", (75, 75))
leveltwo_button_pressed = load_image("images/menu/lvltwo_2.png", (75, 75))

back_none = load_image("images/menu/back_0.png", (72, 72))
back_hovered = load_image("images/menu/back_1.png", (72, 72))
back_pressed = load_image("images/menu/back_2.png", (72, 72))

bg = load_image("images/bg.png", (600, 900))
board_name = load_image("images/menu/board.png", (450, 350))
board_lvl = load_image("images/menu/board_lvl.png", (375, 200))
game_name = load_image("images/menu/game_name.png", (300, 225))
lvl_name = load_image("images/menu/lvl_name.png", (300, 100))

menu_music = "audio/menu_theme.mp3"

# Гра
laser_blast = "audio/laser_blast.wav"
player_default = load_image("images/game/player.png", (112, 105))
enemy_scout_default = load_image("images/game/enemy_scout.png", (96, 90))
enemy_bomber_default = load_image("images/game/enemy_bomber.png", (96, 90))
boss_default = load_image("images/game/boss.png", (216, 291))
enemy_projectile = load_image("images/game/projectiles/enemy_projectile.png", (10, 15))
boss_projectile = load_image("images/game/projectiles/boss_projectile.png", (50, 25))
player_projectile = load_image("images/game/projectiles/player_projectile.png", (10, 15))

restart_button_none = load_image("images/menu/restart_0.png", (234, 90))
restart_button_hovered = load_image("images/menu/restart_1.png", (234, 90))
restart_button_pressed = load_image("images/menu/restart_2.png", (234, 90))

menu_button_none = load_image("images/menu/menu_0.png", (186, 90))
menu_button_hovered = load_image("images/menu/menu_1.png", (186, 90))
menu_button_pressed = load_image("images/menu/menu_2.png", (186, 90))

board_for_end = load_image("images/menu/board_1.png", (565, 325))
victory = load_image("images/menu/victory.png", (300, 120))
game_over = load_image("images/menu/game_over.png", (325, 120))
board_hp = load_image("images/menu/board.png", (125, 70))

player_explosion = []
for i in range(13): # Измени 5 на количество твоих кадров
    player_explosion.append(load_image(f"images/game/player_explosion/explosion_{i}.png", (112, 105)))

enemy_scout_explosion = []
for i in range(9): 
    enemy_scout_explosion.append(load_image(f"images/game/enemy_explosion/scout_explosions/explosion_{i}.png", (96, 90))) # Размер врага

enemy_bomber_explosion = []
for i in range(9): 
    enemy_bomber_explosion.append(load_image(f"images/game/enemy_explosion/bomber_explosions/explosion_{i}.png", (96, 90))) # Размер врага

boss_explosion = []
for i in range(11):
    boss_explosion.append(load_image(f"images/game/enemy_explosion/boss_explosions/explosion_{i}.png", (216, 291)))

levelone_music = "audio/levelone_music.mp3"
leveltwo_music = "audio/leveltwo_music.mp3"
win_music = "audio/win_music.mp3"
gameover_music = "audio/gameover_music.wav"