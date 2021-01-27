class Employee():

    def __init__(self, first, last, salary):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary
    
    def give_raise(self, salary=5_000):
        self.salary += salary


# JQ = Employee('JQ', 'L', 70_000)
# print(f"{JQ.salary}")

# JQ.give_raise()
# print(f"{JQ.salary}")