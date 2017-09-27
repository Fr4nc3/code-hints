# *******************************************************
# @Fr4nc3
# 04/13/2013
# percolation module
# *******************************************************

import numpy as np


def read_grid(input_file):
    """Create a site vacancy matrix from a text file."""
    N = input_file.readline().strip()
    b = []
    for line in input_file.readlines():
        b.append(list(map(int, line.rstrip())))

    # convert the array to numpy array
    a = np.array(b)
    return a


def write_grid(filename, sites):
    """Write a site vacancy matrix to a file."""
    N = str(len(sites))
    np.savetxt(filename, sites, fmt='%d', delimiter='', newline='\n', header=N,
               comments='')


def flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)
    sites is a numpy array representing a site vacancy matrix. This
    function return the corresponding flow matrix generated
    through vertical percolation.
    """
    n = len(sites)
    full = np.zeros((n, n), dtype='int32')

    # identify full sites in row 0
    for j in range(n):
        full[0, j] = sites[0, j]

    # update remaining rows
    for i in range(1, n):
        for j in range(n):
            full[i, j] = sites[i, j] and full[i - 1, j]
    return full


def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation
    flow_matrix is a numpy array representing a flow matrix.
    """
    n = len(flow_matrix)
    full = flow(flow_matrix)
    for j in range(n):
        if full[n - 1, j] == 1:
            return True
    return False


def generate(p):
    """return 1 / 0 in base of thd random number."""
    return np.random.choice([0, 1], p=[p, 1 - p])


def make_sites(n, p):
    """Returns an nxn site vacancy matrix
    Generates a numpy array representing an nxn site vacancy
    matrix with site vacancy probability p.
    """
    a = np.zeros((n, n), dtype='int32')
    for i in range(n):
        for j in range(n):
            a[i, j] = generate(p)

    return a