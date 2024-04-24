def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total
def find_number_with_max_digit_sum(numbers):
    max_sum = 0
    max_number = None
    for number in numbers:
        current_sum = sum_of_digits(number)
        if current_sum > max_sum:
            max_sum = current_sum
            max_number = number
    return max_number