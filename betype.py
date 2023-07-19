s = []
a = input()
for i in a:
    if i != "=":
        s.append(i)
    elif i == "=" and len(s) != 0:
        s.pop()

print("".join(s))
