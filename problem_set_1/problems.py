def sum_of_multiples(multiples, n):
    sum = 0
    for i in range(n):
        if any(i % j == 0 for j in multiples):
            sum += i
    return sum

answer_1 = sum_of_multiples([3, 5], 1000)