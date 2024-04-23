#Задание 1
import math
def S(r):
    return math.pi * r**2
def l(r):
    return 2 * math.pi * r
def krug():
    radius = float(input("Введите радиус окружности: "))
    area = S(radius)
    lenght = l(radius)
    print(f"Площадь круга: {area}, Длина окружности: {lenght}")
krug()

#Задание 2
#Вариант 1
def filter_numbers(input_list):
    output_list = [num for num in input_list if num % 2 == 0 and num > 10]
    return output_list
input_list = [int(x) for x in input("Введите список чисел через пробел: ").split()]
result = filter_numbers(input_list)
print("Результат:",result)

#Варинат 3
def print_average(input_list):
    if len(input_list) == 0:
        print(0)
    else:
        average = sum(input_list) / len(input_list)
        print(average)
input_list = [int(x) for x in input("Введите список чисел через пробел: ").split()]
print_average(input_list)

#Вариант 5
def check_triangle_sides(sides):
    a, b, c = sorted(sides)
    if a + b > c:
        print("Это треугольник")
    else:
        print("Это не треугольник")
sides = [float(x) for x in input("Введите длины отрезков через пробел: ").split()]
check_triangle_sides(sides)

#Задание 3
def process_list(list1, a, b, c):
    sum_of_others = 0
    for element in list1:
        if element > a and element < b and element % c == 0:
            print(element)
        else:
            sum_of_others += element
    print("Сумма остальных элементов списка: ", sum_of_others)
list1 = [10, 20, 30, 40, 50, 60]
a = 15
b = 45
c = 10
process_list(list1, a, b, c)