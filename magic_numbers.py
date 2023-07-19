class Strint(int):

    def __init__(self, number):
        self.number = number

    def __lt__(self, other):
        return self.number % 10 < other % 10

    def __gt__(self, other):
        return self.number % 10 > other % 10

    def __le__(self, other):
        return self.number % 10 <= other % 10

    def __ge__(self, other):
        return self.number % 10 >= other % 10

    def __eq__(self, other):
        return self.number % 10 == other % 10

    def __ne__(self, other):
        return self.number % 10 != other % 10

    def __add__(self, other):
        return int(str(self.number) + str(other))

    def __sub__(self, other):
        mystring = str(self.number)
        secstring = str(other)
        if mystring.endswith(secstring):
            result = mystring[:-len(secstring)]
            if result:
                return int(result)
            return 0
        else:
            raise Exception("The subtraction is not valid!")

    def __len__(self):
        return len(str(self.number))

    def __call__(self):
        s2 = ""
        mydict = {"0": "۰", "1": "۱", "2": "۲", "3": "۳", "4": "۴", "5": "۵", "6": "۶", "7": "۷", "8": "۸", "9": "۹"}
        for char in str(self.number):
            s2 += mydict[char]
        return s2
