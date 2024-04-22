#Задание 1
import math 
k = int(input("Введите число k:")) 
for num in range(k + 1): 
    sqrt = math.sqrt(num) 
cub = num ** 3 
print(f"Корень числа {num} равен {sqrt}, а куб равен {cub}") 

#Задание 2
#Вариант 1
count = 1
for a in range(3,25,3):
    count *= 2
    print("За ",a,"часов получилось",count,"амеб")

#Вариант 3
x = 10
for day in range (1,8,1):
    x = x + x*0.1
print("Суммарный путь пробежал спортсмен за 1 неделю -",x)

#Вариант 5
x = 40
for day in range(1,11,1):
    x = x + x*0.05
print("В книге",x,"страниц")