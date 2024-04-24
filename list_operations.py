def copy_to_another_list(list_A, list_B, K):
    for num in list_A:
        if num != K:
            list_B.append(num)