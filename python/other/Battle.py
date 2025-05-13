from time import sleep
from random import randint

class Hero:
    def __init__(self, name, armor, health, power, weapon, info):
        self.name = name
        self.armor = armor
        self.health = health
        self.power = power
        self.weapon = weapon
        self.info = info

    def greeting_hero(self):
        print(f"-> {self.name}"
              f"\nБроня: {self.armor}"
              f"\nЗдоров'я: {self.health}"
              f"\nСила: {self.power}"
              f"\nЗброя: {self.weapon}"
              f"\nОсобливість: {self.info}\n")
        sleep(2)

    def attack(self, enemy):
        attack_value = randint(self.power - 5, self.power + 5)

        if enemy.armor > 0:
            enemy.armor -= attack_value
            if enemy.armor < 0:
                enemy.health += enemy.armor  # Якщо броня пішла в мінус, це зменшує здоров'я
                enemy.armor = 0
                print(f"{enemy.name} зламали броню!")
        else:
            enemy.health -= attack_value

        print(f"{self.name} атакує {enemy.name} з силою {attack_value}. У {enemy.name}а залишилось {enemy.health} HP.")
        sleep(1)

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            variant = input("Вибери варіант хода:")
            if variant == "1":
                self.attack(enemy)
                sleep(0.5)
                enemy.attack(self)
            if variant == "2":
                special_attack(self, enemy)
                sleep(0.5)

            if enemy.health <= 0:
                print(f"{enemy.name} програв битву!")
                break

            if self.health <= 0:
                print(f"{self.name} програв битву!")
                break
            sleep(0.5)


# Створення героїв
paladin = Hero("Паладін", 30, 160, 15, "Золотий меч", "Має щит для захисту свого хозяїна")
ninja = Hero("Ніндзя", 15, 125, 17, "Катана та сюрікени", "Дуже швидкий, може ухилитися від атаки")
wizard = Hero("Чарівник", 7, 105, 25, "Посох", "Може накласти дезорієнтацію та забрати два хода")
boss = Hero("Циклоп", 16, 200, 25, "Лазер", "Стріляє потужним красним лазером")
rascal = Hero("Хуліган", 5, 90, 10, "Кинжал", "Немає особливих навичок")

# Сюжет
print(f"На королівство напали інопланетні чужаки, а з ними іх босс, тож король попросив допомоги у наших героїв\n")
sleep(1)
paladin.greeting_hero()
ninja.greeting_hero()
wizard.greeting_hero()

choice = input("Напишіть ім'я героя, щоб вибрати його: ")

if choice == "Паладін":
    def special_attack(self, enemy):
        self.armor += randint(self.armor + 5, self.armor + 10)
        print(f"{self.name} ставить щит і у нього тепер {self.armor}.")
        enemy.attack(self)
    print("Варіанти ходів цього персонажа:\n"
          "1. Атакувати мечем\n"
          "2. Захиститись щитом\n")

    print(f"{paladin.name} вирушає в похід через ліс.")
    sleep(1)
    print(f"{paladin.name} зустрів {rascal.name}а.")
    rascal.greeting_hero()
    fight_choice = input("Битися з ним? (так/ні)")

    if fight_choice.lower() == "так":
        print("Починається битва!")
        paladin.fight(rascal)

        if paladin.health > 0:
            paladin.health = 160
            paladin.power = int(paladin.power * 1.7)
            paladin.armor = 30
            print(f"{paladin.name} відновив сили! Нові параметри: HP: {paladin.health}, броня: {paladin.armor}, сила: {paladin.power}")

            sleep(2)
            print(f"{paladin.name} добирається до лігва {boss.name}а.")
            boss.greeting_hero()
            sleep(1)
            print(f"Починається битва з {boss.name}ом!")
            sleep(1)
            paladin.fight(boss)

            if paladin.health > 0:
                print(f"{paladin.name} переміг {boss.name}а!")
            else:
                print(f"{paladin.name} програв...")

    else:
        print(f"{rascal.name} підкрався ззаду і вбив {paladin.name}а...")

elif choice == "Ніндзя":
    def special_attack(self, enemy):
        chance = randint(1, 10)
        if chance > 4:
            print(f"{self.name} ухилився від атаки.")
            self.attack(enemy)
        else:
            print(f"{self.name} не зміг ухилитися від атаки")
            enemy.attack(self)
    print("Варіанти ходів цього персонажа:\n"
          "1. Взмахнути катаною\n"
          "2. Ухилитися від атаки\n")

    print(f"{ninja.name} вирушає в похід через ліс.")
    sleep(1)
    print(f"{ninja.name} зустрів {rascal.name}а.")
    rascal.greeting_hero()
    fight_choice = input("Битися з ним? (так/ні)")

    if fight_choice.lower() == "так":
        print("Починається битва!")
        ninja.fight(rascal)

        if ninja.health > 0:
            ninja.health = 125
            ninja.power = int(ninja.power * 1.5)
            ninja.armor = 15
            print(f"{ninja.name} відновив сили! Нові параметри: HP: {ninja.health}, броня: {ninja.armor}, сила: {ninja.power}")


            sleep(2)
            print(f"{ninja.name} добирається до лігва {boss.name}а.")
            boss.greeting_hero()
            sleep(1)
            print(f"Починається битва з {boss.name}ом!")
            sleep(1)
            ninja.fight(boss)

            if ninja.health > 0:
                print(f"{ninja.name} переміг {boss.name}а!")
            else:
                print(f"{ninja.name} програв...")

    else:
        print(f"{rascal.name} підкрався ззаду і вбив {ninja.name}а...")

elif choice == "Чарівник":
    def special_attack(self, enemy):
        chance = randint(1, 10)
        if chance > 5:
            print(f"{enemy.name} був дезоріентований і не може атакувати!")
            self.attack(enemy)
            self.attack(enemy)
        if chance < 5:
            print("На {enemy.name}а не подіяла дезорієнтація!")
            enemy.attack(self)
    print("Варіанти ходів цього персонажа:\n"
          "1. Атакувати вогняними кулями посоха\n"
          "2. Накласти дезорієнтацію\n")

    print(f"{wizard.name} вирушає в похід через ліс.")
    sleep(1)
    print(f"{ninja.name} зустрів {rascal.name}а.")
    rascal.greeting_hero()
    fight_choice = input("Битися з ним? (так/ні)")

    if fight_choice.lower() == "так":
        print("Починається битва!")
        wizard.fight(rascal)

        if wizard.health > 0:
            wizard.health = 105
            wizard.power = int(wizard.power * 1.5)
            wizard.armor = 7
            print(f"{wizard.name} відновив сили! Нові параметри: HP: {wizard.health}, броня: {wizard.armor}, сила: {wizard.power}")

            sleep(2)
            print(f"{wizard.name} добирається до лігва {boss.name}а.")
            boss.greeting_hero()
            sleep(1)
            print(f"Починається битва з {boss.name}ом!")
            sleep(1)
            wizard.fight(boss)

            if wizard.health > 0:
                print(f"{wizard.name} переміг {boss.name}а!")
            else:
                print(f"{wizard.name} програв...")

    else:
        print(f"{rascal.name} підкрався ззаду і вбив {wizard.name}а...")

else:
    print("Ви ввели неправильне ім'я героя!")
