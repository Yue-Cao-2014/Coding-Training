import pandas as pd

class A:
    instance = None
    num = 0

    def __new__(cls, *args, **kargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def get_num(self):
        self.num += 1
        return self.num
    
a = A()
a1 = a.get_num()
b = A()
b1 = b.get_num()
print(a is b)
print(a1, b1)