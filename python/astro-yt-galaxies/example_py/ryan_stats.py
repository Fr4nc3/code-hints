from yt.mods import *
import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"

#pf = load("/Volumes/SPICA/MWsim/r0058/redshift0058")
pf = load("/astro/data/redshift0058/redshift0058")

pf.h.print_stats()
print pf.h.find_max("Density")