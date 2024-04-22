#Задание 1
str = input("Введите строку из слов, разделенных пробелами: ") 
slv = str.split() 
obratka = " ".join(slv[::-1]) 
print("Новая строка (слова в обратном порядке):", obratka)

#Задание 2
#Вариант 1
str = input("Введите строку, заканчивающуюся точкой: ") 
slv = str.split() 
colvo = len(slv) 
print("Количество слов в строке:", colvo)

#Вариант 8
str = input("Введите строку: ") 
new_str = str.replace(" ", ", ") 
print("Новая строка с запятыми:", new_str)

#Вариант 9
stroka = "Ваша строка; с точкой с запятой"
poz = stroka.find(';')
if poz != -1:
    count = poz
    print(f"Количество символов до точки с запятой: {count}")
else:
    print("Точка с запятой не найдена в строке.")