def process(path):
    file = open("ans.csv", "w")
    with open(path) as csv:
        for row in csv.readlines():
            radif = row.rstrip().split(', ')
            jam = 0
            for i in radif:
                jam = jam + int(i)
            string = ""
            for i in radif:
                string = string + i + ", "
            file.write(string + str(jam) + "\n")
            file.flush()


process("file.csv")
