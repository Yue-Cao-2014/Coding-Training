class MyClass:
    def __init__(self):
        self._my_attribute = 10

    def __getattribute__(self, name):
        print(f"__getattribute__ called for: {name}")
        if name == "my_attribute":
            return object.__getattribute__(self, "_my_attribute") * 2
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        print(f"__setattr__ called for: {name} = {value}")
        if name == "my_attribute":
            object.__setattr__(self, "_my_attribute", value)
        else:
            object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f"__delattr__ called for: {name}")
        if name == "my_attribute":
            print("Cannot delete my_attribute")
        else:
            object.__delattr__(self, name)

    def return_my_atrribute(self):
        return self._my_attribute

# # Usage
# obj = MyClass()
# print(obj.return_my_atrribute())
# print(obj.my_attribute)
# obj.my_attribute = 20
# print(obj.my_attribute)
# del obj.my_attribute
# print(obj.__dict__)
# del obj._my_attribute
# print(obj.__dict__)

class MyClass(object):
    def __init__(self, value):
        self.value = value
    
    #__slots__ = "value"

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"MyClass({self.value!r})"

    def __str__(self):
        return f"Instance of MyClass with value: {self.value}"

    def __eq__(self, other):
      return self.value == other.value

# obj1 = MyClass(10)
# print(id(obj1))
# obj2 = MyClass(20)
# print(id(obj2))
# print(obj1)
# print(repr(obj2))
# print(obj1 == obj2)
# print(hash(obj1) == hash(obj2))
# obj1.a = 10
# print(obj1.__dict__)

class D(object):
    def __init__(self):
        self.a = 1

class B(D):
    pass

class C(D):
    def __init__(self):
        self.a = 2

class A(C, B):
    pass

# inst = A()
# print(inst.a)
# print(A.__mro__)

class Singleton(object):
    b = 2
    def __new__(cls, *args, **kw):

        if not hasattr(cls, '_instance'):
            # orig = super(Singleton, cls)
            cls._instance = super().__new__(cls, *args, **kw)

        return cls._instance

class MyClass(Singleton):
    a = 1

c = MyClass()
print(c.a, c.b)
d = MyClass()
d.b = 3
print(c.a, c.b)
e = MyClass()
print(c.a, c.b)