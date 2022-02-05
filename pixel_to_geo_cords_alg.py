import math
from CONSTANTS import COEFFICIENT


def pixel_to_geo_cords(pos, ll, zoom):
    pos = [pos[0] - 225, 225 - pos[1]]
    x = float(ll[0]) + pos[0] * COEFFICIENT * math.pow(2, 15 - zoom)
    y = float(ll[1]) + pos[1] * COEFFICIENT * math.cos(math.radians(float(ll[1]))) * math.pow(2, 15 - zoom)
    return [str(x), str(y)]
