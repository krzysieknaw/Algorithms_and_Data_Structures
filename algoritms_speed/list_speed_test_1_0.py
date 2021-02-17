import timeit


def test1(): #concat
    l = []
    for i in range(1000):
        l = l + [i]

def test2(): #append
    l = []
    for i in range(1000):
        l.append(i)

def test3(): #comprehension
    l = [i for i in range(1000)]

def test4(): #list range
    l = list(range(1000))

def test5(): #pop first
    x = list(range(100000))
    x.pop(0)
                       
def test6(): #pop last
    x = list(range(100000))
    x.pop()
    
def test7(i): #pop first
    x = list(range(i))
    x.pop(0)

def test8(i): #pop last
    x = list(range(i))
    x.pop()
    

print("concat {:.3f} seconds".format(timeit.timeit(test1, number=1000)))
print("append {:.3f} seconds".format(timeit.timeit(test2, number=1000)))
print("comprehension {:.3f} seconds".format(timeit.timeit(test3, number=1000)))
print("list range {:.3f} seconds".format(timeit.timeit(test4, number=1000)))
print("")
print("pop first {:.3f} seconds".format(timeit.timeit(test5, number=100)))
print("pop last {:.3f} seconds".format(timeit.timeit(test6, number=100)))

for i in range(10000000,100000001,10000000):
    pt = timeit.timeit("test7(i)", setup='from __main__ import test7, i', number=10)
    pz = timeit.timeit("test8(i)", setup='from __main__ import test8, i', number=10)
    print("{:10.0f} {:15.5f} {:15.5f}".format(i,pz,pt))

# spodziewałem się że pop(0) będzie O(n) a pop(1) -> O(1), wychodzi natomiast na to że są liniowe. Dlaczego?





