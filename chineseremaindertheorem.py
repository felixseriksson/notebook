def crt(dictionary):
    from euclid import extended
    '''given a dictionary {di: ai} of length i containing i pairwise coprime moduli ai and the i corresponding divisors di such that for all
       i, x mod di = ai, returns the principal value of x and the product of the divisors - d - where all sols are of the form x + nd. 
       COMMON ERROR: ENSURE DICTIONARY OF FORM DIVISOR:REST (BECAUSE DIVISORS ARE UNIQUE), DESPITE WRITING X = REST (MOD DIVISOR)
       Requirements: Needs an extended euclidean algorithm, for example "extended" in notebook/euclid.py'''
    ### todo: add support for coprime divisors etc
    ### also test that it actually works and is error-free lol...
    # ensure 0<= ai < di for all i
    for key in dictionary.keys():
        while dictionary[key] < 0:
            dictionary[key] += key
        while dictionary[key] >= key:
            dictionary[key] -= key
    divisors = sorted(dictionary.keys(), reverse=True)
    prod = 1
    for i in divisors:
        prod *= i
    div1 = divisors.pop(0)
    rest1 = dictionary[div1]
    for di in divisors:
        div2 = di
        rest2 = dictionary[div2]
        m1, m2, _ = extended(div1, div2)
        sol = rest1*m2*div2 + rest2*m1*div1
        rest1 = sol
        div1 *= div2
    result = rest1
    while result < 0:
        result += prod
    while result >= prod:
        result -= prod

    return result, prod

if __name__ == "__main__":
    #print(crt({3:0, 4:3, 5:4}))
    # sun tzu's original example: (should give x = 23 +105k)
    print(crt({3:2,5:3,7:2}))