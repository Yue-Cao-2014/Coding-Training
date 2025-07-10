from stock import Stock, DStock, read_portfolio_csv
from reader import read_csv_as_instance
from tableformat import print_table
from decimal import Decimal


if __name__ == "__main__":
    # # 3.1
    # google = Stock("GOOG", 100, 490.1)
    # google.show_shares()
    # google.sell(25)
    # google.show_shares()

    # portfolio = read_portfolio_csv("Python_Mastery/Data/portfolio.csv")

    # # 3.2
    # print_table(portfolio, ['name', 'shares', 'price'])
    # print_table(portfolio, ['shares', 'name'])
    # google = Stock("GOOG", 100, 490.1)
    # c = google.cost
    # print(c.__self__)
    # print(c.__func__)
    # print(c.__func__(c.__self__))
    # f = google.sell
    # f.__func__(f.__self__, 25)
    # google.show_shares()

    # 3.3
    row = ["Google", 100, 666]
    stock = Stock.from_row(row)
    print(stock)
    print(stock.cost)
    stock = DStock.from_row(row)
    print(stock)
    print(stock.cost)

    portfolio = read_csv_as_instance("Python_Mastery/Data/portfolio.csv", Stock)
    for s in portfolio:
        print(s)

    # # 3.4
    # s = Stock('GOOG', 100, 490.10)
    # s.shares = 50          # OK
    # print(s)
    # # s.shares = '50'
    # # s.shares = -10
    # s.price = 123.45 
    # print(s)
    # # s.price = '123.45'
    # # s.price = -10.0
    # # s.spam = "xo"

    # s = DStock('AA', 50, Decimal('91.1'))
    # print(s)
    # s.shares = 100
    # s.price = 92.3