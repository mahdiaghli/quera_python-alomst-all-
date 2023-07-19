import re
from re import *

def check_registration_rules(**kwargs):
    mylist = []
    for name, password in kwargs.items():
        if len(name) > 3 and len(password) > 5 and name != "codecup" and name != "quera":
            if len(re.sub("[0-9]", "", password)) != 0:
                print(password)
                mylist.append(name)
    print(mylist)


check_registration_rules(username='648645346', sadegh='He3@lsa')
check_registration_rules(quera='qwerty80', mmdreza='monday80', ali="aliali@", mammad="salam")
