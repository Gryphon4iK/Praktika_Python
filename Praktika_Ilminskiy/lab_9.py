#Задание 1
first_str = input("Введите первую строку: ") 
second_str = input("Введите вторую строку: ") 
if first_str[-1] == second_str[0]: 
    print("ВЕРНО") 
else: 
    print("НЕВЕРНО")

#Задание 2
#Вариант 3
str = input("Введите строку: ") 
result = "" 
for simvol in str: 
    result += simvol * 2 
print("Результат:", result) 

#Вариант 8
name = input("Введите имя файла: ") 
part_name = name.split(".") 
extension = part_name[-1] 
print("Расширение файла:", extension)

#Вариант 9
stroka = input("Введите строку: ")
clear = stroka.replace(" ", "")
if clear == clear[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")