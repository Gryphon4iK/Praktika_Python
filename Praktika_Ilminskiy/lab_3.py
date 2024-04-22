#Задание 1
a = int(input("1-е целое число: "))
b = int(input("2-е целое число: "))
if (a%b == 0):
    print("Первое число нацело делится на второе")
else:
    print("Перво числе нацело НЕ делится на второе")

#Задание 2
#Вариант 1
k = int(input("k = "))
l = int(input("l = "))
j = int(input("j = "))
if (k > 0):
   k = k**2
   print(k)
else:
    k = k**4
    print(k)
if (l > 0):
    l = l**2
    print(l)
else:
   l = l**4
   print(l)
if (j > 0):
   j = j**2
   print(j)
else:
   j = j**4
   print(j)

#Вариант 2
s = int(input("s = "))
d = int(input("d = "))
if (s > d):
    s = s/5
    print (s, d)
else:
   print(s, d)

#Вариант 3
q = int(input("q = "))
w = int(input("w = "))
e = int(input("e = "))
count = 0
if (q < 0):
    count += 1
if (w < 0):
    count += 1
if (e < 0):
    count += 1
print(count)
