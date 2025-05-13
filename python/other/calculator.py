import time, math

print("Привет! Я калькулятор который может много что делать)")
time.sleep(2)
Error = "Ошибка, неизвестный символ операции:"
time.sleep(1)

while True:
    try:
        f_num = float(input("Введите первое число: "))
        oper = input("Введите операцию (+ - * / ** _): ")
        s_num = float(input("Введите второе число: "))
        if oper == "+":
            print("Результат:", f_num + s_num)
        elif oper == "-":
            print("Результат:", f_num - s_num)
        elif oper == "*":
            print("Результат:", f_num * s_num)
        elif oper == "/":
            print("Результат:", f_num / s_num)
        elif oper == "**":
            print("Результат:", f_num ** s_num)
        elif oper == "_":
            print("Результат:", math.sqrt(f_num))
            print("Результат:", math.sqrt(s_num))
        else:
            print(Error, oper)
    except ZeroDivisionError:
        print("Деление на ноль невозможна!")
    except ValueError:
        print("Вы ввели что-то не то...")

# elif choice == 2:
#     print("Возможности: Вычисление найменьшого(-)/найбольшего числа(+)")
#     nums = float(input("Введите несколько чисел: "))
#     oper = input("Введите что вы хотите с ними сделать: ")
#     if oper == "+":
#         print(max(nums))
#     elif oper == "-":
#         print(min(nums))