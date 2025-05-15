from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ["value"]

    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Value is {self.value}."
    
    def __format__(self, format_spec):
        return format(self.value, format_spec)
    
    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(other.value + self.value)
        elif isinstance(other, int):
            return MutInt(other + self.value)
        else:
            return NotImplemented
        
    __radd__ = __add__

    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
        
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return other.value == self.value
        elif isinstance(other, int):
            return other == self.value
        else:
            return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
        
    def __int__(self):
        return int(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __index__(self):
        return self.value
    

if __name__ == "__main__":
    a = MutInt(3)
    print(a)
    print(repr(a))
    print(1 + a)
    b = a
    b += 3
    print(b, type(b))
    print(a)
    print(b<=a)
    l = [1, 2, 3, 4, 5, 6, 7]
    print(l[a])