def capitalize(names):
    myArray = []
    for name in names:
        name = name.lower()
        arraylist = name.split()
        string = ""
        for member in arraylist:
            member = member[0].upper() + member[1:]
            string = string + member + " "
        myArray.append(string.removesuffix(" "))
    return myArray


# capitalize(['ali', 'REYHANEH', 'aMIR', 'AMIR abbas', 'Fatemeh Zahra'])
