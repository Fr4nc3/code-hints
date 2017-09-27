# *******************************************************
# @Fr4nc3
# 04/20/2013
# *******************************************************

import time
import percolation2 as perc


def main():
    A = perc.make_sites(20, 0.6)
    perc.write_grid('sites.txt', A)
    infile = open('sites.txt', 'r')
    B = perc.read_grid(infile)
    infile.close()  # add a line to close the file
    C = perc.directed_flow(B)
    if perc.percolates(C):
        print('percolates')
    else:
        print('does not percolate')


    # visualize flow
    perc.show_perc(B)
    #
    # generate percolation probability graph
    # add time to calculate performance
    start_time = time.time()
    perc.make_plot(10000, 10)
    print("--- %s seconds ---" % (time.time() - start_time))


main()
