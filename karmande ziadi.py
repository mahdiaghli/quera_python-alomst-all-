from math import *

n = int(input())
dict = {}
Max = 1
for i in range(n):
    name, lastname = input().split()
    if name not in dict:
        Max = 1
        dict[name] = Max
    else:
        dict[name] = dict[name] + 1

print(max(dict.values()))
