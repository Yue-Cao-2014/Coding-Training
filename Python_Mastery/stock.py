import csv
from decimal import Decimal

class Stock:
    __slots__ = ('name', "shares", "price", "s_cost")
    types = [str, int, float]
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price
        self.s_cost = self.cost()
    
    def cost(self) -> float:
        return self.shares * self.price
    
    def __repr__(self) -> str:
        return f"Stock name: {self.name}, price: {self.price}, share: {self.shares}, cost: {self.s_cost}"

    def sell(self, sold_share: int) -> float:
        self.shares -= sold_share

    def show_shares(self) -> None:
        print(f"Shares: {self.shares}")

    @classmethod
    def from_row(cls, row) -> type:
        values = [t(v) for t, v in zip(cls.types, row)]
        return cls(*values)


class DStock(Stock):
    types = [str, int, Decimal]
    

def read_portfolio_csv(file: str, obj_type: type) -> list[Stock]:
    res = []
    with open(file, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for r in rows:
            res.append(obj_type.from_row(r))

    return res
