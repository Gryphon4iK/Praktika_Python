#Задание 1
a = {0, 1, 2, 3}
b = {5, 4, 3, 2}
c = a.union(b)
x = a.intersection(b)
print(c,'\n',x)

#Задание 2
#Вариант 1
txt = 'asdf1233515SDf3asdfasd55121390'
print(set(map(int, filter(lambda x: x.isdigit(), txt))))

#Вариант 2
sequence = 'asdf1233515SDf3asdfasd55121390'
unique_set = set(sequence)
letters_set = sorted({x for x in unique_set if x.isalpha() and x.upper() >= 'A' and x.upper() <= 'Z'})
numbers_set = sorted({x for x in unique_set if x.isdigit() and int(x) >= 0 and int(x) <= 5})
print(letters_set,'\n',numbers_set)

#Вариант 10
sequence = 'asdf1233515SDf3asdfasd55121390xzuwy'
unique_set = set(sequence)
letters_set = sorted({x for x in unique_set if (x.isalpha() and ((x.upper() >= 'A' and x.upper() <= 'F') or (x.upper() >= 'X' and x.upper() <= 'Z')) )})
print(letters_set)