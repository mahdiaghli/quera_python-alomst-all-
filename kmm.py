p, d = input().split()
p = int(p)
d = int(d)

while True:
    x = p / 2
    if d % p <= x:
        print(d)
        break
    else:
        d = d + d
