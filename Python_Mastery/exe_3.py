from stock import Stock, DStock, read_portfolio_csv
from tableformat import print_table


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
    print(stock.cost())
    stock = DStock.from_row(row)
    print(stock)
    print(stock.cost())
    portfolio = read_portfolio_csv("Python_Mastery/Data/portfolio.csv", Stock)
    for s in portfolio:
        print(s)
