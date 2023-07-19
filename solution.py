class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __int__(self, name):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug):
        self.drugs.append(drug)

    def add_employee(self, first_name, last_name, age):
        mydict = {"first_name": first_name, "last_name": last_name, "age": age}
        self.employees.append(mydict)

    def total_value(self):
        ans = 0
        for drug in self.drugs:
            ans += drug.amount * drug.price
        return ans

    def employees_summary(self):
        mylist = ["Employees:", "\n"]
        for i, person in enumerate(self.employees):
            mylist.append(
                "The employee number {j} is {first_name} {last_name} who is {age} years old.\n".format(i, person.name,
                                                                                                       person.last_name,
                                                                                                       person.age))
        return mylist

