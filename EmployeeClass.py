class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(first, last)

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        return

    @classmethod
    def set_raise_amount(cls, amount):
        Employee.raise_amount = amount


emp1 = Employee(last="Chris", first="Harris", pay=50000)
print(Employee.num_of_emps)

emp2 = Employee(last="Harris", first="Chris", pay=50000)
print(Employee.num_of_emps)
print(emp1.email)
print(emp1.fullname())
emp1.apply_raise()
print(emp1.pay)

Employee.set_raise_amount(1.10)
emp2.apply_raise()
print(emp2.pay)
