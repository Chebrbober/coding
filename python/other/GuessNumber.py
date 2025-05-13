from random import *

print('Ласкаво просимо до гри — "Вгадай число"! \nПравила гри прості. Ви повинні вгадати число яке я загадав \nвід 1 до 10. Ну що ж, почнемо!')
num = randint(1, 10)
attempts = 1
ans = int(input('Все! Спробуй вгадати!'))
while ans > num:
    attempts += 1
    print("Загадане число менше.")
    ans = int(input('Так спробуй ще раз!'))
while ans < num:
    attempts += 1
    print("Загадане число більше.")
    ans = int(input('Так спробуй ще раз!'))
else:
    print("Ви вгадали за",attempts,"спроб!","Це було —",num)