from random import randint

### TODO:
# Combine with euclid's algorithm to incorporate (elective) pre-testing for compositeness using the fact that
# most numbers have small prime factors (e.g. 88 percent of all numbers have at least one prime factor smaller than 100)
# so to catch 88 percent of all numbers, it is enough to try to divide them by all numbers in
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# integrate known sufficient testing sets:
# for n < 2047: [2]
# for n < 1373653: [2, 3]
# for n < 9080191: [31, 73]
# for n < 25326001: [2, 3, 5]
# for n < 3215031751: [2, 3, 5, 7]
# for n < 4759123141: [2, 7, 61]
# for n < 1122004669633: [2, 13, 23, 1662803]
# for n < 2152302898747: [2, 3, 5, 7, 11]
# for n < 3474749660383: [2, 3, 5, 7, 11, 13]
# for n < 341550071728321: [2, 3, 5, 7, 11, 13, 17]
# for n < 3825123056546413051: [2, 3, 5, 7, 11, 13, 17, 19, 23] (Feitsma and Galway)
# for n < 18446744973709551616 = 2^64: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] (Feitsma and Galway)
# for n < 318665857834031151167461: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] (Sorenson and Webster)
# for n < 3317044064679887385961981: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41] (Sorenson and Webster)

def binpower(base, e, mod):
    result = 1
    base %= mod
    while e:
        if (e & 1):
            result = (result * base) % mod
        base = (base * base) % mod
        e = e >> 1
    return result

def check_composite(n, a, d, s):
    x = binpower(a, d, n)
    if (x == 1 or x == n-1):
        return False
    for _ in range(1, s):
        x = (x * x) % n
        if x == n - 1:
            return False
    return True

def probmillerrabin(n, iternum=5):
    '''Probabilistic Miller-Rabin primality checker, at most 25 percent of composite numbers can be strong liars, meaning that per
    iteration, if n is composite, we have a probability larger than 75 percent of a random base telling us n is composite.
    (Requires "from random import randint")'''
    if n < 4:
        return n == 2 or n == 3
    
    s = 0
    d = n - 1
    while (d & 1) == 0:
        d = d >> 1
        s += 1
    
    for _ in range(iternum):
        a = 2 + randint(0, 9) % (n-3)
        if check_composite(n, a, d, s):
            return False
    
    return True

def detmillerrabin32bit(n):
    '''Deterministic Miller-Rabin primality checker for numbers up to 32 bits,
    the smallest composite number failing this test is 3 215 031 751 = 151*751*28351'''
    if n < 2:
        return False
    
    r = 0
    d = n - 1
    while (d & 1) == 0:
        d = d >> 1
        r += 1

    for a in [2, 3, 5, 7]:
        if n == a:
            return True
        if check_composite(n, a, d, r):
            return False
    return True

def detmillerrabin64bit(n):
    '''Deterministic Miller-Rabin primality checker for numbers up to 64 bits'''
    if n < 2:
        return False
    
    r = 0
    d = n - 1
    while (d & 1) == 0:
        d = d >> 1
        r += 1

    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == a:
            return True
        if check_composite(n, a, d, r):
            return False
    return True