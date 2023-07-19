class Car:

    def __init__(self):
        self.speed = "90km/h"
        self.weight = 500
        self.color = "white"

    def make_sound(self):
        print("boooooooooogh")


new_car = Car()
new_car.make_sound()
print(new_car.color)


class Money:
    def __int__(self):
        pass

    def moneyx2(self, money):
        return money * 2


pool = Money()
print(pool.moneyx2(1200))


class Myself:
    def __init__(self, firstname, lastname):
        print(firstname, lastname)


myself = Myself("mahdi", "aghli")


class this_is_me:
    my_hair_color = "black"

    def __init__(self):
        my_height = "182cm"

    @staticmethod
    def walk(self):
        print("I'm walking")

    def think(self):
        print("I'm thinking")


this_is_me.walk(self="")
print(this_is_me.my_hair_color)
this_is_me.my_hair_color = "red"
print(this_is_me.my_hair_color)


# print(this_is_me.my_height) # doesn't work (didn't instantiate)
# (its_me = this_is_me)

# this_is_me.think(self="")

class Dad(object):
    alaki = "alaki"

    def angry(self):
        print("angry")


class Son(Dad):
    pass


son = Son
print(son.alaki)

try:
    a, b = 5, 0
    s = a / b

except ZeroDivisionError:  # except khali ham mishe gozasht
    print("wrong!")

try:
    my_file = open("myfile.txt", "r")
    my_file2 = open("myfile2.txt", "w")
    my_file2.write("this is python 2")
    my_file.read()

except IOError:
    print("couldn't make the file")

else:
    print("succeed")
    my_file.close()


try:
    my_file3 = open("myfile3.txt","w")
    try:
        my_file3.write("here you are")
    finally:
        print("closed")
        my_file3.close()

except IOError:
    print("ERROR")

