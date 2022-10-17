def segmentsintersect(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    dx_1 = x_2 - x_1
    dy_1 = y_2 - y_1
    dx_2 = x_4 - x_3
    dy_2 = y_4 - y_3
    delta = dx_2 * dy_1 - dy_2 * dx_1
    if delta == 0:
        return False
    s = (dx_1 * (y_3 - y_1) + dy_1 * (x_1 - x_3)) / delta
    t = (dx_2 * (y_1 - y_3) + dy_2 * (x_3 - x_1)) / (-delta)
    return (0 <= s <= 1) and (0 <= t <= 1)

def pointsegmentsquareddistance(p_x, p_y, x_1, y_1, x_2, y_2):
    dx = x_2 - x_1
    dy = y_2 - y_1
    if dx == 0 and dy == 0:
        return (p_x - x_1) * (p_x - x_1) + (p_y - y_1) * (p_y - y_1)
    t = ((p_x - x_1) * dx + (p_y - y_1) * dy) / (dx * dx + dy * dy)
    if t < 0:
        return (p_x - x_1) * (p_x - x_1) + (p_y - y_1) * (p_y - y_1)
    elif t > 1:
        return (p_x - x_2) * (p_x - x_2) + (p_y - y_2) * (p_y - y_2)
    else:
        x = x_1 + t * dx
        y = y_1 + t * dy
        return (p_x - x) * (p_x - x) + (p_y - y) * (p_y - y)

def segmentsquareddistance(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    """
        Given two line segments (x_1, y_1) to (x_2, y_2) and (x_3, y_3) to (x_4, y_3),
        returns square of minimum distance between the segments. Tested with integer
        coordinate end points, should work with floats also. To get distance, simply take
        the square root of returned value. Take care with precision however: Make sure to
        truncate to two decimals, round to two decimals or perform any other operation
        as appropriate.
    """
    if segmentsintersect(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
        return 0
    d = []
    d.append(pointsegmentsquareddistance(x_1, y_1, x_3, y_3, x_4, y_4))
    d.append(pointsegmentsquareddistance(x_2, y_2, x_3, y_3, x_4, y_4))
    d.append(pointsegmentsquareddistance(x_3, y_3, x_1, y_1, x_2, y_2))
    d.append(pointsegmentsquareddistance(x_4, y_4, x_1, y_1, x_2, y_2))
    return min(d)