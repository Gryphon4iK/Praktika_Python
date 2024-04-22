print("Привет, Python!")
print("Приятно познакомится.")

a = input("Введите название фильма: ")
b = input("Введите название кинотеатра: ")
c = input("Введите время начала фильма: ")
print("Билет на ",a, " в ",b, " на ", c," забронирован.")

def sum(x, y, z):
    return x + y + z
k = int(input("Введите первое число: "))
g = int(input("Введите второе число: "))
h = int(input("Введите третье число: "))
print("Сумма чисел = ", sum(k,g,h))

def proiz(x, y, z):
    return x * y * z
k = int(input("Введите первое число: "))
g = int(input("Введите второе число: "))
h = int(input("Введите третье число: "))
print("Произведение чисел = ", proiz(k,g,h))

def srznach(x, y, z):
    return (x + y + z)/3
k = int(input("Введите первое число: "))
g = int(input("Введите второе число: "))
h = int(input("Введите третье число: "))
print("Среднее арифметическое чисел = ", srznach(k,g,h))

from random import randint
n = randint(100,1000)
print('Получено число',n)
print('Его цифры {},{},{}'.format(n//100,n//10%10,n%10))

rub = int(input())
kop = int(input())
pie = int(input())
price = rub * 100 + kop
summa = price * pie
price_rub = summa // 100
price_kop = summa % 100
print(price_rub, price_kop)