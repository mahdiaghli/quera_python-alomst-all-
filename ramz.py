k = int(input())
ramz = input()
num = 0

for i in range(k):
    string2 = input()
    length = len(string2)
    find = string2.find(str(ramz[i]))
    # print(find)
    if length - find > find:
        num = num + find
    else:
        num = num + (length - find)

print(num)
