import time
#from swingfactorial import factorialPS


def timing(f, n, a, d=3):
    """ time the function f called on a n times to d digits precision(default 3), return total time"""
    print(f.__name__)
    r = range(n)
    t1 = time.perf_counter()
    for _ in r:
        f(a)
        f(a)
        f(a)
        f(a)
        f(a)
        f(a)
        f(a)
        f(a)
        f(a)
        f(a)
    t2 = time.perf_counter()
    print("Total time: ", round(t2-t1, d))
    print("Average time: ", round((t2-t1)/n, d))

# example:
# using the timing function to time the function factorialPS from module swingfactorial (uncomment line 2!) called on 10000 over 10 runs
# timing(factorialPS, 10, 10000)
