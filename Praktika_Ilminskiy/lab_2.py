#Задание 1
print('Как Вас зовут?')
a = input()
print('Добрый день!',a)
print('Укажите название техникума.')
b = input()
print('Укажите номер вашей группы.')
c = input()
print('Вы обучаетесь в образовательной организации ',b,' в группе ',c)
print('Какой язык программирования вы начинаете изучать?')
d = input()
print(a, 'желаем Вам успешного обучения программированию на языке',d)

#Задание 2
#Вариант 1
import sys
def main():
    x = float(input("x = "))
    y = float(input("y = "))
    B = x**(x/y) - (y/x)**(1/3)
    sys.stdout.write("x=%f, y=%f, B=%f" % (x, y, B))
    sys.stdout.flush()
if __name__ == "__main__":
    main()    

#Вариант 2
import math
def main():
    a = float(input('\n'"a = "))
    b = float(input("b = "))
    t = float(input("t = "))
    X = b*math.sin((a*t**2*math.cos(2*t)))-1
    sys.stdout.write("a=%f, b=%f, t=%f, X=%f" % (a, b, t, X))
    sys.stdout.flush()
    
if __name__ == "__main__":
    main()
    
#Вариант 3
import math
def main():
    a = float(input('\n'"a = "))
    b = float(input("b = "))
    x = float(input("x = "))
    Y = math.sqrt(x**2 + b) - b**2 * (math.sin(x + a)**3)/x
    sys.stdout.write("a=%f, b=%f, t=%f, X=%f" % (a, b, x, Y))
    sys.stdout.flush()
    sys.exit()
    
if __name__ == "__main__":
    main()
    
