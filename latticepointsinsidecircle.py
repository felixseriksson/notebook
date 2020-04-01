from math import floor
def latticepoints(r):
    """returns number of lattice points inside circle with int or float radius r, requires from math import floor"""
    return 1 + 4*floor(r) + 4*sum([floor(((r**2)-(i**2))**0.5) for i in range(1, floor(r)+1)])

#testing: comment out block comments
'''
for n in range(20):
    print(latticepoints(n))
'''

### Kolla upp Leibniz' Christmas Theorem för beräkning av antal sätt att skriva n som hypotenusa till två heltalskateter