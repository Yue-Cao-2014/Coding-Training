import pandas as pd

class A:
    instance = None
    num = 0

    def __new__(cls, *args, **kargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
            print("New... ", cls.instance.num)
        else:
            print("Existing... ", cls.num, cls.instance.num)
        return cls.instance
    
    def get_num(self):
        print(self.num)
        self.num += 1
        return self.num
    
    @staticmethod
    def add_num():
        A.num += 1
    
class B:
    instance = None
    num = 0

if __name__ == "__main__":
    a = A()
    print(A.__dict__)
    print(a.__dict__)
    a1 = a.get_num()
    print(a.__dict__)
    a.add_num()
    b = A()
    b1 = b.get_num()
    print(a is b)
    print(a1, b1)

    c = B()
    d = B()
    print(c is d)