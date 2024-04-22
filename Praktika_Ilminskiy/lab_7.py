#Задание 1
for i in range(1,10):
    for j in range(1,10):
        print("%4d" % (i*j), end='')
    print()

#Задание 2
#Вариант 5
N = 3   
M = 6   
for i in range(N): 
    for j in range(M): 
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0): 
            print("+", end=" ") 
        else: 
            print("-", end=" ") 
    print()

#Вариант 1
for i in range(1, 6): 
    for j in range(i): 
        print(i, end=" ")  
    print()

#Вариант 7
def draw_numbers(rows):
    for i in range(1, rows + 1):
        row = (str(rows) + ' ') * i
        print(row)
draw_numbers(5)

#Задание 3
import random
for i in range(10):
    ch = random.randint(-10, 10)
    if ch == 0:
        print("Обнаружен ноль. Прерывание цикла.")
        break
    elif ch < 0:
        print(f"Отрицательное число ({ch}). Пропуск итерации.")
        continue
    kv_kor = ch**0.5
    print(f"Квадратный корень числа {ch} равен {kv_kor}")