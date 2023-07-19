import re


def solve(string):
    string2 = re.split(" ", string)
    del string2[1], string2[2]
    x = ""
    y = 0
    if "#" in string2[0]:
        x = string2[0]
        y = int(string2[2]) - int(string2[1])

    if "#" in string2[1]:
        x = string2[1]
        y = int(string2[2]) - int(string2[0])

    if "#" in string2[2]:
        x = string2[2]
        y = int(string2[0]) + int(string2[1])

    if re.match(r"^[0-9]*\.*[0-9]*$", str(y)):
        # A = re.split("['#']", x)
        # B = str(y) - A[1]
        # B = str(y) - A[1]

        # B = re.sub(A, "", str(y))

        answer = []
        answer.append("+")
        answer.append("=")

        if "#" in string2[0]:
            answer.insert(0, y)
            answer.insert(2, string2[1])
            answer.append(string2[2])

        if "#" in string2[1]:
            answer.insert(0, string2[0])
            answer.insert(2, y)
            answer.append(string2[2])

        if "#" in string2[2]:
            answer.insert(0, string2[0])
            answer.insert(2, string2[1])
            answer.append(y)

        final = ""
        for i in answer:
            final = final + " " + str(i)
        return final
    else:
        return "-1"


print(solve("15 + 1#2 = 136"))
