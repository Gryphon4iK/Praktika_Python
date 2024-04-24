#Задание 1
import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for x in range(length))
N = int(input("Введите количество паролей, которые нужно сгенерировать: "))
K = int(input("Введите длину пароля: "))
passwords = [generate_password(K) for x in range(N)]
for password in passwords:
    print([password])

#Задание 2
import random
def generate_schedule(num_exams, subjects):
    days_of_week = ["понедельник","вторник","среда","четверг","пятница"]
    times = [9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0]
    for exam in range(1, num_exams + 1):
        subject = random.choice(subjects)
        day_of_week = random.choice(days_of_week)
        time = random.choice(times)
        ticket_number = random.randint(1, 20)
        print(f"Экзамен по дисциплине {subject} состоится в {day_of_week}, время {time}. Ваш счастливый билет № {ticket_number}.")
num_exams = int(input("Введите количество экзаменов: "))
subjects = input("Введите наименования дисциплин через запятую: ").split(", ")
generate_schedule(num_exams, subjects)

#Задание 3
from datetime import datetime, timedelta
def exam_date(k):
    today = datetime.now()
    exam_date = today + timedelta(days=k)
    return exam_date.strftime("%d %B")
K = int(input("Введите количество дней до экзамена: "))
print(f"Экзамен состоится {exam_date(K)}")


#Задание 4
from datetime import datetime, timedelta
def is_happy_date(date):
    if date.day % 4 != 0 and date.weekday() != 0:
        return True
    return False
def find_happy_dates(start_date, n):
    happy_dates = []
    current_date = start_date
    while len(happy_dates) < 3:
        current_date += timedelta(days=n)
        if is_happy_date(current_date):
            happy_dates.append(current_date)
    return happy_dates
input_date = input("Введите исходную дату в формате ГГГГ/ММ/ДД: ")
year, month, day = map(int, input_date.split('/'))
start_date = datetime(year, month, day)
n = int(input("Введите число n: "))
happy_dates = find_happy_dates(start_date,n)
for date in happy_dates:
    print(date.strftime("%d %B, %A"))