# *************************************
# @Fr4nc3
# 03/06/2015
# file: circuit_tester.py
# *************************************

import circuit


def main():
    '''test capacitator voltage'''
    a = circuit.read_file("params.txt")

    B = int(a[0])
    R = int(a[1])
    C = float(a[2])
    start = int(a[3])
    end = int(a[4])
    outfile = open("rc.txt", "w")
    for t in range(start, end+10, 10):
        # write results in a file
        capacitator_voltage = circuit.capacitator_voltage(B, R, C, t)
        outfile.write('%2d  %.5f \n' % (t, capacitator_voltage))
    outfile.close()

main()