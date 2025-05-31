# Цей модуль містить об'єкти гри, зокрема для рівнів
# Гравець - ваш корабель, який слухає натискання клавіш
# Вороги - є різні типи ворогів: розвідники, бомбардувальники, боси.
# Снаряди - як ваші, так і ворожі
# Вибухи - красиві анімації, коли щось підривається
# Анімацію вибухів я зробив за допомогою швидких змін картинок, які в кінці виглядають як одна ціла анімація
from pygame import *
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT # Убедись, что SCREEN_WIDTH и SCREEN_HEIGHT импортируются правильно


class Projectile(sprite.Sprite):
    def __init__(self, x, y, image, speed, owner_type): # Добавляем speed и owner_type
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.owner_type = owner_type # 'player', 'enemy', 'boss' (или просто 'player'/'enemy')

    def update(self):
        if self.owner_type == "player":
            self.rect.y -= self.speed # Пуля игрока летит вверх
            if self.rect.bottom < 0:
                self.kill()
        else: # Для врагов и боссов (и других вражеских снарядов)
            self.rect.y += self.speed # Пули врагов летят вниз
            if self.rect.top > SCREEN_HEIGHT:
                self.kill()

class Explosion(sprite.Sprite):
    def __init__(self, x, y, frames):
        super().__init__()
        self.frames = frames # Список поверхностей для анимации
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_speed = 4 # Скорость смены кадров (чем меньше, тем быстрее)
        self.frame_counter = 0

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.image = self.frames[self.current_frame]
            else:
                self.kill() # Завершить анимацию и удалить спрайт

# Класс Игрока
class Player(sprite.Sprite):
    def __init__(self, player_img, projectile_img, explosion_frames): # Добавил explosion_frames
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.speed = 5
        self.hp = 100
        self.is_dead = False # Флаг состояния игрока
        self.explosion_started = False # Флаг для однократного запуска взрыва

        self.projectiles_group = sprite.Group()
        self.projectile_img = projectile_img
        self.projectile_speed = 10 # Скорость пуль игрока

        self.explosion_frames = explosion_frames # Кадры для анимации взрыва игрока


    def handle_keys(self, keys):
        if keys[K_w]: self.rect.y -= self.speed
        if keys[K_s]: self.rect.y += self.speed
        if keys[K_a]: self.rect.x -= self.speed
        if keys[K_d]: self.rect.x += self.speed

        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(SCREEN_WIDTH, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(SCREEN_HEIGHT, self.rect.bottom)

    def take_damage(self, amount):
        if not self.is_dead: # Урон наносится только если игрок жив
            self.hp -= amount
            if self.hp <= 0:
                self.hp = 0
                self.is_dead = True # Устанавливаем флаг смерти
                print("Игрок мертв!")

    def shoot(self):
        # Создаем пулю, передавая ей скорость и тип владельца
        projectile = Projectile(self.rect.centerx, self.rect.top, self.projectile_img, self.projectile_speed, "player")
        self.projectiles_group.add(projectile)

    def update(self):
        if not self.is_dead: # Обновляем игрока только если он жив
            self.projectiles_group.update()
        else:
            # Если игрок мертв, его спрайт исчезает, но могут быть анимации взрыва
            pass # Основная логика взрыва теперь в BaseLevel

# Класс Врага
class Enemy(sprite.Sprite):
    def __init__(self, x, y, image, projectile_img, explosion_frames): # Добавил explosion_frames
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.randint(1, 3)
        self.hp = random.randint(50, 70)
        self.projectile_img = projectile_img
        self.projectiles_group = sprite.Group()
        self.projectile_speed = 5 # Скорость пуль врага

        self.direction_timer = 0
        self.direction_change_interval = random.randint(45, 120)
        self.set_random_direction()

        self.shoot_timer = 0
        self.shoot_interval = random.randint(60, 180)

        self.explosion_frames = explosion_frames # Кадры для анимации взрыва врага

    def set_random_direction(self):
        self.dx = random.choice([-1, 0, 1])
        self.dy = random.choice([-1, 0, 1])
        if self.dx == 0 and self.dy == 0:
            self.set_random_direction() # Повторяем, если выбрано (0,0)

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            return True # Возвращаем True, если враг уничтожен
        return False # Возвращаем False, если враг не уничтожен

    def shoot(self):
        # Создаем пулю, передавая ей скорость и тип владельца
        projectile = Projectile(self.rect.centerx, self.rect.bottom, self.projectile_img, self.projectile_speed, "enemy")
        self.projectiles_group.add(projectile)

    def update(self):
        self.direction_timer += 1
        if self.direction_timer >= self.direction_change_interval:
            self.set_random_direction()
            self.direction_timer = 0
            self.direction_change_interval = random.randint(45, 120)

        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

        # Ограничение по экрану и "отскок"
        if self.rect.left < 0:
            self.rect.left = 0
            self.dx = abs(self.dx)
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.dx = -abs(self.dx)

        if self.rect.top < 0:
            self.rect.top = 0
            self.dy = abs(self.dy)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.dy = -abs(self.dy)

        # Логика стрельбы врага
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_interval:
            self.shoot()
            self.shoot_timer = 0
            self.shoot_interval = random.randint(60, 180)

        self.projectiles_group.update()

class Boss(Enemy): # Наследуем от Enemy, чтобы использовать его базовую логику
    def __init__(self, x, y, image, projectile_img, explosion_frames):
        # Для босса можно задать фиксированные, более высокие HP и скорость
        super().__init__(x, y, image, projectile_img, explosion_frames)
        self.hp = 850 # Гораздо больше HP для босса
        self.speed = 1.5 # Босс движется медленнее
        self.projectile_speed = 6.5 # Пули босса могут быть быстрее
        self.shoot_interval = 30 # Босс стреляет чаще (0.5 секунды)

        # Дополнительные поля для босса (например, фазы, специальные атаки)
        self.phase = 1
        self.target_y = SCREEN_HEIGHT * 0.2 # Целевая Y-координата для босса
        self.moving_to_position = True

    def update(self):
        # Логика движения босса
        if self.moving_to_position:
            if self.rect.y < self.target_y:
                self.rect.y += self.speed
            else:
                self.rect.y = self.target_y
                self.moving_to_position = False # Босс достиг своей позиции

        # Если босс достиг позиции, используем его обычную логику движения
        if not self.moving_to_position:
            # Обычная логика движения Enemy
            self.direction_timer += 1
            if self.direction_timer >= self.direction_change_interval:
                self.set_random_direction()
                self.direction_timer = 0
                self.direction_change_interval = random.randint(45, 120)

            self.rect.x += self.dx * self.speed
            # Босс не движется по Y после достижения target_y, только по X
            # self.rect.y += self.dy * self.speed # Закомментировать, если босс стоит на месте по Y

            # Ограничение по экрану
            if self.rect.left < 0:
                self.rect.left = 0
                self.dx = abs(self.dx)
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
                self.dx = -abs(self.dx)

        # Логика стрельбы босса
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_interval:
            self.shoot()
            self.shoot_timer = 0
            # Босс может стрелять чаще, или иметь несколько точек стрельбы
            self.shoot_interval = random.randint(20, 60) # Увеличиваем частоту стрельбы

        self.projectiles_group.update()

    def shoot(self):
        # Босс может стрелять несколькими пулями или в разные стороны
        projectile = Projectile(self.rect.centerx, self.rect.bottom, self.projectile_img, self.projectile_speed, "boss")
        self.projectiles_group.add(projectile)