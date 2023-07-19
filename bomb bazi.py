n, m = input().split()
n = int(n)
m = int(m)
k = int(input())


def check_pos(x, y, map):
    pos = [-1, 0, 1]
    if map[x][y] == "*":
        for i in pos:
            for j in pos:
                if i != 0 or j != 0:
                    # print(x + i)
                    # print(y + j)
                    if -1 < x + i < n and -1 < y + j < m:
                        if map[x + i][y + j] != "*":
                            map[x + i][y + j] += 1



map = []
for x in range(n):
    map.append([])
    for y in range(m):
        map[x].append(0)

for i in range(k):
    sotoon, radif = input().split()
    sotoon = int(sotoon) - 1
    radif = int(radif) - 1
    map[sotoon][radif] = "*"

    # for i in range(n):
    #     for j in range(m):
    check_pos(sotoon, radif, map)
    # for z in range(n):
    #     print(map[z])
    # print()


for i in range(n):
    for j in range(m):
        print(map[i][j],end=" ")
    print()
