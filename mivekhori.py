def fruits(tuple_of_fruits):
    dict = {}
    for mive in tuple_of_fruits:
        mylist = list(mive.values())
        if mylist[1] == "sphere" and 300 <= mylist[2] <= 600 and 100 <= mylist[3] <= 500:
            if mylist[0] in dict:
                dict[mylist[0]] = dict[mylist[0]] + 1
            else:
                dict[mylist[0]] = 1
    return dict


print(fruits((
    {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
    {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})))

