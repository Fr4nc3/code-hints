# *********************************************
# projectile_tester
# this program tests the functions in the
# projectile module
# *********************************************

import projectile


def main():
    # set up initial values
    v_0 = 300
    s_0 = 0
    t = 0
    delta_t = .05

    s = s_0  # start s off at s_0

    # print a table with values computed both ways for positive positions

    print('seconds \t distance_sim \t \t distance_formula')
    print('-----------------------------------------------------------')
    while s >= 0:
        s_formula = projectile.s_standard(t, v_0)
        print('%2d \t \t %.5f \t \t %.5f' % (t, s, s_formula))
        t += 1
        s = projectile.s_sim(t, v_0, s_0, delta_t)


# now run main()
main()