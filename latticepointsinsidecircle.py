from math import floor
def latticepoints(r):
    """returns number of lattice points inside circle with int or float radius r (except for origin), requires from math import floor"""
    return 1 + 4*floor(r) + 4*sum([floor(((r**2)-(i**2))**0.5) for i in range(1, floor(r)+1)])

#testing: comment out block comments
'''
for n in range(20):
    print(latticepoints(n))
'''

### Kolla upp Leibniz' Christmas Theorem för beräkning av antal sätt att skriva n som hypotenusa till två heltalskateter
### kolla även https://www.youtube.com/watch?v=NaL_Cb42WyY ex faktum att faktor 2 inte skadar eller hjälper,
### dvs N(5) = N(2*5=10) = N(2*2*5=20) = N(2^k*5)