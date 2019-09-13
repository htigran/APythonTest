from math import radians, sin, cos, acos

MEAN_EARTH_RADIUS = 6371


def great_circle(lon1, lat1, lon2, lat2):
    """
    The great-circle distance is the shortest distance between two points on the surface of a sphere
    :param lon1: longitude of first point
    :param lat1: latitude of first point
    :param lon2: longitude of second point
    :param lat2: latitude of second point
    :return: the distance between first and second pints
    """

    # convert degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    return MEAN_EARTH_RADIUS * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )
