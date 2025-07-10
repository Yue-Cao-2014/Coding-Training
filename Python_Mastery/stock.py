import csv
from decimal import Decimal

class Stock:
    __slots__ = ('name', "_shares", "_price", "s_cost")
    _types = (str, int, float)
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price
        self.s_cost = self.cost
    
    def cost(self) -> float:
        return self.shares * self.price
    
    @property
    def cost(self) -> float:
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares
        
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise ValueError(f"{value} type {type(value).__name__} for shares is not {self._types[1].__name__}!")
        elif value < 0:
            raise ValueError(f"{value} for shares is negative!")
        self._shares = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value,self._types[2]):
            raise ValueError(f"{value} type {type(value).__name__} for price is not {self._types[2].__name__}!")
        elif value < 0:
            raise ValueError(f"{value} for price is negative!")
        self._price = value  
    
    def __repr__(self) -> str:
        return f"Stock name: {self.name}, price: {self.price}, share: {self.shares}, cost: {self.s_cost}"

    def sell(self, sold_share: int) -> float:
        self.shares -= sold_share

    def show_shares(self) -> None:
        print(f"Shares: {self.shares}")

    @classmethod
    def from_row(cls, row) -> type:
        values = [t(v) for t, v in zip(cls._types, row)]
        return cls(*values)


class DStock(Stock):
    _types = (str, int, Decimal)


def read_portfolio_csv(file: str, obj_type: type) -> list[Stock]:
    res = []
    with open(file, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for r in rows:
            res.append(obj_type.from_row(r))

    return res
