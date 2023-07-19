import math


def get_func(ls):
    mylist = []
    for i in ls:
        if i == "square":
            mylist.append(lambda x : x ** 2)
        elif i == "circle":
            mylist.append(lambda x : x ** 2 * math.pi)
        elif i == "rectangle":
            mylist.append(lambda x, y : x * y)
        elif i == "triangle":
            mylist.append(lambda x, y : x * y / 2)

    return mylist


ls = get_func(['square', 'circle', 'rectangle', 'triangle'])

print(ls[0](1))
print(ls[1](2))
print(ls[2](2, 4))
print(ls[3](4, 5))
