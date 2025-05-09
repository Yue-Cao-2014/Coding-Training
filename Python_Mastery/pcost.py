import os

def portfolio_cost(p_file: str, splitter: str = " ") -> float:

    if not os.path.exists(p_file):
        raise FileNotFoundError(f"File path {p_file} doesn't exist!")

    with open(p_file) as f:
        line = f.readline()
        res = 0
        while line:            
            tmp = line.split(splitter)
            name = tmp[0] 
            position = tmp[1] 
            if tmp[2][-1] == "\n":
                price = tmp[2][:-1]
            else:
                price = tmp[2]

            res += float(position) * float(price)
            line = f.readline()

    return res


class Stock:
    __slots__ = ('name', "shares", "price", "s_cost")
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price
        self.s_cost = self.cost()
    
    def cost(self) -> float:
        return self.shares * self.price
    
    def __repr__(self) -> str:
        return f"Stock name: {self.name}, price: {self.price}, share: {self.shares}, cost: {self.s_cost}"
    

if __name__ == "__main__":
    portfolio_file = "Data/portfolio.dat"
    value = portfolio_cost(portfolio_file)
    print(value)
    stock = Stock('GOOG', 100, 490.10)
    print(stock)