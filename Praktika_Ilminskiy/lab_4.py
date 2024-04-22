#Задание 1
a = float(input("Введите дробное число: "))
if (a<0):
    print("-")
elif(a == 0):
    print("0")
else:
    print("+")

#Задание 2
#Вариант 2
import math
a = 1.5
x = float(input("x = "))
if (x < 1.3):
    y = math.pi*x**2 - 7/x**2
elif (x == 1.3):
    y = a*x**3 + 7*math.sqrt(x)
else:
    y = math.log10(x + 7*math.sqrt(x))
print("y = ",y)

#Вариант 3
import math
a = 2.8
b = -0.3
c = 4
x = float(input("x = "))
if (x < 1.2):
 y = a*x**2 + b*x + c 
elif (x == 1.2):
    y = a/x + math.sqrt(x**2 + 1) 
else:
    y = (a + b*x)/math.sqrt(x**2 + 1)
print("y = ",y)

#Вариант 4
import math
a = 1.65
x = float(input("x = "))
if (x < 1.4):
    y = math.pi*x**2 - 7/x**2
elif (x == 1.4):
    y = a*x**3 + 7*math.sqrt(x)
else:
    y = math.log10(x) + 7*math.sqrt(x + a)
print("y = ",y)
