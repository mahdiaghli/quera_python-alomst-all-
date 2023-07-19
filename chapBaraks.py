array = []
while True:
    a = int(input())
    if a != 0:
        array.append(a)
    elif a == 0:
        break

array.reverse()
for i in range(0, len(array)):
    print(array[i])
