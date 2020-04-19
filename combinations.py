def pcombinations(n,k,setting="prod"):
    '''n choose k, setting = "prod" (default) for the numerical value of n choose k, "facs" for
    a list of lists containing the prime factors and number of occurrances. (Other keywords will give default).
    Example with n = 10 and c = 3: "prod" gives integer 120, while "facs" gives [[2, 3], [3, 1], [5, 1], [7, 0]]'''
    prime_factors = []
    composite = [True] * 2 + [False] * n
    for p in range(n + 1):
        if composite[p]:
            continue
        q = p
        m = 1
        total_prime_power = 0
        prime_power = [0] * (n + 1)
        while True:
            prime_power[q] = prime_power[m] + 1
            r = q
            if q <= k:
                total_prime_power -= prime_power[q]
            if q > n - k:
                total_prime_power += prime_power[q]
            m += 1
            q += p
            if q > n:
                break
            composite[q] = True
        prime_factors.append([p, total_prime_power])
    if setting == "facs":
        return prime_factors
    else:
        v = 1
        for i in prime_factors:
            v *= i[0]**i[1]
        return v

print(pcombinations(1000,4))