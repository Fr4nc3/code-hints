from yt.mods import *
from yt.analysis_modules.star_analysis.api import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *
import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"
def get_density_extrema(halo, sphere):
    my_extrema = sphere.quantities['Extrema']('Density')
    mylog.info('Halo %d has density extrema: %s',
               halo['id'], my_extrema)
    
from yt.analysis_modules.halo_finding.halo_objects import RunFOF 

fn = "/astro/data/d0300/data0300/data0300" # parameter file to load



pf = load(fn) # load data
# Now we need a center of our volume to render.  Here we'll just use
# center of our MW 


c = [4.027091436e-01 ,   4.714863511e-01,   4.621095851e-01] # densest cell


sphere = pf.h.sphere(c, (250., 'kpc')) # 250.

data_source = pf.h.all_data()

stars = (data_source["creation_time"] > 0)
pos_x = data_source["particle_position_x"][stars]
pos_y = data_source["particle_position_y"][stars]
pos_z = data_source["particle_position_z"][stars]

linking_length = 0.017094633 # come from 

# data0300
#RefineRegionLeftEdge   = 0.347627 0.429308 0.436357
#RefineRegionRightEdge  = 0.436006 0.511214 0.52262
# ((xl-xr)*(yl-yr)(zl-zr))^(1/3)*0.2  #0.2 from FOF default linking length

#tags = RunFOF(pos_x, pos_y, pos_z, linking_length)

#print "Found %s unique groupings" % (np.unique(tags))


data_source = pf.h.all_data()

# Find all the haloes, and include star particles.
haloes = FOFHaloFinder(pf, link=linking_length ,dm_only=False)

haloes.dump("MyHalos")
haloes.write_out("FOFHopAnalysis.out")
# Iterate over the haloes.
for halo in haloes:
    ct = halo["creation_time"]

    sm = halo["ParticleMassMsun"]
    metal = halo["metallicity_fraction"]
    # Select just the stars.
    stars = (ct > 0)
    print stars
    ct = ct[stars]
    sm = sm[stars]
    metal = metal[stars]
    print ct
   # print ct.center_of_mass()
    
    #print halo['centerOfMass']['x'] + " , " + halo['centerOfMass']['y'] + " , " + halo['centerOfMass']['z']