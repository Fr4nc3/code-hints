# *******************************************************
# @Fr4nc3
# 04/13/2013
# percolation test module
# *******************************************************


import percolation as perc


def main():
    """Test Percolation Vertical."""
    A = perc.make_sites(25, 0.45)
    perc.write_grid('sites.txt', A)
    infile = open('sites.txt', 'r')
    B = perc.read_grid(infile)
    infile.close()
    C = perc.flow(B)
    if perc.percolates(C):
        print('percolates')
    else:
        print('does not percolate')


main()