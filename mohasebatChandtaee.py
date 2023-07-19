from math import *

def calc(array):
    maximum = max(array)
    miangin = sum(array) / len(array)
    miane = 0
    if len(array) % 2 != 0:
        miane = sorted(array)[int(len(array) / 2)]
    else:
        miane = (sorted(array)[int(len(array) / 2) - 1] + sorted(array)[int(len(array) / 2)]) / 2
    t = miangin, miane, maximum
    return t


print(calc([2, 20, 30, 29]))
