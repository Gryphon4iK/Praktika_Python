#Задание 1
import random
M = int(input("Введите количество строк в матрице: "))
matrix = [[random.randint(1,20) for x in range(4)] for y in range(M)]
print("Исходная матрица:")
for row in matrix:
    print(*row)
for i in range(len(matrix)): 
    if i % 2 == 0: 
        print('\n',*matrix[i])
    else: 
        print('\n',*matrix[i][::-1])

#Задание 2
#Вариант 2
import random
M = int(input("Введите количество строк в матрице: "))
N = int(input("Введите количество столбцов в матрице: "))
matrica = [[random.randint(1,50) for x in range(N)] for y in range(M)]
print("Исходная матрица:")
for r in matrica:
    print(*r)
print("Сумма элементов  каждой строки:")
for r in matrica:
    r_sum = sum(r)
    print(r_sum)

#Вариант 4
import random
A = int(input("Введите размерность квадратной матрицы: "))
mat = [[random.randint(-10,10) for x in range(A)]for y in range(A)]
print("Исходная матрица:")
for r in mat:
  print(*r)
otr_sum = 0
for i in range(A):
  for j in range(i):
    if mat[i][j] < 0:
      otr_sum += mat[i][j]
print("Сумма отрицательных элементов над главной диагональю",otr_sum)

#Вариант 6
import random
B = int(input("Введите размерность квадратной матрицы: "))
mat = [[random.randint(-10,10) for x in range(B)]for y in range(B)]
print("Исходная матрица:")
for r in mat:
  print(*r)
otr_sum = 0
for i in range(B):
  for j in range(B-i, B):
    if mat[i][j] < 0:
      otr_sum += mat[i][j]
print("Сумма отрицательных элементов под дополнительной диагональю",otr_sum)