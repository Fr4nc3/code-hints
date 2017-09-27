# *******************************************************
# @Fr4nc3
# 05/04/2013
# distances module
# *******************************************************

import math
import scipy.spatial.distance as distance
import numpy as np


def cal_distance(a, b, dist_type=1):
    """discriminate which type of distance I am testing."""
    if dist_type == 1:
        return euclidean_distance(a, b)
    elif dist_type == 2:
        return taxicab_distance(a, b)

    elif dist_type == 3:
        return mahalanobis_distance(a, b)

    elif dist_type == 4:
        return cosine_distance(a, b)


def euclidean_distance(a, b):
    """calculate the distance between two array, element by element."""
    dist = 0.0
    length = len(a)

    for i in range(length):
        dist += pow((a[i] - b[i]), 2)
    return math.sqrt(dist)


def taxicab_distance(a, b):
    """calculate the distance using |a-b| element by element."""
    dist = 0.0
    length = len(a)

    for i in range(length):
        dist += abs(a[i] - b[i])
    return dist


def mahalanobis_distance(a, b):
    """ uses the scipy mahalanobis distances to calculate the distance
    between two arrays. """
    x = np.array(a)
    y = np.array(b)
    z = np.vstack((x, y))
    cov = np.cov(z.T)
    return distance.mahalanobis(x, y, cov)


def cosine_distance(a, b):
    """Uses scipy.distances cosine cos(phi) =x*y/||x||*||y||."""
    return distance.cosine(a, b)
