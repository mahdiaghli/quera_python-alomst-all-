matrix1 = [
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ],
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ],
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ]
]


def coloring(matrix):
    tool = len(matrix)
    arz = len(matrix[0])
    ertefa = len(matrix[0][0])
    for i in range(tool):
        for j in range(arz):
            for k in range(ertefa):
                matrix[i][j][k] = 1

    for i in range(1, tool - 1):
        for j in range(1, arz - 1):
            for k in range(1, ertefa - 1):
                matrix[i][j][k] = 0


coloring(matrix1)
for i in range(len(matrix1)):
    print("{}th layer:".format(i + 1))
    for j in matrix1[i]:
        for k in j:
            print(k, end=' ')
        print()
