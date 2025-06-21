import time

class Date:
    datefmt = '{year}-{month}-{day}'
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        tm = time.localtime()
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

    def __str__(self):
        return self.datefmt.format(year=self.year, month=self.month, day=self.day)
    
class USDate(Date):
    datefmt = '{month}/{day}/{year}'

d = USDate(2000, 12, 20)
print(d)
d2 = Date(2000, 12, 20)
print(d2)

class SomeClass:
    @classmethod
    def yow(cls):
        print('SomeClass.yow', cls)

SomeClass.yow()

inst = SomeClass()
inst.yow()

d =  USDate.today()
print(d)

class Base:
    def __init__(self, name):
        self.__name = name

class Child(Base):
    def spam(self):
        print('Spam', self._Base__name)

d = Child("Jack")
d.spam()


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        print("return shares")
        return self._shares

    @shares.setter
    def shares(self, value):
        print("set shares")
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price
    
s = Stock("ACME", 50, 91.1)
print("-------------------------")
print(s.name, s.cost)
print(dir(s))