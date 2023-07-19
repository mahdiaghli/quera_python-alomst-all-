class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    # drugs = []
    # employees = []

    def __init__(self, name):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, otherdrug):
        self.drugs.append(otherdrug)

    def add_employee(self, first_name, last_name, age):
        mydict = {"first_name": first_name, "last_name": last_name, "age": age}
        self.employees.append(mydict)

    def total_value(self):
        ans = 0
        for drug in self.drugs:
            ans += drug.amount * drug.price
        return ans

    def employees_summary(self):
        string = "Employees:\n"
        for i, person in enumerate(self.employees):
            # print(person)
            string += "The employee number {0} is {1} {2} who is {3} years old.\n".format(i + 1, person["first_name"],
                                                                                          person["last_name"],
                                                                                          person["age"])
        return string


drug = Drug("first", 5, 20)
drug2 = Drug("first2", 5, 20)
drug3 = Drug("first3", 5, 20)

pharmacy = Pharmacy("chamran")
pharmacy.add_drug(drug)
pharmacy.add_drug(drug2)
pharmacy.add_drug(drug3)

pharmacy.add_employee("person", "last", 20)
pharmacy.add_employee("person2", "last2", 20)
pharmacy.add_employee("person3", "last3", 20)

answer2 = pharmacy.total_value()
mylist2 = pharmacy.employees_summary()
print(answer2)
print(mylist2)
