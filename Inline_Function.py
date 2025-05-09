l = [1, 3, 6]
f1 = lambda x: x * x
f2 = lambda x: x % 2 ==0
f2 = filter(f2, l)
f3 = map(f1, l)

def f(x,l=[]):
    print(l)
    for i in range(x): 
        l.append(i*i)
    print(l)


if __name__ == "__main__":
    f(2)
    f(3)
    f(3,[3,2,1])
