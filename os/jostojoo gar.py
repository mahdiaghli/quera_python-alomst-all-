import os

dict = {}


def explore(ttype, address):
    ttype = "." + ttype.lower()
    number = 0
    mylist = list(os.walk(address))
    if len(mylist[0][2]) != 0:
        print(mylist[0])
        for file in mylist[0][2]:
            if ttype in str(file).lower():
                number = number + 1

        dict[mylist[0][0]] = number
        print(dict)

        if len(mylist[0][1]) != 0:
            for folder in mylist[0][1]:
                explore(ttype, folder)
    return dict


print(explore("py", "../os"))
