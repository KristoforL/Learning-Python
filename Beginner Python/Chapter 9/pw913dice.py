#Some built in functions that can be used with any python install

from random import randint

class Die:
    """This will roll a 6 sided die and provide a random number"""
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        print(randint(1, self.sides))

    def ten_times(self):
        """Rolls the die 10x"""
        i=0
        while i<10:
            print(randint(1, self.sides))
            i+=1
    

six = Die()
six.roll_die()

print("\n")
ten = Die()
ten.sides=10
ten.ten_times()

print("\n")
twenty = Die()
twenty.sides=20
twenty.ten_times()
