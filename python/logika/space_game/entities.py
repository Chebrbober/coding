from pygame import *
from random import *
from settings import SCREEN_WIDTH, SCREEN_HEIGHT # Убедись, что SCREEN_WIDTH и SCREEN_HEIGHT импортируются правильно

# Класс Игрока
class Player(sprite.Sprite):
    def __init__(self, player_img, projectile_img):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.speed = 5
        self.hp = 100 # Здоровье игрока
        self.projectiles_group = sprite.Group() # Группа для пуль игрока
        self.projectile_img = projectile_img # Картинка для пуль игрока

    def handle_keys(self, keys):
        if keys[K_w]: self.rect.y -= self.speed
        if keys[K_s]: self.rect.y += self.speed
        if keys[K_a]: self.rect.x -= self.speed
        if keys[K_d]: self.rect.x += self.speed

        # Ограничение игрока по экрану
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(SCREEN_WIDTH, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(SCREEN_HEIGHT, self.rect.bottom)

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            # TODO: Добавить логику смерти игрока (например, конец игры, рестарт уровня)
            print("Игрок мертв!")

    def shoot(self):
        projectile = PlayerProjectile(self.rect.centerx, self.rect.top, self.projectile_img)
        self.projectiles_group.add(projectile)
        # mixer.Sound(shoot_sound).play() # Если есть звук выстрела

    def update(self):
        # Обновляем пули игрока
        self.projectiles_group.update()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # Отрисовка пуль игрока
        self.projectiles_group.draw(surface)
        # TODO: Отрисовка полоски здоровья игрока (необязательно, но полезно)

# Класс Врага
class Enemy(sprite.Sprite):
    def __init__(self, x, y, image, projectile_img):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.randint(1, 3)
        self.hp = random.randint(40, 60) # Здоровье врага
        self.projectile_img = projectile_img # Картинка для пуль врага
        self.projectiles_group = sprite.Group() # Группа для пуль врага

        self.direction_timer = 0
        self.direction_change_interval = random.randint(45, 120)
        self.set_random_direction()

        self.shoot_timer = 0
        self.shoot_interval = random.randint(60, 180) # Враг стреляет каждые 1-3 секунды

    def set_random_direction(self):
        self.dx = random.choice([-1, 0, 1])
        self.dy = random.choice([-1, 0, 1])
        if self.dx == 0 and self.dy == 0:
            self.set_random_direction()

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.kill() # Удаляет врага из всех групп, в которых он состоит

    def shoot(self):
        projectile = EnemyProjectile(self.rect.centerx, self.rect.bottom, self.projectile_img)
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
            self.set_random_direction()
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.dx = -abs(self.dx)
            self.set_random_direction()

        if self.rect.top < 0:
            self.rect.top = 0
            self.dy = abs(self.dy)
            self.set_random_direction()
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.dy = -abs(self.dy)
            self.set_random_direction()

        # Логика стрельбы врага
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_interval:
            self.shoot()
            self.shoot_timer = 0
            self.shoot_interval = random.randint(60, 180)

        # Обновляем пули врага
        self.projectiles_group.update()

# Класс пули игрока
class PlayerProjectile(sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed # Пуля летит вверх
        if self.rect.bottom < 0:
            self.kill()

# Класс пули врага
class EnemyProjectile(sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7 # Пуля врага может быть медленнее или быстрее

    def update(self):
        self.rect.y += self.speed # Пуля летит вниз
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()