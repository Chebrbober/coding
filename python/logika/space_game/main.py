from settings import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from scenes import Menu, LevelOne, LevelTwo, GameOverScene, WinScene
import pygame
from sys import exit
from assets import menu_music, levelone_music, leveltwo_music, win_music, gameover_music
from fade import draw_fade_overlay # Убедитесь, что эта функция доступна

# Initialization
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Rush")
clock = pygame.time.Clock()

current_scene = Menu()

try:
    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1) # -1 для бесконечного повтора
    current_playing_music_path = menu_music # Отслеживаем, какая музыка сейчас играет
except pygame.error as e:
    print(f"Ошибка при загрузке начальной музыки меню: {e}")
    current_playing_music_path = None # В случае ошибки, указываем, что музыка не играет


running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        current_scene.handle_event(e)

    current_scene.update()

    if current_scene.next_scene is not current_scene: # Проверяем, есть ли запрос на смену сцены
        next_scene_instance = current_scene.next_scene
        next_music_path = current_scene.next_music_path # Получаем путь к музыке для новой сцены

        current_scene = next_scene_instance # Переключаем сцену
        # Важно: сбросить next_scene в новой сцене, чтобы она не пыталась сразу же перейти куда-то еще
        current_scene.next_scene = current_scene 
        
        # Логика воспроизведения музыки для новой сцены
        if next_music_path: # Убедимся, что путь к музыке не пустой
            # Если текущая музыка отличается от той, которую нужно воспроизвести,
            # или если микшер не занят (т.е. музыка не играет или была остановлена)
            if current_playing_music_path != next_music_path or not pygame.mixer.music.get_busy():
                try:
                    pygame.mixer.music.load(next_music_path)
                    # Определяем режим воспроизведения (один раз или зацикленный)
                    if next_music_path == gameover_music: # Музыка Game Over играет один раз
                        pygame.mixer.music.play(0) 
                    else: # Остальная музыка (меню, уровни, победа) зациклена
                        pygame.mixer.music.play(-1) 
                    current_playing_music_path = next_music_path # Обновляем отслеживаемый трек
                except pygame.error as e:
                    print(f"Ошибка загрузки музыки {next_music_path}: {e}. Пропуск воспроизведения музыки.")
                    current_playing_music_path = None # В случае ошибки, сбросим трек
            elif not pygame.mixer.music.get_busy() and current_playing_music_path == next_music_path:
                # Если нужная музыка та же, что и раньше, но была остановлена (например, fadeout),
                # и микшер не занят, просто возобновляем воспроизведение
                if current_playing_music_path is not None: # Убедимся, что трек был определен
                    try:
                        pygame.mixer.music.load(current_playing_music_path) # Перезагружаем на всякий случай, если что-то пошло не так
                        pygame.mixer.music.play(-1)
                    except pygame.error as e:
                        print(f"Ошибка возобновления музыки {current_playing_music_path}: {e}. Пропуск возобновления.")
                        current_playing_music_path = None

        else: # Если next_music_path равен None, значит, для этой сцены не предусмотрена музыка
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
            current_playing_music_path = None # Сбрасываем трек

    # --- Отрисовка сцены ---
    screen.fill((0, 0, 0)) # Очищаем экран черным цветом перед отрисовкой сцены
    current_scene.draw(screen)
    
    # Отрисовка затемнения/проявления поверх всего
    # Убедитесь, что `fade_alpha` и `is_fading` доступны в `current_scene`
    if current_scene.is_fading or current_scene.fade_alpha > 0:
        draw_fade_overlay(screen, current_scene.fade_alpha)

    pygame.display.flip() 
    clock.tick(FPS)

quit()