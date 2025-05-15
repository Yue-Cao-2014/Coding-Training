import csv
from collections import namedtuple
import tracemalloc


class normal_row:
    def __init__(self, route: str, date: str, daytype: str, rides: str):
        self.route = route 
        self.date = date
        self.daytype = daytype
        self.rides = rides

    def __repr__(self):
        return "Normal class type"


tuple_row = namedtuple('Ride_info', ('route', 'date', 'daytype', 'rides'))


class slot_row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route: str, date: str, daytype: str, rides: str):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    def __repr__(self):
        return "Slot class type"


def read_rides(filename: str, data_type) -> list:
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])

            if data_type is tuple:
                record = (route, date, daytype, rides)
            elif data_type is dict:
                record = {'route': route, 'date': date, 'daytype': daytype, 'rides': rides}
            elif isinstance(data_type, normal_row):
                record = normal_row(route, date, daytype, rides)
            elif isinstance(data_type, tuple_row):
                record = tuple_row(route, date, daytype, rides)
            elif isinstance(data_type, slot_row):
                record = slot_row(route, date, daytype, rides)
            else:
                raise TypeError(f"Data type {data_type} is not correct!")

            records.append(record)

    return records


def test_memory_function(d_type, read_fun = read_rides):
    print(d_type)
    tracemalloc.start()
    rows = read_fun('Python_Mastery/Data/ctabus.csv', d_type)
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()


def read_rides_as_columns(filename: str, d_type):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


if __name__ == '__main__':
    d_type = tuple   
    test_memory_function(d_type)
    d_type = dict
    test_memory_function(d_type)
    d_type = normal_row("", "", "", "")
    test_memory_function(d_type)
    d_type = tuple_row("", "", "", "")
    test_memory_function(d_type)
    d_type = slot_row("", "", "", "")
    test_memory_function(d_type)
    d_type = dict
    test_memory_function(d_type, read_rides_as_columns)
    
    