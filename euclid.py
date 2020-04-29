# some different variations on euclid's algorithm
def gcd(a,b):
    '''not at all optimized but returns the greatest common divisor of two integers a and b'''
    if b < 0:
        b *= -1
    if a < 0:
        a *= -1
    if b > a:
        a, b = b, a
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def extended(a,b):
    '''not at all optimized but returns integers x, y and gcd(a,b) that satisfy bézout's identity, i. e. such that
        ax + by = gcd(a,b). x, and y are also one minimimal pair'''
    ### todo: testa om allt stämmer med hantering av negativa tal...
    (nega, a) = (False, a) if a >= 0 else (True, (-1)*a)
    (negb, b) = (False, b) if b >= 0 else (True, (-1)*b)
    (switched, a, b, nega, negb) = (False, a, b, nega, negb) if b > a else (True, b, a, negb, nega)
    valsold = [None, a, 1, 0]
    valsmid = [None, b, 0, 1]
    while valsmid[1] != 0:
        valsnew = [valsold[1]//valsmid[1], valsold[1] % valsmid[1]]
        valsnew.append(valsold[2]-valsnew[0]*valsmid[2])
        valsnew.append(valsold[3]-valsnew[0]*valsmid[3])
        valsold = valsmid[:]
        valsmid = valsnew[:]
    x = valsold[2]*(-1) if nega else valsold[2]
    y = valsold[3]*(-1) if negb else valsold[3]
    return (y, x, valsold[1]) if switched else (x, y, valsold[1])

if __name__ == "__main__":
    #print(gcd(24,15))
    #print(extended(240, 46))
    print(extended(42, -12))