def dist(p1, p2):
    """returns euclidean distance between tuple points p1 and p2"""
    return (abs(p2[0]-p1[0])**2 + abs(p2[1]-p1[1])**2)**0.5

def line(p1, p2):
    """from points p1 = (x1, y1) and p2 = (x2, y2), produces
    coefficients A, B and C such that Ax + By = C"""
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return [A, B, -C]

def intersection(L1, L2):
    """from lines L1 and L2 on the form of a list [a, b, c] s.t. ax + by = c defines the line, returns the point
    (x, y) satisfying both line equations. If such a point doesn't exist (i. e. lines are parallel), returns False"""
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return (x, y)
    else:
        return False

def incenter(a, b, c):
    """returns center of incircle of triangle given by tuple points a, b and c"""
    perim = dist(a, b) + dist(b, c) + dist(c, a)
    ix = (dist(b, c)*a[0] + dist(c, a)*b[0] + dist(a, b)*c[0])/perim
    iy = (dist(b, c)*a[1] + dist(c, a)*b[1] + dist(a, b)*c[1])/perim
    return (ix, iy)

def inradius(a, b, c):
    """returns radius of incircle of triangle given by tuple points a, b and c"""
    sidea, sideb, sidec = dist(b, c), dist(c, a), dist(a, b)
    s = 0.5*(sidea + sideb + sidec)
    return ((s*(s-a)*(s-b)*(s-c))**0.5)/s

def circumcenter(a, b, c):
    """returns center of circumcircle of triangle given by tuple points a, b and c"""
    return

def circumradius(a, b, c):
    """returns radius of circumcircle of triangle given by tuple points a, b and c"""
    return