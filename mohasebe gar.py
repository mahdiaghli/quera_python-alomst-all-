def calculator(n, m, ls):
    ls2 = []
    number = 0
    index = 0
    x = 0
    for i in ls:
        number = number + i
        if index == m - 1:
            ls2.append(number)
            index = -1
            number = 0
        if n - x < m - 1 and index != -1:
            ls2.append(number)
        index = index + 1
        x = x + 1

    print(ls2)

    answer = 0
    for i in range(0, len(ls2), 2):
        if len(ls2) % 2 == 0:
            answer = answer + ls2[i]
            answer = answer - ls2[i + 1]
            if i == len(ls2) - 1:
                answer = answer + ls2[i]
        if len(ls2) % 2 == 1:
            answer = answer + ls2[i]
            if i != len(ls2) - 1:
                answer = answer - ls2[i + 1]

    return answer


print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
