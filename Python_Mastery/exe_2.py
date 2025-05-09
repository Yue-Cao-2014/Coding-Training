import tracemalloc
f = open('Data/ctabus.csv')
tracemalloc.start()
data = f.read()
print(len(data))
current, peak = tracemalloc.get_traced_memory()
print(current, peak)