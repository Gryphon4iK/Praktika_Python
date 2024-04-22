#Задание 1
import random
num_grades = int(input("Введите количество оценок: "))
grades = []
for i in range(num_grades):
    grade = round(random.uniform(2,5),1)
    grades.append(grade)
print("Введенные оценки:", grades)
average_grade = sum(grades) / len(grades)
print("Средняя оценка за урок:", average_grade)

#Задание 2
#Вариант 1
import random
count = 0
A = [random.randint(-10,10) for x in range(20)]
print("Сгенерированный список: ",A)
count = sum(1 for x in A if x < 0)
print("Количество отрицательных чисел: ",count)

#Вариант 2
import random
sum_pol = 0
B = [random.randint(-10,10) for x in range(20)]
print("Сгенерированный список: ",B)
for x in B:
    if x > 0:
        sum_pol += x
print("Сумма положительных чисел: ",sum_pol)

#Вариант3
import random
sequence = [random.randint(1, 50) for _ in range(16)]
even_index = [sequence[i] for i in range(0, len(sequence), 2)]
print("Сгенерированная последовательность:", sequence)
print("Список из значений под четными номерами:", even_index)

#Задание 3
#Вариант 1
import random
a = [random.randint(1,30) for x in range(20)]
print("Исходный список: ",a)
max_index = a.index(max(a))
a[0], a[max_index] = a[max_index], a[0]
print("Измененный список: ",a)

#Вариант 3
import random
b = [random.uniform(1,30) for x in range(15)]
print("Исходный список: ",b)
max_index = b.index(max(b))
b[-1], b[max_index] = b[max_index], b[-1]
print("Измененный список: ",b)

#Вариант 5
import random
c = [random.uniform(1,15) for x in range(10)]
print("Изначальный вариант списка: ", c)
c.sort(reverse=True)
print("Список в порядке убывания: ",c)
