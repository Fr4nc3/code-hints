from yt.mods import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *

# If desired, start loop here.
fn = "/astro/data/d0099/data0099" # parameter file to load

pf = load(fn) # load data



c = [0.403290331 , 0.471765608 , 0.461319029]

dd = pf.h.sphere(c, 300.0/pf['kpc']) # only the MK simulation \

halos = HaloFinder(dd)

halos.write_out("HopAnalysis.out")