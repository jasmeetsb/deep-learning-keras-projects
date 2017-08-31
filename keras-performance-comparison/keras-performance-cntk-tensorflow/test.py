def test():
    """Stupid test function"""
    L = []
    for i in range(1000):
        L.append(i)
        #print(i)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test",number=10))
