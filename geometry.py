def dist(p1, p2):
    """ returns euclidean distance between tuple points p1 and p2. """
    return (abs(p2[0]-p1[0])**2 + abs(p2[1]-p1[1])**2)**0.5

def line(p1, p2):
    """ from points p1 = (x1, y1) and p2 = (x2, y2), produces
    coefficients A, B and C such that Ax + By = C"""
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return [A, B, -C]

def intersection(L1, L2):
    """ from lines L1 and L2 on the form of a list [a, b, c] s.t. ax + by = c defines the line, returns the point
    (x, y) satisfying both line equations. If such a point doesn't exist (i. e. lines are parallel), returns False. """
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
    """ returns center of incircle of triangle given by tuple points a, b and c. """
    perim = dist(a, b) + dist(b, c) + dist(c, a)
    ix = (dist(b, c)*a[0] + dist(c, a)*b[0] + dist(a, b)*c[0])/perim
    iy = (dist(b, c)*a[1] + dist(c, a)*b[1] + dist(a, b)*c[1])/perim
    return (ix, iy)

def inradius(a, b, c):
    """ returns radius of incircle of triangle given by tuple points a, b and c. """
    sidea, sideb, sidec = dist(b, c), dist(c, a), dist(a, b)
    s = 0.5*(sidea + sideb + sidec)
    return ((s*(s-a)*(s-b)*(s-c))**0.5)/s

def circumcenter(a, b, c):
    """ returns center of circumcircle of triangle given by tuple points a, b and c. """
    D = 2*(a[0]*(b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1]))
    ux = ((a[0]**2 + a[1]**2)*(b[1] - c[1]) + (b[0]**2 + b[1]**2)*(c[1] - a[1]) + (c[0]**2 + c[1]**2)*(a[1] - b[1]))/D
    uy = ((a[0]**2 + a[1]**2)*(c[0] - b[0]) + (b[0]**2 + b[1]**2)*(a[0] - c[0]) + (c[0]**2 + c[1]**2)*(b[0] - a[0]))/D
    return (ux, uy)

def circumradius(a, b, c):
    """ returns radius of circumcircle of triangle given by tuple points a, b and c. """
    return dist(circumcenter(a, b, c), a)

def circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line=True, tangent_tol=1e-9):
    """ returns list of intersection points between line through points pt1 and pt2 and circle centered at circle_center
    with radius equal to circle_radius. Intersection can happen at 0, 1, or 2 points.

    :param circle_center: The (x, y) location of the circle center
    :param circle_radius: The radius of the circle
    :param pt1: The (x, y) location of the first point of the segment
    :param pt2: The (x, y) location of the second point of the segment
    :param full_line: True to find intersections along full line - not just in the segment.  False will just return intersections within the segment.
    :param tangent_tol: Numerical tolerance at which we decide the intersections are close enough to consider it a tangent
    :return Sequence[Tuple[float, float]]: A list of length 0, 1, or 2, where each element is a point at which the circle intercepts a line segment.

    Note: We follow: http://mathworld.wolfram.com/Circle-LineIntersection.html
    """

    (p1x, p1y), (p2x, p2y), (cx, cy) = pt1, pt2, circle_center
    (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
    dx, dy = (x2 - x1), (y2 - y1)
    dr = (dx ** 2 + dy ** 2)**.5
    big_d = x1 * y2 - x2 * y1
    discriminant = circle_radius ** 2 * dr ** 2 - big_d ** 2

    if discriminant < 0:  # No intersection between circle and line
        return []
    else:  # There may be 0, 1, or 2 intersections with the segment
        intersections = [
            (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant**.5) / dr ** 2,
             cy + (-big_d * dx + sign * abs(dy) * discriminant**.5) / dr ** 2)
            for sign in ((1, -1) if dy < 0 else (-1, 1))]  # This makes sure the order along the segment is correct
        if not full_line:  # If only considering the segment, filter out intersections that do not fall within the segment
            fraction_along_segment = [(xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy for xi, yi in intersections]
            intersections = [pt for pt, frac in zip(intersections, fraction_along_segment) if 0 <= frac <= 1]
        if len(intersections) == 2 and abs(discriminant) <= tangent_tol:  # If line is tangent to circle, return just one point (as both intersections have same location)
            return [intersections[0]]
        else:
            return intersections