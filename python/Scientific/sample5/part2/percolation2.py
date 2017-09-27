# *******************************************************
# @Fr4nc3
# 04/20/2013
# percolation module
# *******************************************************

import numpy as np
import matplotlib.pyplot as plt


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


def directed_flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)."""
    n = len(sites)
    full = np.zeros((n, n), dtype='int32')
    for j in range(n):
        flow_from(sites, full, 0, j)
    return full


def flow_from(sites, full, i, j):
    """Adjusts the full array for flow from a single site."""
    n = len(sites)

    """ verify is the dimension are correct
    if not return and do nothing.
    """
    # if the range of i,j are offset return and do nothing
    if i < 0 or i >= n:
        return
    if j < 0 or j >= n:
        return

    # if the element i,j in sites is vacant do nothing
    if sites[i, j] == 0:
        return
    # if the element i,j in full matrix is full return and do nothing
    if full[i, j] == 1:
        return

    full[i, j] = 1  # set i, j  as full, in the full matrix

    # recursive call for down right left up flow.
    flow_from(sites, full, i + 1, j)
    flow_from(sites, full, i, j + 1)
    flow_from(sites, full, i, j - 1)
    flow_from(sites, full, i - 1, j)


def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation."""
    n = len(flow_matrix)
    full = directed_flow(flow_matrix)
    for j in range(n):
        if full[n - 1, j] == 1:
            return True
    return False


def generate(p):
    """return 1 / 0 in base of the random number."""
    return np.random.choice([0, 1], p=[1 - p, p])


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


def show_perc(sites):
    """Displays a matrix using three colors for vacant, blocked, full
    Used to visualize directed flow on the matrix sites.
    """
    fig, ax = plt.subplots()
    full = directed_flow(sites)

    """ Meaning of the sum of the two matrix.
    # 2 (in blue) full
    # 1 (in light blue) open
    # 0 (in white) closed """
    matrix_flow = sites + full  # add two matrix

    ax.set_xticklabels([])  # remove labels
    ax.set_yticklabels([])

    ax.matshow(matrix_flow, cmap='Blues')  # show the matrix in blue colors.
    plt.savefig('percolation_visualization.pdf')
    plt.show()


def make_plot(trials, n):
    """generates and displays a graph of percolation p vs. vacancy p."""
    # initial variables
    p = 0  # probability start in 0
    vacancy_p = []
    percolation_p = []

    # runs until the probability is 1
    while p < 1:
        count_success = 0
        # loops of trials
        for j in range(trials):
            sites = make_sites(n, p)
            full = directed_flow(sites)

            if percolates(full):
                count_success += 1

        """percolation probability is the success number of percolation
        divided  by trials."""
        percolation_probability = count_success / trials

        # add values of p (probability) and percolation_probability
        vacancy_p.append(p)
        percolation_p.append(percolation_probability)

        # increases the probability p of percolation 0.04 per time
        p += 0.04

    # create plot x = vacancy_p and y = percolation_p
    plt.plot(vacancy_p, percolation_p, color="blue", linewidth=2, linestyle="-")

    # plot labels
    plt.xlabel('vacancy p')
    plt.ylabel('percolation p')
    plt.title('Percolation vs. Vacancy Probability')

    plt.savefig('percolation_plot.pdf')
    plt.show()



