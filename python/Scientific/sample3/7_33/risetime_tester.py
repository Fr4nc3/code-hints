# *************************************
# @Fr4nc3
# 03/06/2015
# file: risetime_tester.py
# *************************************
import risetime


def main():
    '''test risetime '''
    a = risetime.read_file("rc.txt")
    last = a[len(a)-1].split("  ")

    B = float(last[1])

    for l in a:
        p = l.split("  ")  # split line in two variables
        v_1 = float(p[1])
        print(risetime.rise_time(v_1,B))

main()