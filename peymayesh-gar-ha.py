class Reverse:
    mylist2 = []

    def __init__(self, mylist):
        self.mylist = mylist
        self.index = len(self.mylist) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        number = self.mylist[self.index]
        self.index = self.index - 1
        return number


ls = [10, 20, 30]
for it in Reverse(ls):
    print(it)
print(ls)
