# *********************************************
# @Fr4nc3
# file: P35_m.py
# this program tests the functions in the
# P35_f module
# *********************************************
import P35_f


def main():
    ''' Tester for Science P35 Electric Wire'''

    # print header
    print('\t \t \t \t \t Resistance')
    print('length \t AWG \t  \t copper \t \t aluminum')
    print('-----------------------------------------------------------')
    # create a range of number to test length
    for length in range(1, 11):
        # create a range of numbers to test AWG
        for awg in range(0, 10):
            copper_wire_resistance = P35_f.copper_wire_resistance(length, awg)
            aluminum_wire_resistance = P35_f.aluminium_wire_resistance(length, awg)

            print('%2d \t \t %.1d \t \t %.5f \t \t %.5f' % (
                length, awg, copper_wire_resistance, aluminum_wire_resistance))


# now run main()
main()
