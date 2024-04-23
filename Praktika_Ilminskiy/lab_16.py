#Задание 1
import math
def calculate_expression(x, y, z):
    first_term = math.sqrt(x**2 + z**2 + math.cos(x * z)**3)
    second_term = math.sqrt(y**2 + x**2 + math.cos(y * x)**3)
    third_term = math.sqrt(z**2 + y**2 + math.cos(z * y)**3)
    result = (first_term + second_term) / third_term
    return result
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))
result = calculate_expression(x, y, z)
print("Значение выражения L =", result)

#Задание 2 Проверить на работоспособность
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)
# def calculate_expression(n, m):
#     C = factorial(n) // (factorial(m) * factorial(n - m))
#     return C
# n = int(input("Введите значение n: "))
# m = int(input("Введите значение m: "))
# result = calculate_expression(n, m)
# print("Значение выражения C =", result)

#Задание 3
#Вариант 2
def sum_of_negative_cubes(numbers):
    result = 0
    for number in numbers:
        if number < 0:
            result += number ** 3
    return result
numbers = [3, -2, 5, -7, 10, -4]
print("Сумма кубов отрицательных чисел в списке:", sum_of_negative_cubes(numbers))

#Вариант 4
numbers = [34, 51, 68, 85, 102, 119, 136, 153]
div_by_17 = [num for num in numbers if num % 17 == 0]

print(div_by_17)

#Вариант 6
numbers = [22, 33, 44, 55, 66, 77, 88, 99]
odd_and_div_by_11 = [num for num in numbers if num % 2 != 0 and num % 11 == 0]
print(odd_and_div_by_11)