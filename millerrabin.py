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
    for r in range(1, s):
        x = (x * x) % n
        if x == n - 1:
            return False
    return True

