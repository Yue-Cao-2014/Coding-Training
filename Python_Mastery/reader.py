import csv
from pprint import pprint
from sys import intern
import tracemalloc
from readrides import RideData

# A function that reads a file into a list of dicts
def read_portfolio(filename: str) -> list[dict]:
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio


def read_csv_as_dicts(file_name: str, data_type: list[type]) -> list[dict]:
    res = []
    with open(file_name) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {}
            for h, v, t in zip(headers, row, data_type):
                record[h] = t(v)
            res.append(record)
    return res


def read_csv_as_columns(file_name: str,  data_type: list[type]) -> RideData:
    res = RideData()
    with open(file_name) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {}
            for h, v, t in zip(headers, row, data_type):
                record[h] = t(v)
            res.append(record)
    return res


def read_csv_as_instance(file_name: str, obj_type):
    res = 


if __name__ == "__main__":
    # portfolio = read_csv_as_dicts('Python_Mastery/Data/portfolio.csv', 
    #                               [str, int ,float]) 
    # pprint(portfolio)
    tracemalloc.start()
    ride = read_csv_as_dicts('Python_Mastery/Data/ctabus.csv', 
                             [intern, intern, str, int]) 
    routeid = {id(r["route"]) for r in ride}
    print(len(routeid))
    print(tracemalloc.get_traced_memory())
    