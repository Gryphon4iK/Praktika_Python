#Задание 1
def create_sentence(indexes, words_string):
    words_list = words_string.split()
    new_sentence = ' '.join(words_list[i-1] for i in indexes)
    return new_sentence.capitalize()
indexes = [2, 4, 1, 3]
words_string = "это предложение из примера" 

new_sentence = create_sentence(indexes, words_string)
print(new_sentence)

#Задание 2
# Вариант 1
str = input("Введите строку: ")
words = str.upper().split()
UpWord = []
for word in words:
    NewWord = "-".join(char for char in word)
    UpWord.append(NewWord)
res = " ".join(UpWord)
print(res)

#Вариант 3
nab_ch = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split()))
beg, end = map(int, input("Введите два целых числа, начало и конец интервала для суммирования: ").split())
sum_ch= sum(nab_ch[beg:end+1])
print(f"Сумма чисел от {beg} до {end}: {sum_ch}")

#Вариант 5
nab_chis = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split()))
begin, ending = map(int, input("Введите два целых числа, начало и конец интервала для суммирования: ").split())
sum_kv = sum(x**2 for x in nab_chis[begin:ending+1])
print(f"Сумма квадратов чисел от {begin} до {ending}: {sum_kv}")