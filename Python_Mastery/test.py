import collections
d = collections.Counter()
d2 = collections.Counter()
d["a"] += 1
d["b"] += 2
d2["c"] += 3
d2["b"] += 4
print(d2 - d)

a = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
b = { 'name': '6/11/2007', 'time': '9:45am' }

print({**a, **b})
print(a.update(b))