def solve(path):
    file = open(path, "r")
    n = 0
    while True:
        line = file.readline()
        # print(line)
        if line == "":
            break

        line = line.strip()
        # print(line)

        if line == "":
            n = n - 1

        if line != "" and line[0] == "#":
            n = n - 1

        n = n + 1

    return n


print(solve("count.py"))
