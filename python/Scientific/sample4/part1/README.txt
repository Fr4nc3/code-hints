@Fr4nc3

effects module implements

1) object_filter
2) shades_of_gray
3) negate_red
4) negate_green
5) negate_blue



* For the Object Filter I had the idea to have N files to clean, however, for
the limited time it was impossible to test. So, I fixed the number to 3 files.

* Also, in effects_tester can be run only with enter, without params
so fast to test.

* in effects_tester I added start_time  to calculate the execution time
of the effects.

* object_filter takes less than  2 second approx. to execute.

* shades of gray, negate_red, negate_blue and negate_green take less than a
second to execute.

* I used ''' comment ''' when # it was more than two lines.

* This is my console output
/usr/local/Cellar/python3/3.4.1_1/Frameworks
/Python.framework/Versions/3.4/bin/python3.4
effects_tester.py

Portable Pixmap (PPM) Image Editor!
Choose the effect you would like to try:
1) object_filter
2) shades_of_gray
3) negate_red
4) negate_green
5) negate_blue
Enter your Option: 1
Enter an input file name:
Enter name of output file:
Enter  other image
(to finish enter 0): 0
--- 1.6806139945983887 seconds ---

Process finished with exit code 0
