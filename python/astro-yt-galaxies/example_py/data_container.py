import sys
from yt.mods import * # set up our namespace

import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"


fn = "/astro/data/redshift0058/redshift0058" # parameter file to load

pf = load(fn) # load data

c = [0.403290331 , 0.471765608 , 0.461319029] 

my_mw= pf.h.sphere(c, 250.0/pf['kpc'])



print  "center of mass  :"
#print  my_mw.center_of_mass()
print  "\n"


print  "virial mass  :"
print my_mw.virial_mass()
print  "\n"

print  "virial radius  :"
print  my_mw.virial_radius()
print  "\n"

print  "# particles   :"
print my_mw.get_size()
print  "\n"