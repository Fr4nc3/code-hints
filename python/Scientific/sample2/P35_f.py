# *************************************
# @Fr4nc3
# file: P35_f.py
# implements methods diameter copper_wire_resistance aluminium_wire_resistance
# wire_resistance
# *************************************
import math

COPPER_RESISTIVITY = 1.678e-8
ALUMINUM_RESISTIVITY = 2.82e-8


def diameter(wire_gauge):
    # 1000 to convert mm to m
    return (0.127 * 92 ** ((36 - wire_gauge) / 39)) / 1000


def wire_resistance(resistivity, length, wire_gauge):
    return (4 * resistivity * length) / (math.pi * diameter(wire_gauge) ** 2)


def copper_wire_resistance(length, wire_gauge):
    return wire_resistance(COPPER_RESISTIVITY, length, wire_gauge)


def aluminium_wire_resistance(length, wire_gauge):
    return wire_resistance(ALUMINUM_RESISTIVITY, length, wire_gauge)