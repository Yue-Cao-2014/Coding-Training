import tracemalloc
import sys
import csv

# tracemalloc.start()
# import readrides
# rows = readrides.read_rides('Python_Mastery/Data/ctabus.csv', dict)
# rt22 = [row for row in rows if row['route'] == '22']
# print(sys.getsizeof(rows), sys.getsizeof(rt22))
# print(max(rt22, key=lambda row: int(row['rides'])))
# print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
# tracemalloc.stop()

tracemalloc.start()
f = open('Python_Mastery/Data/ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)
rows = (dict(zip(headers,row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
print(sum(int(r["rides"]) for r in rt22))
#print(next(rt22))
#print(sum(rt22, key=lambda row: int(row['rides'])))
print(sum(int(r["rides"]) for r in rt22))
print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
tracemalloc.stop()