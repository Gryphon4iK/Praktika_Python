#Задание 1
import random
n = int(input("Введите количество номеров телефонов: "))
names = [f"Имя_{i}" for i in range(n)]
phones = [random.randint(1000000000, 9999999999) for x in range(n)]
phone_book = dict(zip(names, phones))
print(phone_book)
query = input("Введите имя для поиска: ")
if query in phone_book:
    print(f"Номер телефон: {phone_book[query]}")
else:
    print("Нет в телефонной книге")

#Задание2
#Вариант 2
a = int(input("Введите количество специальностей: "))
specialties = {}
for x in range(a):
    info = input("Введите название специальности и номера групп через тире и запятую: ").split(" - ")
    name = info[0]
    groups = info[1].split(", ")
    for group in groups:
        specialties[group] = name
    query = input("Введите номер группы: ")
    if query in specialties:
        print(f"Специальность: {specialties[query]}")
    else:
        print("")

#Вариант 4
import random
N = int(input("Введите количество сотрудников: "))
vacation_shedule = {}
months = ["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
for x in range(N):
    name = f"Сотрудник_{x}"
    day = random.randint(1,28)
    month = random.choice(months)
    if month not in vacation_shedule:
        vacation_shedule[month] = []
    vacation_shedule[month].append((name,day))
query_month = random.choice(months)
if query_month in vacation_shedule:
    print(f"Отпуск в месяце {query_month}: ")
    for name, day in vacation_shedule[query_month]:
        print(f"{name} - {day} {query_month}")
else:
    print(f"Никто не идет в отпуск в месяце {query_month}")


#Вариант 6
word = input("Введите слово: ")
letter_count = {}
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
print(letter_count)

#Задание 3
translit_dict = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I',
    'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F',
    'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i',
    'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
    'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia'
}
def transliterate(text):
    result = ""
    for char in text:
        if char in translit_dict:
            result += translit_dict[char]
        else:
            result += char
    return result
text = input("Введите текст на русском: ")
transliterated_text = transliterate(text)
print("Транслитерированный текст:", transliterated_text)