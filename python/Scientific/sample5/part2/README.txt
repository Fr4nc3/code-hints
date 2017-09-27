Fr4nc3

percolation2 modules implemented

make_sites
generate
percolates
directed_flow
flow_from
write_grid
read_grid
make_plot
show_perc


* show_perc uses matplotlib matshow adding the sites matrix and the full matrix
generates a new matrix.

[[2 0 2 2 2 0 2 2]
 [0 0 0 2 2 2 0 2]
 [1 1 0 2 2 0 1 0]
 [1 0 0 2 0 1 1 1]
 [1 1 1 0 1 1 1 0]
 [1 0 1 1 1 1 0 1]
 [0 0 1 1 0 1 1 1]
 [1 0 1 1 1 1 1 0]]

* 2 is full site
* 1 is open site
* 0 is closed

* directed_flow return a matrix with full and vacant elements

* show_plot generate a plot trying m trials increasing the probability of
percolation after the m trials. Save in vacancy_p the proportion between
success percolation / m trials and  probability p in percolation_p.
It Takes 563.5543148517609 seconds (almost 10 minutes) to generate the plot.


Used this document:
A Fast Monte Carlo Algorithm for Site or Bond Percolation.
http://www.santafe.edu/media/workingpapers/01-02-010.pdf

Montecarlo
percolation by running a Monte Carlo simulation using the variable trials
number of trials for each point.
Monte Carlo Simulation is a way of studying probability distributions
with sampling. The basic idea is that if you draw many samples from a
distribution and then make a histogram, the histogram will be shaped a lot
like the original distribution.
https://www.chrisstucchio.com/blog/2013/basic_income_vs_basic_job.html

http://pythonprogramming.net/monte-carlo-simulator-python/