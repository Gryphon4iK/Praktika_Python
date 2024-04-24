def sum_of_elements_less_than_K(list_A, K):
    total = 0
    for num in list_A:
        if num < K:
            total += num
    return total
