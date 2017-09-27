CONTENTS OF THIS FILE
---------------------
* Introduction
* Files
* Question 1
* Question 2
* Troubleshooting
* Author


INTRODUCTION
------------
Written in Python 3.4 using PEP8 style guidelines
this homework gives a solution to:
- Question 1) Science P35 Electric Wire
- Question 2) Projectile-Flight


FILES
------------
Question 1
* P35_f.py implement methods for question 1
* P35_m.py test methods for question 1

Question 2
* projectile.py implement methods for question 2
* projectile.py test methods for question 2

* README.txt this file


QUESTION 1
------------
Electric wire is a cylindrical conductor covered by an insulating material.
The resistance of a piece of wire is given by the formula
R=4pL/pid^2

where p is the resistivity of the  conductor
L is the length and d is the diameter of the wire

in P35_F, we implemented two method to calculate the wire resistance of Copper
and aluminum. Those methods are copper_wire_resistance(length, wire_gauge) and
aluminium_wire_resistance(length, wire_gauge).

The value of length is expected in meters and wireGauge(awg) is expected to be
an integer.

in P35_m, we tested a range different length from 1 to 10 and awg from 0 to 9
and we get the resistance for copper and aluminum for those ranges.


QUESTION 2
------------
Projectile-Flight, when we calculate the distance traveled by a projectile
we generally used the formula s(t) = -0.5 g t2 + v0 t, which ignore
the difference of gravity depending on the h.

Therefore, in this question we calculate the simulated position of a projectile
depending in the gravity at that position.

Projectile.py implements the follow methods

* g(h) - where h is altitude and the function returns the value of acceleration
due to gravity at altitude h.

* s_next ( s_current, v_current, delta_t) -  which returns s(t+∆t).

* v_next(s_next, v_current, delta_t) - which returns v(t+∆t) .

* s_sim(t, v_init, s_init, delta_t) -  which returns the projectile's position
at time t from now.

* s_standard(t,v_init) - which returns the position using equation (1) and
initial position = 0.

Projectile_tester.py test the accuracy of the methods implemented


TROUBLESHOOTING
------------
Question 1 was straight forward the implementation.
run > python3.4 P35_m.py

Question 2 the definition and the name of the method  and variables are not
developer friendly and gives a hard time to understand and implement.
run > python3.4 projectile_tester.py

AUTHOR
------------
Fr4nc3
last updated 02/20/2015