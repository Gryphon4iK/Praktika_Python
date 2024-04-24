#Задание 1
import module.mymodule as mymodule
name = input("Введите ваше имя: ")
print(mymodule.greet(name))
result = mymodule.multiply(8, 7)
print(result)

#Здание2
#Вариант 1
import module.list_operations as list_operations
list_A = [1, 2, 3, 4, 5, 6]
list_B = []
K = 3
list_operations.copy_to_another_list(list_A, list_B, K)
print(list_B)

#Вариант 3
import module.operations as operations
list_A = []
K = 5
num_to_fill = int(input("Сколько элементов списка следует заполнить? "))
operations.fill_list_with_value(list_A, K, num_to_fill)
print(list_A)

#Вариант 5
import module.operation as operation
list_A = [1, 5, 3, 6, 7, 1, 2]
K = 5
result = operation.sum_of_elements_less_than_K(list_A, K)
print(f"Сумма элементов списка, меньших {K}: {result}")

#Задание 3
import module.digit_operations as digit_operations
print(digit_operations.sum_of_digits(12345))
numbers = [123, 45, 678, 90, 54321]
result = digit_operations.find_number_with_max_digit_sum(numbers)
print(f"Число с максимальной суммой цифр: {result}")